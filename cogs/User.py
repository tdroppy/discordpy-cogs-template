import discord
from discord.ext import commands
from discord.utils import get

class User(commands.Cog): #creates class that stores commands
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command() #executes when user types '$myid'
    async def myid(self, ctx):
        embed=discord.Embed(title=f"User Profile of **{ctx.author}** ({ctx.author.display_name})", description=f"A summary of {ctx.author.display_name}'s profile.", color=ctx.author.accent_color)
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.add_field(name="UID", value=ctx.author.id)
        embed.add_field(name="Date Created", value=ctx.author.created_at)
        await ctx.reply(embed=embed)
        print(__name__)

async def setup(bot):
    await bot.add_cog(User(bot)) #adds selected cog to main bot




    
