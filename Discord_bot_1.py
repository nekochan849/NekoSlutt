# neko slut by Neko_Chan

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='~')

import random

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
@commands.has_any_role("Mods")
async def kick(ctx, user: discord.Member):
    await bot.say("Cya, {}. next time dont be a meanie!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def puke(ctx, target: discord.Member = None):
    async for message in bot.logs_from(ctx.message.channel, 20):
        if message.author == target:
                await bot.add_reaction(message, '🤢')

@bot.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.CommandOnCooldown):
        cd = round(error.retry_after) + 1
        message = await bot.send_message(channel, 'You need to wait {0:d} more second{1}.'.format(cd, 's' if cd != 1 else ''))
    elif isinstance(error, commands.CheckFailure):
        message = await bot.send_message(channel, 'NO your not aloud cutie this command is for the adults')

@bot.command(pass_context=True)
async def what(ctx):
    possible_responses = [
        'you have a hard pussy',
        'why is my dick wet?',
        'FUCK ME~!!',
        'dont be alittle bitch',
        'idk what you want me to say',
    ]
    await bot.say(random.choice(possible_responses) + ", " + ctx.message.author.mention)

@bot.listen()
async def on_member_join(member):
	is_verified = False
	for role in member.roles:
		if role.name == "Verified":
			is_verified = True
			break
	if is_verified == False:
		await bot.send_message(member,"Please message the bot with the command ~verify to get normal permissions")

@bot.command(pass_context=True)
async def roles(context):
    """Displays all of the roles with their ids"""
    roles = context.message.server.roles
    result = "`The roles are "
    for role in roles:
        result += role.name + ": " + role.id + ", "
    result += "`"
    await bot.say(result)

@bot.event
async def on_message(message):
    if random.randrange(50) == 0:
        possible_responses = [
            'mummy is thicc af',
            'how is everybodys day so far?',
            'i want to hold your hand',
            'I hope you all are playing nice!~',
            '''I'm horny as hell right now''',
            'Neko Slut here just reminding you that Lolis or for patting and not lewding',
            'Pssst, daddy touches mummy at night.',
            'Paul is trash POGGERS :dogeLuL:'
        ]
        message = await bot.send_message(message.channel, random.choice(possible_responses))
    await bot.process_commands(message)

bot.run("NDYwNjM2Njg2MzMwNjI2MDQ4.Di7w_A.HDm_Rbrexrh7BoHKo62fycJc-qk")
