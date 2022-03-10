import pyfiglet
import sys
import socket
from datetime import datetime
  
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


ip = input("IP que você deseja scannear: ")
porta_init = int(input("Porta inicial: "))
porta_fin = int(input("Porta final: "))
     
    # translate hostname to IPv4
target = socket.gethostbyname(ip)
if target == "":
    print("IP Inválido")

# Add Banner
print("-" * 50)
print("Scanneando Target IP: " + target)
print("Scanning começou às:" + str(datetime.now()))
print("-" * 50)
  
try:
     
    
    for port in range(porta_init, porta_fin + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            service = socket.getservbyport(port, "tcp")
            print("Porta {} está aberta e {} está rodando".format(port, service))
        else:
            print("Porta {} está fechada".format(port))
            
            
        s.close()


         
except KeyboardInterrupt:
        print("\n Scanneanto interrompido !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Inválido!!!!")
        sys.exit()
except socket.error:
        print("\ Servidor sem reposta !!!!")
        sys.exit()

print("-" * 50) 
print("FIM DO SCANNING")
print("-" * 50)


#Referências:
# [1] - https://resources.infosecinstitute.com/topic/write-a-port-scanner-in-python/
# [2] - https://github.com/tanc7/hacking-books/blob/master/Violent%20Python%20-%20A%20Cookbook%20for%20Hackers%2C%20Forensic%20Analysts%2C%20Penetration%20Testers%20and%20Security%20Engineers.pdf
