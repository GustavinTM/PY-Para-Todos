@bot.event
async def on_message(message):
  channel = message.channel
  if bot.user.mentioned_in(message):
    await channel.send("Coloque a mensagem aqui ou use um embed")
  await bot.process_commands(message)
