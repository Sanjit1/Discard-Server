from http import server
import os
from discord.ext import commands
from flask import Flask
from threading import Thread

bot = commands.Bot(command_prefix="d!")

@bot.event
async def on_connect():
  print("Here")

app = Flask('')

@app.route('/')
def home():
    return "servers up"

def run():
    app.run(host='0.0.0.0', port=8080)

serverThread = Thread(target=run)
serverThread.start()

# Bot token
token = os.environ.get("token")
bot.run(token)
