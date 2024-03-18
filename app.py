import os
import datetime
import json
import aiohttp
import asyncio
import requests
import logging
import discord
import discord.ui
import mcstatus
import time
import http.server
import threading
import youtube_dl

from dotenv import load_dotenv
from discord import Embed
from discord.ext import commands
from discord.ui import View, Button
from discord.utils import get
from mcstatus import JavaServer
from mcstatus import BedrockServer


# Basic HTTP server to process health check requests
class HealthCheckHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

health_server = http.server.HTTPServer(('', 8080), HealthCheckHandler)

health_thread = threading.Thread(target=health_server.serve_forever)
health_thread.daemon = True
health_thread.start()

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents, help_command=None)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# #############
# Configuration
# #############
# Omit any unnecessary fields when customizing your bot.
# Please ensure to include the developer's discord user ID as the first string in the OWNER_UID list.
# The OWNER_UID grants individuals additional privileges and permissions, including access to moderation commands and other exclusive benefits.
# Loads BOT_TOKEN from .env file or environment variables.
BOT_TOKEN = os.getenv('BOT_TOKEN') or os.environ.get('BOT_TOKEN')
OWNER_UID = ["<Owner 1>", "<Owner 2>"]

# Server Info
SERVER_NAME = "<Your server's Name>"
SERVER_ADDRESS = "<Your server's Address>"
SERVER_PORT = "<Your server's Port>"
SERVER_STORE = "<Your server's Store URL>"

# Cloud Image Directory URL
BOT_IMG_SRC = "<root directory of your bot's images url>"
ICON_URL = f"{BOT_IMG_SRC}Logo.png"
# if your bot's images are stored in https://example.com/images/ then you would set BOT_IMG_SRC = "https://example.com/images/"
# for example ICON_URL is now set to "https://example.com/images/Logo.png"

# Discord Server's "Ask Questions" & "Create a Ticket" Channels
DISCORD_TICKET_CHANNEL = "<Ticket Channel Link or <#Channel-ID>>"
DISCORD_QA_CHANNEL = "<QA Channel Link or <#Channel-ID>>"
# Exmaple:
# Link "https://discord.com/channels/11532342342343872694/1153453023423454337"
# Channel ID: <#1153453023423454337>

# Discord Server's Voice Channels
# Exmaple:
# DISCORD_VOICE_CHANNEL_1 = 11534530213123123231
DISCORD_VOICE_CHANNEL_1 = <Voice Channel ID>
DISCORD_VOICE_CHANNEL_2 = <Voice Channel ID> 

# Log Channels
DISCORD_STATUS_CHANNEL = <Status log Channel ID>
DISCORD_VIOLATION_CHANNEL = <Violation log Channel ID>
DISCORD_COMMAND_CHANNEL = <Command log Channel ID>
DISCORD_DM_CHANNEL = <Dm log Channel ID>
DISCORD_ERROR_CHANNEL = <Error log Channel ID>

# Appearance of the bot
# Bot's main border color (Purple)
BORDER_COLOR = 0xC300FF
BORDER_COLOR_GREEN = 0x00B300
BORDER_COLOR_YELLOW = 0xFFD700
BORDER_COLOR_RED = 0xFF3333

# Vote Websites
VOTE_WEBSITE_1_NAME = "<Vote-Website-Name-1>"
VOTE_WEBSITE_1_URL = "<Vote-Website-URL-1>"
VOTE_WEBSITE_2_NAME = "<Vote-Website-Name-2>"
VOTE_WEBSITE_2_URL = "<Vote-Website-URL-2>"
VOTE_WEBSITE_3_NAME = "<Vote-Website-Name-3>"
VOTE_WEBSITE_3_URL = "<Vote-Website-URL-3>"
VOTE_WEBSITE_4_NAME = "<Vote-Website-Name-4>"
VOTE_WEBSITE_4_URL = "<Vote-Website-URL-4>"
VOTE_WEBSITE_5_NAME = "<Vote-Website-Name-5>"
VOTE_WEBSITE_5_URL = "<Vote-Website-URL-5>"
# Example:
# VOTE_WEBSITE_5_NAME = "ExampleVote"
# VOTE_WEBSITE_5_URL = "https://vote.example.com"

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


