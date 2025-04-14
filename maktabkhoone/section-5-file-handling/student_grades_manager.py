import csv
# For the average
from statistics import mean 
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):

    fout=open(output_file_name,'a')
    with open(input_file_name) as fin:
        reader=csv.reader(fin)
        for row in reader:
            fout.write(row[0]+ ',')
            grade=list()
            for i in row[1:]:
                grade.append(int(i))
            fout.write(str(mean(grade))+'\n')
    fout=open(output_file_name)
    print(fout.read())
        

def calculate_orsted_averages(input_file_name, output_file_name):

    fin=open (input_file_name)
    fout=open (output_file_name,'a')
    templist= list()
    with open(input_file_name) as f:
        reader=csv.reader(f)
        for row in reader:
            grades=list()
            for i in row[1:]:
               grades.append(int(i))
            templist.append([mean(grades),row[0]])
            templist.sort()   
        for i in range(0,len(templist)):
            fout.write(templist[i][1]+','+str(templist[i][0])+'\n')        
    fout=open(output_file_name)
    print(fout.read())
    


def calculate_three_best(input_file_name, output_file_name):

    fin=open(input_file_name)
    fout=open(output_file_name,'a')
    with open(input_file_name) as f:
        reader=csv.reader(f)
        temp=list()
        for row in reader:
            grades=list()
            for i in row[1:]:
                grades.append(int(i))
            temp.append([mean(grades),row[0]])
            print(temp)
        temp.sort(reverse=True)
        print(temp)
        for i in range(0,3):
            fout.write(temp[i][1]+","+str(temp[i][0])+'\n')
        fout=open(output_file_name)
        print(fout.read())


def calculate_three_worst(input_file_name, output_file_name):
    fin=open(input_file_name)
    fout=open(output_file_name,'a')
    with open(input_file_name) as f:
        reader=csv.reader(f)
        temp=list()
        for row in reader:
            grades=list()
            for i in row[1:]:
                grades.append(int(i))
            temp.append(mean(grades))
        temp.sort()
        for i in range(0,3):
            fout.write(str(temp[i])+'\n')
        fout=open(output_file_name)
        print(fout.read())


def calculate_average_of_averages(input_file_name, output_file_name):
    fout=open(output_file_name,'a')
    with open(input_file_name) as f:
        reader=csv.reader(f)
        avg=list()
        for row in reader:
            grades=list()
            for i in row[1:]:
                grades.append(int(i))
            avg.append(mean(grades))
        fout.write(str(mean(avg)))
    fout=open(output_file_name)
    print(fout.read())
