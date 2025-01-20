import discord

async def pokedex_embed(ctx, Name, id, Type_1, Type_2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary):
  embed = discord.Embed(    
  title = f"{Name}:",
  description = f"Information about {Name}:",
  color= discord.Color.red()
  )
  embed.add_field(name=f"ID of {Name}", value={id}, inline = False)
  embed.add_field(name="Type 1:", value={Type_1}, inline = False)
  embed.add_field(name="Type 2:", value={Type_2}, inline = True)
  embed.add_field(name="The Total Stats:", value={Total}, inline = False)
  embed.add_field(name="Healthpoints:", value={HP}, inline = True)
  embed.add_field(name="Attackpoints:", value={Attack}, inline = True)
  embed.add_field(name="Defencepoints:", value={Defense}, inline = True)
  embed.add_field(name=f"Special Attack:", value={Sp_Atk}, inline = True)
  embed.add_field(name=f"Special Defence:", value={Sp_Def}, inline = True)
  embed.add_field(name=f"Speed", value={Speed}, inline = True)
  embed.add_field(name=f"Generation:", value={Generation}, inline = False)
  embed.add_field(name=f"Legendary Pokemon:", value={Legendary}, inline = True)
  await ctx.respond(embed=embed)