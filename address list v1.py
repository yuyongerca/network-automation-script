import csv
import sys



file = open(r"C:\Users\lc5544359\Documents\my script\newtest.txt")
result = open(r"C:\Users\lc5544359\Documents\my script\result.txt", "w")
ip = ["10.189.10.0", "10.189.1.0", "10.189.39.0", " 10.189.41.0", "10.189.0.0", "10.99.37.0", "10.99.40.0"]
i = 0
for line in file:
    for i in range(len(ip)):
        if ip[i] in line:
           result.write(line)
#find all name related to client
file.close()
result.close()
result = open(r"C:\Users\lc5544359\Documents\my script\result.txt", "r")
all_add = open(r"C:\Users\lc5544359\Documents\my script\addresslist.txt", "w")
name_list =[]
policy_list =[]
for line in result:
    keyword = line.split()
    if keyword[2] != "policies":
         if keyword[5] != "SantaAna":
            name_list.append(keyword[5])
    if keyword[2] == "address-book":
        all_add.write(line)

#find all policy name
file = open(r"C:\Users\lc5544359\Documents\my script\newtest.txt", "r")
new_result = open(r"C:\Users\lc5544359\Documents\my script\new_result.txt", "w")
Address =  open(r"C:\Users\lc5544359\Documents\my script\address.txt", "w")
Address_set =  open(r"C:\Users\lc5544359\Documents\my script\address_set.txt", "w")
Policy =  open(r"C:\Users\lc5544359\Documents\my script\policy.txt", "w")
Application =  open(r"C:\Users\lc5544359\Documents\my script\application.txt", "w")
Addre_src =  open(r"C:\Users\lc5544359\Documents\my script\address_src.txt", "w")
length_a = 0
length_p = 0



add_dst_list = []
add_dst_check = []
policy_dst_list = []
policy_src_list = []
policy_app_list = []
add_src_list = []
app_pro = []
app_port = []
app_name = []
name_set = set(name_list)
name_set = list(name_set)
Application_protocol = []
Application_port = []
Application_name = []
policy_set = set(policy_list)
del policy_list[:]
policy_list = list(policy_set)
i = 0
add_src_bool = False
add_dst_bool = False
for i in range(len(ip)):
    name_set.append(ip[i])
for line in file:
    line_word = line.split()
    if line_word[2] == "address-book":
        if line_word[4] == "address":
            Address.write(line)
        if line_word[4] == "address-set":
            Address_set.write(line)
    if line_word[2] == "application":
        Application_name.append(line_word[3])
        Application.write(line)
        if line_word[4] == "protocol":
            Application_protocol.append(line_word[5])
        elif line_word[4] == "destination-port":
            Application_port.append(line_word[5])
    if line_word [2] == "policies":
        Policy.write(line)
Policy.close()
Policy =  open(r"C:\Users\lc5544359\Documents\my script\policy.txt", "r")
for line in Policy:
    P_line = line.split()
    for length_a in range(len(name_set)):
        if name_set[length_a] == P_line[len(P_line)-1]:
            policy_list.append(P_line[len(P_line)-4])
policy_list = list(set(policy_list))
print policy_list
Policy.close()
all_add.close()
temp_policy = str()
Policy =  open(r"C:\Users\lc5544359\Documents\my script\policy.txt", "r")
all_add = open(r"C:\Users\lc5544359\Documents\my script\addresslist.txt", "r")
add_src_check = []
for line in Policy:
    P_line = line.split()
    for i in range(len(policy_list)):
        if policy_list[i] == P_line[len(P_line)-4] and P_line[len(P_line)-2] == "source-address":
           # policy_src_list.append(P_line[len(P_line)-4])
            #add_src_list.append(P_line[len(P_line)-1])
            Addre_src.write(line)
        if policy_list[i] == P_line[len(P_line) - 4] and P_line[len(P_line) - 2] == "destination-address":
            #policy_dst_list.append(P_line[len(P_line) - 4])
            #add_dst_list.append(P_line[len(P_line) - 1])
            Addre_src.write(line)
        if policy_list[i] == P_line[len(P_line) - 4] and P_line[len(P_line) - 2] == "application":
            policy_app_list.append(P_line[len(P_line) - 4])
            app_name.append(P_line[len(P_line) - 1])
            Addre_src.write(line)

print add_src_list
#find all dst address related src address policy list
Addre_src.close()
Addre_src =  open(r"C:\Users\lc5544359\Documents\my script\address_src.txt", "w")


























