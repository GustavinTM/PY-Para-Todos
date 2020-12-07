@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, *, member: discord.Member=None, reason="Razão não especificada"):
  if member == None:
    await ctx.send("**Quem você quer banir?**")
  else:
    try:
      await member.ban(reason=reason)
      await ctx.send(f"**O membro {member} foi banido com sucesso!**\n**Razão: {reason}**")
    except:
      await ctx.send("**Não foi possível banir esse membro!**")
@ban.error
async def ban_handler(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send("**- Usuário Inválido!**")
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("**- Você não tem permissão para executar esse comando**")
