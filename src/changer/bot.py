"""
This module will change users bio
"""

import json
import logging
import os

from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Bot:
    """
    Main class for the bot
    """

    def __init__(self) -> None:
        """
        Initialize the bot
        """
        self.client: TelegramClient = None
        self.api_id: int = None
        self.api_hash: str = None
        self.get_config()

        logger.info('Config loaded\nApi id: %s\nApi hash: %s', self.api_id, self.api_hash)

        self.max_retries = 5  # Maximum number of retries
        self.base_delay = 1  # Base delay in seconds

    def get_config(self) -> None:
        """
        Get the config from the config file
        :return:
        """
        parent_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file: str = os.path.join(parent_dir, 'config.json')
        with open(config_file, 'r', encoding="utf-8") as f:
            config = json.load(f)
            self.api_id = config['api_id']
            self.api_hash = config['api_hash']

    async def setBio(self, bio):
        async with TelegramClient('anon', self.api_id, self.api_hash) as client:
            await client.start()
            await client(UpdateProfileRequest(about=bio))
            logger.info('Bio changed to %s', bio)
