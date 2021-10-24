import discord #Imports modül
from discord.ext import commands #Imports discord uzantilari
#burayi ellemeyin
client = commands.Bot(command_prefix='pb?')
#burası tokeni saklayan yer
token = "tokenini Yaz"

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen Tüm Gereksinimleri İletin.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Tüm Gereksinimlere Sahip Değilsin.")

#burası banlama yeri
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#burası unban yeri
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await csx.guild.unban(user)
            await csx.send(f'Banı Açıldı {user.mention}')
            return

#burayı ellemeyin
client.run(token)
