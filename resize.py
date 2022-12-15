import os
import argparse
from PIL import Image
from numpy import asarray

parser = argparse.ArgumentParser(description='Resize image')
parser.add_argument('--data', type=str, default='test',
                    help='location of the data corpus')
args = parser.parse_args()
image_path = args.data
# images = [f for f in os.listdir(image_path) if f.endswith(".png")]
txt = sorted([f for f in os.listdir(image_path) if f.endswith(".png")])
print(txt)
 
# process and resize

def resize(image, size):
  image = image.resize(size, Image.ANTIALIAS)
#   numpydata = asarray(image)
  return image

path = "./resized/"
if not os.path.exists(path):
    os.mkdir("./resized")
for file in txt:
    image = Image.open(image_path +"/"+ file)
    resized = resize(image, (32, 32))
    # save a image using extension
    resized.save(path + file)





