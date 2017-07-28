import random
import discord
import asyncio
#list of images (mems)
imglist = ["1.jpg", "3.jpg", "4.gif", "5.gif", "6.png",
          "7.png", "8.jpg", "9.jpg", "10.png", "11.jpg", "12.jpg",
          "13.jpeg", "14.png", "15.png", "16.png"]
#name of client
Yello = discord.Client()
#bot prefix, idk how to make it so you have 2 prefix so i created prefix 2
prefix = ">"
prefix2 = "<:yellow_fruit:337972191427821568>"
#shows some info on terminal
@Yello.event
async def on_ready():
    print("Welcome young worshipper to Botang!")
    print("Logged in as")
    print(Yello.user.name)
    print(Yello.user.id)
    print("-----")
#receives message
@Yello.event
async def on_message(message):
    #changes game
    await Yello.change_presence(game=discord.Game(name="type " + prefix + "help for commands"))
    #normal shitty help message
    if message.content.startswith(prefix + "help"):
        await Yello.send_message(message.channel, "list of available comands:\n" +
                                prefix + "help: displays this message\n" +
                                prefix + "classic: shows a message to our saviour\n" +
                                prefix + "meme: shows a random image of yellow lord\n"
                                "you can use <:yellow_fruit:337972191427821568> too, if you want")
    #shows the needed pslam
    elif message.content.startswith(prefix + "classic"):
        await Yello.send_message(message.channel, 'Beware the Orangman!')
    #the only redeemable part of this mess, the memes
    elif message.content.startswith(prefix + "meme"):
        await Yello.send_file(message.channel, random.choice(imglist))
    #this was supossed to be a secret but i guess it isn't now :(
    elif message.content.startswith(prefix + "don'tdaretousethiscommandisweartogodifyoufuckinguseityou'llgetfuckingbannedkiddo"):
        await Yello.send_file(message.channel, "imnotevengonnasayitsname.jpg")

    #now here's the messy stuff, i basically copied and pasted the code so i could use prefix2 lol
    #if someone knows a better way add it pls

    elif message.content.startswith(prefix2 + "help"):
        await Yello.send_message(message.channel, "list of available comands:\n" +
                                 prefix2 + "help: displays this message\n" +
                                 prefix2 + "classic: shows a message to our saviour\n" +
                                 prefix2 + "meme: shows a random image of yellow lord\n"
                                 "you can use > too, if you want")
    elif message.content.startswith(prefix2 + "classic"):
        await Yello.send_message(message.channel, 'Beware the Orangman!')
    elif message.content.startswith(prefix2 + "meme"):
        await Yello.send_file(message.channel, random.choice(imglist))
    elif message.content.startswith(prefix2 + "don'tdaretousethiscommandisweartogodifyoufuckinguseityou'llgetfuckingbannedkiddo"):
        await Yello.send_file(message.channel, "imnotevengonnasayitsname.jpg")

#bot token
Yello.run("token")
