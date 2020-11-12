


#import packages and stuff

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio 
import random
import os 
import zenora





#read token with another file named token.txt




#edit prefix and delete basic help command

bot = Bot(command_prefix="#")
bot.remove_command("help")


#making sure its online and changing presence
@bot.event
async def on_ready():

    #to see if we logged in or not

    print(f'LOCKED AND LOADED, SIR!')


    await bot.change_presence(status = 
            discord.Status.do_not_disturb,
            activity = discord.Activity
            (type = discord.ActivityType.
                playing, 
                name = "With...."))


#help embed with fields

@bot.group(invoke_without_command= True)
async def help(ctx):
    em = discord.Embed(title= "Help", description = "use <prefix>help <command> for extended info")

    em.add_field(name = "**Test**", value = "ping ")
    
    em.add_field(name = "**Moderation**", value = "kick, ban")
    

    await ctx.send(embed = em)

#template on how to add commands to help on command usage embed

@help.command()
async def kick(ctx):
    em = discord.Embed(title = "kick", description = "kicks a user from the guild.")
    
    em.add_field(name = "**Syntax**", value = "<prefix>k or kick @User")
    
    await ctx.send(embed = em)


@help.command()
async def ban(ctx):
    em = discord.Embed(title = "kick", description = "bans a user from the guild.")
    
    em.add_field(name = "**Syntax**", value = "<prefix>b or ban @User")
    
    await ctx.send(embed = em)

@help.command()
async def ping(ctx):
    em = discord.Embed(title = "ping", description = "pong")

    em.add_field(name = "**Syntax**", value = "<prefix>ping")

    await ctx.send(embed = em) 

#COMMANDS

#PING PONG
@bot.command()
async def ping(ctx):
    await ctx.send("pong") 





@bot.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, amount = 2):
    await ctx.channel.purge(limit = amount)
    await ctx.message.delete()
    

                    

#say command

@bot.command(aliases= ['s'])
async def say(ctx, * , msg):
    await ctx.message.delete()
    await ctx.send(f"{msg}" .format(msg))


#emojis

@bot.command()
async def dance(ctx):
   await ctx.message.delete()
   await ctx.send(" <a:dance:775321551205302292>")
   
@bot.command()
async def dance2(ctx):
   await ctx.message.delete()
   await ctx.send(" <a:dance2:775464800863649793>")   

@bot.command()
async def party(ctx):
   await ctx.message.delete()
   await ctx.send("<a:party:775459336091598879>")
   
   
@bot.command()
async def party2(ctx):
   await ctx.message.delete()
   await ctx.send("<a:party2:775466749961306172>")
   
   
   
@bot.command()
async def nom(ctx):
   await ctx.message.delete()
   await ctx.send("<a:nom:775464943411003403>")
   
   
@bot.command()
async def yis(ctx):
   await ctx.message.delete()
   await ctx.send("<a:yis:775466976679690251>")
@bot.command()
async def angwy(ctx):
   await ctx.message.delete()
   await ctx.send("<a:angwy:775467252144668703>")
 

@bot.command()
async def thonk(ctx):
   await ctx.message.delete()
   await ctx.send("<a:thonk:775468359545389121>")
 

 
@bot.command()
async def eatu(ctx):
   await ctx.message.delete()
   await ctx.send("<a:eatu:775469505077837885>")
 

@bot.command()
async def uhh(ctx):
   await ctx.message.delete()
   await ctx.send("<a:uhh:775469627870412800>")
 
 
@bot.command()
async def aaa(ctx):
   await ctx.message.delete()
   await ctx.send("<a:aaa:775469750406742087>")
 
 
  
@bot.command()
async def smort(ctx):
   await ctx.message.delete()
   await ctx.send("<a:smort:775469859449471037>")
 
 
  
@bot.command()
async def headbang(ctx):
   await ctx.message.delete()
   await ctx.send("<a:headbang:775470813872259132>")
   

@bot.command()
async def jump(ctx):
   await ctx.message.delete()
   await ctx.send("<a:jump:775608800744046612>")
   


