#ORAsterbater.py

ORAsterbater is a content pipeline for openraster graphics. While building game graphics every additional asset adds multiple operations to your pipeline. For example a game with 30 monsters, with 3 frames each, 8 status icons, and six backgrounds with 3 paragraph layers:

``
= (30*3)+8+(6*3)
= 116 images
``

That's 116 separate exports, with god knows how many file-ops. As the asset tree grows this problem becomes more pronounced. Orasturbator reads a tree containing .ora files, and exports them to a specified project asset directory.

###Features

- [x] 256*256 thumbnail
- [ ] full flattened image with transparency
- [ ] export layers to separate files
- [ ] automatic flattening of layer groups
- [ ] easy config.ini
- [ ] output report for missing frames
- [ ] useful -h --help switch
- support multiple operating systems
    - [x] linux
    - [ ] windows
    - [ ] mac OS

###usage

Move `orasturbater.py` to the root directory of your assets and call it with `python3 orasturbater.py`
