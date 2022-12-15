import os
import argparse
from PIL import Image
from numpy import asarray
import re

parser = argparse.ArgumentParser(description='Split images by class')
parser.add_argument('--data', type=str, default='flowerset',
                    help='location of the data corpus')
args = parser.parse_args()
image_path = args.data
filenames = sorted([f for f in os.listdir(image_path)])

path = "./flower102/"
if not os.path.exists(path):
    os.mkdir("./flower102")

for file in filenames:
    classname = file.split("_")[1]
    classname = '{:0>3}'.format(classname) # pad zeros
    path = "./flower102/" + classname
    if not os.path.exists(path):
        os.mkdir(path)
    image = Image.open(image_path +"/"+ file) 
    image.save(path + "/" + file) 

     
 