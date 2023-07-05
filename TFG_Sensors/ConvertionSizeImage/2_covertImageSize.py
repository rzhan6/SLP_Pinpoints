import cv2
import matplotlib.pyplot as plt
from skimage import io 
import numpy as np

HEIGHT=120
WIDTH=160

# HEIGHT=576
# WIDTH=1024

def resizeImage(imagePath, height, width):
    #read image
    img=cv2.imread(imagePath)
    
    h,w=img.shape[:2]
    print('Image Height is', h)
    print('Image Width is', w)
    fx = round(WIDTH/w,2) #two decimal points
    fy = round(HEIGHT/h,2) 

    """ print('factor',fx , 'factor y: ', fy )

    
    img_75 = cv2.resize(img, (w/fx,h/fy)) """
    # img_75 = cv2.resize(img, None, fx, fy)
    
    # resized_img = cv2.resize(img, (120, 84))

    # Calculate the aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0] #w/h

    print('aspect_ratio: ', aspect_ratio)
    # Resize the image to (120, 84) while preserving the aspect ratio
    resized_img = cv2.resize(img, (84, int(84/aspect_ratio)), interpolation=cv2.INTER_AREA)



    # Filename
    filename = 'Resizedir1.png'#+ imagePath
    print(filename)
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imshow('resized image',resized_img)
    cv2.imwrite(filename, resized_img) 
    print('Image Height is',resized_img.shape[0])
    print('Image Width is',resized_img.shape[1])
   
    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)
    
    # closing all open windows
    cv2.destroyAllWindows()


    #cv2.INTER_LINEAR	The standard bilinear interpolation, ideal for enlarged images.

    # src:input;
    # dsize:outputimagesize(wight,height);
    # fx: the scale factor for the X axis
    # fy: the scale factor for the y axis
    # interpolation: the technique for adding or removing pixels during the resizing process. the default is cv2.INTER_LIMEAR
    # 
    # cv2.resize(src, dsize, fx, fy, interpolation)

def resizergb():
    # Read the image
    image = cv2.imread('r:\SLP_Project\Projects\OpenCVProject\cmos-2.jpg')

    # Rotate the image counterclockwise by 90 degrees
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Resize the image
    new_size = (HEIGHT, WIDTH)  # Specify the new size (width, height)
    resized_image = cv2.resize(rotated_image, new_size)

    # Save the resized image
    cv2.imwrite('r:\SLP_Project\Projects\OpenCVProject\output_cmos2.jpg', resized_image)

def resize():
    # Read the image
    # image = cv2.imread('r:\SLP_Project\Projects\OpenCVProject\ir.png')
    # image = cv2.imread('C:\\Users\\rzhan\Documents\GitHub\TFG_Sensors\ConvertionSizeImage\ir.png')
    image = cv2.imread('C:\\Users\\rzhan\Documents\GitHub\TFG_Sensors\ConvertionSizeImage\irsup.jpg')
    print(image.shape)
    # image = cv2.imread('r:\SLP_Project\SLP_dataset\SLP\danaLab\\00056\IR\\uncover\image_000035.png')
    # print(image.shape)
    # Rotate the image counterclockwise by 90 degrees
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Resize the image
    new_size = (HEIGHT, WIDTH)  # Specify the new size (width, height)
    resized_image = cv2.resize(rotated_image, new_size)
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    normalized_image = cv2.normalize(grayscale_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Save the resized image
    cv2.imwrite('C:\\Users\\rzhan\Documents\GitHub\TFG_Sensors\ConvertionSizeImage\grayirsup.jpg', normalized_image)

def show():
    # image = cv2.imread('r:\SLP_Project\Projects\OpenCVProject\ir.png')
    # print(image.shape)
    # image = cv2.imread('r:\SLP_Project\SLP_dataset\SLP\danaLab\\00056\IR\\uncover\image_000035.png')
    # print(image.shape)
    img = io.imread('r:\SLP_Project\Projects\OpenCVProject\output_ir.jpg')
    img = np.array(img) #numpy data 
    print("0. input image shape: ", img.shape)

    img = io.imread('r:\SLP_Project\SLP_dataset\SLP\danaLab\\00056\IR\\uncover\image_000035.png')
    img = np.array(img) #numpy data 
    print("1. input image shape: ", img.shape)

if __name__=='__main__':
    resize()
    # show()
    # pth="DepthImage.png"
    # pth1="rgbImage.png"
    # pth2="grayImage.png"
    # resizeImage(pth,HEIGHT,WIDTH)
    # resizeImage(pth1,HEIGHT,WIDTH)
    # resizeImage(pth2,HEIGHT,WIDTH)
    
    # pth1="r:\SLP_Project\Projects\OpenCVProject\cmos-1.jpg"
    # resizeImage(pth1,HEIGHT,WIDTH)

    # keep the image en dimension (x, 84) 
    # also need to convert to dim (120, 84). #FALTA A IMPLEMENTAR 