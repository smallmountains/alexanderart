# -*- coding: utf-8 -*-
#------------------------------------------------------------
# (c) 2017 - Smallmountains
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.alexanderart'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID = "AAlexanderArt"

# Entry point
def run():
    plugintools.log("alexanderart.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("alexanderart.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="William Alexander - The Happy Painter",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        folder=True )

run()
