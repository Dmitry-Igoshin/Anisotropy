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

Box_1 = geompy.MakeBoxDXDYDZ(math.sqrt(2), math.sqrt(2), 1)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Translation_1 = geompy.MakeTranslation(Rotation_1, 2, 1, 0)
Translation_2 = geompy.MakeTranslation(Rotation_1, 2.25, 1.25, 0.25)
Vertex_1 = geompy.MakeVertex(0, 0, 0)
Vertex_2 = geompy.MakeVertex(2, 2, 0)
Vertex_3 = geompy.MakeVertex(2, 2, 2)
Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Translation_1, 'WorkBox' )
geompy.addToStudy( Translation_2, 'WorkBox_2' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Line_1, 'Line_1' )

i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12]
alpha=[0.08]
for element in alpha:
	Sphere_1 = geompy.MakeSpherePntR(Vertex_1, math.sqrt(3)/4/(1-alpha[i]))
	Down = geompy.MakeMultiTranslation2D(Sphere_1, OX, 1, 5, OY, 1, 5)
	Vector_1 = geompy.MakeVectorDXDYDZ(0.5, 0.5, 0.5)
	Sceleton = geompy.MakeMultiTranslation1D(Down, Vector_1, math.sqrt(3)/2, 5)
	#MT_2 = geompy.MakeMultiTranslation1D(MT_1, OZ, 1, 2)
	Pore = geompy.MakeCutList(Translation_1, [Sceleton], True)
	Pore_2 = geompy.MakeCutList(Translation_2, [Sceleton], True)
	#Translation_2 = geompy.MakeTranslation(MT_1, 0.5, 0.5, 0.5)
	#Cut_2 = geompy.MakeCutList(Cut_1, [Translation_2], True)
	#Rotation_2 = geompy.MakeRotation(Multi_Translation_1, Line_1, 90*math.pi/180.0)
	#Cut_3 = geompy.MakeCutList(Cut_2, [Rotation_2], True)
	#Translation_4 = geompy.MakeTranslation(Rotation_2, 0, 0, 2)
	#Cut_4 = geompy.MakeCutList(Cut_3, [Translation_4], True)
	geompy.addToStudy( Sphere_1, 'Sphere_1' )
	geompy.addToStudy( Down, 'Down' )
	geompy.addToStudy( Sceleton, 'Sceleton' )
	geompy.addToStudy( Pore, 'Pore' )
	geompy.addToStudy( Pore_2, 'Pore_2' )
	#geompy.addToStudy( Cut_2, 'Pore' )
	#geompy.addToStudy( Rotation_2, 'Rotation_2' )
	#geompy.addToStudy( Cut_3, 'Cut_3' )
	#geompy.addToStudy( Translation_4, 'Translation_4' )
	#geompy.addToStudy( Cut_4, 'Cut_'+str(i+1) )
	i = i + 1
	if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(True)

