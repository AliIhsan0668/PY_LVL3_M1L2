import discord
from discord.ext import commands
from config import token

#ARABANIN SINIFI
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    #İNFOMUN VERECEĞİ MESAJ
    def info(self):
        return f"Arabanın rengi {self.color} ve markası {self.brand}."

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='*', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py kütüphanesi ile oluşturulmuş echo-bot!')

@client.command()
async def info(ctx):
    botmesaj = "Ben BotMıstık dünyama hoşgeldiniz diyorum"
    await ctx.send(botmesaj)

@client.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

#GERİ BİLDİRİM TARAFI
@client.command()
async def car(ctx, color: str, brand: str):
    car = Car(color, brand)
    await ctx.send(car.info())

@client.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

client.run(token)