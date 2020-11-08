from network import Server

server = Server("127.0.0.1") # Insert the IP the server is going to run on

while True:
  conn = server.accept()
  data = server.recieve(conn)
  print(data)
  server.log(data)