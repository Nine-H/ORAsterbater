#!/usr/bin/python3

# ORAsterbater.py

# Nine-H_2017.05.31

# Content pipeline for openraster graphics.

import os
import zipfile
import subprocess
import re
import xmltodict
from PIL import Image

BASE_PATH="~/Projects/UnnamedMonsters/Assets/Sprites/"
RELATIVE_PATH='../test/'
THUMBNAIL_FILE='Thumbnails/thumbnail.png'
META_DATA='stack.xml'
TMP_DIR='./tmp/'
OUTPUT_DIR='./build/'

def for_image(ora):
    clean_up()
    data = re.findall('\w+', ora) #data[0] = directory #data[1] = filename
    ora_ref = zipfile.ZipFile(ora, 'r')
    ora_ref.extractall(TMP_DIR)#don't pass this reference, just use the file tree.
    os.system('mkdir -p '+OUTPUT_DIR+'/'+data[0]+'/')
    ora_xml = read_xml()
    flatten(data[0],data[1])
    #print (ora_xml['image']['stack']['stack'])
    #os.system('mv '+TMP_DIR+THUMBNAIL_FILE+' ./'+OUTPUT_DIR+data[0]+'/'+data[1]+'.png')

def clean_up():
    os.system ('rm -rf '+TMP_DIR)

def read_xml():
    f = open (TMP_DIR+'stack.xml')
    return xmltodict.parse(f.read())
    
def flatten(directory, name):
    print ("flatten_layer_groups: "+name)
    foreground = Image.open(TMP_DIR+'data/001-000.png')
    background = Image.open(TMP_DIR+'data/001-001.png')
    background = Image.alpha_composite(background, foreground)
    background.save('./'+OUTPUT_DIR+directory+'/'+name+'.png')
    
find = subprocess.run(['find', '-depth', '-name', '*.ora'], stdout=subprocess.PIPE)
image_list = find.stdout.decode('utf-8')
for image in image_list.splitlines():
    for_image(image)
clean_up() # Commenting this line leaves last TMP_DIR state on disk for debug purposes
