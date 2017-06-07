#!/usr/bin/python3

# ora_tree.py

# Nine_H_2017.6.2

# dump data from current stack.xml in tmp to stdout

import xml.etree.ElementTree as ET

def recursive_tree(elem):
    if elem.tag == 'layer':
        print (elem.tag, elem.attrib['composite-op'], elem.attrib['name'], elem.attrib['opacity'], elem.attrib['src'], elem.attrib['visibility'], elem.attrib['x'], elem.attrib['y'])
    if elem.tag == 'stack':
        if 'name' in elem.attrib:
            print (elem.attrib['composite-op'], elem.attrib['name'], elem.attrib['opacity'], elem.attrib['visibility'])
        for child in elem:
            recursive_tree(child)

tree = ET.parse('./tmp/stack.xml')
print (tree)
root = tree.getroot()
print (root.tag, root.attrib['h'], root.attrib['w'])
for elem in root:
    recursive_tree(elem)
