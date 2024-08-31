'''Given an array of strings , group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Input: strs = ["x"]
Output: [["x"]]

Input: strs = [""]
Output: [[""]]
'''
import unittest
import re
from collections import defaultdict

def is_anagram_pair(w1: str, w2: str) -> bool:
    print(f"Inside function with w1: {w1} and w2: {w2}")
    w1_dict, w2_dict = {}, {}
    w1 = re.sub(r'[^a-z,A-Z]','',w1)
    w2 = re.sub(r'[^a-z,A-Z]','', w2)
    for c in w1:
        if c in w1_dict.keys():
            w1_dict[c] += 1
        w1_dict[c] = 1    
    for c in w2:
        if c in w2_dict.keys():
            w2_dict[c] += 1
        w2_dict[c] = 1
    
    return w1_dict  == w2_dict

def groupAnagrams_mine(strs: list[str]) -> list[list[str]]:
    temp_hash, final_list = {}, []
    print(strs)
    for word in strs:        
        size = len(word)
        if size in temp_hash.keys():
            temp_hash[size].extend([word])        
        else:
            temp_hash[size] = [word]
    print(temp_hash)
    for key, words in temp_hash.items():
        print(f"at Key: {key} we have words: {words}")
        size = len(words)
        temp_outer_list = []
        if key == 4:
            for idx, word in enumerate(words):
                temp_inner_list =  []
                for i in range(idx + 1, size):                
                    check = is_anagram_pair(w1=word, w2=words[i])
                    if not check:
                        temp_inner_list.append([words[i]])
                        print(f" After append : {temp_inner_list}")
                    else:
                        for list in temp_inner_list:
                            print(f"List is {list} and word is {word} and word2 is {words[i]}")
                            if word in list:
                                if words[i] in list:
                                    pass
                                list.append(words[i])
                                break           
                        else:
                            print(f"In Else word is {word} and word2 is {words[i]}")
                            if word in list:
                                if words[i] in list:
                                    pass
                            list.append(words[i])
                            print(f"Adding in Else : {word} and {words[i]}")
                            #temp_inner_list.append([word, words[i]])
                        print(f" After Extend : {temp_inner_list}")   
                temp_outer_list.extend(temp_inner_list)
                print(f"Temp Outer List is {temp_outer_list}")  
            final_list.extend(temp_outer_list)
            print(f"Final is : {final_list}")

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    print(f"Incoming is {strs}")
    ans = defaultdict(list)

    for s in strs:
        print(f"S is {s}")
        count = [0] * 26
        for c in s:
            print(f" C is {c}")
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
        print(ans)
    return ans.values()

class TestgroupAnagrams(unittest.TestCase):
    def test_groupAnagrams(self):
        test_data = [
            {'input': ["act","pots","tops","cat","stop","hat"], 'expected': [["hat"],["act", "cat"],["stop", "pots", "tops"]]},
            {'input': ["eat","tea","tan","ate","nat","bat", "ant"], 'expected': [["bat"],["nat", "tan", "ant"],["ate", "eat", "tea"]]},
            {'input': ["x"], 'expected': ["x"]},
            {'input': [""], 'expected': [""]}, 
        ]

if __name__ == "__main__":
    # unittest.main()
    print(groupAnagrams(strs=["act","pots","tops","cat","stop","hat"]))