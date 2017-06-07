#!/usr/bin/python3

# ORAsterizer.py

# Nine-H_2017.05.31

# Content pipeline for openraster graphics.


import subprocess #FIXME remove
import re #FIXME remove

import os
import zipfile
from PIL import Image
import xml.etree.ElementTree as ET

BASE_PATH=""
RELATIVE_PATH='../test/'
THUMBNAIL_FILE='Thumbnails/thumbnail.png'
META_DATA='stack.xml'
TMP_DIR='./tmp/'
OUTPUT_DIR='./build/'

def for_image(ora):
    clean_up()
    data = re.findall('\w+', ora) #data[0] = directory #data[1] = filename
    print('opened: '+data[1])
    ora_ref = zipfile.ZipFile(ora, 'r')
    ora_ref.extractall(TMP_DIR)#don't pass this reference, just use the file tree.
    os.system('mkdir -p '+OUTPUT_DIR+'/'+data[0]+'/')
    xml = ET.parse(TMP_DIR+META_DATA)
    print (xml)
    root = xml.getroot()
    print (root.tag, root.attrib['h'], root.attrib['w'])
    create_new_buffer(int(root.attrib['h']),int(root.attrib['w']))
    for elem in root:
        ora_tree(elem)
    print ('woot woot get the loot')
    dump (data[1], data[0])
    
def clean_up():
    os.system ('rm -rf '+TMP_DIR)

def ora_tree(elem):
    if elem.tag == 'layer':
        print (elem.tag, elem.attrib['composite-op'], elem.attrib['name'], elem.attrib['opacity'], elem.attrib['src'], elem.attrib['visibility'], elem.attrib['x'], elem.attrib['y'])
        add_to_buffer(elem.attrib['src'])
    if elem.tag == 'stack':
        if 'name' in elem.attrib:
            print (elem.attrib['composite-op'], elem.attrib['name'], elem.attrib['opacity'], elem.attrib['visibility'])
            if elem.attrib['name'] == 'skip':
                return
        for child in elem:
            ora_tree(child)

#FIXME: I probably shouldn't be abusing globals like this
def create_new_buffer(height, width):
    global image_buffer
    image_buffer = Image.new('RGBA', (height, width), (255, 0, 0, 0))
    
def add_to_buffer(filename):
    print ("flattening layer groups, god help us all")
    global image_buffer
    file = Image.open(TMP_DIR+filename)
    image_buffer = Image.alpha_composite(file, image_buffer)

def dump(name,directory):
    global layer_group
    global image_buffer
    image_buffer.save('./'+OUTPUT_DIR+directory+"/"+name+'_'+'layer_group'+'.png')

#FIXME: I probably shouldn't be abusing the unix shell like this
find = subprocess.run(['find', '-depth', '-name', '*.ora'], stdout=subprocess.PIPE)
image_list = find.stdout.decode('utf-8')
for image in image_list.splitlines():
    for_image(image)
clean_up() # Commenting this line leaves last TMP_DIR state on disk for debug purposes
