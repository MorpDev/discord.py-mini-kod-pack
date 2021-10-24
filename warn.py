import discord
from discord.ext.commands import commands,has_permissions, MissingPermissions
import json

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

client = discord.ext.commands.Bot(command_prefix = 'prefix')

@client.command(pass_context = True)
@has_permissions(manage_roles=True, ban_members=True)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await client.say("Sebep Gir")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)

@client.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await client.say(f"{user.name} Uyarıldı {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
      break
  else:
    await client.say(f"{user.name} Uyarıldı")  

@warn.error
async def kick_error(error, ctx):
  if isinstance(error, MissingPermissions):
      text = "Pardon {}, Yetkin Yok!".format(ctx.message.author)
      await client.send_message(ctx.message.channel, text)   

client.run("token")user.name
