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
from commands.commands import reboot, shutdown, password, verify_password, cancel

def load_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

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
