"""
OOTR random item picker

dummy simple, just returns a random item from
a list of possible starting items

includes c button items and equipment
"""
import random
import os

def main():
    items_path = os.path.join(os.getcwd(), "items.txt")
    items = []
    with open(items_path, "r") as f:
        for line in f.readlines():
            items.append(line.strip())
    
    if items == []:
        print(f"no items found in file '{items_path}'")
        return -1
    
    choice = random.randint(0, len(items))

    print(f"your random item is: '{items[choice]}'")

if __name__ == "__main__":
    main()