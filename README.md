# timelapse
Generate a timelapse as .gif or .mp4 from set of images.

## Requires
* Python 2.7.15 - Python 3.6.4
* ffmpeg and dependencies
* imageio and dependencies

## Setup
1. `git clone https://github.com/wafer-bw/timelapse.git`
2. `cd timelapse`
3. `apt-get install libav-tools`
4. `apt-get install ffmpeg`
5. `pip install -r requirements.txt`

## gif.py
Generate small timelapses in GIF format. If this script runs out of memory you'll need to switch to `mp4.py`.

### Usage
```
usage: gif.py [-h] [-r] [-f FRAME_DURATION] [-s SOURCE_EXTENSION]
              source_dir output_dir

positional arguments:
  source_dir            Source directory containing the frame images. (Ex:
                        '~/test/images/') Images must be named so that they
                        are sortable. (Ex: YYYY-MM-DD)
  output_dir            Output directory of GIF. (Ex: '~/test/movie.gif')

optional arguments:
  -h, --help            show this help message and exit
  -r, --reverse         Reverse sort images before generating.
  -f FRAME_DURATION, --frame_duration FRAME_DURATION
                        Duration of each frame. (Default: 0.25)
  -s SOURCE_EXTENSION, --source_extension SOURCE_EXTENSION
                        Extension of source images. (Default: '.jpg')
```

## mp4.py
Generate large timelapses in MP4 format.

### Usage
```
usage: mp4.py [-h] [-r] [-f FPS] [-s SOURCE_EXTENSION] source_dir output_dir

positional arguments:
  source_dir            Source directory containing the frame images. (Ex:
                        '~/test/images/') Images must be named so that they
                        are sortable. (Ex: YYYY-MM-DD)
  output_dir            Output directory of MP4. (Ex: '~/test/movie.mp4')

optional arguments:
  -h, --help            show this help message and exit
  -r, --reverse         Reverse sort images before generating.
  -f FPS, --fps FPS     Frames per second of output video. (Default: 24)
  -s SOURCE_EXTENSION, --source_extension SOURCE_EXTENSION
                        Extension of source images. (Default: '.jpg')
```