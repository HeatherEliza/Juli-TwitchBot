import socket
import re
from time import sleep 

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "Enter bot's username. all lower case"
PASS = "oauth:"
CHAN = "#channel you want to connect to- all lower case"
RATE = (20/30)

s=socket.socket()
s.connect((HOST,PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

msg=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :\r\n")


class bot:

    def chat(s, msg):
        s.send("PRIVMSG {} :{}\r\n".format(CHAN, msg).encode("utf-8"))

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            #print(response)
            username = re.search(r"\w+", response).group(0)
            message = msg.sub("", response)
            print(username + ": " + message)
            if message.find("!herp") != -1:
                print("Bong")
                chat(s, "derp")
                
            if message.find("Sigma") != -1:
                chat(s, "Sigma is a pretty cool dude.")
            
            if message.find("stupid bot") != -1:
                chat(s, "I'm not a HamBot :O)")
        sleep(1 / RATE)
