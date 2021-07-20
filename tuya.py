from tuyaha import TuyaApi
from utils.logging import logger
import json
class Switch:
    _device=None
    _api=TuyaApi()
    def __init__(self) -> None:
        with open('config/tuya.json') as config:
            data = json.load(config)
            
        username,password,country_code,application = data['username'],data['password'],data['country_code'],data['application']
        self._api.init(username,password,country_code,application)
        device_ids = self._api.get_all_devices()
        self._device=device_ids[0]
    def turn_off(self):
        self._device.turn_off()
    def turn_on(self):
        self._device.turn_on()
    def is_on(self):
        self._device._update(False)
        state = self._device.data.get('state')
        online= self._device.data.get('online')
        return state and online