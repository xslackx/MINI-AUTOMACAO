from abc import ABC, abstractmethod

class InfoRecon(ABC):
    @abstractmethod
    def automata(nmap: bool, domain: bool, arjun: bool): pass