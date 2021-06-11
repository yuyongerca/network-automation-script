import csv
import sys

ofile  = open(r"c:\python27\ttest4.csv", "wt")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
ip = ["1.1.1.1", "2.2.2.2", "3.3.3.3", " 4.4.4.4", "5.5.5.5", "6.6.6.6", "7.7.7.7"]
name = ["ip0", "ip2", "ip2", "ip3", "ip3", "ip3", "ip6"]
src_list = []
policy_src_dic = {}
for i in range(len(name)):

    if i == 0:
        src_list.append(ip[i])
        key = name[i]
    else:
        if name[i] == name[i-1]:
            src_list.append(ip[i])
        else:
            #key = name[i]
            policy_src_dic[key] = str(src_list)
            key = name[i]
            src_list[:] = []
            src_list.append(ip[i])
for key in policy_src_dic:
    policy_src_dic[key] = list(policy_src_dic[key])
print policy_src_dic


