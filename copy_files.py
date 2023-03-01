#!/usr/bin/env python3

import shutil
import sys
import os

SOURCE_FOLDER = sys.argv[1]
DESTINATION_FOLDER = sys.argv[2]

if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

for root, dirs, files in os.walk(SOURCE_FOLDER):
    for file in files:
        source_file = os.path.join(root, file)
        dest_file = os.path.join(DESTINATION_FOLDER, os.path.relpath(source_file, SOURCE_FOLDER))
        shutil.copy2(source_file, dest_file)
