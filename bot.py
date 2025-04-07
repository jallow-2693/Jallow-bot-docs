import os
import discord
from discord.ext import commands

# Récupérer le token depuis les variables d'environnement
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} a bien démarré!')

@bot.command()
async def hello(ctx):
    await ctx.send('Bonjour ! Je suis Jallow Bot.')

# Lancer le bot
bot.run(TOKEN)
