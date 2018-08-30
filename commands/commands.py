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
import logging
import repository.repository as repository
from services.raspberryPiService import restart, shutdown

def reboot(bot, update):
    if get_dbc().get_user_authenticated(update.message.chat_id):
        update.message.reply_text("Your Raspberry Pi will be rebooted now.")
        restart()
    else:
        update.message.reply_text("You haven't putted your password yet. Use the command /password to confirm it.")


def shutdown(bot, update):
    if get_dbc().get_user_authenticated(update.message.chat_id):
        update.message.reply_text("Your Raspberry Pi will be shut down now.")
        shutdown()
    else:
        update.message.reply_text("You haven't putted your password yet. Use the command /password to confirm it.")

def password(bot, update):
    None