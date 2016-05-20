import socket, telnetlib, atexit
from color import bcolors

class remote():
    def __init__(self, host, port, timeout=2):
        self.host = host
        self.port = port
        self.buffer = ''
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.host,self.port))
        if isinstance(timeout, int) and timeout > 0:
            self.timeout = timeout
        else:
            self.timeout = 2
        self.sock.settimeout(self.timeout)
        print(bcolors.green + '[+] ' + bcolors.end + 'Opening connection to {} on port {}'.format(self.host,self.port))

        atexit.register(self.close)

    def recvline(self):
        while not self.buffer.endswith('\n'):
            self.buffer += self.sock.recv(1) 
        data = self.buffer
        self.buffer = ''
        return data

    def recvlines(self,num):
        lines = []
        for _ in range(num):
            lines.append(self.recvline())
        return lines

    def recvuntil(self,until) :
        while not self.buffer.endswith(until):
            self.buffer += self.sock.recv(1)
        data = self.buffer
        self.buffer = ''
        return data

    def send(self,data):
        self.sock.send(data)
     
    def sendline(self,data):
        self.sock.send(data + '\n')

    def interactive(self):
        print(bcolors.green + '[*] ' + bcolors.end + 'Switching to interactive mode')
        t = telnetlib.Telnet()
        t.sock = self.sock
        t.interact()

    def close(self): 
        if self.sock:
            self.sock.close()
            print(bcolors.red + '[+] ' + bcolors.end + 'Closed connection to {} port {}'.format(self.host,self.port))