@bot.command()
async def spinn(ctx):
   await ctx.message.delete()
   await ctx.send("<a:spinn:775608889856098314>")
   
   
@bot.command()
async def huhh(ctx):
   await ctx.message.delete()
   await ctx.send("<a:huhh:775609501981868034>")
   

@bot.command()
async def woww(ctx):
   await ctx.message.delete()
   await ctx.send("<a:woww:775610296277532673>")
   
   
@bot.command()
async def what(ctx):
   await ctx.message.delete()
   await ctx.send("<a:what:775611794093113356>")
   
   
    
@bot.command()
async def lol(ctx):
   await ctx.message.delete()
   await ctx.send("<a:lol:775611985362157608>")

@bot.command()
async def jump2(ctx):
   await ctx.message.delete()
   await ctx.send("<a:jump2:775613390033780736>")
   
@bot.command()
async def oki(ctx):
   await ctx.message.delete()
   await ctx.send("<a:oki:775613961977987072>")
   
@bot.command()
async def duckk(ctx):
   await ctx.message.delete()
   await ctx.send("<a:duckk:775753411895230475>")
   
@bot.command()
async def trigger(ctx):
   await ctx.message.delete()
   await ctx.send("<a:trigger:775759545494536212>")
   
@bot.command()
async def dogdance(ctx):
   await ctx.message.delete()
   await ctx.send("<a:dogdance:775759772770107424>")
   
@bot.command()
async def pepeclap(ctx):
   await ctx.message.delete()
   await ctx.send("<a:pepeclap:775759908238393364>")
   
   
@bot.command()
async def surprised(ctx):
   await ctx.message.delete()
   await ctx.send("<a:surprised:775760016212361256>")
   
   
@bot.command()
async def cya(ctx):
   await ctx.message.delete()
   await ctx.send("<a:cya:775760109413466152>")
   
  
      
   
@bot.command()
async def cya2(ctx):
   await ctx.message.delete()
   await ctx.send("<a:cya2:775760197909741638>")    
   
   
   
@bot.command()
async def ahye(ctx):
   await ctx.message.delete()
   await ctx.send("<a:ahye:775786972916482108>")  


@bot.command()
async def nono(ctx):
   await ctx.message.delete()
   await ctx.send("<a:nono:775832075021320192>")  

@bot.command()
async def wut(ctx):
   await ctx.message.delete()
   await ctx.send("<:wut:763632367038103572>")  
   

@bot.command()
async def hungy(ctx):
   await ctx.message.delete()
   await ctx.send("<a:hungy:775834827136041014>")  


@bot.command()
async def cry1(ctx):
   await ctx.message.delete()
   await ctx.send("<a:cry1:775835411058393159>")  



@bot.command()
async def cry2(ctx):
   await ctx.message.delete()
   await ctx.send("<a:cry2:775835857855709244>")  


@bot.command()
async def haha(ctx):
   await ctx.message.delete()
   await ctx.send("<a:haha:775836441719996436>")  


@bot.command()
async def lala(ctx):
   await ctx.message.delete()
   await ctx.send("<a:lala:775836593335697428>")  

@bot.command()
async def lala2(ctx):
   await ctx.message.delete()
   await ctx.send("<a:lala2:775836678702497844>")  


@bot.command()
async def uuu(ctx):
   await ctx.message.delete()
   await ctx.send("<a:uuu:775836761040355328>")  



@bot.command()
async def petpy(ctx):
  await ctx.message.delete()
  await ctx.send("<a:petpy:775950614303604746>")


#kick
@bot.command(aliases = ['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member, *,reason = "No Reason Provided. "):
  await member.kick(reason = reason)
  await ctx.channel.send("The User Has Been Kicked, Reason : "+reason)

#ban
@bot.command(aliases = ['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member, *,reason = "No Reason Provided. "):
  await member.ban(reason = reason)
  await ctx.channel.send("The User Has Been Banned, Reason : "+reason)




#RUN THE BOT 

bot.run("NzczNjI2ODgyODc2NTA2MTQy.X6L-Lg.ZvWrbQeZV0RsZL2zHodatfeSh0M")

