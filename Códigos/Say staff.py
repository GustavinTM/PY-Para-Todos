@bot.command(
  name="say"
  )
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, arg=None):
  if arg == None:
    await ctx.send("Por favor especifique a mensagem")
  else:
    await ctx.send(arg)
    await ctx.message.delete()
@say.error
async def say_handler(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Você não tem permissão para executar esse comando")
