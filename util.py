import os, shutil, optparse



def synchronize_files(source, dest):
    if check_file_paths(source, dest):
        dest = open(dest, 'wb')
        dest.write(open(source, 'rb').read())
        dest.close()

def check_file_paths(source, dest):
    validity = True
    if not os.path.isfile(source):
        print("Source: " + source + " isn't a file.")
        validity = False
    elif not os.path.isfile(dest):
        validity = input("Dest file: \"" + dest + "\" doesn't exist. Proceed? y/n\n") == 'y'
    return validity

def synchonize_folders(source, dest):
    if check_folders_paths(source, dest):
        os.mkdir(dest)
        for (path, dir_names, file_names) in os.walk(source):
            for d in dir_names:
                os.mkdir(os.path.join(dest, d))
            for f in file_names:
                source_path = os.path.join(path, f)
                dest_path = dest + source_path[len(source):]
                dest_file = open(dest_path, 'wb')
                dest_file.write(open(source_path, 'rb').read())
                dest_file.close()


def check_folders_paths(source, dest):
    validity = True
    if not os.path.isdir(source):
        print("Source: " + source + " isn't a directory.")
        validity = False
    elif not os.path.isdir(dest):
        validity = input("Dest folder: \"" + dest + "\" doesn't exist. Proceed? y/n\n") == 'y'
    else:
        shutil.rmtree(dest)
    return validity

