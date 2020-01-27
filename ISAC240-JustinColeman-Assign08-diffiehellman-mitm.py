import socket, random

secretKey = random.randint(20000, 500000)
HOST = "127.0.0.1" #"10.10.2.66"
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print('Connected by', addr)
    while True:
      clientPublicKey = conn.recv(1024)
      if not clientPublicKey:
        break
      
      localPublicKey = 6 ** secretKey % 761
      conn.sendall(str(localPublicKey).encode())

      partnerPublicKey = (clientPublicKey.decode())
      print('Received Alice\'s Public Key: ', partnerPublicKey)
      sharedSecret = str((int(partnerPublicKey) ** secretKey % 761))
      print("Shared secret: ", sharedSecret)
  s.close()

input("Press enter to continue")

secretKey2 = random.randint(20000, 500000)
cHOST = "127.0.0.1"
cPORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((cHOST, cPORT))
  localPublicKey = str(6 ** secretKey2 % 761)
  print("Local Public Key (Eve): ", localPublicKey)
  s.sendall(str(localPublicKey).encode()) #(partnerPublicKey.encode())

  spublicKey = s.recv(1024)
  serverPublicKey = (spublicKey.decode())
  print('Received Bob\'s Public Key: ', serverPublicKey)
  sharedSecret = str(int(serverPublicKey) ** secretKey2 % 761)
  print("Shared secret: ", sharedSecret)

