import json
import os

from telethon import TelegramClient


class Bot:

    def __init__(self):
        self.client = TelegramClient
        self.api_id = None
        self.api_hash = None
        self.get_config()

    def get_config(self):
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file = os.path.join(parent_dir, 'config.json')
        with open(config_file, 'r') as f:
            config = json.load(f)
            self.api_id = config['api_id']
            self.api_hash = config['api_hash']
