''' du equivalent'''
import os

def find_disk_usage(path: str) ->int:
    total = os.path.getsize(path)
    print(f"1. {total}",path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += find_disk_usage(childpath)
    print(f"2. {total}",path)
    return total

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(f"We are in : {BASE_DIR}")
    #find_disk_usage("c:\\Users\\kaush\\OneDrive\\Desktop\\Code\\Testing\\NeetCode")
    find_disk_usage(BASE_DIR)