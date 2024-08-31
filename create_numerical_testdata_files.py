''' 
Write a Python code to create a 4 big files each of which has 
Only random numbers from 1 to 100,000,000
One number only once in any of the 4 files
'''

import random
import os

def create_large_files(num_files=4, max_num=100_000_000, chunk_size=1_000_000):
    # Create a set of all numbers from 1 to max_num
    all_numbers = set(range(1, max_num + 1))
    
    file_sizes = [max_num // num_files] * num_files
    # Distribute any remainder
    for i in range(max_num % num_files):
        file_sizes[i] += 1

    for file_num in range(num_files):
        filename = f"large_file_{file_num + 1}.txt"
        file_size = file_sizes[file_num]
        
        with open(filename, 'w') as f:
            numbers_written = 0
            while numbers_written < file_size:
                # Determine how many numbers to write in this chunk
                chunk_numbers = min(chunk_size, file_size - numbers_written)
                
                # Get a chunk of unique random numbers
                chunk = random.sample(list(all_numbers), chunk_numbers)
                
                # Write the numbers to the file
                f.write('\n'.join(map(str, chunk)) + '\n')
                
                # Remove these numbers from the set of available numbers
                all_numbers -= set(chunk)
                
                numbers_written += chunk_numbers
                
                # Print progress
                print(f"File {file_num + 1}: {numbers_written / file_size * 100:.2f}% complete")
        
        print(f"File {filename} created with {file_size} numbers")
        print(f"File size: {os.path.getsize(filename) / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    create_large_files()