#-*- coding: utf-8 -*-
__author__ = 'jhyun'

import sys
import csv
import numpy as np

def isNotNumber(s):
    try:
        float(s)
        return False
    except ValueError:
        return True


def pearson_1d(x, y):
    mc_x = x - np.mean(x)
    mc_y = y - np.mean(y)
    a = mc_x.dot(mc_y)
    b = mc_x.dot(mc_x)
    c = mc_y.dot(mc_y)
    return a / (np.sqrt(b) * np.sqrt(c))


infile = sys.argv[1]
outfile = sys.argv[1] + ".correlate_before_after"
point_resolution = int(sys.argv[2])
bin_resolution = int(sys.argv[3])
max_binsize = int(sys.argv[4])

def main():
    f_out = open(outfile, 'wb')

    f_out.write("editnumber\tbinsize\tcorrelation\n")

    ind = 0
    point_index = 0

    editorlist = []

    with open(infile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in reader:
            if(len(row[0]) != 0 and row[0][0] == "#"):
                continue
            editorlist.append(row[0])
            if((ind - 2 * max_binsize) % point_resolution == 0):
                print point_index
                if(point_index < 1):
                    point_index = point_index + 1
                    ind = ind + 1
                    continue
                current = ind - max_binsize
                editor_editnumber = {}
                cur_point = point_index * point_resolution
                for i in xrange(bin_resolution, max_binsize, bin_resolution):
                    for j in range(i - bin_resolution, i):
                       if(editorlist[point_resolution + j] not in editor_editnumber):
                            temp = [0, 1]
                            editor_editnumber[editorlist[point_resolution + j]] = temp
                        else:
                            editor_editnumber[editorlist[point_resolution + j]][1] = editor_editnumber[editorlist[point_resolution + j]][1] + 1

                        if(editorlist[point_resolution - j - 1] not in editor_editnumber):
                            temp = [1, 0]
                            editor_editnumber[editorlist[point_resolution - j - 1]] = temp
                        else:
                            editor_editnumber[editorlist[point_resolution - j - 1]][0] = editor_editnumber[editorlist[point_resolution - j - 1]][0] + 1
                    array = zip(*editor_editnumber.itervalues())
                    f_out.write(str(cur_point) + "\t" + str(i) + "\t" + str(pearson_1d(array[0], array[1])) + "\n")
                editorlist = editorlist[point_resolution:]
                f_out.write("\n")
                point_index = point_index + 1
            ind = ind + 1

            
if(__name__ == "__main__"):
    main()