@client.event
async def on_ready():
  owner_id = OWNER_UID[0]
  owner = await client.fetch_user(int(owner_id))
  print(f'We have logged in as {client.user}')
  await client.tree.sync()
  DISCORD_STATUS_CHANNEL_GET = client.get_channel(DISCORD_STATUS_CHANNEL)
  if DISCORD_STATUS_CHANNEL_GET:
    embed=discord.Embed(title="", description=":green_circle: Bot is online", color=BORDER_COLOR_GREEN)
    await DISCORD_STATUS_CHANNEL_GET.send(embed=embed)
  else:
    print("Error getting channel")


# Reaction on Ping! This fun and quirky addition to our bot will automatically react with a funny emoji whenever someone pings the users specified in the section below.
# Example:
#   if f'<@1209606605830750309>' in message.content:
#     await message.add_reaction('<:s_catuwu:1211269079311187980>')
@client.event
async def on_message(message):
  if f'<User ID>' in message.content:
    await message.add_reaction('<Reaction emoji ID>')
  if f'<User ID>' in message.content:  
    await message.add_reaction('<Reaction emoji ID>')
  await client.process_commands(message)


# A feature that records every command used by users with detailed information.
@client.event
async def on_command(ctx):
    COMMAND_CHANNEL = client.get_channel(DISCORD_COMMAND_CHANNEL)
    embed = discord.Embed(title="Command Used", color=BORDER_COLOR)
    embed.add_field(name="Server", value=ctx.guild.name) 
    embed.add_field(name="Channel", value=ctx.channel.name)
    embed.add_field(name="User", value=f"<@{ctx.author.id}> • {ctx.author} • (ID: {ctx.author.id})")
    embed.add_field(name="Command", value=ctx.command.name)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.add_field(name="Time", value=ctx.message.created_at.strftime("%m/%d/%Y, %H:%M:%S")) 
    
    await COMMAND_CHANNEL.send(embed=embed)


# This function effectively identifies, records, and removes any banned words utilized by users within the Discord server.
full_time = datetime.datetime.now()
truncated_time = str(full_time).split('.')[0]
banned_words = ["bannedword"] 
user_violations = {}  
@client.event
async def on_message(message):
  for word in banned_words:
    if word in message.content:
      if message.author.id in user_violations:
        user_violations[message.author.id] += 1
      else:
        user_violations[message.author.id] = 1
      embed = discord.Embed(title="Word Violation", color=BORDER_COLOR_RED)
      embed.add_field(name="User", value=message.author.mention)
      embed.add_field(name="Channel", value=message.channel.mention)
      embed.add_field(name="Word Used", value=word)
      embed.set_thumbnail(url=message.author.avatar.url)
      embed.add_field(name="Time", value=truncated_time)
      await client.get_channel(DISCORD_VIOLATION_CHANNEL).send(embed=embed)
      await message.delete()

  await client.process_commands(message)


# =-=-=-=-=-=-=-=-=-=-=
# ! Commands          -
# =-=-=-=-=-=-=-=-=-=-=
# ONLY OWNER COMMANDS -
# =-=-=-=-=-=-=-=-=-=-=
# Usage: !say <message>
@client.command()
async def say(ctx, *, message):
  if str(ctx.message.author.id) in OWNER_UID:
    await ctx.send(message)
    await ctx.message.delete()
  else:
    await ctx.send("You are not authorized to use this command.")


# Usage: !purge <count>
@client.command()
async def purge(ctx, amount: int):
  if str(ctx.message.author.id) in OWNER_UID:
    await ctx.channel.purge(limit=amount)
  else:
    await ctx.send("You are not authorized to use this command.")


# Usage: !sync
@client.command(name='sync')
async def sync(ctx):
    if str(ctx.message.author.id) in OWNER_UID:
        await client.tree.sync()
        await ctx.send('Synced commands!')
    else:
        await ctx.send('You are not authorized to use this command.')


# Usage: !clearall
@client.command()
async def clearall(ctx):
  if str(ctx.message.author.id) in OWNER_UID:
    await ctx.send("Are you sure you want to clear all contents in this channel? (yes/no)")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        response = await client.wait_for('message', check=check, timeout=30)
        if response.content.lower() == 'yes':
            await ctx.channel.purge(limit=None)
            await ctx.send('All contents in this channel have been cleared.')
        else:
            await ctx.send('Clear all operation cancelled.')
    except asyncio.TimeoutError:
        await ctx.send('No response received. Clear all operation cancelled.')
  else:
    await ctx.send('You are not authorized to use this command.')


