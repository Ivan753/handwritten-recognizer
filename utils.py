import PIL
from PIL import Image
import pickle
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


def resize_images():
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


def img2lsit(path): #"dataset/Sample001/img001-001.png"
    res = []
    
    img = Image.open(path)
    
    for i in range(img.size[1]):
        res.append([])
        for j in range(img.size[0]):
            res[i].append(img.getpixel((j, i))[0])
    
    return res
    

def create_dataset():
    res = []
    y = []
    
    for i in range(62):
        for j in range(55):
            res.append(img2lsit("dataset/Sample{0:0>3}/img{0:0>3}-{1:0>3}.png"
                                .format(i+1, j+1)))
            y.append([0 for x in range(62)])
            y[i*55+j][i] = 1
        
    return res, y
    
    
# X, y = create_dataset()

# with open('x.txt', 'wb') as pickle_file:
    # pickle.dump(X, pickle_file)
# with open('y.txt', 'wb') as pickle_file:
    # pickle.dump(y, pickle_file)


with open('x.txt', 'rb') as pickle_file:
    X = pickle.load(pickle_file)

with open('y.txt', 'rb') as pickle_file:
    y = pickle.load(pickle_file)


    
    
