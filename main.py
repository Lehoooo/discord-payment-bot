import time
import discord
from discord.ext import commands
from discord.ext import tasks
import requests

# ltcaddy = open("ltcaddy.txt", "r")
# btcaddy = open("btcaddy.txt", "r")
# bchaddy = open("bchaddy.txt", "r")

TOKEN = open("token.txt", "r").read()  # loads the token file
bot = commands.Bot(command_prefix='>')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="crypto payment bot"))
    print("Ready")

@bot.command()
async def pay(ctx, arg, arg2, arg3="MJn6s9ZaESkdj4avjYVDETzqjnFiQXoTjj"): # arg = crypto, arg2 = amount, arg3 = where to send after confirmation
    await ctx.send("Generating Payment Address. Please Wait.", delete_after=2)
    argcap = arg.upper()

    if argcap == "LTC":
        data = {
            'type': '0',
            'destination': 'MJn6s9ZaESkdj4avjYVDETzqjnFiQXoTjj',
            'amount': str(arg2),
            'callback': 'https://webhook.site/c6b2e3e0-d0b2-44a3-9e1e-22261648bae6'
        }

        walletapi = requests.post("https://api.payrobot.io/ltc/payments", data=data).json()
        print("New Litecoin Payment Requested: - Address: " + walletapi["address"] + " - PaymentID: " + walletapi["paymentId"] + " - Amount: " + walletapi["amount"] + " - FeeAmount: " + walletapi["feeAmount"] + " - FinalAmount: " + walletapi["finalAmount"] + " - Destination: " + walletapi["destination"] + " - Pin: " + walletapi["pin"])
        print(walletapi)

        embed = discord.Embed()
        embed.add_field(name="Currency", value="Litecoin - LTC", inline=False)
        embed.add_field(name="Address", value=walletapi["address"], inline=False)
        embed.add_field(name="Payment ID", value=walletapi["paymentId"], inline=False)
        embed.add_field(name="Amount To Pay", value=walletapi["amount"], inline=False)
        await ctx.send(embed=embed)



    elif argcap == "BTC":
        await ctx.send("btc")

    elif argcap == "BCH":
        await ctx.send("bch")

    else:
        await ctx.send("unsupported")



bot.run(TOKEN)
