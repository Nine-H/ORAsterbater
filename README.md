# ORAsterizer.py

ORAsterizer is a content pipeline for openraster graphics. While building game graphics every additional asset adds multiple operations to your pipeline. For example a game with 30 monsters, with 3 frames each, 8 status icons, and six backgrounds with 3 paragraph layers:

``
= (30*3)+8+(6*3)
= 116 images
``

That's 116 separate exports, with god knows how many file-ops. As the asset tree grows this problem becomes more pronounced. Orasterizer reads a tree containing .ora files, and exports them to a specified project asset directory.

### features

- [x] full flattened image with transparency
- [ ] export layer groups to separate files
- [x] automatic flattening of layer groups
- [x] skip layers
- [ ] easy config.ini
- [ ] output report for missing frames
- [ ] handy -h --help switch
- OS support
- [x] linux
- [ ] windows
- [ ] mac OS

### usage

Move `orasterizer.py` to the root directory of your assets and call it with `./orasterizer.py`

### examples

filename | export (gimp) | orasterized
--|--|--
basic.ora | ![](ORAsterizer/test_exported/basic.png) | ![]()
separate_layers.ora | ![]() | ![]() ![]()
skip.ora | ![]() | ![]()
