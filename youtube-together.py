from discord.ext import commands
from discord_together import DiscordTogether

client = commands.Bot(command_prefix="!") #sizin prefix

@client.event
async def on_ready():
    client.togetherControl = await DiscordTogether("token")
    print('Bot Çevrimiçi!')

@client.command()
async def start(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Link'e Tıkla!\n{link}")

client.run("bot_token")
