# Use Gradients to Identify Edge Pixels
# Colorspace
# gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
#  hls = cv2.cvtColor(im, cv2.COLOR_RGB2HLS)
  
import numpy as np
import cv2
  
#  Sobel
#     Note: Make sure you use the correct grayscale conversion depending on how you've read in your images. Use cv2.COLOR_RGB2GRAY if you've read in an image using mpimg.imread(). Use cv2.COLOR_BGR2GRAY if you've read in an image using cv2.imread().
#   
#   # X derivative
#   sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
#   # Y Derivative
#   sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
#   # ABS
#   abs_sobelx = np.absolute(sobelx)
#   #Abs to IMg
#   scaled_sobel = np.uint8(255*abs_sobelx/np.max(abs_sobelx))
#   
#   # Thresholding
#   thresh_min = 20
#   thresh_max = 100
#   sxbinary = np.zeros_like(scaled_sobel)
#   sxbinary[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1
#   plt.imshow(sxbinary, cmap='gray')

  
def sobel_abs_thresh(gray, orient='x', thresh=(0, 255), sobel_kernel = 3):
  # Grayscale
  # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  # Apply cv2.Sobel()
  if orient == 'x':
    sobel_grad = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
  elif orient == 'y':
    sobel_grad = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
  # Take the absolute value of the output from cv2.Sobel()
  abs_sobel_grad = np.absolute(sobel_grad)
  # Scale the result to an 8-bit range (0-255)
  scaled_sobel = np.uint8(255*abs_sobel_grad/np.max(abs_sobel_grad))
  # Apply lower and upper thresholds
  grey_thresh = np.zeros_like(gray)
  index = (scaled_sobel >= thresh[0]) & (scaled_sobel <= thresh[1])
  grey_thresh[index] = scaled_sobel[index]
  # Create binary_output
  return grey_thresh
  
# Define a function that applies Sobel x and y, 
# then computes the magnitude of the gradient
# and applies a threshold
def sobel_mag_thresh(gray, thresh=(0, 255), sobel_kernel=3):
    # Apply Sobel x and y, then computes magnitude
    # of the gradients and applies a threshold.
    # Input is a grayscale image
    
    # Apply the following steps to img
    # 1) Convert to grayscale
    # 2) Take the gradient in x and y separately
    # 3) Calculate the magnitude 
    # 4) Scale to 8-bit (0 - 255) and convert to type = np.uint8
    # 5) Create a binary mask where mag thresholds are met
    # 6) Return this mask as your binary_output image
    
    # Grayscale
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Apply cv2.Sobel()
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    # Take the absolute value of the output from cv2.Sobel()
    #abs_sobelx = np.sqrt(sobelx**2)
    #abs_sobely = np.sqrt(sobely**2)
    abs_sobel_grad = np.sqrt(sobelx**2 + sobely**2)
    
    # Scale the result to an 8-bit range (0-255)
    scaled_sobel = np.uint8(255*abs_sobel_grad/np.max(abs_sobel_grad))
    
    # Apply lower and upper thresholds
    grey_thresh = np.zeros_like(gray)
    index = (scaled_sobel >= thresh[0]) & (scaled_sobel <= thresh[1])
    grey_thresh[index] = scaled_sobel[index]
    # Create binary_output
    return grey_thresh

def sobel_dir_thresh(gray, thresh=(0, np.pi/2), sobel_kernel=3):
    # Apply the following steps to img
    # 1) Convert to grayscale
    # grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # 2) Take the gradient in x and y separately
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0 , ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1 , ksize = sobel_kernel)
    
    # 3) Take the absolute value of the x and y gradients
    abs_sobelx = np.sqrt(sobelx**2)
    abs_sobely = np.sqrt(sobely**2)
    
    # 4) Use np.arctan2(abs_sobely, abs_sobelx) to calculate the direction of the gradient 
    anglegrad = np.arctan2(abs_sobely,abs_sobelx)
    
    # 5) Create a binary mask where direction thresholds are met
    grey_thresh = np.zeros_like(gray)
    index = (anglegrad >= thresh[0]) & (anglegrad <= thresh[1])
    grey_thresh[index] = gray[index]
    # 6) Return this mask as your binary_output image
    return grey_thresh