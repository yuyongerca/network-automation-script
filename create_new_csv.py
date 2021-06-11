import csv


def new_csv(srcfile,tmpfile):

    with open(srcfile,'r') as infile:
        reader = csv.reader(infile)
        with open (tmpfile,'w') as outfile:
            writ = csv.writer(outfile)
            new_row =[]
            for row in reader:
                new_row.append(row[2])
                new_row.append(row[3])
                new_row.append(row[4])
                # print (new_row)
                writ.writerow(new_row)
                new_row.clear()

def rm_duplicate(tmpfile,dstfile):
    with open(tmpfile,'r') as infile:
        reader = csv.reader(infile)
        seen = []
        with open(dstfile,'w') as outfile:
            writ = csv.writer(outfile)
            for line in reader:
                if line in seen:
                    continue
                else:
                    seen.append(line)
                    writ.writerow(line)



dstfile ='100.72.48.0_22_subnet_traffic_trafficsummary.csv'
srcfile ='100.72.48.0_22_subnet_traffic.csv'
tmpfile ='100.72.48.0_22_subnet_traffic_trafficsummary_tmp.csv'
new_csv(srcfile,tmpfile)
rm_duplicate(tmpfile,dstfile)
