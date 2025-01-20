import discord
import asyncio
import os
import json
import requests
from bs4 import BeautifulSoup
from embedforpokedex import pokedex_embed
from discord.ext import bridge
from dotenv import load_dotenv
load_dotenv()

class PyCordBot(bridge.Bot):
  TOKEN = os.getenv("DISCORD_TOKEN")
  intents = discord.Intents.all()

client = PyCordBot(intents=PyCordBot.intents, command_prefix='!')

@client.listen()
async def on_ready():
  print(f'Logged in as {client.user.name}!')

@client.bridge_command(description='Pings the bot!')
async def ping(ctx):
  latency = (str(client.latency)).split('.')[1][1:3]
  await ctx.respond(f' The Bots latency is: {latency}ms.')

@client.bridge_command(description='Type out the ID of a Pokemon and get its Information!')
async def pokedex(ctx, pokemon_id:int):
  with open('pokemondata.json', 'r') as f:
    data = json.load(f)
  if pokemon_id != None and pokemon_id <= 800:
    await pokedex_embed(ctx, **data[pokemon_id - 1])
  else:
    if pokemon_id > 800:
      await ctx.respond("The Pokemon with the highest ID is 800 and can not be above it.")


@client.bridge_command(description='Get a image of any requested pokemon!')
async def pokemon_artwork(ctx, pokemon_name:str):
  HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
  }
  url = "https://pokemondb.net/sprites/"
  response = requests.get(url) # ,headers=HEADERS (use if the request for the image has not gone through)
  soup = BeautifulSoup(response.text, 'html.parser')
  img_tag = soup.find('img', {'class': 'img-fixed icon-pkmn', 'alt': {pokemon_name}})
  if img_tag:
    img_src = img_tag["src"]
    await pokemon_images_embed(ctx, img_src, pokemon_name)
  else:
    await ctx.respond(f"There is no Pokemon with the name ({pokemon_name})")

async def pokemon_images_embed(ctx, img_src, pokemon_name):
  embed = discord.Embed(    
  title = f"Artwork of {pokemon_name}:",
  color= discord.Color.red()
  )
  embed.set_image(url=img_src)
  await ctx.respond(embed=embed)

async def main_bot():
  print('Bot is starting...')
  await client.start(PyCordBot().TOKEN)


if __name__=='__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(asyncio.gather(main_bot()))

