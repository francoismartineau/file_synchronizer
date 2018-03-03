from util import synchronize_files, synchonize_folders
import os, sys



"""
    Synchronizes two files.
    Arg[1] : A file to be copied
    Arg[2] : A file to immitate first file

"""
argument_validity = True
if len(sys.argv[1:]) == 2:
    source = sys.argv[1:][0]
    dest = sys.argv[1:][1]
    if os.path.isfile(source):
        synchronize_files(source, dest)
    elif os.path.isdir(source):
        synchonize_folders(source, dest)
    else:
        argument_validity = False
else:
    argument_validity = False

if not argument_validity:
    print("Arguments are: source_path dest_path")

