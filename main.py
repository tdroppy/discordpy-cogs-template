import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv() #used to store discord token (DISC_TOKEN)
DISC_TOKEN = os.getenv('DISC_TOKEN')

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="$", intents=intents)

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="da servers"))

        try:
            for file in os.listdir("./cogs"): #iterates through all files in ./cogs
                if file.endswith(".py"): 
                    name = file[:-3] #removes .py extension from file name string
                    await bot.load_extension(f"cogs.{name}") #loads said file (cog)
                    print(f'Loaded {name}')
            print('ready!')
        except:
            print('An error occured while loading cogs.') #very vague i know

    @bot.command() #users can perform '$obliterate [cogs.name]' to unload a cog forcefully
    async def obliterate(ctx, arg): #may want to add a check to lock out unwanted users from access this
        try:
            await bot.unload_extension(f'cogs.{arg}')
            await ctx.send(f'Successfully obliterated extension: {arg}')
        except: #very vague once again, will work on this
            await ctx.send(f'Failed to load extension: {arg}; This could happen if you misspell the extension or it is already unloaded.')

    @bot.command() #users can perform '$load [cogs.name]' to load cog into bot (this does not require a restart)
    async def load(ctx, arg): #refer to comment made in obliterate()
        try:
            await bot.load_extension(f'cogs.{arg}')
            await ctx.send(f'Successfully loaded extension: {arg}')
        except: #once again refer to comment made in obliterate()
            await ctx.send(f'Failed to load extension: {arg}; This could happen if you misspell the extension or it is already loaded.')
        
    @bot.command()
    async def reload(ctx): #reloads extension, may want to add user check (allows editing code without restart)
        for file in os.listdir('./cogs'): #im so proud of this all :)
            if file.endswith('.py'):
                name = file[:-3]
                try:
                    await bot.unload_extension(f'cogs.{name}')
                    await bot.load_extension(f'cogs.{name}')
                    print(f'reloaded cog: {name}')
                except:
                    print('WARNING: Extension already unloaded!') #will work on vague excepts i promise
        await ctx.send('All extensions reloaded!')

    bot.run(DISC_TOKEN)

if __name__ == "__main__":
    main()