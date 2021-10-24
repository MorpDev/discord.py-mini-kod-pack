@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
await client.kick(member)
await ctx.send(f'User {member} sunucudan gönderildi')
