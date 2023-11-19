import os
import shutil
from PIL import Image
train_path = r'./train/'
val_path = r'./valid/'
test_path = r'./test/'

#ignore csv files in train path
train = [f for f in os.listdir(train_path) if f.endswith('.png') or f.endswith('.jpg')]
val = [f for f in os.listdir(val_path) if  f.endswith('.png') or f.endswith('.jpg')]
test = [f for f in os.listdir(test_path) if  f.endswith('.png') or f.endswith('.jpg')]

#create image folder and mask folder
if os.path.exists(train_path + 'image/') == False:
    os.mkdir(train_path + 'image/')
if os.path.exists(train_path + 'mask/') == False:
    os.mkdir(train_path + 'mask/')
if os.path.exists(val_path + 'image/') == False:
    os.mkdir(val_path + 'image/')
if os.path.exists(val_path + 'mask/') == False:
    os.mkdir(val_path + 'mask/')
if os.path.exists(test_path + 'image/') == False:
    os.mkdir(test_path + 'image/')
if os.path.exists(test_path + 'mask/') == False:
    os.mkdir(test_path + 'mask/')

for file in train:
    if 'mask' in file:
        shutil.move(train_path + file, train_path + 'mask/' + file)
    else:
        shutil.move(train_path + file, train_path + 'image/' + file)
for file in val:
    if 'mask' in file:
        shutil.move(val_path + file, val_path + 'mask/' + file)
    else:
        shutil.move(val_path + file, val_path + 'image/' + file)
for file in test:
    if 'mask' in file:
        shutil.move(test_path + file, test_path + 'mask/' + file)
    else:
        shutil.move(test_path + file, test_path + 'image/' + file)

# now go to the mask folder and then edit the mask images

train_masks = [f for f in os.listdir(train_path + 'mask/') if f.endswith('.png') or f.endswith('.jpg')]
val_masks = [f for f in os.listdir(val_path + 'mask/') if f.endswith('.png') or f.endswith('.jpg')]
test_masks = [f for f in os.listdir(test_path + 'mask/') if f.endswith('.png') or f.endswith('.jpg')]

for file in train_masks:
    # open the mask file and then set pixel values of 2 to 255 and background to transparent 0 png
    img = Image.open(train_path + 'mask/' + file)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 2 and item[1] == 2 and item[2] == 2:
            newData.append((255, 255, 255, 1))
        else:
            newData.append((0, 0, 0, 0))