while 1 < 2:
  status = ["texto1", "texto2", "etc"]
  choice = random.choice(status)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=choice))
  await asyncio.sleep(15)


# Obs: No início do main.py tem os imports neah? Pois é, la vc vai adicionar mais 2:
import random
import asyncio

# Lembrando o código da atualização de status automática tem que ser colocada dentro do evento "on_message"
