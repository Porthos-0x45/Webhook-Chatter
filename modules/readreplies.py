import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import json

with open('./config.json') as f:
    config = json.load(f)
    
token = config.get('bot_token')
