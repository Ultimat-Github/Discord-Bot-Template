import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

intents = discord.Intents.default()
intents.message_content = True 


@bot.event
async def on_ready():
    activity = discord.Game(name="Disocord", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('We have logged in as {0.user}'.format(bot))


    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!",ephemeral=True)    



try:
  token = "YOUR TOKEN" or "" 
  if token=="":
      raise Exception("Please add your token.")     
  bot.run(token) 
except discord.HTTPException as e:
   if e.status ==429:
      print("The Discord servers denied the connection for making too many requests")     
      print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")    
   else:
       raise e