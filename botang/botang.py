import random
import discord
import asyncio
#list of images (mems)
imglist = ["http://i.imgur.com/fudWw3B.png", "http://i.imgur.com/pqxq50V.png", "http://i.imgur.com/z9j2MdA.jpg",
          "http://i.imgur.com/wHzyvDC.png", "http://i.imgur.com/bsaaLai.jpg", "http://i.imgur.com/RUxQbCt.png",
          "http://i.imgur.com/nNRolMW.gifv", "http://i.imgur.com/FzfbzrN.jpg", "http://i.imgur.com/WOtXRbU.jpg", 
          "http://i.imgur.com/Y0sMxhI.png", "http://i.imgur.com/DvEfV1v.png", "http://i.imgur.com/gkqbDjd.jpg",
          "http://i.imgur.com/B2uEC81.jpg", "http://i.imgur.com/85NtyVh.gifv", "http://i.imgur.com/lpNtyFm.jpg"]
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

def do_command_stuff(command, channel, author):
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
        await Yello.send_message(channel, random.choice(imglist))
    #this was supossed to be a secret but i guess it isn't now :(
    elif command.startswith("don'tdaretousethiscommandisweartogodifyoufuckinguseityou'llgetfuckingbannedkiddo"):
        await Yello.send_message(channel, "http://i.imgur.com/VAJNVGF.jpg")
    elif command.startswith("rate"):
        thing_to_rate = strip(command[4:]) # remove the "rate" and also spaces at the beginning/end
        if thing_to_rate = "": # in case someone didn't specify what to rate
            await Yello.send_message(channel, "Type `{}rate <thing>` to rate a thing.").format(prefixes[0])
        elif thing_to_rate.count("yellow") > 0 or thing_to_rate.count("orang") > 0: # if there is orang or yellow
            await Yello.send_message(channel,
                                     "<:thonk_yellow_fruit:324662249090449418>  |  <@!{}>, I'd give {} an 11/10").format(author.id, thing_to_rate)
        elif thing_to_rate.count("lime") > 0: # if there is lime
            await Yello.send_message(channel,
                                     "<:thonk_yellow_fruit:324662249090449418>  |  <@!{}>, I'd give {} a -666/10").format(author.id, thing_to_rate)
        else: # if it's just a normal thing
            await Yello.send_message(channel,
                                     "<:thonk_yellow_fruit:324662249090449418>  |  <@!{}>, I'd give {} a {}/10").format(author.id, thing_to_rate, hash(thing_to_rate) % 11)

@Yello.event
async def on_message(message):
    for p in prefixes:
          if message.content.startswith(p):
              command = message.content[len(p):] # cut out the prefix
              do_command_stuff(command, message.channel, message.author)
              break

#bot token
Yello.run("token")
#changes game
await Yello.change_presence(game=discord.Game(name="type " + prefixes[0] + "help for commands"))
