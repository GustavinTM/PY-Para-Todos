@bot.command(name="say")
async def say(ctx, *, arg=None):
  if arg == None:
    await ctx.send("Especifique a frase")
  else:
    await ctx.send(arg)
