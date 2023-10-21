import PIL
import os
import os.path
from PIL import Image

f = r'C:\Users\Abhishek Raman\Desktop\Abhishek\Recordings\2d Frames'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((720,560))
    img.save(f_img)
    #print(img.size)