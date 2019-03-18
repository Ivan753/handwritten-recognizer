import PIL
from PIL import Image
import pickle
import os
from sklearn.model_selection import train_test_split

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


def img2lsit(path):
    res = []
    
    img = Image.open(path)
    
    for i in range(img.size[1]):
        res.append([])
        for j in range(img.size[0]):
            res[i].append([(img.getpixel((j, i))[0] - 127.5) / 255])
    
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


def y2letter(i):
    letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
              ]
    
    return letters[i]
    
 
def pickle_dump_dataset():
    X, y = create_dataset()

    with open('x.txt', 'wb') as pickle_file:
        pickle.dump(X, pickle_file)
    with open('y.txt', 'wb') as pickle_file:
        pickle.dump(y, pickle_file)


def pickle_read_dataset():
    with open('x.txt', 'rb') as pickle_file:
        X = pickle.load(pickle_file)
    with open('y.txt', 'rb') as pickle_file:
        y = pickle.load(pickle_file)
    
    return X, y


def get_samples():
    X, y = pickle_read_dataset()
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.1, 
                                                        random_state=241)
    return X_train, X_test, Y_train, Y_test

