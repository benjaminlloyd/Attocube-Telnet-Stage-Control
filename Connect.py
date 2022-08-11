class Connect():
    def __init__(self,ip):
        import telnetlib
        import time
        HOST = ip#'192.168.7.10'
        self.tn = telnetlib.Telnet(HOST, 7230)
        self.tn.read_until(b"Authorization code: ")
        self.tn.write( b"123456\n" ) 