#encoding=utf-8

import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print("Waiting for connections....")
s.listen(1)

while True:
	try:
		clientsock,clientaddr = s.accept()
	except KeyboardInterrupt:
		raist
	except:
		traceback.print_exc()
		continue
	try:	
		print("Got connection from",clientsock.getpeername())
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

	try:	
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()

