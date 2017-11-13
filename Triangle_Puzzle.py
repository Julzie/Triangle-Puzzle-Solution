#!/usr/bin/env python
import datetime

class Result:
    """ Class to store and manipulate the sum and path to solution"""
    def __init__(self):
        self.sum_keep = 0              # permanent sum, best seen so far
        self.sum_temp = 0             # temporary sum
        self.keep = str()                   # permanent array to keep best solution seen so far
        self.temp = []                       # temporary array to keep path
        self.mem = {}                       # dictionary to keep the already traversed results for future reference
        self.mem_path = {}

    def memoize(self, i,j, max, path):
        self.mem[(i,j)] = [max] + [data[i][j]] +re.mem[path][1:]

    def append(self, var):
        """Append  new item to the path so far"""
        return self.temp.append(var)

    def remove(self, var):
        return self.temp.pop()

    def add_sum(self,var):
        """Add to the sum so far"""
        self.sum_temp = self.sum_temp + var
        return self.sum_temp

    def subs_sum(self,var):
        self.sum_temp = self.sum_temp - var
        return self.sum_temp

    def copy(self):
        """Copy the complete temporary sum and path to permanent one until will find something better"""
        self.sum_keep = self.sum_temp
        self.keep = self.temp

def traverse(i, j):
    """Function to traverse the array"""
    if data[i][j] == data[-1][j]:                               # If reached last row
        re.append(data[i][j])
        re.add_sum(data[i][j])
        if re.sum_keep < re.sum_temp:             # copy the temp result to permanent IF it is a better solution
            re.copy()
            re.sum_keep = re.sum_temp
        return
    else:                                              # append possible next step to partial solution array (temp)
        re.append(data[i][j])
        re.add_sum(data[i][j])
        for c in (0, 1):                                   # loop over left and right option from this cell (data[i][j])
            if (i+1,j+c) in re.mem:                  # If the cell was traversed in the past, return result from mem
                if re.sum_keep < re.sum_temp + re.mem[(i+1,j+c)][0]:
                    re.keep = re.temp + re.mem[(i+1,j+c)][1:]
                    re.sum_keep = re.sum_temp + re.mem[(i+1,j+c)][0]
                continue
            else:
                traverse(i+1,j+c)                       # traverse next cell
                if i+1 == len(data)-1:               # memoize for last row, special case
                    re.mem[(i+1, j+c)] =[data[i+1][j+c]] +  [data[i+1][j+c]]
                else:
                    temp = {key: re.mem[key] for key in [(i+2,j+c), (i+2,j+c+1)]}
                    m = max(zip(temp.values(),temp.keys()))
                    re.memoize(i+1,j+c, m[0][0] + data[i+1][j+c], m[1])   # memoize
                re.remove(data[i + 1][j + c])                       # remove last option before traceback
                re.subs_sum(data[i+1][j+c])


""" Driver program"""

with open('/Users/yulia/Desktop/triangle.txt', newline='') as f:
    data = [[int(digit) for digit in line.split()] for line in f]

re = Result()
len_data = len(data)
tmst = datetime.datetime.now()
traverse(0,0)
print("Running time {} sec.".format(datetime.datetime.now() - tmst))

print("Max Sum: {}".format(re.sum_keep))
print("Path {}".format(re.keep))
