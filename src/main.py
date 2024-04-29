import asyncio

from changer.bot import Bot


async def main():
    """
    Main function
    :return:
    """
    bot = Bot()
    bio = 'Changed test bio'
    await bot.setBio(bio)


if __name__ == '__main__':
    asyncio.run(main())
