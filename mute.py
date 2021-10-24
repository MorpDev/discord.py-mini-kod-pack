@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator veya ctx.message.author.id == 'bot owner id':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="Adam Mutelendi", description="**{0}** Muteleyen **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Reddedildi", description="Yetkin Yok Dostum.", color=0xff00f6)
        await bot.say(embed=embed)
