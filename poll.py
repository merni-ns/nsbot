from discord.ext import commands
from discord     import Embed
from datetime    import datetime
from bns         import region

with open("token.txt") as f:
    token = f.read()
    
NOLIST = [chr(i) for i in range(0X30, 0X3A)]
NOEMOJI = [i+'\uFE0F\u20E3' for i in NOLIST] + ['\U0001F51F']
REGIND = [chr(i) for i in range(0X1F1E6, 0X1F200)]
EMOJI = NOEMOJI + REGIND

bot = commands.Bot(command_prefix="!!")

@bot.event
async def on_ready():
    print(bot.user.name, "connected successfully.")

@bot.command(name="pollusers")
async def cmd_pollusers(ctx, title):
    guild = ctx.guild
    roles = guild.roles
    for i in roles:
        if i.name == "Player (Alive)":
            reqrole = i
    members = guild.members
    alive = []
    for i in members:
        if reqrole in i.roles:
            alive += [i]
    msg = ""
    numused = 0
    for i in range(len(alive)):
        msg += f"{EMOJI[i]} {alive[i].display_name} ({alive[i].name}#{alive[i].discriminator})\n"
        numused += 1
    poll = await ctx.send(title+"\n"+msg)
    i = 0
    while i < numused:
        await poll.add_reaction(EMOJI[i])
        i += 1

bot.run(token)
