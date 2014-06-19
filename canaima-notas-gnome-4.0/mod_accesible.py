#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (C) 2013 Canaima GNU/Linux
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

@author: Francisco Javier Vásquez Guerrero <franjvasquezg@gmail.com>

'''

import atk


def atk_acc(objeto, etiqueta):
	'''
	Este metodo es utilizado para relacionar una etiqueta a un objeto como por ejemplo Botones y 
	Deslizadores etc.
	'''
	atk_obj = objeto.get_accessible()
	atk_l = etiqueta.get_accessible()
	
	relation_set = atk_l.ref_relation_set()
	relation = atk.Relation((atk_obj,), atk.RELATION_LABEL_FOR)
	relation_set.add(relation)

def atk_acc_vd(objeto, descrip):
	'''
	Metodo para asignar descripciones a objetos por ejemplo ventana de desplazamiento(gtk.ScrolledWindow)
	la descripción debe venir entre comillas simples
	'''
	
	atk_vd = objeto.get_accessible()
	atk_vd.set_description(descrip)


def atk_label(etiqueta):

	'''
	Metodo para activar el foco de las etiquetas (gtk.label) de esta manera, orca las leerá
	'''
	etiqueta.set_selectable(True)

