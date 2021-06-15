import socket

target = "45.55.99.208"
def portscan(port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((target, port))
		return True

	except:
		return False

print(portscan(80))