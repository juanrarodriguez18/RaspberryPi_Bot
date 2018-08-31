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
import time
from repository.repository import DBC, get_dbc


def start(bot, update):
    # print(update.message.chat_id)
    is_inserted = get_dbc().insert_user_configuration(update.message.chat_id)

    if is_inserted:
        update.message.reply_text("User configured! Use the command /password to put the same password "+
        "that you had put at the config file. \n\nWhen you enter the password, your user "+
        "will be verified and you will be able to use the commands.")
    else:
        update.message.reply_text("You user already exists! Remember, use the command /password to put the same password "+
        "that you had put at the config file. \n\nWhen you enter the password, your user "+
        "will be verified and you will be able to use the commands.")

def help(bot, update):
    update.message.reply_text("Help")

def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))



