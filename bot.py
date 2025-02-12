import discord
import asyncio
from discord.ext import commands

# Configuração do bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de status para alternar a cada 5 segundos
status_list = [
    "Jogando Craft Survival CFS",
    "Explorando o servidor!",
    "Aventuras no mundo CFS!",
    "Desbravando terras desconhecidas!"
]

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} está online!")

    # 🔹 Loop para atualizar o status a cada 5 segundos
    async def update_status():
        while True:
            for status in status_list:
                await bot.change_presence(activity=discord.Game(name=status))  # Status "Jogando"
                await asyncio.sleep(5)  # Aguarda 5 segundos antes de mudar novamente

    bot.loop.create_task(update_status())

# 🔹 Comando para mostrar o status do bot (Apenas para quem tem o cargo "☯ ⌞Fundador⌝ ☯")
@bot.command()
async def status(ctx):
    role_name = "☯ ⌞Fundador⌝ ☯"  # Nome exato do cargo necessário

    # Verifica se o usuário tem o cargo
    if any(role.name == role_name for role in ctx.author.roles):
        current_status = ctx.me.activity.name if ctx.me.activity else "Nenhum status definido"
        await ctx.send(f"📢 **Status atual do bot:** `{current_status}`")
    else:
        await ctx.send("❌ **Você não tem permissão para usar este comando!**")

# 🔹 Iniciar o bot (adicione o token manualmente ao rodar o script)
bot.run("SEU_TOKEN_AQUI")
