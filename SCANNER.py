#!/bin/python3

import sys
import socket
from datetime import datetime 
 
# Above 3 are the dictionaries which I'm using.

# Defining our Target 

if len(sys.argv) == 2:
         target=socket.gethostbyname(sys.argv[1])   # translating host name to IPv4
         
else : 
       print("Invalid amout of argument.")
       print("Syntax: python3 scanner.py <ip>")


# Adding banner layout 

print("-"* 100)
print("Scanning Target: " +target)
print("Time Started : " + str (datetime.now()))
print("-"* 100)

try : 
         for port in range (50,1000):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if result == 0:
                     print(f"Port {port} is open" )
                     s.close()
         
except KeyboardInterrupt:
       print ("\n Exiting Program.")
       sys.exit()

except socket.gaierror:
       print("Host could not be resolved.")
       sys.exit()

except socket.error:
       print("Could not connect to server.")
       sys.exit()

