#Cliquet botten
'''
#note this bot may no longer work

Features:
help: shows command instructions
gme: show current price of GME stock and volume (also if its aftermarket or not)
price[stocktag]: show same as the above but for another stock
profit[stocktag][buyprice]: calculate profit since bought stock
starttrack[stockname]: starts to track [stockname] price/volume and write it every hour during market
stopttrack[stockname]: stops the tracking
mrbobogetstatus: show if the website is online

'''
# pycharm env syntax os.environ['SOME_VAR']

import os
import discord
import requests
import math
from discord.ext import commands
from dotenv import load_dotenv
from yahoo_fin import stock_info as si


load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
SERVER = os.environ['DISCORD_SERVER']


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')  # Show if it connected



@bot.command(name = 'cringe', help = 'use this command if you detected cringe')
async def on_message(message):

        response = 'CRINGE DETECTED INITIATING CONTAMINATION PROCEDURES :Amogus:' #cringe test
        await message.channel.send(response)


@bot.command(name = 'mrboboget',help='check the status of https://mrboboget.se/')
async def on_message(message):
    try:
        response = requests.get('https://mrboboget.se/',verify = False)
    except Exception as e:
        await message.channel.send(f"NOT OK: {str(e)}")
    else:
        if response.status_code == 200:
            await message.channel.send("mrboboget är och betar på hagen!")
        else:
            await message.channel.send(f"NOT OK: HTTP response code {response.status_code}")


@bot.command(name='price',help='tells the price and volume of the stock')
async def stock(ctx, stocktag):
    price = si.get_live_price(stocktag)
    marketStatus = si.get_market_status()
    roundedPrice = round(price,2)

    response = (f" @{ctx.author.name},{stocktag} **Price**: *{roundedPrice}*, **maket**: *{marketStatus}*")
    await ctx.channel.send(response)

@bot.command(name='profit',help='calculate the profit, <stockname>, <buying price>, <amount of stocks>')
async def stock(ctx, stock, buyingprice: int, amount: int):
    stocktag = stock.capitalize()
    price = si.get_live_price(stocktag)
    profitval = (price/buyingprice - 1 ) * buyingprice * amount
    roundedPrice = round(price,2)

    response = (f" {ctx.author.name}: {stocktag} current price: {roundedPrice}, buying price: {buyingprice}\n"
                f"profit:{profitval}")
    await ctx.channel.send(response)

@bot.command(name='navyseal', help = 'use with care')
async def navy(ctx, target):
    if target == None:
        copypasta = f' What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US Armed Forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak, I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo. '
        await ctx.channel.send(copypasta)
    else:
        copypasta = f'@{target}! What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US Armed Forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak, I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo. '
        await ctx.channel.send(copypasta)

@bot.command(name='Eldenring',help='HYYPPEEEEEE!!!!')
async def hype(ctx):
    await ctx.channel.send("ELDENRINGGGGGG\n"
                           "______---___🔥🔥🔥🔥__________\n"
                           "----🔥------------🔥-------\n"
                           "--🔥----------------🔥-----\n"
                           "--🔥----------------🔥-----\n"
                           "--🔥----------------🔥-----\n"
                           "---🔥--------------🔥------\n"
                           "------🔥🔥🔥🔥---------\n"
                           "OOOOOOOOOOOOOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Walla lär dig skriva bror, om du glömt skriv \"!help\" ")

bot.run(TOKEN)


