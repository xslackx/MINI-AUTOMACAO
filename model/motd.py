from pyfiglet import figlet_format
from dataclasses import dataclass

@dataclass
class Banner:
    motd: str = figlet_format("RECON!!\n") + "By: Ismael Oliveira\n\n"
    