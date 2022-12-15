import os
import argparse
from PIL import Image
from numpy import asarray
import re

parser = argparse.ArgumentParser(description='Split images by class')
parser.add_argument('--data', type=str, default='cifar10',
                    help='location of the data corpus')
args = parser.parse_args()
image_path = args.data
# images = [f for f in os.listdir(image_path) if f.endswith(".png")]
class1 = sorted([f for f in os.listdir(image_path) if f.startswith("airplane")])
# print(class1)

def getFiles(classname):
    return sorted([f for f in os.listdir(image_path) if f.startswith(classname)])

classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck" ]

my_files = {}
for i in range(0, 10):
    my_files[classes[i]] = getFiles(classes[i])
# print(my_files)
# process and resize
path = "./cifar10/"
if not os.path.exists(path):
    os.mkdir("./cifar10")

def create_folder(filename):
    name = re.split("_", filename)[0]
    # print(name)
    path = "./cifar10/" + name
    if not os.path.exists(path):
        os.mkdir(path)
    # print(path)
    return path

def create_images(classname, filename, src):
    des = create_folder(classname)
    image = Image.open(image_path +"/"+ file) 
    image.save(des + "/" + file) 

for key in my_files:
    for file in my_files[key]:
        # print("file", file)
        # print("key", key)
        create_images(key, file, image_path)

