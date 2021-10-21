import hashlib
import random


class Build:
    
    def gridbuilder(self, grid):
        gridlist = []
        index = 0
        rindex = 0
        cindex = 0
        
        for rindex in range(0,6): #for the 6 rows prior to the row of 15 digits
            row = []
            for cindex in range (0,9):
                row.append(grid[index])
                index = index + 1
            for cindex in range(9,15):
                row.append('invalid')
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
                row.append('invalid')
            for cindex in range(6,15):
                row.append(grid[index])
                index = index + 1
            gridlist.append(row)
            
