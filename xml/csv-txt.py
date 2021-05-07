import csv 
csv_file=csv.reader(open('../annotations/annotations.csv','r'))
#print(csv_file) 
data=[] 
for line in csv_file:
    #print(line) 
    data.append(line)
print(data)

#import numpy as np
#np.savetxt("data.txt",data)
with open("data.txt","w") as f:
     for i in data:
         i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'
         f.write(i)
