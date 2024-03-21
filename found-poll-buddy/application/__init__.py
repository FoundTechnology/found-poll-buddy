from .. import data
from .mention import Mention  # noqa: F401
from .option import Option  # noqa: F401
from .poll import Poll  # noqa: F401


async def init():
    await data.init()
