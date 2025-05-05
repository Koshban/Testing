"""
You are given a string consisting of lowercase English letters. Repeatedly remove adjacent duplicate letters, one pair at a time. 
Both members of a pair of adjacent duplicate letters need to be removed.
"""

def remove_adj_dupes(input: str) -> str:
    stack = []
    for s in input:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)

def main():
    inputs = ["g", 
        "ggaabcdeb", 
        "abbddaccaaabcd",
        "aannkwwwkkkwna", 
        "abbabccblkklu"
    ]

    for index, element in enumerate(inputs):
        print("-" * 110)
        print(index +1, ".\tInput Element is :", element)
        print(f"\tAfter removing Adjacent dupes, {element} becomes", remove_adj_dupes(input=element))
        print("-" * 110)

if __name__ == '__main__':
    main()