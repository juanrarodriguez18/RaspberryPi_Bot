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
import os
from tinydb import TinyDB, Query, where
from tinydb.operations import add


db = None


def get_dbc():
    return db


def set_dbc(dbc):
    global db
    db = dbc


class DBC:
    def __init__(self, path=None):
        if path is None:
            self.db = TinyDB(os.path.join('my-config', 'raspberryPi-db.json'))
        else:
            self.db = TinyDB(path)
        self.db.table('UserConfiguration')

    def get_table(self, table_name):
        return self.db.table(table_name)

    def purge(self):
        self.db.purge_tables()

    def insert_user_configuration(self, user_id):
            result = False
            if len(self.db.table('UserConfiguration').search(where('user_id') == user_id)) == 0:
                self.db.table('UserConfiguration').insert({'user_id': user_id, 'cpu_alert': None, 'temp_alert': None, 'ram_alert': None, 'disk_alert': None, 'auth': False})
                result = True

            return result

    def get_cpu_alert(self, user_id):
        return self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['cpu_alert']

    def get_temp_alert(self, user_id):
        return self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['temp_alert']
    
    def get_ram_alert(self, user_id):
        return self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['ram_alert']

    def get_disk_alert(self, user_id):
        return self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['disk_alert']

    def get_user_authenticated(self, user_id):
        return self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['auth']

    def set_cpu_alert(self, user_id, percentage):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'cpu_alert': percentage},
                             query.user_id == user_id)

    def set_temp_alert(self, user_id, degrees):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'temp_alert': degrees},
                             query.user_id == user_id)
    
    def set_ram_alert(self, user_id, percentage):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'ram_alert': percentage},
                             query.user_id == user_id)

    def set_disk_alert(self, user_id, percentage):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'disk_alert': percentage},
                             query.user_id == user_id)

    def set_user_authenticated(self, user_id):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'auth': True},
                             query.user_id == user_id)