
from time import sleep
import http.client
import urllib

#a leitura dos canais no txt é feita com
#primeiro char como o field 
#segundo char como ON e OFF



#CRIAR UM CANAL SO PRA ESCOLA!!!!!!!!!!!!
#CRIAR UM CANAL SO PRA ESCOLA!!!!!!!!!!!!
#CRIAR UM CANAL SO PRA ESCOLA!!!!!!!!!!!!
#CRIAR UM CANAL SO PRA ESCOLA!!!!!!!!!!!!
#CRIAR UM CANAL SO PRA ESCOLA!!!!!!!!!!!!
key = "49OKMDYHRDA1WJGW"

def split(word):
    return [char for char in word]

def postaLeitura(posLine):
    f = open("fila.txt","r")
    for i in range(posLine):
        line = f.readline()
    
    print(line)
    
    if len(line.strip()) != 0 :
        posLine += 1
    
        line = split(line)

        field = line[0]
        onOff = line[1]

        if(field == '1'):
            params = urllib.parse.urlencode({'field1': onOff, 'key':key})
        elif(field == '2'):
            params = urllib.parse.urlencode({'field2': onOff, 'key':key})
        elif(field == '3'):
            params = urllib.parse.urlencode({'field3': onOff, 'key':key})
        elif(field == '4'):
            params = urllib.parse.urlencode({'field3': onOff, 'key':key})


        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")

        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            conn.close()
        except:
            print ("connection failed")

    return posLine

if __name__ == "__main__":
    posLine = 2
    
    while(True):
        posLine = postaLeitura(posLine)
        print(posLine)
        sleep(15)