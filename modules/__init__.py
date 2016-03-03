__author__ = 'ahanes'

# import modules.skill as sk
# import modules.error as err_handle
# import modules.webnews as webnews
# import modules.drink as drink
import modules.control as control
import modules.control_key as control_key
import actions

# actions.actions['UserSearch'] = sk.skillcheck
# actions.actions['Error'] = err_handle.error
# actions.actions['WebNews'] = webnews.check_webnews
# actions.actions['DropDrink'] = drink.main

control_client = control.ControlAlexa(api_key=control_key.api_key)
actions.actions["Help"] = control_client.help
actions.actions["ToggleLights"] = control_client.toggle_lights
actions.actions["ToggleRadiator"] = control_client.toggle_radiator
actions.actions["ChangeVolume"] = control_client.change_volume
actions.actions["Mute"] = control_client.mute
