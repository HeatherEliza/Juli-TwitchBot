## Config Juli in bot.py

```python
>NICK = "Enter bot's username. all lower case"
```

Replace this with the username of the bot you plan to use. (Yes, you need to create an additional twitch account at www.twitch.tv)

```python
>NICK = "lizabot"
```

This MUST be lower case or it will not work.

--------------------

```python
>PASS = "oauth:"
```

Get your OAUTH code for the BOT ACCOUNT here and place it in the quots for PASS.

https://twitchapps.com/tmi/

--------------------

```python
>CHAN = "#channel you want to connect to- all lower case"
```

This is the channel you plan to connect to and use your bot in. Here's an example:

```python
CHAN = "#sodapoppin"
```

This MUST be lower case or it will not work.

--------------------

You should have something like this:

```python
NICK = "lizabot"
PASS = "oauth:aaskdfa2304adfajls202jalf"
CHAN = "#sodapoppin"
```

If you dont have the correct format, the bot wont connect properly. 

--------------------
## Adding Simple Commands

```python
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
```

In this section of the code, lets look at the following:

```python
 if message.find("Sigma") != -1:
    chat(s, "Sigma is a pretty cool dude.")
```

What we will want to change are "Sigma" and "Sigma is a pretty cool dude."

"Sigma" is the text the bot will read/look for in chat while "Sigma is a pretty cool dude." is what the bot will say in response to "Sigma" when it sees it in chat. Keep in mind, this is case sensitive.

Lets say I want the bot to let everyone know my twitter account when I type !twitter in chat. we would change it to the following:

```python
 if message.find("!twitter") != -1:
    chat(s, "Follow me on twitter: http://www.twitter.com/julieannahbot")
```

Add this line of code to your bot like so:

```python
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
                
            if message.find("!twitter") != -1:
                chat(s, "Follow me on twitter: http://www.twitter.com/julieannahbot")
        sleep(1 / RATE)
```

Restart your bot and run the command. You should now have a twitter information command. Good Job!

### To Do list

- Add status messages to the console and IRC/twitch chat to indicate the bot connecting/connected
- Add moderation commands
- Add user roles
- Add mini games
- Discord Integration
- Song requests
- Neural Network integration
- Move commands to a separate file. XML maybe?
- Create a command to add commands.


# Warning

This program is under development and WILL encounter errors. I will make my best attempts to ONLY push stable versions of the program to GitHub, but I can't garuantee that this will always be the case. Use at your own risk.
