import os
import sys
import imageio
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("source_dir", help="Source directory containing the frame images. (Ex: '~/test/images/') Images must be named so that they are sortable. (Ex: YYYY-MM-DD)")
argparser.add_argument("output_dir", help="Output directory of GIF. (Ex: '~/test/movie.gif')")
argparser.add_argument("-r", "--reverse", action="store_true", help="Reverse sort images before generating.")
argparser.add_argument("-f", "--frame_duration", type=float, default=0.25, help="Duration of each frame. (Default: 0.25)")
argparser.add_argument("-s", "--source_extension", type=str, default=".jpg", help="Extension of source images. (Default: '.jpg')")
args = argparser.parse_args()

if ".gif" not in args.output_dir:
    sys.exit("Error: Invalid output directory file extension, must use '.gif'. Use timelapse.py -h for more info.")

try:
    images = [imageio.imread(args.source_dir + "/" + image) for image in sorted(os.listdir(args.source_dir)) if image.endswith(args.source_extension)]
except MemoryError:
    sys.exit("Error: Ran out of memory, use mp4.py instead.")

if not images:
    sys.exit("Error: no images found at '" + args.source_dir + "' with extension '" + args.source_extension + "'")

if args.reverse:
    images = reversed(images)

imageio.mimsave(args.output_dir, images, duration=args.frame_duration)
