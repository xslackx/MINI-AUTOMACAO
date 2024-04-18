from model.rcn import InfoRecon
from model.motd import Banner
from socket import gethostbyname
from subprocess import PIPE, Popen
from urllib.parse import urlparse

class Recon(InfoRecon):
    def __init__(self, domainame: str) -> None:
        print(Banner.motd)
        
        self.restools = {
            "nmap": {},
            "findomain": {},
            "arjun": {}
        }
        
        try:
            if urlparse(domainame):
                self.iphost = gethostbyname(urlparse(domainame).netloc)
                self.domainame = domainame
        except:
            raise
        
        super().__init__()
    
    def automata(self, nmap: bool, domain: bool, arjun: bool):

        if domain:
            cmd = "findomain -q -t " + self.domainame
            with Popen(cmd, shell=True, stdout=PIPE) as finddomain:
                response = finddomain.stdout.read()
                self.restools["findomain"] = response.decode()
                
        if arjun:
            if self.restools.get("findomain"):
                cmd = "arjun -u " + self.domainame
                with Popen(cmd, shell=True, stdout=PIPE) as Arjun:
                    response = Arjun.stdout.read()
                    self.restools["arjun"] = response
        
        if nmap:
            cmd = "nmap -p 21,22,25,53,80,110,123,143,443,465,631,993,995 " + self.iphost
            with Popen(cmd, shell=True, stdout=PIPE) as netmap:
                response = netmap.stdout.read()
                response = response.decode().split("\n\n")
                self.restools["nmap"] = response[1]