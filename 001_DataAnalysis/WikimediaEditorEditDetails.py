#-*- coding: utf-8 -*-

# Input file format: Wikimedia xml metadata (https://dumps.wikimedia.org/)


import xml.etree.ElementTree as ET
import datetime
import sys
import os
import glob

input_folder = sys.argv[1]
input_start = int(sys.argv[2])
input_end = int(sys.argv[3])

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
    if(input_end == -1):
        file_list = sorted(glob.glob(input_folder + '*.xml'))[input_start:]
    else:
        file_list = sorted(glob.glob(input_folder + '*.xml'))[input_start:input_end+1]


    for input_file in file_list:
        infile = input_file

        outfile = infile + ".data_prod_editor"

        f_out = open(outfile, 'wb')

        f_out.write("#Editor_Name\tNumber_of_Edit\tProduced_Size_of_Editor\tABS_Produced_Size_of_Editor\tPOS_Produced_Size_of_Editor\tNEG_Produced_Size_of_Editor\n")

        print "#Editor_Name\tNumber_of_Edit\tProduced_Size_of_Editor\tABS_Produced_Size_of_Editor\tPOS_Produced_Size_of_Editor\tNEG_Produced_Size_of_Editor"

        bytes = [] #for single article
        final_bytes = []
        article_edit_num = []
        nowword = ""
        tempbytes = -1
        temptime = -1
        start_time = datetime.datetime.fromtimestamp(10000000000)
        timestamp = [start_time]
        buff_contents = ""
        negative_time_marker = 0
        numarticle = 0
        currentid = ""
        cont_marker = 0
        id = {}
        abs_diff = {}
        diff = {}
        id_list = []
        with open(infile) as f:
            for line in f:
                buff_contents = buff_contents + line
                if(line.find('<title>') > 0):
                    numarticle = numarticle + 1
                    cont_marker = 0

                    if(nowword.find(',')>0):
                        nowword = nowword.replace(',', ';')
                    if(len(timestamp) is not 0 and (timestamp[0]-start_time).total_seconds() < 0):
                        start_time = timestamp[0]

                    timestamp = []
                    article_edit_num.append(len(bytes))
                    beforebytes = 0
                    for c_idx in range(0, len(id_list)):
                        if(id_list[c_idx] == ""):
                            continue
                        elif(id_list[c_idx] in diff):
                            diff[id_list[c_idx]] = diff[id_list[c_idx]] + (bytes[c_idx] - beforebytes)
                            abs_diff[id_list[c_idx]] = abs_diff[id_list[c_idx]] + abs(bytes[c_idx] - beforebytes)
                        else:
                            diff[id_list[c_idx]] = bytes[c_idx] - beforebytes
                            abs_diff[id_list[c_idx]] = abs(bytes[c_idx] - beforebytes)
                        beforebytes = bytes[c_idx]
                    id_list = []
                    if(len(bytes) is not 0):
                        try:
                            final_bytes.append(bytes[-1])
                        except MemoryError:
                            print len(final_bytes)
                        bytes = []
                elif(line.find('</revision>')>0):
                    if(negative_time_marker == 1):
                        negative_time_marker = 0
                        right_pos = 0
                        if(tempbytes >= 0 and temptime != -1):
                            for i in range(len(timestamp)):
                                if((temptime-timestamp[i]).total_seconds() < 0):
                                    right_pos = i
                                    break
                            bytes.insert(right_pos, tempbytes)
                            id_list.insert(right_pos, currentid)
                            timestamp.insert(right_pos, temptime)
                            #print timestamp
                    elif(tempbytes >= 0 and temptime != -1):
                        id_list.append(currentid)
                        bytes.append(tempbytes)
                        timestamp.append(temptime)
                    else:
                        print temptime
                        print tempbytes
                        print currentid
                        print buff_contents
                    tempbytes = -1
                    temptime = -1
                    buff_contents = ""
                elif(line.find('<timestamp>') > 0):
                    temptime = datetime.datetime.strptime(line.strip()[11:-12], "%Y-%m-%dT%H:%M:%SZ")
                    if(len(timestamp)==0):
                        continue
                    if((temptime-timestamp[-1]).total_seconds() < 0 ):
                        negative_time_marker = 1
                elif(line.find('<contributor>') > 0):
                    cont_marker = 1
                elif(line.find('<id>') > 0 and cont_marker == 1):
                    currentid = line.strip()[4:-5]
                    if (line.strip()[4:-5] in id):
                        id[line.strip()[4:-5]] = id[line.strip()[4:-5]] + 1
                    else:
                        id[line.strip()[4:-5]] = 1
                elif(line.find('<ip>') > 0 and cont_marker == 1):
                    currentid = line.strip()[4:-5]
                    if (line.strip()[4:-5] in id):
                        id[line.strip()[4:-5]] = id[line.strip()[4:-5]] + 1
                    else:
                        id[line.strip()[4:-5]] = 1
                elif(line.find('</contributor>') > 0):
                    cont_marker = 0
                elif(line.find('<text') > 0 and line.find('bytes') > 0):
                    try:
                        #iter = ET.fromstring(line)
                        #tempbytes = iter.get('bytes') #For mal-identified xmls
                        tempbytes = get_bytes(line)
                    except AssertionError:
                        print line
                elif(line.find('<text') > 0 and line.find('deleted') > 0):
                        tempbytes = 0

        numarticle = numarticle + 1
        cont_marker = 0
        if(nowword.find(',')>0):
            nowword = nowword.replace(',', ';')
        if(len(timestamp) is not 0 and (timestamp[0]-start_time).total_seconds() < 0):
            start_time = timestamp[0]

        timestamp = []
        article_edit_num.append(len(bytes))
        for c_idx in range(len(id_list)):
            if(id_list[c_idx] == ""):
                continue
            elif(id_list[c_idx] in diff):
                diff[id_list[c_idx]] = diff[id_list[c_idx]] + bytes[c_idx]
                abs_diff[id_list[c_idx]] = abs_diff[id_list[c_idx]] + abs(bytes[c_idx])
            else:
                diff[id_list[c_idx]] = bytes[c_idx]
                abs_diff[id_list[c_idx]] = abs(bytes[c_idx])
        id_list = []
        if(len(bytes) is not 0):
            try:
                final_bytes.append(bytes[-1])
            except MemoryError:
                print len(final_bytes)
            bytes = []

        for idx, ned in id.iteritems():
            print str(idx) + "\t" + str(ned) + "\t"+ str(diff[idx]) + "\t" + str(abs_diff[idx]) + "\t" + str((float(diff[idx]) + float(abs_diff[idx]))/2) + "\t" + str((float(abs_diff[idx])-float(diff[idx]))/2)
            f_out.write(str(idx) + "\t" + str(ned) + "\t"+ str(diff[idx]) + "\t" + str(abs_diff[idx]) + "\t" + str((float(diff[idx]) + float(abs_diff[idx]))/2) + "\t" +str((float(abs_diff[idx])-float(diff[idx]))/2) + "\n")

            
if(__name__ == "__main__"):
    main()