# Usage: !joinvc1
@client.command()
async def joinvc1(ctx):
  if str(ctx.message.author.id) in OWNER_UID:
    channel = client.get_channel(DISCORD_VOICE_CHANNEL_1)
    await channel.connect()
  else:
    await ctx.send('You are not authorized to use this command.')


# Usage: !joinvc2
@client.command()
async def joinvc2(ctx):
  if str(ctx.message.author.id) in OWNER_UID:
    channel = client.get_channel(DISCORD_VOICE_CHANNEL_2)
    await channel.connect()
  else:
    await ctx.send('You are not authorized to use this command.')


# Usage: !leavevc
@client.command()
async def leavevc(ctx):
  if str(ctx.message.author.id) in OWNER_UID:
    if ctx.voice_client:
      await ctx.voice_client.disconnect()
      await ctx.send("Left the voice channel")
    else:
      await ctx.send("Not in a voice channel")
  else:
    await ctx.send('You are not authorized to use this command.')


# Usage: !admin
@client.command()
async def admin(ctx):
  if str(ctx.message.author.id) in OWNER_UID:
    embedVar = discord.Embed(title=f"{SERVER_NAME} Admin Commands", description="", color=BORDER_COLOR)
    embedVar.add_field(name="!admin", value="", inline=False)
    embedVar.add_field(name="!say <message>", value="", inline=False)
    embedVar.add_field(name="!purge <count>", value="", inline=False)
    embedVar.add_field(name="!sync (update '/' commands)", value="", inline=False)
    embedVar.add_field(name="!clearall", value="", inline=False)
    embedVar.add_field(name="!joinvc1 | !joinvc2", value="", inline=False)
    embedVar.add_field(name="!leavevc | !leavevc", value="", inline=False)
    embedVar.set_thumbnail(url=ICON_URL)
    embedVar.timestamp = datetime.datetime.utcnow()
    embedVar.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
    await ctx.send(embed=embedVar)
  else:
    await ctx.send('You are not authorized to use this command.')


# =-=-=-=-=-=-=-=-=
# Hybrid Commands -
# =-=-=-=-=-=-=-=-=
# PUBLIC COMMANDS -
# =-=-=-=-=-=-=-=-=
# Usage: !ping | /ping
@client.hybrid_command(name="ping", description=f"Get the ping of {SERVER_NAME} Bot", aliases=["latency"])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


# Usage: !avatar | /avatar
# Usage: !avatar <server member> | /avatar <server member>
@client.hybrid_command(name="avatar", description="Get the avatar of a server member", aliases=["av"])
async def avatar(ctx, member: discord.Member = None):
  if not member:
    member = ctx.author
  embed = discord.Embed(title="",
                        description=f"{member.display_name}'s avatar",
                        colour=member.colour)
  embed.set_author(name=f"{SERVER_NAME}", icon_url=ICON_URL)
  embed.set_image(url=member.avatar.url)
  embed.timestamp = datetime.datetime.utcnow()
  embed.set_footer(text=f"Requested by {ctx.author.name} \u200b",
                   icon_url=ctx.author.avatar.url)
  await ctx.send(embed=embed)


# Usage: !status | /status
@client.hybrid_command(name="status", description=f"Get the ping and status of the {SERVER_NAME} server")
async def status(ctx):
  try:
    start = time.time()
    server = mcstatus.JavaServer.lookup(SERVER_ADDRESS)  
    status = server.status()
    status.latency
    end = time.time()
    ping = (end - start) * 1000
    players = []
    for player in status.players.sample or []:
      players.append(player.name)
    embed = discord.Embed(title=f"Server Status for {SERVER_NAME}",
                          color=discord.Color.green(), description="<a:yes:1145493371981402183> Online")
    embed.add_field(name="Players Online",
                    value=f"{status.players.online}/{status.players.max}", inline=False)
    embed.add_field(name="Players List", value='\n'.join(players), inline=False)
    embed.set_footer(text=f'Ping: ~50ms • Version: {status.version.name}', icon_url=ICON_URL)
    embed.set_thumbnail(
        url=ICON_URL)
    await ctx.send(embed=embed)
  except Exception as e:
    await ctx.send(f"An error occurred while pinging the server: {str(e)}")


