import discord
from discord.ext import commands
import random
import os

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$",intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command()
async def contaminacion(ctx):
    contaminacion = random.choice(os.listdir("contaminacion"))
    with open(f'contaminacion/{contaminacion}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def idea1(ctx):
    await ctx.send ('Hola amigo , que hay de nuevo , cansado de las ideas aburridas para reciclar , pues nosotros tambien ; la siguiente idea es muy sencilla , con materiales de casa crea algo nuevo que te guste , no un aburrido lapicero ,algo que te guste y te motive a reciclar')

@bot.command()
async def idea2(ctx):
    await ctx.send ('Hola my friend 😜, recuerda no botar basura ,existen las canecas y si no tienes canecas cerca guardala para separarla debidamente')

@bot.command()
async def idea3(ctx):
    await ctx.send ('Hola mi bro , otra idea es el reciclaje , ahhh😪,no algo aburrido,aprendete o creo una cancion que te ayude a recordar como se separan los elementos en los diferentes coolores , no olvides separar muy bien los reciduos')

@bot.command()
async def idea4(ctx):
    await ctx.send ('Que hubo mi amigo , otra idea es que cuando puedas salgas a recoger basura , con tus amigos o familia ,escuchando musica o bailando ;lo importante es que ayudes al planeta 🌍')

@bot.command()
async def idea5(ctx):
    await ctx.send ('Hola que más , ¿tienes mascota? , si dijiste que si felicitaciones , si no busca algun animal afectado por la contaminacion cuidalo y adoptalo ,habras salvado una vida y obtenido un amigo')

@bot.command()
async def carton(ctx):
    await ctx.send ('Puedes hacer una bonita caja , o pequeñas mascotas , recuerda alimentar al canariton')

@bot.command()
async def papel(ctx):
    await ctx.send ('Haz figuras de origami o dibujos divertidos')

@bot.command()
async def plastico(ctx):
    await ctx.send ('Forra tus cuadernos y otras cosas que no quieras ensuciar o dañar')

@bot.command()
async def pilas(ctx):
    await ctx.send ('vendelas🤑,no ganaras mucho dinero😒,pero ayudaras al planeta😎🥳')

@bot.command()
async def botella_plastico(ctx):
    await ctx.send ('pintala, y conviertela en lo que quieras: un avion ✈👨‍✈️, tu personaje favorito🧞‍♂️ , lo que quieras ')
bot.run("token")
