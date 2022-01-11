import random
import discord
from discord.ext import commands
urls = {"php": "https://www.php.net/docs.php",
        "bash": "https://ryanstutorials.net/bash-scripting-tutorial/\nhttps://www.youtube.com/watch?v=oxuRxtrO2Ag\nhttps://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html\nhttps://devhints.io/bash\nhttps://www.shellscript.sh/\nhttps://www.shell-tips.com/bash/arrays/#bash-associative-array-dictionaries-hash-table-or-keyvalue-pair",
        "mySQL":"https://dev.mysql.com/doc/refman/8.0/en/language-structure.html",
        "python":"https://docs.python.org/3/",
        "discord":"https://discordpy.readthedocs.io/en/latest/#manuals\nhttps://github.com/Rapptz/discord.py/tree/master/examples\nhttps://discord.com/invite/r3sSKJJ\nhttps://www.techwithtim.net/tutorials/discord-py/hosting-a-discord-bot-for-free/",
        "c":"First link is to Lib Gen\nhttp://libgen.is/book/index.php?md5=556E6BEE561B776C95C6872C441BAAD1\n Ding's book https://diveintosystems.org/book/index.html\n Free Coruse https://github.com/zedshaw/learn-c-the-hard-way-lectures",
        "commands":"-bash\n-c\n-commands\n-disc\n-linux\n-php\n-python\n-playlist\n-njit\n-pma\n-twitter\n-VScode\n-pma",
        "linux":"https://ubuntu.com/download \nhttps://getfedora.org/\nhttps://www.commandlinefu.com/commands/browse/sort-by-votes\nWindows has WSL so here's a link to that:\nhttps://docs.microsoft.com/en-us/windows/wsl/install-win10",
        "Playlist":"https://open.spotify.com/playlist/576j38Yts0TeQGzOpPHvTm?si=ugUeJNk3T26mYJLmCznP6g",
        "njit":"Fuck NJIT.\nhttps://twitter.com/NJIT/status/971122883815763968",
        "twitter":"https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2\nhttps://github.com/twitterdev/Twitter-API-v2-sample-code",
        "VScode":"This is how you setup vscode to do ssh\n https://discord.com/channels/883082292879323157/883082293332279386/885628408703356938",
        "pma": ""
        }#dict of all the links
cdPhrases=['Fuck off.',
           'My dude chill out',
           'I *JUST* posted those links.',
           'Listen it aint hardwork but it is honest work.',
           'I am going to delete canvas if you bug me again.',
           'That is it you will not like me when I am angry.',
           'Hail Hydra! You prick!',
           'Heil BASSEL! OUR LORD AND SAVIOR!',
           'Somebody get this guy a body bag for when I am done with him.'] #Spam phrases for those dickheads trying to abuse the bot
pmaVids=['https://www.youtube.com/watch?v=DykVJl6wr_4',
         'https://www.youtube.com/watch?v=fzoYZV8WIUo&t=2s',
         'https://www.youtube.com/watch?v=0yGSQOWEXRo&t=2s',
         'https://www.youtube.com/watch?v=U_XFTwFGCwQ',
         'https://www.youtube.com/watch?v=65BrEZxZIVQ']

client=commands.Bot(command_prefix='-',case_insensitive=True)#this is what the bot will be called ie bot or client,also not case sensitivity
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("NJIT hasn't gotten it together."))#Sets the game being played to this custom message, bot status is Online always
    print('My guy I am busy deleting Canvas.')

#Gives the links for the command "!php"
@client.command(name='php')
@commands.cooldown(1, 60, commands.BucketType.user)
async def php(ctx):
    if (ctx.author.bot): return
    response=urls["php"]
    await ctx.send(response)


#Gives the links for the command "!mySQL"
@client.command(name='mySQL')
@commands.cooldown(1, 60, commands.BucketType.user)
async def mySQL(ctx):
    if (ctx.author.bot): return
    response=urls["mySQL"]
    await ctx.send(response)


#Gives the links for the command "!python"
@client.command(name='python')
@commands.cooldown(1, 60, commands.BucketType.user)
async def python(ctx):
    if (ctx.author.bot): return
    response=urls["python"]
    await ctx.send(response)


#Gives the links for the command "!bash"
@client.command(name='bash')
@commands.cooldown(1, 60, commands.BucketType.user)
async def bash(ctx):
    if (ctx.author.bot): return
    response=urls["bash"]
    await ctx.send(response)


#Gives the links for the command "!c"
@client.command(name='c')
@commands.cooldown(1, 60, commands.BucketType.user)
async def c(ctx):
    if (ctx.author.bot): return
    response=urls["c"]
    await ctx.send(response)

#Gives the links for the command "!disc"
@client.command(name='disc')
@commands.cooldown(1, 60, commands.BucketType.user)
async def disc(ctx):
    if (ctx.author.bot): return
    response=urls["discord"] #This gives a ton of resources for discord.py
    await ctx.send(response)

#Gives the links for the command "!linux"
@client.command(name='linux')
@commands.cooldown(1, 60, commands.BucketType.user)
async def linux(ctx):
    if (ctx.author.bot): return
    response=urls["linux"]
    await ctx.send(response)


#Gives the links for the command "!playlist"
@client.command(name='playlist')
@commands.cooldown(1, 60, commands.BucketType.user)
async def linux(ctx):
    if (ctx.author.bot): return
    response=urls["Playlist"]
    await ctx.send(response)


#Gives the links for the command "!njit"
@client.command(name='NJIT')
@commands.cooldown(1, 60, commands.BucketType.user)
async def njit(ctx):
    if (ctx.author.bot): return
    response=urls["njit"]
    await ctx.send(response)


#detects messages with the content PMA and sends a video
@client.command(name='pma')
@commands.cooldown(1, 15, commands.BucketType.user)
async def pma(ctx):
    if (ctx.author.bot): return
    pmaSend=random.choice(pmaVids)
    await ctx.send(pmaSend)

@client.command(name='twitter')
@commands.cooldown(1,60,commands.BucketType.user)
async def twitter(ctx):
    if (ctx.author.bot):return
    response=urls["twitter"]
    await ctx.send(response)


#Gives the links for the command "vsCode"
@client.command(name='vscode')
@commands.cooldown(1, 60, commands.BucketType.user)
async def vscode(ctx):
    if (ctx.author.bot): return
    response=urls["VScode"]
    await ctx.send(response)


#Dm's user a list of commands to use
@client.command(name='commands')
async def on_message(ctx):
    if (ctx.author.bot): return
    #random comment
    houseKeeping='Each command has resources for that language or topic,the following are a list of commands available to you:\n '
    response=urls["commands"]#Dict entry for all the commands
    await ctx.author.send(houseKeeping+response)

#Gives the links for the command "!poll"
@client.command(name='poll')
@commands.cooldown(1, 15, commands.BucketType.user)
async def python(ctx):
    if (ctx.author.bot): return
    response=urls["poll"]
    await ctx.send(response)

@client.event  #Error handling for invalid commands,Sends the message below to tell them how to get the list of valid commands
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command is invalid. Please use -commands to receive  a dm telling you the valid commands.')
    if isinstance(error, commands.CommandOnCooldown):
        pharses=random.choice(cdPhrases)
        await ctx.send(pharses)

client.run('Not allowed to publish this token publicly. Discord will remove the bot.')#Bot token goes here
