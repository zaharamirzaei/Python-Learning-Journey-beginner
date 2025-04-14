
import csv
from hashlib import sha256
from os import read
def hash_password_hack(input_file_name, output_file_name):
    fout=open(output_file_name,'a')
    myhash={}
    for i in  range(1000,10000):
        #repr(i).encode('utf-8')
        myhash[sha256(b'%i'%i).hexdigest()]=i
    with open(input_file_name) as f:
        reader=csv.reader(f)
        for row in reader:
            fout.write(row[0]+',')
            fout.write(str(myhash[row[1]])+'\n')
    fout=open(output_file_name)
    print(fout.read())
hash_password_hack('input.csv','output.txt')    
