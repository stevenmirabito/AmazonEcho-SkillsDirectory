__author__ = 'ahanes'

import modules.skill as sk
import modules.error as err_handle
import modules.webnews as webnews
import actions

actions.actions['UserSearch'] = sk.skillcheck
actions.actions['Error'] = err_handle.error
actions.actions['WebNews'] = webnews.check_webnews


