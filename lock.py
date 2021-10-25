# etiketleyerek kanal kilitleme

@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Kanal Kilitlendi.')
   
# kanalda lock yazınca kilitleme

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Kanal Kilitlendi.')
@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('Yetkin Yok!')
