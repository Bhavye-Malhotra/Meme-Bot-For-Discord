import discord
from discord.ext import commands
from colorama import Back, Fore, Style
import auth
import help_info
from meme import *

client = discord.Client()
bot = commands.Bot(command_prefix='+')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(('<' + bot.user.name) + ' Online>')
    print(f"discord.py {discord.__version__}\n")
    await bot.change_presence(activity=discord.Game(name='+help'))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        emb = discord.Embed(description="Invalid command passed.  Use +help", colour=0xff0000)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(description=f"There was an error, sorry!\nIf you think this should be fixed, report it on Github \"what happened\"", colour=0xff0000)
        await ctx.send(embed=emb)
    
    print(Style.BRIGHT + Fore.RED + f"Error occured with: {ctx.command}\n{error}\n")
    print(Style.RESET_ALL)

@bot.command()
async def help(ctx, page=None):
    if page == 'meme':
        emb = discord.Embed(description=help_info.help_meme, colour=0xff0000)
        emb.set_author(name='Meme Help')   
    else:
        emb = discord.Embed(description=help_info.help_page, colour=0xff0000)
        emb.set_author(name='Meme.exe')
    
    await ctx.channel.send(embed=emb)


@bot.command()
async def normie(ctx):
    data=normie_meme()
    e=discord.Embed(title=data[1],colour=0xff0000)
    emb = e.set_image(url=data[0])
    msg= await ctx.send(embed=emb)
    emoji=["🇱","🇲","🇦","🇴","😂"]
    for i in emoji:
        await msg.add_reaction(i)

@bot.command()
async def dank(ctx):
    data=dank_meme()
    e=discord.Embed(title=data[1],colour=0xff0000)
    emb = e.set_image(url=data[0])
    await ctx.send(embed=emb)
    

@bot.command()
async def stonks(ctx):
    data=stonks_meme()
    e=discord.Embed(title=data[1],colour=0xff0000)
    emb = e.set_image(url=data[0])
    msg= await ctx.send(embed=emb)
    emoji=["🇸","🇹","🇴","🇳","🇰"]
    for i in emoji:
        await msg.add_reaction(i)


@bot.command()
async def edgy(ctx):
    data=edgy_meme()
    e=discord.Embed(title=data[1],colour=0xff0000)
    emb = e.set_image(url=data[0])
    msg = await ctx.send(embed=emb)
    emoji=["🇴","🇺","🇨","🇭"]
    for i in emoji:
        await msg.add_reaction(i)


if __name__ == '__main__':
    bot.run(auth.auth_token)