import csv
import sys

ofile  = open(r"c:\python27\ttest.csv", "wt")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)





#file = open(r"c:\python27\newtest.txt")
#result = open(r"c:\python27\result.txt", "w")
ip = ["10.189.10.0", "10.189.1.0", "10.189.39.0", " 10.189.41.0", "10.189.0.0", "10.99.37.0", "10.99.40.0"]
name = ["ip0", "ip2", "ip2", "ip3", "ip3", "ip3", "ip6"]
#assocate multiple value to one key
k = list(zip(name, ip))
d = {}
for (x,y) in k:
    if x in d:
        d[x] = d[x] +","+ y #or whatever your function needs to be to combine them
    else:
        d[x] = y
print d
print k


#print the dictoinary to CSV file
for key,value in d.items(): # iteritems if py2
    new = str()
    for item in value:
        if item != ",":
            new = new + str(item)
        else:
            new = new +"\n"
    print new
    writer.writerow([str(key), new])
