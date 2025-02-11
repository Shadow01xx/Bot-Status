import discord
import asyncio
from discord.ext import commands

# Criação do bot com o prefixo "!"
intents = discord.Intents.default()
intents.message_content = True  # Permite ler o conteúdo das mensagens
bot = commands.Bot(command_prefix='!', intents=intents)

# Lista de status que o bot vai exibir
status_messages = [
    'Craft Survival CFS',
    'Craft Survival CFS',
    'Craft Survival CFS',
    'Craft Survival CFS',
]

# Função para atualizar o status a cada 5 segundos
async def update_status():
    while True:
        for status_message in status_messages:
            activity = discord.Game(name=status_message)  # Status "Jogando"
            await bot.change_presence(activity=activity)  # Muda o status
            await asyncio.sleep(5)  # Espera 5 segundos antes de mudar novamente

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

    # Inicia a atualização de status em paralelo
    bot.loop.create_task(update_status())

# Inicie o bot com o token
bot.run('MTMyOTMwNzE1Mjc0OTE3MDgwMg.G5BaUH.GQcVKp-FA4n6HmAMnYtTCdz9uvy-WQ_fk514zQ')  # Substitua 'SEU_TOKEN_AQUI' pelo seu token de bot
