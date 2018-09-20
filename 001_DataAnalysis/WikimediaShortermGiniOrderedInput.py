#-*- coding: utf-8 -*-
__author__ = 'jhyun'

import datetime
import sys
import csv

def gini(list_of_values):
    if(list_of_values.count(list_of_values[0]) == len(list_of_values)):
        if(list_of_values[0] == 0):
            return -1
        else:
            return 0
    sorted_list = sorted(list_of_values)
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2.
    fair_area = height * len(list_of_values) / 2
    return (fair_area - area) / fair_area

def isNotNumber(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

infile = sys.argv[1]
outfile = sys.argv[1] + ".shorterm_gini_for_" + sys.argv[2] + "_edits"
resolution = int(sys.argv[2])

def main():
    ind = 0
    f_out = open(outfile, 'wb')
    id = {}
    with open(infile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in reader:
            if(len(row[0]) != 0 and row[0][0] == "#"):
                continue
            if(row[0] in id):
                id[row[0]] = id[row[0]] + 1
            else:
                id[row[0]] = 1
            if(ind%resolution == 0):
                f_out.write(str(ind) + "\t" + str(gini(id.values())) + "\n")
                id = {}
            ind = ind + 1
     str(gini(id.values())) + "\n")
        return 0
            
if(__name__ == "__main__"):
    main()
