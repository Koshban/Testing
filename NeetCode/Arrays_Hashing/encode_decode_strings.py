'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode separately

Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

'''
import unittest
e_list = []
def encode_mine(strs: list[str]) -> str:
    global e_list
    e_list = [len(x) for x in strs]
    print(e_list)
    combined_str = ''.join(f'{word}' for word in strs)
    print(combined_str, type(combined_str))
    return combined_str    

def decode_mine(s: str) -> list[str]:
    templist = list(s)
    newlist = []
    print(templist)
    for i, n in enumerate(e_list):        
        newword = ''
        try:
            for i in range(n):
                newword += templist.pop(0)
            print(newword)
            newlist.append(newword)
        except:
            continue
    return newlist
            
def encode(strs: list[str]) -> str:
    result = ''
    for s in strs:
        result += str(len(s)) + '#' + s
    return result

def decode(s: str) -> list[str]:
    print(f"S is {s}")
    result, i = [], 0

    while i < len(s): # s = wesay:yes!@#$%^&*()
        j = i
        while s[j] != '#':
            j += 1
        print(f"I {i} and J {j}")
        lengthofstr = int(s[i:j])
        result.append(s[j + 1  : j + 1 + lengthofstr])
        i = j + 1 + lengthofstr                
        print(result)
    return result

if __name__ == "__main__":
    encodedstr = encode(strs=["we","say",":","yes","!@#$%^&*()"])
    print(encodedstr)
    decoded_list = decode(s=encodedstr)
    print(decoded_list)