# Usage: !help | /help
@client.hybrid_command(name="help", description="Get help from the bot", aliases=["faq"])
async def help(ctx):
    response_message = f"Hi <@{ctx.author.id}>, {SERVER_NAME} bot is here! If you have any questions/issues related to the Minecraft or Discord Server, you can ask in {DISCORD_QA_CHANNEL} or create a ticket at {DISCORD_TICKET_CHANNEL} and one of our staff members will reply as soon as possible!, Run '!command' for more."
    await ctx.send(response_message)


# Usage: !about | /about
@client.hybrid_command(name="about", description="Get info about the bot", aliases=["info"])
async def about(ctx):
    response_message = f"Hi <@{ctx.author.id}>, {SERVER_NAME} Bot is a multipurpose tool designed to assist with all your server needs. Developed by the {SERVER_NAME} Team :purple_heart:"
    await ctx.send(response_message)


# Usage: !ip | /ip
@client.hybrid_command(name="ip", description=f"Get the address and port for the {SERVER_NAME} server", aliases=["address"])
async def ip(ctx):
    embedVar = discord.Embed(title=f"{SERVER_NAME} Server Address", color=BORDER_COLOR)
    embedVar.add_field(name="Java & Bedrock Address", value=f"{SERVER_ADDRESS}", inline=False) 
    embedVar.add_field(name="Java & Bedrock Port", value=f"{SERVER_PORT}", inline=False)
    embedVar.set_thumbnail(url=ICON_URL)
    embedVar.timestamp = datetime.datetime.utcnow()
    embedVar.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
    await ctx.send(embed=embedVar)


# Usage: !store | /store
@client.hybrid_command(name="store", description="Get link to the server store", aliases=["shop"])
async def store(ctx):
  embedVar = discord.Embed(title=f"{SERVER_NAME} Store", color=BORDER_COLOR)
  embedVar.add_field(name="Store Link", value=f"{SERVER_STORE}", inline=False)
  embedVar.set_thumbnail(url=ICON_URL) 
  embedVar.timestamp = datetime.datetime.utcnow()
  embedVar.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
  await ctx.send(embed=embedVar)


# Usage: !color | /color
@client.hybrid_command(name="color", description="Get Minecraft color codes", aliases=["colors"])
async def color(ctx):
  embedVar = discord.Embed(title="Minecraft Color Codes", color=BORDER_COLOR)
  embedVar.set_thumbnail(url=ICON_URL)
  embedVar.set_image(url=f"{BOT_IMG_SRC}ColorsEthel.png")
  embedVar.timestamp = datetime.datetime.utcnow()
  embedVar.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
  await ctx.send(embed=embedVar)


# Usage: !vote | /vote
@client.hybrid_command(name="vote", description="Get links to vote for the server", aliases=["votes", "voting"])
async def vote(ctx):
  embedVar = discord.Embed(
        title=f"{SERVER_NAME} Voting",
        description=f"Vote for {SERVER_NAME} and win amazing in-game rewards!", 
        color=BORDER_COLOR)
  embedVar.add_field(name="Vote Link 1", value=f"[{VOTE_WEBSITE_1_NAME}]({VOTE_WEBSITE_1_URL})", inline=False)
  embedVar.add_field(name="Vote Link 2", value=f"[{VOTE_WEBSITE_2_NAME}]({VOTE_WEBSITE_2_URL})", inline=False)
  embedVar.add_field(name="Vote Link 3", value=f"[{VOTE_WEBSITE_3_NAME}]({VOTE_WEBSITE_3_URL})", inline=False)
  embedVar.add_field(name="Vote Link 4", value=f"[{VOTE_WEBSITE_4_NAME}]({VOTE_WEBSITE_4_URL})", inline=False)
  embedVar.add_field(name="Vote Link 5", value=f"[{VOTE_WEBSITE_5_NAME}]({VOTE_WEBSITE_5_URL})", inline=False)
  embedVar.set_thumbnail(url=ICON_URL)
  embedVar.timestamp = datetime.datetime.utcnow()
  embedVar.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
  view = View()
  button1 = Button(style=1, label="Vote Link 1", url=f"{VOTE_WEBSITE_1_URL}")
  button2 = Button(style=1, label="Vote Link 2", url=f"{VOTE_WEBSITE_2_URL}")
  button3 = Button(style=1, label="Vote Link 3", url=f"{VOTE_WEBSITE_3_URL}")
  button4 = Button(style=1, label="Vote Link 4", url=f"{VOTE_WEBSITE_4_URL}")
  button5 = Button(style=1, label="Vote Link 5", url=f"{VOTE_WEBSITE_5_URL}")
  view.add_item(button1)
  view.add_item(button2)
  view.add_item(button3)
  view.add_item(button4) 
  view.add_item(button5)
  await ctx.send(embed=embedVar, view=view)


