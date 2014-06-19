'''
Copyright (C) 2010 Canaima GNU/Linux
<desarrolladores@canaima.softwarelibre.gob.ve>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA

Created on 08/02/2013

@author: Erick Birbe <erickcion@gmail.com>
'''
import os
import urllib
from common import list_to_lines, TXT_FILE
import gettext
from gettext import gettext as _

# Traducciones de Canaima-notas-gnome -----
gettext.textdomain("canaima_notas_gnome")
gettext.bindtextdomain("canaima_notas_gnome", "/usr/share/locale")


URL_SEND = "http://notas.canaima.softwarelibre.gob.ve/enviar_consola"

class Note():

    def __init__(self, title=None, author=None, email=None, details=None):
        '''
        Constructor
        '''
        self.__data = []
        self.title = title
        self.author = author
        self.email = email
        self.details = details
        self.is_viewonly = True

    def __str__(self):
        return list_to_lines(self.__data)

    def add(self, string):
        self.__data.append(string)

    def add_log_output(self, command, subtitle=None):

        if subtitle:
            self.add("----- %s:" % subtitle)
        else:
            self.add("----- [%s]:" % command)

        self.add("")
        self.add(os.popen(command).read())
        self.add("")

    def append_defaults(self):
        assert self.title is not None
        assert self.author is not None
        assert self.email is not None
        assert self.details is not None

        if self.is_viewonly:
            self.add(_("TITLE: %s") % self.title)
            self.add(_("AUTHOR: %s") % self.author)
        
        self.add(_("EMAIL: %s") % self.email)

        self.add("")
        self.add(_("_____________________ NOTE TO USER ____________________"))
        self.add("")
        self.add(self.details)
        self.add("__________________________________________________________")
        self.add("")

    def send_note(self):
        params = urllib.urlencode({'codigo_form': self.__str__(),
                                   'titulo_form': self.title,
                                   'nombre_form': self.author})
        f = urllib.urlopen(URL_SEND, params)
        self.msg = f.read()

    def write_to_file(self):
        note_file = open(TXT_FILE, 'w')
        note_file.writelines(self.__str__())
        note_file.close()
