import logging as log
from datetime import datetime


def actualData():
    actualData = datetime.now().strftime(r"%d-%m-%Y - %H_%M_%S")
    return actualData


log.basicConfig(level=log.DEBUG, filename=f'{actualData()}.log', filemode='w',
                format="%(asctime)s - %(levelname)s - %(message)s")

x = 2

log.debug('teste')
log.info(f'the value of x is {x}')
log.warning('teste')
log.error('teste')
log.critical('teste')

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("ZeroDivisionError", exc_info=True)
    log.info("------------------------------")
    # Same thing
    log.exception("ZeroDivisionError")

# another way
logger = log.getLogger(__name__)

handler = log.FileHandler('test.log')
formatter = log.Formatter('%(asctime)s - %(name)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("test the custom logger")
