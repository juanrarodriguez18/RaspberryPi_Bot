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
import locale
import services.raspberryPiService as raspberryPiService

def info_resumed(bot, update):
    info_resumed_string = ("This is your Pi's resumed info: \n"+
                            "\n - *CPU*: "+str(raspberryPiService.get_cpu_percentage())+" %"+
                            "\n - *TEMP*: "+str(raspberryPiService.get_temp_info())+" ºC"+
                            "\n - *RAM*: "+str(raspberryPiService.get_ram_info().percent)+" %"+
                            "\n - *DISK*: "+str(raspberryPiService.get_disk_info().percent)+" %")

    msg_send = bot.send_message(chat_id=update.message.chat_id, parse_mode="Markdown", text=info_resumed_string)

    return msg_send is not None

def info_cpu(bot, update):
    info_cpu_string = ("This is your Pi's cpu info: \n"+
                       "\n - *CPU*: "+str(raspberryPiService.get_cpu_percentage())+" %")
    
    i = 0
    for percentage in raspberryPiService.get_cpu_info():
        info_cpu_string += "\n - *CPU"+str(i)+"*: "+str(percentage)+" %"
        i += 1

    msg_send = bot.send_message(chat_id=update.message.chat_id, parse_mode="Markdown", text=info_cpu_string)

    return msg_send is not None

def info_temp(bot, update):
    temp = raspberryPiService.get_temp_info()
    info_temp_string = "This is your Pi's temperature: "+str(temp)+" ºC "

    if temp < 40:
        info_temp_string += '⬇️'
    elif temp >= 40 and temp < 85:
        info_temp_string += '✅'
    else:
        info_temp_string += '‼️'
    
    msg_send = bot.send_message(chat_id=update.message.chat_id, parse_mode="Markdown", text=info_temp_string)

    return msg_send is not None
    
def info_ram(bot, update):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    info_ram_string = ("This is your Pi's RAM info: \n"+
                            "\n - *PERCENTAGE*: "+str(raspberryPiService.get_ram_info().percent)+" %"+
                            "\n - *TOTAL*: "+locale.format('%d', raspberryPiService.get_ram_info().total/1024, True)+" MB"+
                            "\n - *AVAILABLE*: "+locale.format('%d', raspberryPiService.get_ram_info().available/1024, True)+" MB"+
                            "\n - *USED*: "+locale.format('%d', raspberryPiService.get_ram_info().used/1024, True)+" MB"+
                            "\n - *FREE*: "+locale.format('%d', raspberryPiService.get_ram_info().free/1024, True)+" MB")

    msg_send = bot.send_message(chat_id=update.message.chat_id, parse_mode="Markdown", text=info_ram_string)

    return msg_send is not None

def info_disk(bot, update):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    info_disk_string = ("This is your Pi's DISK info: \n"+
                            "\n - *PERCENTAGE*: "+str(raspberryPiService.get_disk_info().percent)+" %"+
                            "\n - *TOTAL*: "+locale.format('%d', raspberryPiService.get_disk_info().total/1024, True)+" MB"+
                            "\n - *USED*: "+locale.format('%d', raspberryPiService.get_disk_info().used/1024, True)+" MB"+
                            "\n - *FREE*: "+locale.format('%d', raspberryPiService.get_disk_info().free/1024, True)+" MB")

    msg_send = bot.send_message(chat_id=update.message.chat_id, parse_mode="Markdown", text=info_disk_string)

    return msg_send is not None