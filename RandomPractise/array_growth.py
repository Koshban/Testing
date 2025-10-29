''' growth in size of a list'''

import sys

def growth_array(k: int = 20) -> None:
    data = [i for i in range(k)]
    print(data)
    sizeofarr = sys.getsizeof(data)
    for i in range(k):
        lenoflist = len(data)
        data.pop()
        temp_sizeofarr = sys.getsizeof(data)                  
        
        if temp_sizeofarr != sizeofarr:            
            print(f"Inside I: {i} and Length : {lenoflist} and Size : {temp_sizeofarr}")
            sizeofarr = temp_sizeofarr      
        

if __name__ == "__main__":
    growth_array()
