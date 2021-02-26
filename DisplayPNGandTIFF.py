# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:38:08 2021
@author: kristina mishra
Consider citing or mentioning me if you find helpful
"""
# Python program to display Tiff or PNG images that have transparency

import os
import torch
import matplotlib.pyplot as plt

#what is the working directory?
print (os.getcwd())
#use this if you need to specify a specific directory that is diff than the current working directory
#replace <path name> with your image path name like 'c:\\FunDrive\\Data'
os.chdir('<path name>')

# Python program to read image using matplotlib
import matplotlib.image as mpimg 

# Read Images.  
img = mpimg.imread('123.jpg')       #Use jpg as baseline image that we know displays outside of python
img2 = mpimg.imread('123.png')      #large, more complicated segmentation image saved in png format
img3 = mpimg.imread('123.tiff')     #tiff format that has transparency and won't display in windows/other apps

# Output Images 
plt.imshow(img)     #shows as expected
plt.imshow(img2)    #multi class transparent png won't show here
plt.imshow(img3)    #should show here, but you may have to do similar to below if it has addln items that prevent from displaying


#fix it to display properly
#create a new variable so we can overwrite as needed for tests
mask=img2
#what is the shape of this image?
mask.shape
#use this line as needed depending on shape of image. 
#This is an example of what to use if the image has a size of 3 dim (x,y,z) and you want to change it to (x,y)
mask=mask[:,:,1]
#verify the shape change (comment out if not using the shape change above)
mask.shape
#change to torch iage. There are other ways to do this, but I already was using this for a torch project
mask=torch.tensor(mask)
#verify shape is same. 
mask.shape
#add a dimension in the front
mask=mask.unsqueeze(0)
#verify new dimension was added to beginning
mask.shape
#add another if needed (comment out if not)
mask=mask.unsqueeze(0)
#check that the extra dim is there
mask.shape

#voila!
imgplot = plt.imshow(mask[0][0])
#plt.show()


