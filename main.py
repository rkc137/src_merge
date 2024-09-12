import os
import argparse

parser = argparse.ArgumentParser(description = "merge all folders files into common one")
parser.add_argument("input_folder", help = "input folder")
parser.add_argument("-o", default = "data.txt", help = "output file")
parser.add_argument("--ext", default = "cpp;hpp", help = "extensions list, seps by ;")

args = parser.parse_args()

exts = []
for ext in args.exts.split(';'):
    ext = ext.strip()
    if(ext[0] != '.'):
        ext = '.' + ext
    exts.append(ext)

with open(args.output_file, 'w', encoding = "utf-8") as outfile:
    for root, dirs, files in os.walk(args.input_folder):
        for file in files:
            if any(file.endswith(ext) for ext in exts):
                file_path = os.path.join(root, file)
                outfile.write(f'\n// {file}\n')
                with open(file_path, 'r', encoding = "utf-8") as infile:
                    outfile.write(infile.read())

print("done")
