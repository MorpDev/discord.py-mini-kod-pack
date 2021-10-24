@client.event
async def on_message_delete(message):
    embed = discord.Embed(title="{} Mesaj Silindi".format(message.author.name),
                          description="", color=0xFF0000)
    embed.add_field(name=message.content, value="Bu Mesaj Silindi",
                    inline=True)
    channel = client.get_channel(kanalID) #log kanal ID
    await channel.send(channel, embed=embed)

#mesaj düzenleme kısmı
@client.event
async def on_message_edit(message_before, message_after):
    embed = discord.Embed(title="{} Mesaj Düzenlendi".format(message_before.author.name),
                          description="", color=0xFF0000)
    embed.add_field(name=message_before.content, value="Eski Mesaj",
                    inline=True)
    embed.add_field(name=message_after.content, value="Yeni Mesaj",
                    inline=True)
    channel = client.get_channel(kanalID) #log kanal ID
    await channel.send(channel, embed=embed)
