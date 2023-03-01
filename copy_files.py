import shutil
import sys
import os

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_file = os.path.join(root, file)
        dest_file = os.path.join(destination_folder, os.path.relpath(source_file, source_folder))
        shutil.copy2(source_file, dest_file)

