import asyncio
import logging
import os

from dotenv import load_dotenv

from . import application
from .logger import setup_logger
from .presentation.paul import Paul

load_dotenv()
setup_logger()

token = os.environ["BOT_TOKEN"]
logger = logging.getLogger("found-poll-buddy.main")


async def main():
    logger.info("starting found-poll-buddy ...")

    # Connect to the database
    await application.init()

    # empty space effectively disables prefix since discord strips trailing spaces
    bot = Paul()

    # Run Discord bot
    await bot.start(token)


def _main():
    asyncio.run(main())


if __name__ == "__main__":
    _main()
