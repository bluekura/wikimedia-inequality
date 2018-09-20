#-*- coding: utf-8 -*-
__author__ = 'jhyun'

# Fastest version using line by line parsing. 

import xml.etree.ElementTree as ET
import datetime
import sys
import os
import glob

infile = sys.argv[1]
outfile = "./gini_for_editnum_growing/" + infile + ".gini_for_editnum_growing" 
resolution = int(sys.argv[2])

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

def get_bytes(s):
    i = s.find("bytes")
    bytes = s[i:].split("\"")[1]
    return float(bytes)

def main():
    temptime = -1
    timestamp = []
    currentid = ""
    cont_marker = 0
    id = {}
    id_list = []
    f_out = open(outfile, 'wb')
    f_out.write("#Editnumber\tGiniCoefficient\n")
    with open(infile) as f:
        for line in f:
            if(line.find('</revision>')>0):
                right_pos = 0
                if(temptime != -1):
                    id_list.append(currentid)
                    timestamp.append(temptime)
                else:
                    print temptime
                    print currentid
                temptime = -1
                currentid = ""
                buff_contents = ""
            elif(line.find('<timestamp>') > 0):
                temptime = datetime.datetime.strptime(line.strip()[11:-12], "%Y-%m-%dT%H:%M:%SZ")
                if(len(timestamp)==0):
                    continue
            elif(line.find('<contributor>') > 0):
                cont_marker = 1
            elif(line.find('<id>') > 0 and cont_marker == 1):
                currentid = line.strip()[4:-5]
            elif(line.find('<ip>') > 0 and cont_marker == 1):
                currentid = line.strip()[4:-5]
            elif(line.find('</contributor>') > 0):
                cont_marker = 0

    timestamp, id_list = (list(t) for t in zip(*sorted(zip(timestamp,id_list))))

    for i in range(len(timestamp)):
        if(id_list[i] in id):
            id[id_list[i]] = id[id_list[i]] + 1
        else:
                    #print line.strip()[4:-5]
            id[id_list[i]] = 1
        if(i%resolution == 0):
            f_out.write(str(i) + "\t" + str(gini(id.values())) + "\n")
    return 0
            
if(__name__ == "__main__"):
    main()
