####--------------------------------####
#--# Author:   by Umbrellla777      #--#
#--# Telegram: @Umbrellla777        #--#
#--# VK:       @Umbrellla777        #--#
####--------------------------------####

###########################
## Импорт библиотек
###########################
import sys
import asyncio
import time
import random


from asyncio import sleep
from collections import deque
from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon import events

##from telethon                       import functions, types
##from telethon.tl.types              import ChatBannedRights
##from telethon.tl.functions.users    import GetFullUserRequest
##from telethon.tl.functions.channels import EditBannedRequest


###########################
## Цвет консоли
###########################
red = [206, 76, 54]
green = [68, 250, 123]
blue = [253, 127, 233]
yellow = [241, 250, 118]
orange = [255, 184, 107]


def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text)


###########################
## Настройки
###########################
api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])

## Connect
client = TelegramClient('users/current_user', api_id, api_hash)
client.start()

###########################
## Импорт папок|добавить
###########################

###########################
## Информация о аккаунте
###########################
entity = client.get_entity("me")
MY_ID = entity.id
print(
    "["
    + colored(green, "PROFILE: ")
    + str(entity.first_name)
    + " | " + colored(orange, "Id: ") + str(MY_ID)
    + " | " + colored(orange, "Uname: ") + "@" + str(entity.username)
    + "]"
)

###########################
## Проверка бота
###########################
@client.on(events.NewMessage(pattern='.ping'))
async def pong(event):
    message = event.message
    await message.edit("pong")
###########################
###########################
@client.on(events.NewMessage(chats="@testbotgitumb"))  # Замените "@ваш_канал" на имя вашего канала
async def handle_message(event):
    message_text = event.message.text.lower()
    pattern = r"@umbrellla777"
    match = re.search(pattern, message_text)

    if match:
        target_chat_id = "@chaksads"
        await client.send_message(target_chat_id, "Привет, я выйграл!")

client.run_until_disconnected()
