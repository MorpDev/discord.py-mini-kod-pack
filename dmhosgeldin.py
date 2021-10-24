import discord
from discord.ext import commands

#bunu eklemeyi dene 
intents=intents=discord.Intents.all()

#yukarıdakiler işe yaramazsa bununla deneyin
#intents = discord.Intents()
#intents.members = True

#bot token ve komuta özel prefix yeri
token = 'bot tokenin' #bot tokenini girin 
bot=commands.Bot(command_prefix='prefix',intents=intents)

#Eventler
@bot.event
async def on_member_join(member):
    await member.send('buraya dm gidecek mesajı yaz')

@bot.event
async def on_ready():
    print('Bot Hazır')

bot.run(token)
