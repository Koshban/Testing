"""
Given an array of integers, and a number sum, find the number of pairs of integers in the array whose sum is equal to sum.
# Test array
arr = [1, 5, 7, -1, 5]

# Target sum
sum = 6
Using this test data, we want to find pairs of numbers in arr that add up to sum (6 in this case).

Here are the pairs that do so in the test array:

Pair (1, 5) at indices 0 and 1 adds up to 6.
Pair (1, 5) at indices 0 and 4 adds up to 6.
Pair (7, -1) at indices 2 and 3 adds up to 6.
"""


def find_pairs_on2(input: list) -> int: # Nested Iterations taking O(n2) time complexity
    try:
        target = input[1]
        arr  = input[0]
        pairs_index = []
        pairs_num = []
        size = len(arr)
        if len(input) > 2:
            return -1
        else:
            for index, num in enumerate(arr):
                for j in range(index + 1, size):
                    if num + arr[j] == target:
                        pairs_index.append([index, j])
                        pairs_num.append([num, arr[j]])
        print(pairs_index)
        print(pairs_num)
        return len(pairs_num)
    except:
        return -1

def find_pairs_on(input: list) -> int: # Taking O(N) time complexity as just one sweep
    print("!!" * 110)
    print(input)
    try:
        target = input[1]
        arr  = input[0]
        pairs_index = []
        pairs_num = []
        size = len(arr)
        dict_store = {}
        if len(input) > 2:
            return -1
        else:
            for index, num in enumerate(arr):
                if num in dict_store:
                    dict_store[num].append(index)
                else:
                    dict_store[num] = [index]
        print(f"Hey there {dict_store}")   

        for index, num in enumerate(arr):
            complement = target - num
            if complement in dict_store.keys():
                print(f"Complement {complement} for NUmber {num} is {dict_store[complement]}")
                for i, x in enumerate(dict_store[complement]):
                    pairs_index.append([min(index, x), max(index, x)])  
                    pairs_num.append([min(num, complement), max(num, complement)])
        print(pairs_num)
        print(pairs_index)
        pairs_index = set(tuple(pair) for pair in pairs_index)
        pairs_num = set(tuple(pair) for pair in pairs_num)
        print(pairs_num)
        print(pairs_index)




    
    except Exception as e:
        print(e)
        return -1

def find_pairs_with_indices_optimized(arr, target_sum):
    # This dictionary will store the value as key and list of indices as value
    num_indices = {}
    for index, num in enumerate(arr):
        if num in num_indices:
            num_indices[num].append(index)
            print(f"ON {index}, {num} the value is {num_indices}")
        else:
            num_indices[num] = [index]
    
    # This will store the pairs and their indices
    pairs_with_indices = []
    
    # This set ensures that we don't count duplicates
    visited = set()

    for index, num in enumerate(arr):
        complement = target_sum - num
        if complement in num_indices:
            for complement_index in num_indices[complement]:
                # Ensure we don't use the same element twice and count unique pairs
                if complement_index > index and (index, complement_index) not in visited:
                    visited.add((index, complement_index))
                    pairs_with_indices.append(((num, arr[complement_index]), (index, complement_index)))
    
    # Return the number of pairs and the list of pairs with indices
    return len(pairs_with_indices), pairs_with_indices

if __name__ == "__main__":
    test_data = [[1, 5, 7, -1, 5], 6]
    arr = [1, 5, 7, -1, 5]
    sum = 6
    print(find_pairs_on2(input=test_data))
    # count, pairs_with_indices = find_pairs_with_indices_optimized(arr, sum)
    # print("Number of pairs:", count)  # Output: Number of pairs: 3
    # print("Pairs with indices:", pairs_with_indices)  # Output: Pairs with indices: [((1, 5), (0, 1)), ((1, 5), (0, 4)), ((7, -1), (2, 3))]
    print("*" * 110)
    print(find_pairs_on(input=test_data))
    print("*" * 110)
    