import cv2

def resize_image(src_image, width, height, target_image):
    image = cv2.imread(src_image)
    src_height,src_width = image.shape[0], image.shape[1]
    #scale = src_height/height
    #width_size= int (src_width/width) 
    new_image = cv2.resize(image, (width, height))
    cv2.imwrite(target_image, new_image)
