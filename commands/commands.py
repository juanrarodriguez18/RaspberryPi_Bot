# Copyright 2018 by RaspberryPi Bot contributors. All rights reserved.
#
# This file is part of RaspberryPi Bot.
#
#     RaspberryPi Bot is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     RaspberryPi Bot is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with RaspberryPi Bot.  If not, see <http:#www.gnu.org/licenses/>.
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler
import logging
from repository.repository import get_dbc
import services.raspberryPiService as raspberryPiService
from config.loadConfig import get_config

PASSWORD = 1

def reboot(bot, update):
    if get_dbc().get_user_authenticated(update.message.chat_id):
        update.message.reply_text("Your Raspberry Pi will be rebooted now.")
        raspberryPiService.restart()
    else:
        update.message.reply_text("You haven't putted your password yet. Use the command /password to confirm it.")

def shutdown(bot, update):
    if get_dbc().get_user_authenticated(update.message.chat_id):
        update.message.reply_text("Your Raspberry Pi will be shut down now.")
        raspberryPiService.shutdown()
    else:
        update.message.reply_text("You haven't putted your password yet. Use the command /password to confirm it.")

def password(bot, update):
    update.message.reply_text("Send me the password that you put at the config file:")

    return PASSWORD

def verify_password(bot, update):
    password = update.message.text

    if(get_config().password_raspberryPi == password):
        update.message.reply_text("Your user has been successfully verified!")  
        get_dbc().set_user_authenticated(update.message.chat_id)
        return ConversationHandler.END 
    else:
        update.message.reply_text("Wrong password! Try again:")  
        return PASSWORD

def cancel(bot, update):
    user = update.message.from_user
    logging.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Operation cancelled.')

    return ConversationHandler.END