import numpy as np
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry,SamPredictor
from PIL import Image

class SamModel():
    
    def __init__(self, sam_checkpoint_path="sam_prediction/SAM_data/sam_vit_l_0b3195.pth", model_type="vit_l"):
        device="cuda"
        sam = sam_model_registry[model_type](checkpoint=sam_checkpoint_path)
        # sam.to(device=device)
        self.predictor = SamPredictor(sam)

    def hello(self):
        print("HELLO")
    
    def segmentImage(self, fileImage):
        pil_image = Image.open(fileImage)
        rgb_image = pil_image.convert('RGB')

        numpy_image = np.array(rgb_image)
        numpy_image = numpy_image.astype(np.uint8)

        print("Making Segmentation...")

        self.predictor.set_image(numpy_image)
        
        input_point = np.array([[int(numpy_image.shape[1]/2),int(numpy_image.shape[0]/2)]])
        input_label = np.array([1])
        masks, scores, logits = self.predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=True,
        )
        
        sorted_segments = [masks[i,:,:] for i in range(0,masks.shape[0])]
        seg_image=self._getFinalImage(numpy_image,sorted_segments,scores)
        
        print("OK Segmentation...")
        
        return seg_image
    
     
    def _getFinalImage(self,image,segments,scores,sensitive=0.05, background=0):
        max_area=0
        max_score=0
        
        for i in range(0,len(segments)):
            seg_sample= segments[i]

            seg_matrix= seg_sample*1

            count = np.count_nonzero(seg_matrix)

            if(i==0 or scores[i]>max_score):
                max_score=scores[i]
                selected_seg=self._getSegment(seg_matrix,image)


        for i in range(0,len(segments)):
            
            seg_sample= segments[i]
            
            seg_matrix= seg_sample*1

            count = np.count_nonzero(seg_matrix)

            if(i==0 or count>max_area and max_score-scores[i]<=sensitive):
                selected_seg=self._getSegment(seg_matrix,image)


        return selected_seg    
    
    
    def _getSegment(self,segment_matrix,image,background=0):
                      
        expanded_seg = np.expand_dims(segment_matrix, axis=2)
        expanded_seg = np.repeat(expanded_seg, 3, axis=2)

        samples_seg_img = np.multiply(expanded_seg,image)

        nz = np.nonzero(samples_seg_img) # Indices of all nonzero elements
        samples_seg_img = samples_seg_img[nz[0].min():nz[0].max()+1,
                    nz[1].min():nz[1].max()+1]

        samples_seg_img[samples_seg_img == 0] = background
        selected_seg=samples_seg_img
        return selected_seg 
            