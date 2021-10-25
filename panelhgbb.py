intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='prefix', intents=intents) #prefix yeri

async def on_member_join(member):
    member_channel = client.get_channel(KanalID) #panel kanalının ID'si
    await member_channel.edit(name=f"Members: {member.guild.member_count}")
#kod şu işe yarar: sunucuya biri katıldığında sunucudaki kişi sayısına göre ses kanalını düzenler
