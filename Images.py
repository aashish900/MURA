
# coding: utf-8

# # Load the relevant libraries 

# In[1]:


import cv2
import datetime as dt
import h5py
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np
import csv
import os


# In[2]:


os.getcwd()


# # Load path of the images

# In[3]:


#Load path to images
root_Path_CSV = 'C:/Users/Aashish/Desktop/MURA-v1.1/train_image_paths.csv'
#root_Path_CSV = 'MURA-v1.1/train_image_paths.csv'
with open(root_Path_CSV) as csvfile:
    path = csv.reader(csvfile, delimiter = ',')
    
    train_Image_Path = []
    
    for row in path:
        image = row[0]
        train_Image_Path.append(image)


# In[4]:


len(train_Image_Path)


# In[5]:


root = 'C:/Users/Aashish/Desktop/'
path = []
for i in range(len(train_Image_Path)):
    pa = root + train_Image_Path[i]
    path.append(pa)


# # Creating Labels for Images

# In[6]:


#Assigning images appropriate labels
new_Labels = []
for i in range (0, len(train_Image_Path)):
    if "positive" in train_Image_Path[i]:
        new_Labels.append(1)
    elif "negative" in train_Image_Path[i]:
        new_Labels.append(0)
    else:
        new_Labels.append(None)


# In[7]:


len(new_Labels)


# # Printing path to Images and Labels

# In[8]:


#Printing new labels
for counter, value in enumerate(new_Labels):
    serial_Number = str(counter) + ")."
    print(serial_Number, "Image Path =", train_Image_Path[counter], "||", "Label =", value)


# # Print image to check data

# In[9]:


im = cv2.imread(path[0])
cv2.imshow("Test", im)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Save images in HDF5 file

# In[10]:


start = dt.datetime.now()

HEIGHT = 312
WIDTH = 312
CHANNELS = 3

with h5py.File('Saved_Images.h5', 'w') as hf: 
    for i,img in enumerate(path):            
        # Images
        image = cv2.imread(img)
        image = cv2.resize(image, (WIDTH, HEIGHT), interpolation = cv2.INTER_CUBIC)
        Xset = hf.create_dataset(
            name = 'X' + str(i),
            data = image,
            shape = (HEIGHT, WIDTH, CHANNELS),
            maxshape = (HEIGHT, WIDTH, CHANNELS),
            compression = "gzip",
            compression_opts = 9)
            
        yset = hf.create_dataset(
            name = 'y' + str(i),
            data = new_Labels[i],
            shape = (1, ),
            maxshape = (None,),
            compression = "gzip",
            compression_opts = 9)

        if(i % 10 == 0 and i >= 1):
            t = dt.datetime.now()
            print("\r", "Loaded Images:", i, "||" ,"Time Elapsed:", (t - start).seconds, "seconds", end = "")
    
end = dt.datetime.now()
print("\r", "Loaded Images:", i, "||" ,"Time Elapsed:", (end - start).seconds, "seconds", end = "")


# # Print a few images to see if data is saved properly

# In[11]:


with h5py.File('Saved_Images.h5', 'r') as hf:
    plb.imshow(hf["X19"])
    print(hf["y23"].value)


# In[12]:


with h5py.File('Saved_Images.h5', 'r') as hf:
    plb.imshow(hf["X325"])
    print(hf["y325"].value)


# In[13]:


with h5py.File('Saved_Images.h5', 'r') as hf:
    plb.imshow(hf["X864"])
    print(hf["y864"].value)


# In[14]:


with h5py.File('Saved_Images.h5', 'r') as hf:
    plb.imshow(hf["X493"])
    print(hf["y493"].value)


# In[15]:


with h5py.File('Saved_Images.h5', 'r') as hf:
    plb.imshow(hf["X33323"])
    print(hf["y33323"].value)

