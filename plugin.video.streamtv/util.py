import xbmc xbmcgui, xbmcaddon
	 
addon = xbmcaddon.Addon('plugin.video.tvstreamer')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
link='http://zdf_hds_ng-f.akamaihd.net/i/none02_v1@87014/master.m3u8?dw=0 playpath=f24_livefr app=france24_live/fr'

li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={ "Title": title })
li.setProperty('IsPlayable', 'true')

xbmc.Player().play(item=link)
