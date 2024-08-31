

def maximumSum(mylist: list) -> int:
    sumofnums = 0
    max_sum = -float('inf')
    for num in mylist:
        sumofnums = max(num, sumofnums + num)
        max_sum = max(max_sum, sumofnums)
        print(f"Num : {num} sumofnums : {sumofnums} and max_sum: {max_sum}")

    return int(max_sum)

if __name__ == '__main__':
    test_input = [-1, 3, 4, -2, 5, -7]
    print(maximumSum(mylist=test_input))



