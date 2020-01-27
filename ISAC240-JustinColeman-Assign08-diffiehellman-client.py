import socket, random

HOST = '127.0.0.1' #'10.10.2.66'
PORT = 65432        
secretKey = random.randint(20000, 500000) 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))

  localPublicKey = str(6 ** secretKey % 761)
  print("Local Public Key (Alice): ", localPublicKey)
  s.sendall(localPublicKey.encode())

  publicKey = s.recv(1024)
  partnerPublicKey = (publicKey.decode())
  print('Received: ', partnerPublicKey)
  sharedSecret = str(int(partnerPublicKey) ** secretKey % 761)
  print("Shared secret: ", sharedSecret)