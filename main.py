from utils.logging import logger
from alexa import Alexa
from tuya import Switch
import datetime, time

INTERVAL_MINUTES=2

class Runner:
    _switch=None
    _alexa=None
    _last_run=0
    _last_status=None
    _runtime=0
    def __init__(self) -> None:
        self._alexa=Alexa()
        self._switch=Switch()
    
    def run(self):
        while True:
            logger.info("Checking....")
            switch_status=self._switch.is_on()
            if switch_status:
                self._alexa.announce(f'Pump is running for greater than {self._runtime} minutes')
                self._runtime+=INTERVAL_MINUTES
            else:
                self._runtime=0
                if self._last_status:
                    self._alexa.announce(f'Pump is switched off. Closed.')
            self._last_status=switch_status
            self._last_run=datetime.datetime.now()
            time.sleep(INTERVAL_MINUTES*60)
            logger.info("Check Completed")

while True:
    try:
        runner=Runner()
        runner.run()
    except Exception as e:
        logger.exception('Something went wrong...Sleeping for 2 minutes')
        time.sleep(120)