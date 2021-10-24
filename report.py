from discord.ext import commands #modül


client = commands.Bot(command_prefix='prefix') #komuta özel prefix yeri


@client.command()
async def suggest(ctx, suggestion):
    dm_user = client.get_user(ID) #ID YAZAN YERE ID'Nİ GİR
    await dm_user.send("{} Report Sebebi:      '{}'".format(ctx.author.mention, suggestion))

client.run('token')
#bu kod bot sahibine birini report etmeyi sağlar
