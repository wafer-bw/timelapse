import os
import sys
import shutil
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("source_dir", help="Source directory containing the frame images. (Ex: '~/test/images/') Images must be named so that they are sortable. (Ex: YYYY-MM-DD)")
argparser.add_argument("output_dir", help="Output directory of MP4. (Ex: '~/test/movie.mp4')")
argparser.add_argument("-r", "--reverse", action="store_true", help="Reverse sort images before generating.")
argparser.add_argument("-f", "--fps", type=int, default=24, help="Frames per second of output video. (Default: 24)")
argparser.add_argument("-s", "--source_extension", type=str, default=".jpg", help="Extension of source images. (Default: '.jpg')")
args = argparser.parse_args()

if not args.output_dir.endswith(".mp4"):
    sys.exit("Error: Invalid output directory file extension, must use '.mp4'. Use timelapse.py -h for more info.")

# Collect the images to combine into a video
filenames = [image_name for image_name in sorted(os.listdir(args.source_dir)) if image_name.endswith(args.source_extension)]

if not filenames:
    sys.exit("Error: no images found at '" + args.source_dir + "' with extension '" + args.source_extension + "'")

# Get the digit padding to use for the images. Ex: img001.jpg - img112.jpg
padding_count = len(list(str(len(filenames))))

if args.reverse:
    filenames = reversed(filenames)

# Make a temporary directory to store the sequentially named images
temp_dir = args.source_dir + "/timelapse-py_tmp_build_folder"
if os.path.exists(temp_dir):
    sys.exit("Error: Temp directory (" + temp_dir + ") used to build images already exists.")
os.mkdir(temp_dir)

# Create sequentially named images inside the temp directory
for i, filename in enumerate(filenames):
    num = str(i + 1)
    padded_num = ''.join(['0' for _ in range(0, padding_count - len(list(num)))]) + num
    shutil.copyfile(args.source_dir + "/" + filename, temp_dir + "/img" + padded_num + args.source_extension)

# Move into temp directory and create video using sequentially named images
os.chdir(temp_dir)
os.system("ffmpeg -r " + str(args.fps) + " -i img%0" + str(padding_count) + "d" + args.source_extension + " -vcodec mpeg4 -y " + args.output_dir)

# Cleanup temp directory
for filename in os.listdir(temp_dir):
    os.remove(temp_dir + "/" + filename)
os.removedirs(temp_dir)
