'''You left your computer unlocked and your friend decided to troll you by copying a lot of your files to random spots all over your file system.

Even worse, she saved the duplicate files with random, embarrassing names ("this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).

Write a function that returns a list of all the duplicate files. We'll check them by hand before actually deleting them, since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return a list of tuples ↴ where:

the first item is the duplicate file
the second item is the original file
For example:

  [('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
 ('/home/trololol.mov', '/etc/apache2/httpd.conf')]
You can assume each file was only duplicated once.

Approach : Use cryptographic Hash function e.g. SHA256 to find the dupes ?
1)  Data Structures
 1.1 ) Create a dictionary file_hashes {} of format {'hashid' : 'abspath/filename }
 1.2 ) Create another tuple of format ('abspath/dupefilename', 'abspath/originalfilename')
 1.3 ) Append to finallist
2)  Algo
 2.1 ) Recursively traverse the file system
 2.2 ) Find a file, Hash it
 2.3 ) if HashKey already exists in file_hashes , then add to tuple
 2.4 ) If not, add to the dictionary

'''

import os
import hashlib
import xxhash
import pprint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"Base directory is : {BASE_DIR}")
ignore_folders = ["/tmp", "koshenv"]

def should_skip_path(path, exclude_folders):
    # Convert DirEntry to string if necessary
    path_str = path.path if isinstance(path, os.DirEntry) else str(path)

    if any(excluded in path_str for excluded in exclude_folders):
        return True
    
    path_parts = path_str.split(os.sep)
    return any(part.startswith('.') for part in path_parts)

def traverse_directory(directory, exclude_folders, file_hashes, duplicates):
    try:
        for entry in os.scandir(directory):
            if entry.is_symlink():
                continue # Skip Symlinks

            if entry.is_dir():
                if not should_skip_path(path=entry, exclude_folders=exclude_folders):
                    traverse_directory(directory=entry.path, exclude_folders=exclude_folders, file_hashes=file_hashes, duplicates=duplicates)
            else:
                if not os.path.basename(entry.path).startswith('.'):
                    process_file(file_path=entry.path, file_hashes=file_hashes, duplicates=duplicates)    

    except PermissionError:
        print(f"Permission Denied on : {directory}")

def hash_file(filename):
    try:
        #h = hashlib.sha256()
        h = xxhash.xxh64()
        with open(file=filename, mode='rb', buffering=0) as f:
            for b in iter(lambda : f.read(128 * 1024), b''): #iter(func, sentinel) creates an iterator that calls func until it returns the sentinel value.
                h.update(b)
            return h.hexdigest() # hexdigest() returns the hash as a string of hexadecimal digits
    except Exception as e:
        print(f"Encountered error in hash_file for file ; {filename}. Error is :{str(e)}")
        return None


def get_file_info(file_path):
    try:
        if os.name == 'nt':
            creation_time = os.path.getmtime(file_path)
        else:
            creation_time = (os.stat(file_path)).st_mtime
        return {
            'path': file_path,
            'creation_time': creation_time,
            'size': os.path.getsize(file_path)
        }
    except Exception as e:
        print(f"Encountered error in file_info for file ; {file_path}. Error is :{str(e)}")
        return None


def process_file(file_path, file_hashes, duplicates):
    try:
        #print(f"1: {file_path}")
        file_info = get_file_info(file_path)
        #print(f"2: {file_path}")
        if file_info is None:
            print(f"Skipping file due to error: {file_path}")
            return
        file_hash = hash_file(file_path)
        if file_hash in file_hashes:
            existing_info = file_hashes[file_hash]
            if file_info['creation_time'] < existing_info['creation_time']:
                # Current file is older, treat it as original
                duplicates.append((existing_info['path'], file_path))
                file_hashes[file_hash] = file_info
            else:
                # Current file is newer, treat it as duplicate
                duplicates.append((file_path, existing_info['path']))
        else:
            file_hashes[file_hash] = file_info
    except Exception as e:
        print(f"Caught Exception in process_file while processing Path : {file_path}. Error is : {str(e)}")
    
def find_files(root_dir, exclude_folders=None) -> list[str]:
    if exclude_folders is None:
        exclude_folders = []

    file_hashes = {}
    duplicates = []
    
    traverse_directory(directory=root_dir, exclude_folders=exclude_folders, file_hashes=file_hashes, duplicates=duplicates)
    return duplicates

def main():
    
    duplicate_files = find_files(root_dir=BASE_DIR, exclude_folders=ignore_folders)
    for dupe, original in duplicate_files:
        print(f"Duplicate: {dupe}")
        print(f"Original: {original}")
        print()
    #pprint.pprint(duplicate_files)

if __name__ == "__main__":
    main()
    
