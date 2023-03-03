#!/usr/bin/env python3
'''This is a script which copies recursively files from one folder to another,
including sub-dirs.'''

import argparse
import os
import shutil
import sys

def main():
    parser = argparse.ArgumentParser(description='Recursively copy files from one folder to another.')
    parser.add_argument('source_folder', help='The source folder to copy files from.')
    parser.add_argument('destination_folder', help='The destination folder to copy files to.')
    args = parser.parse_args()

    source_folder = args.source_folder
    destination_folder = args.destination_folder

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(destination_folder, os.path.relpath(source_file, source_folder))
            try:
                shutil.copy2(source_file, dest_file)
            except IOError as e:
                print(f"Error copying {source_file} to {dest_file}: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
