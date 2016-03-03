# Computer Science House
# Control client for the Amazon Echo
# Author: Steven Mirabito (smirabito@csh.rit.edu)

import control_key
import requests


class AlexaSpokenError:
    def __init__(self, error=""):
        self.error = error


class ControlAPI:
    def __init__(self, api_key=None, endpoint="http://control.csh.rit.edu:8080/"):
        self.api_key = "" if not api_key else api_key
        self.endpoint = endpoint
        self.messages = {
            "help": "You can say, turn on or off the lights, turn on or off the radiator, or set the volume to a value between zero and eighty.",
            "no_api_key": "I'm sorry Dave, I'm afraid I can't do that.",
            "server_error": "Sorry, I can't connect to the server right now. Please try again later.",
            "lights_off": "OK, I turned the lights off for you.",
            "lights_on": "OK, I turned the lights on for you.",
            "radiator_off": "OK, I turned the radiator off for you.",
            "radiator_on": "OK, I turned the radiator on for you.",
            "volume_invalid": "Sorry, the volume level I heard was not between one and eighty. Please try again.",
            "volume_changed": "OK, I changed the volume to {} for you.",
            "muted": "OK, I muted the audio for you."
        }

    def get(self, route):
        request = requests.get(self.endpoint + route)
        if request.status_code == 200:
            return request.json()
        else:
            return AlexaSpokenError(self.messages["server_error"])

    def put(self, route, key, value_dict):
        if not self.api_key:
            return False
        else:
            data = {
                "token": {
                    "id": self.api_key
                },
                key: value_dict
            }
            request = requests.put(self.endpoint + route, json=data)

            return request.status_code == 200

    def get_lights(self):
        request = self.get("lounge/lights")
        if isinstance(request, AlexaSpokenError):
            return request.error
        else:
            return request["lights"]

    def set_lights(self, toggle, lights_state):
        request = self.put("lounge/lights", "lights", lights_state)
        if request:
            if toggle:
                return self.messages["lights_on"]
            else:
                return self.messages["lights_off"]
        else:
            return self.messages["server_error"]

    def toggle_radiator(self, toggle):
        if toggle:
            state = {
                "fan": True
            }
        else:
            state = {
                "fan": False
            }

        if self.put("lounge/radiator", "radiator", state):
            if toggle:
                return self.messages["radiator_on"]
            else:
                return self.messages["radiator_off"]
        else:
            return self.messages["server_error"]

    def change_volume(self, level):
        state = {
            "level": int(1.27 * level)
        }

        if self.put("lounge/receiver/volume", "volume", state):
            return self.messages["volume_changed"].format(level)
        else:
            return self.messages["server_error"]

    def mute(self):
        state = {
            "state": True
        }

        if self.put("lounge/receiver/mute", "mute", state):
            return self.messages["muted"]
        else:
            return self.messages["server_error"]


class ControlAlexa:
    def __init__(self, api_key=None, endpoint=None, api=None):
        if api:
            # Use the passed ControlAPI object instead of instantiating a new one
            if isinstance(api, ControlAPI):
                self.api = api
            else:
                raise TypeError("API must be a ControlAPI object")
        else:
            # Instantiate a ControlAPI object
            if not endpoint:
                self.api = ControlAPI(api_key)
            else:
                self.api = ControlAPI(api_key, endpoint)

    def help(self):
        return self.api.messages["help"]

    def get_lights(self):
        # Not implemented
        return self.api.messages["no_api_key"]

    def toggle_lights(self, toggle=None):
        if toggle == "on":
            toggle = True
            lights_state = {
                "L1": True,
                "L2": True
            }
        else:
            toggle = False
            lights_state = {
                "L1": False,
                "L2": False
            }

        return self.api.set_lights(toggle, lights_state), True

    def toggle_radiator(self, toggle=None):
        toggle = True if toggle == "on" else False
        return self.api.toggle_radiator(toggle), True

    def change_volume(self, level=None):
        if not level or int(level) < 0 or int(level) > 80:
            return self.api.messages["volume_invalid"], True
        else:
            return self.api.change_volume(int(level)), True

    def mute(self):
        return self.api.mute(), True


if __name__ == "__main__":
    control = ControlAlexa(api_key=control_key.api_key)
    control.toggle_lights(True)
