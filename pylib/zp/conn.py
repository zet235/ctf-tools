import socket, telnetlib, atexit
from color import bcolors

class remote():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.buffer = ''
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.host,self.port))
        print bcolors.green + '[+] ' + bcolors.end + 'Opening connection to {} on port {}'.format(self.host,self.port)

        atexit.register(self.close)

    def recvline(self):
        while not self.buffer.endswith('\n'):
            self.buffer += self.sock.recv(1) 
        data = self.buffer
        self.buffer = ''
        return data

    def recvlines(self,num):
        lines = []
        for _ in xrange(num):
            lines.append(self.recvline())
        return lines

    def recvuntil(self,until) :
        data = ""
        while not data.endswith(until):
            data += self.sock.recv(1)
        return data

    def sendline(self,data):
        self.sock.send(data + '\n')

    def interactive(self):
        t = telnetlib.Telnet()
        t.sock = self.sock
        t.interact()

    def close(self): 
        if self.sock:
            self.sock.close()
            print bcolors.red + '[+] ' + bcolors.end + 'Closed connection to {} port {}'.format(self.host,self.port)

