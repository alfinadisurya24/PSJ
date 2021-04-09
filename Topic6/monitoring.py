#from pprint import pprint
import os
import threading
import time
import datetime

ip_array = []
r = open('hosts.cfg')

p = r.readlines()
for line in p:
    line = line.strip()
    ip_array.append(line)
r.close()

#pprint(ip_array)

def cek_ping(ip):
    cek_ip = os.system('ping -c1 '+ip+' >/dev/null 2>&1')
    ct = datetime.datetime.now()
    ct = ct.strftime("%m-%d-%Y %H:%M:%S")

    w = open('report-monitor.csv', 'a')
    if cek_ip == 0:
        print(f'{ct};{ip};UP')
        w.write(f'{ct};{ip};UP\n')
    else :
        print(f'{ct};{ip};DOWN')
        w.write(f'{ct};{ip};UP\n')
    w.close()

Threads = []
while True:
    T1 = time.perf_counter()
    print('Mulai Monitor . . . . .')
    for x in ip_array:
        P = threading.Thread(target=cek_ping, args=[x])
        P.start()
        Threads.append(P)
        P.join()
    T2 = time.perf_counter()
    print(f"Selesai dalam ... {round(T2-T1,2)} detik")
    print("\n")
    time.sleep(10)

# for process in Threads:
#     process.join()
    