# read in a simple file 
# Author Andre Hoarau   
filename= "data.txt"


print(filename)
with open(filename, "rt") as fp:
    total = 0
    for line in fp:
        total += int(line)
        print(f"{line} is size {len(line)}")
    print("")
    print (f"total is {total}")
    
# This prints the number of the characters and it also reads the new lines hence why there is one more 
