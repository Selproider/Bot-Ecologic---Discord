import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#--------------------------------------
@bot.command()
async def objetos(ctx):
    await ctx.send(f'1. tabaco\n2. gases\n3. limpieza\n4. pesticidas\n5. mobilario\n6. moho\n7. cosmeticos\n8. envases\n 9. aerosoles\n10. electronicos')

# ----------- 1 --------------
@bot.command()
async def tabaco(ctx):
    await ctx.send(f'Una de las fuentes de contaminación del interior más peligrosas y evitables, que libera numerosas sustancias químicas tóxicas.')

# ----------- 2 --------------
@bot.command()
async def gases(ctx):
    await ctx.send(f'Provienen de estufas, calefactores y cocinas de gas o leña, especialmente sin ventilación adecuada.')

# ----------- 3 --------------
@bot.command()
async def limpieza(ctx):
    await ctx.send(f'Muchos contienen comuestos orgánicos volátiles (COV), disolventes, y otras sustancias químicas agresivas que contaminan el aire y el agua.')

# ----------- 4 --------------
@bot.command()
async def pesticidas(ctx):
    await ctx.send(f'Su uso en interiores o jardines introduce toxinas persistentes que pueden afectar la salud.')

# ----------- 5 --------------
@bot.command()
async def mobiliario(ctx):
    await ctx.send(f'Pinturas con plomo, formaldehído en muebles de aglomerado y asbesto en edificios antiguos liberan sustancias nocivas con el tiempo.')

# ----------- 6 --------------
@bot.command()
async def moho(ctx):
    await ctx.send(f'El moho, los ácaros del polvo y el polen prosperan en ambientes húmedos, causando alergias y problemas respiratorios.')

# ----------- 7 --------------
@bot.command()
async def cosmeticos(ctx):
    await ctx.send(f'Algunos contienen microplásticos o sustancias nocivas que terminan en el sistema de aguas.')

# ----------- 8 --------------
@bot.command()
async def envases(ctx):
    await ctx.send(f'Especialmente los que contienen BPA, pueden transferir químicos a los alimentos y generan residuos de difícil degradación.')

# ----------- 9 --------------
@bot.command()
async def aerosoles(ctx):
    await ctx.send(f'Ambientadores y desodorantes liberan COV y otros compuestos que también pueden afectar la atmósfera.')

# ----------- 10 -------------
@bot.command()
async def electronicos(ctx):
    await ctx.send(f'Contienen metales pesados como plomo y mercurio que, sin una gestión adecuada, contaminan suelo y agua.')


bot.run("TOKEN")
