import shutil
import sys

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

shutil.copytree(source_folder, destination_folder)

