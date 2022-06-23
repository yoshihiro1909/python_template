

import datetime
import logging
from rich.logging import RichHandler

def setup_logger():
    logger = logging.getLogger(__name__)  
    logger.setLevel(logging.DEBUG)  

    handler1 = logging.StreamHandler()
    fmt = "%(asctime)s %(name)s [%(levelname)s] %(message)s"
    handler1.setFormatter(logging.Formatter(fmt))

    today_datetime = datetime.datetime.today()
    today_iso_datetime = datetime.datetime.isoformat(today_datetime)
    handler2 = logging.FileHandler(filename=f"log/{today_iso_datetime}.log")  # handler2はファイル出力
    handler2.setLevel(logging.DEBUG)  
    handler2.setFormatter(logging.Formatter(fmt))

    # logger.addHandler(handler1)
    logger.addHandler(RichHandler(rich_tracebacks=True))
    logger.addHandler(handler2)

    return logger


if __name__ == '__main__':
    logger = setup_logger()
    logger.debug('setup logger')
