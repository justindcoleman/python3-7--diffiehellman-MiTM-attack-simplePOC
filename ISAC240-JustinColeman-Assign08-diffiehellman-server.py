import socket, random

secretKey = random.randint(20000, 500000)
HOST = "127.0.0.1" #"10.10.2.66"
PORT = 65431


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print('Connected by', addr)
    while True:
      publicKey = conn.recv(1024)
      if not publicKey:
        break
      
      localPublicKey = 6 ** secretKey % 761
      print("Local Public Key (Bob): ", localPublicKey)
      conn.sendall(str(localPublicKey).encode())
      

      partnerPublicKey = (publicKey.decode())
      print('Received: ', partnerPublicKey)
      sharedSecret = str((int(partnerPublicKey) ** secretKey % 761))
      print("Shared secret: ", sharedSecret)
