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
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, \
    RegexHandler, Filters
from commands.generic import start, help, error
from commands.information import info_resumed, info_cpu, info_temp, info_ram, info_disk
from commands.commands import reboot, shutdown, password, verify_password, cancel
from commands.alerts import add_alert, set_new_alert, save_new_alert, modify_alert, set_alert, \
    save_modified_alert, remove_alert, save_removed_alert

def load_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

    # INFO
    dispatcher.add_handler(CommandHandler('info_resumed', info_resumed))
    dispatcher.add_handler(CommandHandler('info_cpu', info_cpu))
    dispatcher.add_handler(CommandHandler('info_temp', info_temp))
    dispatcher.add_handler(CommandHandler('info_ram', info_ram))
    dispatcher.add_handler(CommandHandler('info_disk', info_disk))

    # COMMANDS
    dispatcher.add_handler(CommandHandler('reboot', reboot))
    dispatcher.add_handler(CommandHandler('shutdown', shutdown))
    
    # VERIFY PASSWORD
    PASSWORD = 1
    conv_verify_password = ConversationHandler(
        entry_points=[CommandHandler('password', password)],
        states={
            PASSWORD: [MessageHandler(Filters.text, verify_password)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_verify_password)
    dispatcher.add_error_handler(error)

    # ADD ALERT
    SET_NEW_ALERT, SAVE_NEW_ALERT = range(2)
    conv_add_alert = ConversationHandler(
        entry_points=[CommandHandler('add_alert', add_alert)],
        states={
            SET_NEW_ALERT: [MessageHandler(Filters.text, set_new_alert, pass_user_data=True)],
            SAVE_NEW_ALERT: [RegexHandler(r'^\d+$', save_new_alert, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_add_alert)
    dispatcher.add_error_handler(error)

    # MODIFY ALERT
    SET_ALERT, SAVE_MODIFIED_ALERT = range(2)
    conv_modify_alert = ConversationHandler(
        entry_points=[CommandHandler('modify_alert', modify_alert)],
        states={
            SET_ALERT: [MessageHandler(Filters.text, set_alert, pass_user_data=True)],
            SAVE_MODIFIED_ALERT: [RegexHandler(r'^\d+$', save_modified_alert, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_modify_alert)
    dispatcher.add_error_handler(error)

    # REMOVE ALERT
    SAVE_REMOVED_ALERT = 1
    conv_remove_alert = ConversationHandler(
        entry_points=[CommandHandler('remove_alert', remove_alert)],
        states={
            SAVE_REMOVED_ALERT: [MessageHandler(Filters.text, save_removed_alert)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_remove_alert)
    dispatcher.add_error_handler(error)
