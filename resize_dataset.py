import PIL
from PIL import Image
import os

# resize images
def create_new_img(path, base_path, new_base, height):
    base_width = height
    
    img = Image.open(base_path+path)
    wpercent = (base_width / float(img.size[1]))
    hsize = int((float(img.size[0]) * float(wpercent)))
    img = img.resize((hsize, base_width), PIL.Image.ANTIALIAS)
    img.save(new_base+path)
    print(new_base+path)


base_path = 'EnglishHnd/EnglishHnd/English/Hnd/Img/'

file = open(base_path+'all.txt~')
new_file = "";

# 50x66 - height/width
base_width = 50
new_base = 'dataset/'

# samples sample
i, j = 1, 1

for line in file:
    
    if j == 56:
        j = 1
    
    # create folder
    if j == 1:
        print()
        os.mkdir(new_base+'Sample{0:0>3}'.format(i))
        i += 1
    
    j += 1
    
    create_new_img(line[:-1], base_path, new_base, base_width)

