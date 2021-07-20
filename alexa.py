import requests,json
class Alexa:
    _base_url='https://api.voicemonkey.io/trigger'
    _data=None
    def __init__(self) -> None:
        with open('config/alexa.json') as config:
            self._data = json.load(config)
    def announce(self,text):
        self._data['announcement']=text
        try:
            response = requests.get(self._base_url,params=self._data)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')