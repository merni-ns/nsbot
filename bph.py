from discord.ext import commands
from discord     import Embed
from datetime    import datetime
from bns         import region

token = "NzQzMDUyNzE5NTQzMjg3ODI5.XzPDxQ.vE_-TBMEQGbw5wfROLcWKYtTH5U" # Replace with token

bot = commands.Bot(command_prefix="!!")

@bot.event
async def on_ready():
    print(bot.user.name, "connected successfully.")

@bot.command(name='date')
async def cmd_date(ctx):
    await ctx.send(f"The time now is {str(datetime.now())} !")

@bot.command(name='region')
async def cmd_region(ctx, *, name):
    x = region(name)
    '''
    await ctx.send(f"\nData on region **{name}** at {datetime.utcnow().isoformat(sep=' ', timespec='seconds')} UTC:\n"
                   f"Nations: **{x[0]}**\nFounder: **{x[3]}**\n"
                   f"WA Delegate: **{x[1]}**\nWA Delegate's endorsements: **{x[2]}**\n"
                   f"{x[4]}")
    '''
    e = Embed(title=f"Data on region **{name}**", type='rich', timestamp=datetime.utcnow())
    e.set_thumbnail(url=x[4])
    e.add_field(name="Nations",value=f"{x[0]}").add_field(name="Founder",value=f"{x[3]}")
    e.add_field(name="WA Delegate",value=f"{x[1]}").add_field(name="WA Delegate's endorsements",value=f"{x[2]}")
    await ctx.send(embed=e)

bot.run(token)
