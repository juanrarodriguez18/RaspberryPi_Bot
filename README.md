# RaspberryPi_Bot

Telegram's Bot that shows and alerts you from the state of your Rasbpberry Pi.

## Basic Configuration

These are the basic parameters of the bot's configuration:

- **TOKEN**: The bot's token, [@BotFather](https://telegram.me/BotFather) can show us when we ask it for the Token of the created bot.
- **PATH**: The path were the bot will save the Database used for the data of the bot.
- **DEFAULT_REFRESH_TIME**: The refresh time of the alerts.
- **LOG_LEVEL**: Log Level to save in the Log file.
- **LOG_PATH**: Path were the Log file will be saved.

It exists two examples where we can save that commands, the first is `my_config/config_example.ini`, this configuration is used when we execute the bot directly from Python. On the other hand, if we execute the bot from Docker, we have the `.example.env` file.

## Running the Bot

We can launch the bot in two differents ways:

- [Python](./README.md#python) (v3)
- [Docker](./README.md#docker)

## Python

In order to launch the bot from Python, we will use the next commands:

```bat
pip install -r requirements.txt
python raspberryPi_bot.py --config_path my-config/my_config.ini
```

The parth `my-config/my_config.ini` will be the path that we have configurated ath the configuration's file, the showed path is the path that it is recommend.

## Docker

[In progress]

## Bot Commands

- **start** - Start the Bot and the configurated alerts
- **info_resumed** - Show the resumed Raspberry info
- **info_cpu** - Show the detailed info of the cpu
- **info_temp** - Show the detailed info of the Temperature
- **info_ram**- Show the detailed info of the Ram
- **info_disk** - Show the detailed info of the Disk
- **reboot** - Reboot the Raspberry
- **shutdown** - Shutdown the Raspberry
- **password** - Verify the password (needed to execute the commands of reboot and shutdown)
- **add_alert** - Create a new Alert
- **modify_alert** - Modify the value of one existing Alert
- **remove_alert** - Remove on existing Alert
- **help** - Show the Help info