import random
import discord
import asyncio
#list of images (mems)
imglist = ["1.jpg", "3.jpg", "4.gif", "5.gif", "6.png",
          "7.png", "8.jpg", "9.jpg", "10.png", "11.jpg", "12.jpg",
          "13.jpeg", "14.png", "15.png", "16.png"]
#name of client
Yello = discord.Client()

prefixes = (">", "<:yellow_fruit:337972191427821568>")

#shows some info on terminal
@Yello.event
async def on_ready():
    print("Welcome young worshipper to Botang!")
    print("Logged in as")
    print(Yello.user.name)
    print(Yello.user.id)
    print("-----")

def do_command_stuff(command, channel):
    #normal shitty help message
    if command.startswith("help"):
        await Yello.send_message(channel,
                                """list of available commands:
                                >help: displays this message
                                >classic: shows a message to our saviour
                                >meme: shows a random image of yellow lord
                                you can use <:yellow_fruit:337972191427821568> too, if you want""")
    #shows the needed pslam
    elif command.startswith("classic"):
        await Yello.send_message(channel, 'Beware the Orangman!')
    #the only redeemable part of this mess, the memes
    elif command.startswith("meme"):
        await Yello.send_file(channel, random.choice(imglist))
    #this was supossed to be a secret but i guess it isn't now :(
    elif command.startswith("don'tdaretousethiscommandisweartogodifyoufuckinguseityou'llgetfuckingbannedkiddo"):
        await Yello.send_file(channel, "imnotevengonnasayitsname.jpg")

@Yello.event
async def on_message(message):
    for p in prefixes:
          if message.content.startswith(p):
                    command = message.content[len(p):]
                    do_command_stuff(command, message.channel)
                    break

#bot token
Yello.run("token")
#changes game
await Yello.change_presence(game=discord.Game(name="type " + prefixes[0] + "help for commands"))
