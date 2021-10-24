@client.command()
async def sunucubilgi(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  Id = str(ctx.guild.id)
  bolge = str(ctx.guild.region)
  membercount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Sunucu Bilgileri",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Kurucu", value=owner, inline=True)
  embed.add_field(name="Sunucu ID", value=Id, inline=True)
  embed.add_field(name="Bölge", value=bolge, inline=True)
  embed.add_field(name="Üye Sayısı", value=membercount, inline=True)
