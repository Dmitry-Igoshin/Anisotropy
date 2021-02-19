# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'C:/SALOME-8.3.0-WIN64/WORK')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

Box_1 = geompy.MakeBoxDXDYDZ(2*math.sqrt(2), 2*math.sqrt(2), 2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Translation_2 = geompy.MakeTranslation(Rotation_1, 2, 0, 0)
Vertex_1 = geompy.MakeVertex(2, 0, 0)
Vertex_2 = geompy.MakeVertex(2, 2, 0)
Vertex_3 = geompy.MakeVertex(2, 2, 2)
Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Translation_2, 'Translation_2' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Line_1, 'Line_1' )

i = 0
alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28]
#alpha=[0.01,0.02,0.03]
for element in alpha:
	Sphere_1 = geompy.MakeSpherePntR(Vertex_1, 1/(1-alpha[i]))
	Multi_Translation_1 = geompy.MakeMultiTranslation1D(Sphere_1, OY, 2, 3)
	Cut_1 = geompy.MakeCutList(Translation_2, [Multi_Translation_1], True)
	Translation_3 = geompy.MakeTranslation(Multi_Translation_1, 0, 0, 2)
	Cut_2 = geompy.MakeCutList(Cut_1, [Translation_3], True)
	Rotation_2 = geompy.MakeRotation(Multi_Translation_1, Line_1, 90*math.pi/180.0)
	Cut_3 = geompy.MakeCutList(Cut_2, [Rotation_2], True)
	Translation_4 = geompy.MakeTranslation(Rotation_2, 0, 0, 2)
	Cut_4 = geompy.MakeCutList(Cut_3, [Translation_4], True)
	#geompy.addToStudy( Sphere_1, 'Sphere_1' )
	#geompy.addToStudy( Multi_Translation_1, 'Multi-Translation_1' )
	#geompy.addToStudy( Cut_1, 'Cut_1' )
	#geompy.addToStudy( Translation_3, 'Translation_3' )
	#geompy.addToStudy( Cut_2, 'Cut_2' )
	#geompy.addToStudy( Rotation_2, 'Rotation_2' )
	#geompy.addToStudy( Cut_3, 'Cut_3' )
	#geompy.addToStudy( Translation_4, 'Translation_4' )
	geompy.addToStudy( Cut_4, 'Cut_'+str(i+1) )
	i = i + 1
	if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(True)

