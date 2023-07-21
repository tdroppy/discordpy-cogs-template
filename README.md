# droppy-discord-bot
Discord bot template that features discord.py's cog feature.

# How to run


1: download/clone the repository

2: Depending on whether you are on windows or linux run the following commands in the bot's main directory:

Windows: 'pip install discord' then 'pip install dotenv'

Linux: 'source .venv/bin/activate' this creates your python environment, in that you can then do 'pip install discord' then 'pip install dotenv'


3: create a file in the root folder fo the bot called '.env'

4: then write 'DISC_TOKEN=your token'

if you dont know what or how to get your bot token follow this guide: https://www.writebots.com/discord-bot-token/

Now you should be good to go, run the main.py file and your done.

# How to use (developing wise)

Essentially, main.py is the bot itself, when the bot starts it loads the modules or 'cogs' that store the commands that you would want to write. 


Look at ./cogs/User.py for example. First we import our dependancies, then we declare a class (make sure to pass commands.Cog as I did or it wont work)


Then we create an __init__ function containting 'self.bot = bot' so we can use normal bot utilities in this class. Instead of @bot.command(), with cogs we
change this to @commands.command


We then create the normal async ctx command as usual, then finally we include the function that allows main.py to include this file, setup().

main.py should remain relatively untouched as you wont need to edit any code to add more commands/cogs.

Enjoy!

