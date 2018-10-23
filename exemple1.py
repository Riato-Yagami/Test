import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!carre'):
        N=10
        for i in range(N):
            await client.send_message(message.channel, 'Vertmo'*5)
    elif message.content.startswith('!bot'):
        await client.send_message(message.channel, 'You rang?')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('')