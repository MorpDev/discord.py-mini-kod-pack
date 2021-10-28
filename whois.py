@bot.command()
async def bukim(ctx, *, member: discord.Member = None):
  if member==None:
    member=ctx.author
  roles=[x.mention for x in member.roles]
  roles=", ".join(roles)
  embed = discord.Embed(title="Bu Kim")
  embed.description = """
**İsmi Ve Etiketi:** {.name}#{.discriminator}\n**Kullanıcı Adı:** {.nick}\n**Hesap Kuruluş Tarihi:** {.hesap}\n**Sunucuya Girdiği Tarih:** {.giris}\n**Durum:** {.durm}\n**Avatar URL:** [Tıkla]({.avatar_url})\n**Bot mu:** {.bot}\n**Rolleri:**  {}""".format(member, member, member, member, member, member, member, member, roles)
  embed.set_thumbnail(url=member.avatar_url)
  await ctx.send(embed=embed)
@whois.error
async def whois_error(ctx, error):
    if isinstance(error, commands.BadArgument):
      member=ctx.author
      roles=[x.mention for x in member.roles]
      roles=", ".join(roles)
      embed = discord.Embed(title="Info")
      embed.description = """
**İsmi Ve Etiketi:** {.name}#{.discriminator}\n**Kullanıcı Adı:** {.nick}\n**Hesap Kuruluş Tarihi:** {.hesap}\n**Sunucuya Girdiği Tarih:** {.giris}\n**Durum:** {.durm}\n**Avatar URL:** [Tıkla]({.avatar_url})\n**Bot mu:** {.bot}\n**Rolleri:** {}""".format(member, member, member, member, member, member, member, member, roles)
      embed.set_thumbnail(url=member.avatar_url)
      await ctx.send(embed=embed)
