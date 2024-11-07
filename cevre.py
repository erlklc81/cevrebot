import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def neyapabilirim(ctx):
    fikirler = [
        "Diğer kişilere öğrendiklerini söyle :)",
        "Elektrikli kullanıma geçebilirsin. Soba gibi aletler yerine daha çevre dostu alternatifleri tercih edebilirsin.",
        "Eski pilli araç gereçlerini metal geri dönüşümüne atabilirsin.",
        "Yeni alet satın almak yerine eskilerini kullanabilirsin."
    ]

    await ctx.send(f"Evde çevre için yapabileceğin öneriler:\n- " + "\n- ".join(fikirler))

bot.run("token")
