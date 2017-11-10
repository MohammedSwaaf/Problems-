import webbrowser
from random import choice
class rand:
    def sits(self):
        random_sites=["https://github.com/github/hub","https://docs.djangoproject.com/en/1.11/",
              "https://nmap.org/","https://docs.python.org/3/tutorial/"
              ,"https://www.metasploit.com/","https://www.wireshark.org/#learnWS"]
        webbrowser.open(choice(random_sites))
s=rand()
s.sits()