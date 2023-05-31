#!/bin/env python3

import sys
import numpy as np

def get_matrix(eval_file, posi_file, threshold):
    with open(posi_file) as file:
        positive_list = []
        for line in file:
            positive_list.append(line.strip()) #appending positive ids in a python list
    with open(eval_file) as file1:
        tp, tn, fp, fn = 0, 0, 0, 0
        for line1 in file1: #reading the file with evalues associated to each entry...
            line1 = line1.rstrip().split() #...removing spaces and splitting the line...
            entry = line1[0] #...and assigning each entry and evalue to a variable
            e_val=float(line1[1])
            if e_val <= threshold and entry in positive_list:
                tp += 1
            elif e_val <= threshold and entry not in positive_list:
                fp += 1
                print("FALSE POSITIVE!", entry, "with evalue", e_val) #print statement to retrieve the false positives/negatives, to uncomment only when testing
            elif e_val > threshold and entry in positive_list:
                fn +=1
                print("FALSE NEGATIVE!", entry, "with evalue", e_val)
            else:
                tn +=1
        conf_matrix = np.array([[tp, fp], [fn, tn]]) #filling the confusion matrix
        acc = (conf_matrix[0][0]+conf_matrix[1][1])/np.sum(conf_matrix)
        mcc = ((conf_matrix[1][1]*conf_matrix[0][0]) - (conf_matrix[0][1]*conf_matrix[1][0]))/np.sqrt((conf_matrix[1][1]+conf_matrix[0][1])*(conf_matrix[1][1]+conf_matrix[1][0])*(conf_matrix[0][0]+conf_matrix[0][1])*(conf_matrix[0][0]+conf_matrix[1][0]))
        return conf_matrix, acc, mcc

if __name__ == "__main__":
    eval_file = sys.argv[1]
    posi_file = sys.argv[2]
    threshold = float(sys.argv[3])
    matrix, acc, mcc = get_matrix(eval_file, posi_file, threshold)
    print()
    print("Matrix:", matrix, "\nACC:", acc, "\nMCC:", mcc, "\nThreshold:", threshold, "\n")

