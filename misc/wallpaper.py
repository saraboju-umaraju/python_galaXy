#!/usr/bin/python3
#import gconf
#conf = gconf.client_get_default()
#conf.set_string('/desktop/gnome/background/picture_filename','/path/to/filename.jpg')
import os
command = "gsettings set org.gnome.desktop.background picture-uri file:///home/umaraju/Wallpapers/IMG_20160511_192108995.jpg"
os.system(command)
