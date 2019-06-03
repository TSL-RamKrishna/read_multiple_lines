#!/usr/bin/env python3
import sys

class multi_read_lines():

    def __init__(self, infile, N):

        self.infile = infile
        self.N = N

    def open_infile(self):
        ''' opens the infile '''
        self.fh = open(self.infile, 'r')


    def multilines(self):
        ''' reads N number of lines and return an iterable array of N lines'''
        self.lines=[]
        for x in range(self.N):
            oneline = self.fh.readline().rstrip()
            if oneline is '':
                return []       # this makes sure, it returns only the number of lines divisible by N
            else:
                self.lines.append(oneline)

        return self.lines


if __name__=="__main__":

    test = multi_read_lines(sys.argv[1], 4)

    test.open_infile()
    while True:
        data = test.multilines()
        if data == []:
            break
        else:
            print(data)
