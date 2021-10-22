import hashlib
import random

def gridbuilder():
    gridlist = []
    index = 0
    rindex = 0
    cindex = 0
    grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
        
    for rindex in range(0,6): #for the 6 rows prior to the row of 15 digits
        row = []
        for cindex in range (0,9):
            row.append(grid[index])
            index = index + 1
        for cindex in range(9,15):
            row.append('Invalid')
        gridlist.append(row)
        
    for rindex in range(6,9): #for the 3 middle rows that have 15 digits
        row = []
        for cindex in range(0,15):
            row.append(grid[index])
            index = index + 1
        gridlist.append(row)
        
    for rindex in range(9,15): #final rows where empty portions are at beginning of row
        row = []
        for cindex in range(0,6): #the portion of emptiness
            row.append('Invalid')
        for cindex in range(6,15):
            row.append(grid[index])
            index = index + 1
        gridlist.append(row)

    prehash = ""
    for cindex in range(0,15): #working from top down to form the hash. 
        for rindex in range(0,15):
            if gridlist[rindex][cindex] != 'Invalid': #removing the invalid that represent the blank areas within the 15x15 area
                prehash += str(gridlist[rindex][cindex])
    
    
    myHash = hashlib.sha256() #given formula from assignment 4
    myHash.update(prehash.encode())
    myHashDigest = myHash.hexdigest()
    randomStart = random.randint(0, len(myHashDigest) - 8)
    rnghash = myHashDigest[randomStart:randomStart + 8]
    print(rnghash)


if __name__ == "__main__":
    gridbuilder()
    
                