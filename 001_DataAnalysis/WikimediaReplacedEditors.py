#-*- coding: utf-8 -*-
__author__ = 'jhyun'

import sys
import csv
import copy

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
outfile = sys.argv[1] + ".replaced_editors_per_" + sys.argv[2] + "_edits"
outfile_acc = sys.argv[1] + ".replaced_editors_per_" + sys.argv[2] + "_edits_accumulated_id"
resolution = int(sys.argv[2])
percentile_resolution = float(sys.argv[3])

def main():
    ind = 0
    f_out = open(outfile, 'wb')
    f_out_acc = open(outfile_acc, 'wb')

    id_perm = {}
    id_now = {}
    id_before = {}

    f_out.write("Editnumber\t")
    f_out_acc.write("Editnumber\t")
    for i in range(1, int(1/percentile_resolution) + 1):
         f_out.write(str(i*percentile_resolution) + "\t")
         f_out_acc.write(str(i * percentile_resolution) + "\t")
    f_out.write("Total#ofEditors\n")
    f_out_acc.write("Total#ofEditors\n")

    with open(infile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in reader:
            if(len(row[0]) != 0 and row[0][0] == "#"):
                continue
            if(row[0] in id_now):
                id_now[row[0]] = id_now[row[0]] + 1
                if (row[0] in id_perm):
                    id_perm[row[0]] = id_perm[row[0]] + 1
                else:
                    id_perm[row[0]] = 0
            else:
                id_now[row[0]] = 1
                if (row[0] in id_perm):
                    id_perm[row[0]] = id_perm[row[0]] + 1
                else:
                    id_perm[row[0]] = 0
            if(ind%resolution == 0):
                list_id_now = sorted(id_now.items(), reverse= True, key=lambda lk: lk[1])
                list_id_before = sorted(id_before.items(), reverse= True, key=lambda lk: lk[1])
                list_id_perm = sorted(id_perm.items(), reverse=True, key=lambda lk: lk[1])
                f_out.write(str(ind) + "\t")
                f_out_acc.write(str(ind) + "\t")
                for i in range(1, int(1/percentile_resolution) + 1):
                    f_out.write(str(float(len(set.intersection(set([a[0] for a in list_id_now[0:int(percentile_resolution * i * len(list_id_now))]]),set([b[0] for b in list_id_before[0:int(percentile_resolution * i * len(list_id_before))]]))))/float(percentile_resolution * i * len(list_id_now))) + "\t")
                    f_out_acc.write(str(float(len(set.intersection(set([a[0] for a in list_id_now[0:int(percentile_resolution * i * len(list_id_now))]]),set([b[0] for b in list_id_perm[0:int(percentile_resolution * i * len(list_id_perm))]]))))/float(percentile_resolution * i * len(list_id_now))) + "\t")
                f_out.write(str(len(list_id_now)) + "\n")
                f_out_acc.write(str(len(list_id_now)) + "\n")
                id_before = copy.deepcopy(id_now)
                id_now = {}
            ind = ind + 1

            
if(__name__ == "__main__"):
    main()
