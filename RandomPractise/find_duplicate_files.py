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
import logging
import xxhash
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IGNORE_FOLDERS = {"tmp", "koshenv"}  # folder names without slashes for matching

def should_skip_path(path: str, exclude_folders: set[str]) -> bool:
    # Skip hidden files/folders or excluded folder names anywhere in the path
    parts = Path(path).parts
    if any(part.startswith('.') for part in parts):
        return True
    if exclude_folders.intersection(parts):
        return True
    return False

def hash_file(filepath: str) -> str | None:
    try:
        h = xxhash.xxh64()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(128 * 1024), b''):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        logger.warning(f"Failed to hash file {filepath}: {e}")
        return None

def get_file_info(filepath: str) -> dict | None:
    try:
        stat = os.stat(filepath)
        return {
            'path': filepath,
            'ctime': stat.st_mtime,
            'size': stat.st_size
        }
    except Exception as e:
        logger.warning(f"Failed to get info for file {filepath}: {e}")
        return None

def find_duplicates(root_dir: str, exclude_folders: set[str]) -> list[tuple[str, str]]:
    file_hashes: dict[str, dict] = {}
    duplicates: list[tuple[str, str]] = []

    for current_root, dirs, files in os.walk(root_dir):
        # Modify dirs in-place to prune excluded or hidden folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in exclude_folders]

        # Skip this whole folder if it's excluded or hidden
        if should_skip_path(current_root, exclude_folders):
            continue

        for filename in files:
            if filename.startswith('.'):
                continue
            filepath = os.path.join(current_root, filename)
            if should_skip_path(filepath, exclude_folders):
                continue

            file_info = get_file_info(filepath)
            if file_info is None:
                continue

            file_hash = hash_file(filepath)
            if file_hash is None:
                continue

            if file_hash in file_hashes:
                current_original = file_hashes[file_hash]
                # Oldest file is original
                if file_info['ctime'] < current_original['ctime']:
                    duplicates.append((current_original['path'], filepath))
                    file_hashes[file_hash] = file_info
                else:
                    duplicates.append((filepath, current_original['path']))
            else:
                file_hashes[file_hash] = file_info

    return duplicates

def main():
    duplicates = find_duplicates(BASE_DIR, IGNORE_FOLDERS)
    for dupe, orig in duplicates:
        print(f"Duplicate: {dupe}")
        print(f"Original : {orig}")
        print()

if __name__ == "__main__":
    main()
