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
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
import logging
import repository.repository as repository

SET_NEW_ALERT, SAVE_NEW_ALERT = range(2)
SET_ALERT, SAVE_MODIFIED_ALERT = range(2)
SAVE_REMOVED_ALERT = 1

def add_alert(bot, update):
    
    reply_keyboard_markup = ReplyKeyboardMarkup([['CPU'], ['TEMP'], ['RAM'], ['DISK']], resize_keyboard=True, one_time_keyboard=True)

    bot.send_message(chat_id=update.message.chat_id, 
                     parse_mode="Markdown", 
                     text="Select what Alert do you want to add:",
                     reply_markup=reply_keyboard_markup)

    return SET_NEW_ALERT

def set_new_alert(bot, update, user_data):
    type_of_alert = update.message.text

    if type_of_alert == "CPU" and repository.get_dbc().get_cpu_alert(update.message.chat_id):
        update.message.reply_text('You already have a CPU alarm configured, use the command /modify_alert and then select "CPU" to modify it.')
        return ConversationHandler.END
    elif type_of_alert == "TEMP" and repository.get_dbc().get_temp_alert(update.message.chat_id):
        update.message.reply_text('You already have a TEMP alarm configured, use the command /modify_alert and then select "TEMP" to modify it.')
        return ConversationHandler.END
    elif type_of_alert == "RAM" and repository.get_dbc().get_ram_alert(update.message.chat_id):
        update.message.reply_text('You already have a RAM alarm configured, use the command /modify_alert and then select "RAM" to modify it.')
        return ConversationHandler.END
    elif type_of_alert == "DISK" and repository.get_dbc().get_disk_alert(update.message.chat_id):
        update.message.reply_text('You already have a DISK alarm configured, use the command /modify_alert and then select "DISK" to modify it.')
        return ConversationHandler.END
    else:
        update.message.reply_text("Enter an integer value (the desired Degrees in case of TEMP alarm, and percentage for the rest) to adjust the alarm:")
        user_data['type_of_alert'] = type_of_alert    
        return SAVE_NEW_ALERT       

def save_new_alert(bot, update, user_data):
    type_of_alert = user_data['type_of_alert']

    if type_of_alert == "CPU":
        repository.get_dbc().set_cpu_alert(update.message.chat_id, update.message.text)
    if type_of_alert == "TEMP":
        repository.get_dbc().set_temp_alert(update.message.chat_id, update.message.text)
    if type_of_alert == "RAM":
        repository.get_dbc().set_ram_alert(update.message.chat_id, update.message.text)
    if type_of_alert == "DISK":
        repository.get_dbc().set_disk_alert(update.message.chat_id, update.message.text)

    update.message.reply_text('Your alarm has been configured successfully!')

    return ConversationHandler.END

def modify_alert(bot, update):

    reply_keyboard_markup = ReplyKeyboardMarkup([['CPU'], ['TEMP'], ['RAM'], ['DISK']], resize_keyboard=True, one_time_keyboard=True)

    bot.send_message(chat_id=update.message.chat_id, 
                     parse_mode="Markdown", 
                     text="Select what Alert do you want to modify:",
                     reply_markup=reply_keyboard_markup)

    return SET_ALERT

def set_alert(bot, update, user_data):
    type_of_alert = update.message.text

    if type_of_alert == "CPU" and repository.get_dbc().get_cpu_alert(update.message.chat_id) == None:
        update.message.reply_text('You  haven\'t yet a CPU alarm configured, use the command /add_alert and then select "CPU" to create it.')
        return ConversationHandler.END
    elif type_of_alert == "TEMP" and repository.get_dbc().get_temp_alert(update.message.chat_id) == None:
        update.message.reply_text('You  haven\'t yet a TEMP alarm configured, use the command /add_alert and then select "CPU" to create it.')
        return ConversationHandler.END
    elif type_of_alert == "RAM" and repository.get_dbc().get_ram_alert(update.message.chat_id) == None:
        update.message.reply_text('You  haven\'t yet a RAM alarm configured, use the command /add_alert and then select "CPU" to create it.')
        return ConversationHandler.END
    elif type_of_alert == "DISK" and repository.get_dbc().get_disk_alert(update.message.chat_id) == None:
        update.message.reply_text('You  haven\'t yet a DISK alarm configured, use the command /add_alert and then select "CPU" to create it.')
        return ConversationHandler.END
    else:
        update.message.reply_text("Enter an integer value (the desired Degrees in case of TEMP alarm, and percentage for the rest) to adjust the alarm:")
        user_data['type_of_alert'] = type_of_alert    
        return SAVE_MODIFIED_ALERT    

def save_modified_alert(bot, update, user_data):
    type_of_alert = user_data['type_of_alert']

    if type_of_alert == "CPU":
        repository.get_dbc().set_cpu_alert(update.message.chat_id, update.message.text)
    if type_of_alert == "TEMP":
        repository.get_dbc().set_temp_alert(update.message.chat_id, update.message.text)
    if type_of_alert == "RAM":
        repository.get_dbc().set_ram_alert(update.message.chat_id, update.message.text)
    if type_of_alert == "DISK":
        repository.get_dbc().set_disk_alert(update.message.chat_id, update.message.text)

    update.message.reply_text('Your alarm has been modified successfully!')

def remove_alert(bot, update):
    reply_keyboard_markup = ReplyKeyboardMarkup([['CPU'], ['TEMP'], ['RAM'], ['DISK']], resize_keyboard=True, one_time_keyboard=True)

    bot.send_message(chat_id=update.message.chat_id, 
                     parse_mode="Markdown", 
                     text="Select what Alert do you want to remove:",
                     reply_markup=reply_keyboard_markup)

    return SAVE_REMOVED_ALERT

def save_removed_alert(bot, update):
    None
