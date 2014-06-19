#-*- coding: UTF-8 -*-
'''
Copyright (C) 2010 Canaima GNU/Linux
<desarrolladores@canaima.softwarelibre.gob.ve>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Ucumari; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

Created on 08/02/2013

@author: Erick Birbe <erickcion@gmail.com>
'''
import sys
from subprocess import Popen, PIPE
import gtk

# Declaraciones ---------------------------------------------------------------

WORKDIR = sys.path[0]
APP_NAME = 'canaima-notas-gnome'
TOP_BANNER_PATH = WORKDIR + '/img/banner-app-top.png'
ICON_PATH = WORKDIR + '/img/canaima-notas-icons.png'
# FIXME: Rutas de archivos temporales no optimas en ambientes multiusuarios
# si varios usuarios utilizan la herramienta a la vez se pueden mezclar los
# contenidos de los archivos
TXT_FILE = '/tmp/notas-document.txt'
URL_PASTE_PLATFORM = 'http://notas.canaima.softwarelibre.gob.ve/'

# Funciones generales ---------------------------------------------------------


def launch_help(widget=None):

    Popen(["yelp /usr/share/gnome/help/%s/es/c-n.xml" % APP_NAME], \
              shell=True, stdout=PIPE)


def list_to_lines(the_list):
    '''Converts each value of a list in a string line and returns the
    concatenated text.
    Arguments:
        the_list: The list that will be converted.
    Return:
        The string composed of concatenated lines.'''
    data = ""
    i = 0
    for line in the_list:
        if i > 0:
            data += "\n"
        i += 1
        data += str(line)
    return data


# GTK Dialogs -----------------------------------------------------------------

def message_question(message, parent=None):
    msg_box = gtk.MessageDialog(parent=parent,
                             type=gtk.MESSAGE_QUESTION,
                             buttons=gtk.BUTTONS_YES_NO,
                             message_format=message)
    response = msg_box.run()
    msg_box.destroy()
    return response


def message_error(message, parent=None):
    msg_box = gtk.MessageDialog(parent=parent,
                             type=gtk.MESSAGE_ERROR,
                             buttons=gtk.BUTTONS_CLOSE,
                             message_format=message)
    response = msg_box.run()
    msg_box.destroy()
    return response

def message_info(message, parent=None):
    msg_box = gtk.MessageDialog(parent=parent,
                             type=gtk.MESSAGE_INFO,
                             buttons=gtk.BUTTONS_CLOSE,
                             message_format=message)
    response = msg_box.run()
    msg_box.destroy()
    return response
