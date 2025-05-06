import discord
from discord.ext import commands
from colorama import Fore, Style
from discord.commands import slash_command, Option


intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix="/", intents=intents, activity=discord.Game(name="NRW System V1"))

@bot.event
async def on_ready():
    ascii_banner = rf"""{Fore.CYAN}
                   _     _   ____        _   
     /\           (_)   | | |  _ \      | |  
    /  \   ___ ___ _ ___| |_| |_) | ___ | |_ 
   / /\ \ / __/ __| / __| __|  _ < / _ \| __|
  / ____ \\__ \__ \ \__ \ |_| |_) | (_) | |_ 
 /_/    \_\___/___/_|___/\__|____/ \___/ \__|
{Style.RESET_ALL}"""
    print(ascii_banner)
    print(f"{Fore.GREEN}{bot.user} is now online!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Connected to {len(bot.guilds)} servers.{Style.RESET_ALL}")

@bot.slash_command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} wurde vom Server gekickt! mit dem Grund: {reason}I")
    except discord.Forbidden:
        await ctx.send(f"Ich kann {member.mention} nicht vom Server kicken!")
    except discord.HTTPException:
        await ctx.send(f"Fehler beim Kicken von {member.mention}.")

bot.run("MTMxNzI0Njc4MzgxMzg0NTExNA.Gjq2U0.QGTOOnEo_dkdD9o398WaC_vP81chBxcgwJz-n8")
