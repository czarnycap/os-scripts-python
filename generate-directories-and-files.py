#!/usr/bin/env python3

import os
import random
import string
import argparse

def generate_random_files(root_dir, depth, num_files):
    if depth == 0:
        return
    for i in range(num_files):
        filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.txt'
        filepath = os.path.join(root_dir, filename)
        with open(filepath, 'w') as f:
            f.write('This is a random file.')
    subdirectories = [os.path.join(root_dir, ''.join(random.choices(string.ascii_lowercase, k=5))) for _ in range(3)]
    for subdir in subdirectories:
        os.mkdir(subdir)
        generate_random_files(subdir, depth-1, num_files)

def main():
    parser = argparse.ArgumentParser(description='Generate a random directory structure.')
    parser.add_argument('root_dir', type=str, help='The root directory for the generated directory structure.')
    parser.add_argument('depth', type=int, help='The maximum depth of the directory structure.')
    parser.add_argument('num_files', type=int, help='The number of random files to generate in each directory.')
    args = parser.parse_args()

    if not os.path.exists(args.root_dir):
        os.mkdir(args.root_dir)

    generate_random_files(args.root_dir, args.depth, args.num_files)

if __name__ == '__main__':
    main()

