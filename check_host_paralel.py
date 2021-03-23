import os 
import time
import concurrent.futures
# import 

T1 = time.perf_counter()

def check_host(ip):
    cek_ip = os.system('ping -c3 '+ip+' >/dev/null 2>&1')
    if cek_ip == 0:
        print(f'host {ip} is UP')
    else :
        print(f'host {ip} is DOWN')
    time.sleep(1)
    return "IP Berhasil dicek . . ."

with concurrent.futures.ProcessPoolExecutor() as executor:
    ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "8.8.8.8", "8.8.4.4"]
    results = executor.map(check_host,ip_list)     
    for result in results:        
        print(result)
    

T2 = time.perf_counter()
print(f"Proses pengecekan IP berjalam selama ... {round(T2-T1,2)} detik")