# Usage: !skin | /skin
@client.hybrid_command(name="skin", description="Get help with changing your skin", aliases=["skins"])
async def skin(ctx):
  embedVar = discord.Embed(
        title= f"Looking to change up your skin on {SERVER_NAME}? Follow these simple steps:",
        color=BORDER_COLOR)
  embedVar.set_thumbnail(url=ICON_URL)
  embedVar.set_image(url=f"{BOT_IMG_SRC}NameMC-3.png")
  embedVar.add_field(name="1. Head over to the NameMC Website to explore a variety of skins. Once you find one you love, copy the Skin Page link (URL).", value="https://namemc.com/minecraft-skins", inline=False)
  embedVar.add_field(name=f"2. Hop over to the {SERVER_NAME} Discord server and create a ticket requesting assistance with setting your new skin. Make sure to include the Skin Page URL along with your in-game username.", value=f"{DISCORD_TICKET_CHANNEL}", inline=False)
  embedVar.add_field(name="3. That's it! Your new skin will be set, and you can now enjoy playing with your fresh look. Have fun!", value="", inline=False)
  embedVar.timestamp = datetime.datetime.utcnow()
  embedVar.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
  await ctx.send(embed=embedVar)


# Usage: !commands | /commands
@client.hybrid_command(name="commands", description="Get a list of all bot commands", aliases=["command"])
async def command(ctx):
  embedVar = discord.Embed(title=f"{SERVER_NAME} Bot Commands", description="", color=BORDER_COLOR)
  embedVar.add_field(name="playerlist (Survival Chat)", value="", inline=False)
  embedVar.add_field(name="!ip", value="", inline=False)
  embedVar.add_field(name="!status", value="", inline=False)
  embedVar.add_field(name="!vote", value="", inline=False)
  embedVar.add_field(name="!store", value="", inline=False)
  embedVar.add_field(name="!colors", value="", inline=False)
  embedVar.add_field(name="!skin", value="", inline=False)
  embedVar.add_field(name="!avatar", value="", inline=False)
  embedVar.add_field(name="!membercount | !mc", value="", inline=False)
  embedVar.add_field(name="!commands", value="", inline=False)
  embedVar.add_field(name="!ping", value="", inline=False)
  embedVar.add_field(name="!invite", value="", inline=False)
  embedVar.add_field(name="!help", value="", inline=False)
  embedVar.add_field(name="!about", value="", inline=False)
  embedVar.set_thumbnail(url=ICON_URL)
  embedVar.timestamp = datetime.datetime.utcnow()
  embedVar.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
  await ctx.send(embed=embedVar)


# Usage: !membercount | /membercount
@client.hybrid_command(name="membercount", description="Get the member count for the server", aliases=["mc"])
async def membercount(ctx):
    server = ctx.guild
    member_count = server.member_count
    embed = discord.Embed(title=f"{server.name} Member Count", description="", color=BORDER_COLOR)
    embed.add_field(name=f"**{member_count}**", value="", inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{SERVER_NAME} \u200b', icon_url=ICON_URL)
    await ctx.send(embed=embed)


# Usage: !invite | /invite
@client.hybrid_command(name="invite", description="Generates a temporary invite link to the server", aliases=["inv"])
async def invite(ctx):
    invite = await ctx.channel.create_invite(max_age=86400, max_uses=1)
    await ctx.send(f"Here is your temporary invite link to the server <:ZeroTwo_heartlove:1209962520794898564>\n{invite}")


client.run(BOT_TOKEN)