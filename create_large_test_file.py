import random
import string
import os

def generate_random_text(size=1024):
    return ''.join(random.choices(string.ascii_lowercase + string.digits + ' \n', k=size))

def create_large_file(filename, size_gb=5, keyword="koshban"):
    target_size = size_gb * 1024 * 1024 * 1024  # Convert GB to bytes
    chunk_size = 1024 * 1024  # 1 MB chunks
    keyword_frequency = 1000  # Insert keyword approximately every 1000 chunks

    with open(filename, 'w') as file:
        written_size = 0
        chunk_count = 0

        while written_size < target_size:
            if chunk_count % keyword_frequency == 0:
                chunk = generate_random_text(chunk_size - len(keyword)) + keyword
            else:
                chunk = generate_random_text(chunk_size)
            
            file.write(chunk)
            written_size += len(chunk.encode('utf-8'))
            chunk_count += 1

            # Print progress
            if chunk_count % 100 == 0:
                print(f"Progress: {written_size / target_size * 100:.2f}%")

    print(f"File '{filename}' created successfully.")
    print(f"Final file size: {os.path.getsize(filename) / (1024 * 1024 * 1024):.2f} GB")

if __name__ == "__main__":
    filename = "large_test_file.txt"
    create_large_file(filename)