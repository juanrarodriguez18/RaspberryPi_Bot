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

import logging
import schedule
import psutil
import os

def get_cpu_info():
    return psutil.cpu_percent(interval=1, percpu=True)

def get_temp_info():
    result = 0
    try:
        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(tFile.read())
        result = temp/1000
        tFile.close()
    except:
        tFile.close()

    return result

def get_mem_info():
    return psutil.virtual_memory()

def get_hdd_info():
    return psutil.disk_usage('/')

def shutdown():
    os.system("sudo shutdown -h now")

def restart():
    os.system("sudo restart now")

def check_raspberryPi():
    None

def schedule_raspberryPi(time_seconds):
    # print(time_seconds)
    schedule.every(time_seconds).seconds.do(check_raspberryPi)
    
print(psutil.disk_usage('/'))