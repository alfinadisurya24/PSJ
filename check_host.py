import os
import sys

#dialog = sys.argv[0]

def eror():
    sys.exit('Gagal: IP address belum diberikan')

def checkping():
    if not len(sys.argv) == 2:
        eror()
    else:
        host = sys.argv[1]
        respon = os.system('ping -c3 '+host+' >/dev/null 2>&1')
        
        if respon == 0:
            print('host '+host+' is UP')
        else :
            print('host '+host+' is DOWN')

checkping()
