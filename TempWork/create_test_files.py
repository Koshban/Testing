''' Test files for the Merge_sorted_files code'''
def create_test_files():
    # Create test files
    # File 1: Numbers increasing by 2
    with open('file1.txt', 'w') as f:
        for i in range(10):
            f.write(f"{(i+1)*2}\n")
    
    # File 2: Odd numbers
    with open('file2.txt', 'w') as f:
        for i in range(10):
            f.write(f"{i*2 + 1}\n")
    
    # File 3: Numbers increasing by 3
    with open('file3.txt', 'w') as f:
        for i in range(10):
            f.write(f"{(i+1)*3}\n")

    # Print original files
    print("Original files content:")
    for filename in ['file1.txt', 'file2.txt', 'file3.txt']:
        print(f"\n{filename}:")
        with open(filename, 'r') as f:
            print(f.read().strip())

if __name__ == "__main__":
    create_test_files()