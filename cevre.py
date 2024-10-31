import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def sohbet(ctx):
    await ctx.send(f'Merhaba {ctx.author.name}, çevre ile ilgili sohbet etmek ister misin?')

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