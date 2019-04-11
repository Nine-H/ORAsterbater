#! /usr/bin/env python3

# ORAsterizer
# Nine-H_2017.05.31
# Content pipeline for openraster graphics.

import click
import os
import zipfile
from PIL import Image
import xml.etree.ElementTree as ET

THUMBNAIL_FILE = os.path.join('Thumbnails','thumbnail.png')
META_DATA = 'stack.xml'

def process(ora, tmp, out_dir):
    data = re.findall('\w+', ora)  # data[0] = directory #data[1] = filename
    click.echo('opened: '+data[1])
    ora_ref = zipfile.ZipFile(ora, 'r')
    ora_ref.extractall(tmp)  # don't pass this reference, just use the file tree.
    os.mkdirs(os.path.join(out_dir, data[0]))
    xml = ET.parse(os.path.join(tmp, META_DATA))
    click.echo(xml)
    root = xml.getroot()
    click.echo(root.tag, root.attrib['h'], root.attrib['w'])
    create_new_buffer(int(root.attrib['h']), int(root.attrib['w']))
    for elem in root:
        ora_tree(tmp, elem, data[0], data[1], int(root.attrib['h']), int(root.attrib['w']))
    dump(out_dir, data[1], data[0])

def ora_tree(tmp, elem, directory, name, h, w):
    if elem.tag == 'layer':
        click.echo('layer operations')
        click.echo(elem.tag, elem.attrib['composite-op'], elem.attrib['name'], elem.attrib['opacity'], elem.attrib['src'], elem.attrib['visibility'], elem.attrib['x'], elem.attrib['y'])
        add_to_buffer(tmp, elem.attrib['src'])
    if elem.tag == 'stack':
        click.echo('stack operations')
        if 'name' in elem.attrib:
            click.echo(elem.tag, elem.attrib['composite-op'], elem.attrib['name'], elem.attrib['opacity'], elem.attrib['visibility'])
            if elem.attrib['name'] == 'skip':
                return
            global layer_group
            dump(name, directory)
            create_new_buffer(h, w)
            layer_group = elem.attrib['name']
        for child in elem:
            ora_tree(child, directory, name, h, w)


# FIXME: I probably shouldn't be abusing globals like this
def create_new_buffer(height, width):
    global image_buffer
    image_buffer = Image.new('RGBA', (height, width), (255, 0, 0, 0))


def add_to_buffer(tmp, filename):
    click.echo("flattening layer groups, god help us all")
    global image_buffer
    file = Image.open(tmp+filename)
    image_buffer = Image.alpha_composite(file, image_buffer)


def dump(out_dir, name, directory):
    click.echo('woot woot get the loot')
    global layer_group
    global image_buffer
    try:
        layer_group = "_"+layer_group
    except:
        layer_group = ""
    click.echo(os.path.join(".", out_dir, directory, name+"_"+layer_group+".png"))
    image_buffer.save(os.path.join(".", out_dir, directory, name+"_"+layer_group+".png"))
    del layer_group

@click.command()
@click.option('--src_dir', default='./', help='Path to source directory')
@click.option('--tmp', default='./.tmp/', help='Path to temp directory')
@click.option('--out_dir', default='./build/', help='Path to output directory')
@click.option('--keep', default=False, help='Save temp directory for debug')
def main (src_dir, tmp, out_dir):
    '''
    Content management pipeline for openraster graphics.
    
    docs/examples/contribute @ https://github.com/nine-h/orasterizer
    '''
    if not os.path.exists(src_dir):
        click.echo("error: source folder "+src_dir+" not found!")
        quit()
    if not os.path.exists(tmp):
        os.makedirs(tmp)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    content_files = []
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            if ".ora" in filename:
                click.echo("found content: "+os.path.join(dirpath,filename))
                content_files.append(os.path.join(dirpath,filename))
    [process(i, tmp, out_dir) for i in content_files]
    if not keep:
        os.rmdir(tmp)

if __name__ == '__main__':
    main()
