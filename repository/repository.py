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

    def get_table(self, table_name):
        return self.db.table(table_name)

    def purge(self):
        self.db.purge_tables()
