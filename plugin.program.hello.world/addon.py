import xbmc
import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon(id='plugin.video.helloworld')
addonname   = addon.getAddonInfo('name')
icon        = addon.getAddonInfo('icon')

title = "Hello World"
text = "This is some text"
time = 5000  # ms

xbmcgui.Dialog().ok(addonname, title, text, time) 
