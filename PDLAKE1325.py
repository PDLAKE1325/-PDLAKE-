import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("/ke_wind 프사"):
        await message.channel.send('https://cdn.discordapp.com/attachments/710146103005413446/738726827140579448/ke_wind.png')
    if message.content.startswith("/PDLAKE1325 프사"):
        await message.channel.send('https://cdn.discordapp.com/attachments/710146103005413446/738727218272010250/PDLAKE1325.png')

@client.event
async def on_mamber_join(member):
    role = ""
    for i in member.server.roles:
        if i.name == "[ 일반유저 ]":
            role = i
            break
    await client.add_roles(member, role)


client.run("NzM2NDA2NTE3OTUxMjM0MDc4.XxuWAw.Gwm27xOiznCfBkxg5bNeIOpKs40")
