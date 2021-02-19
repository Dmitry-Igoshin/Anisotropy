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
V_1 = geompy.MakeVectorDXDYDZ(1, 1, 0)
V_2 = geompy.MakeVectorDXDYDZ(1, -1, 0)

a=1/math.sqrt(2)
b=0.5

Vertex_1 = geompy.MakeVertex(-a, -a, -b)
Vertex_2 = geompy.MakeVertex(a, a, b)
Vertex_3 = geompy.MakeVertex(-b, -b, -b)
Vertex_4 = geompy.MakeVertex(-1, -1, -b)
Vertex_5 = geompy.MakeVertex(-b, 0, -0)

#Box_1 = geompy.MakeBoxDXDYDZ(math.sqrt(2), math.sqrt(2), 1)
Box_1 = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
#Translation_1 = geompy.MakeTranslation(Rotation_1, 2, 1, 0)
#Translation_2 = geompy.MakeTranslation(Rotation_1, 2.25, 1.25, 0.25)
#Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( V_1, 'V_1' )
geompy.addToStudy( V_2, 'V_2' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
#geompy.addToStudy( Translation_1, 'WorkBox' )
#geompy.addToStudy( Line_1, 'Line_1' )

i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12]
alpha=[0.08]
for element in alpha:
	Radius = math.sqrt(2)/4/(1-alpha[i])
	Sphere_1 = geompy.MakeSpherePntR(Vertex_3, Radius)
	Down = geompy.MakeMultiTranslation2D(Sphere_1, OX, 1, 2, OY, 1, 2)
	Up_Down = geompy.MakeMultiTranslation1D(Down, OZ, 1, 2)
	Cut_1 = geompy.MakeCutList(Rotation_1, [Up_Down], True)
	
	Sphere_2 = geompy.MakeSpherePntR(Vertex_4, Radius)
	Down_2 = geompy.MakeMultiTranslation2D(Sphere_2, OX, 1, 3, OY, 1, 3)
	Up_Down_2 = geompy.MakeMultiTranslation1D(Down_2, OZ, 1, 2)
	Cut_2 = geompy.MakeCutList(Cut_1, [Up_Down_2], True)
	
	Sphere_3 = geompy.MakeSpherePntR(Vertex_5, Radius)
	Middle = geompy.MakeMultiTranslation2D(Sphere_3, V_1, a, 2, V_2, a, 2)
	Cut_3 = geompy.MakeCutList(Cut_2, [Middle], True)
	
	#Pore = geompy.MakeCutList(Translation_1, [Sceleton], True)
	#Pore_2 = geompy.MakeCutList(Translation_2, [Sceleton], True)
	#Translation_2 = geompy.MakeTranslation(MT_1, 0.5, 0.5, 0.5)
	#Cut_2 = geompy.MakeCutList(Cut_1, [Translation_2], True)
	#Rotation_2 = geompy.MakeRotation(Multi_Translation_1, Line_1, 90*math.pi/180.0)
	#Cut_3 = geompy.MakeCutList(Cut_2, [Rotation_2], True)
	#Translation_4 = geompy.MakeTranslation(Rotation_2, 0, 0, 2)
	#Cut_4 = geompy.MakeCutList(Cut_3, [Translation_4], True)
	
	geompy.addToStudy( Sphere_1, 'Sphere_1' )
	geompy.addToStudy( Down, 'Down' )
	geompy.addToStudy( Up_Down, 'Up_Down' )
	geompy.addToStudy( Cut_1, 'Cut_1' )
	geompy.addToStudy( Sphere_2, 'Sphere_2' )
	geompy.addToStudy( Down_2, 'Down_2' )
	geompy.addToStudy( Up_Down_2, 'Up_Down_2' )
	geompy.addToStudy( Cut_2, 'Cut_2' )
	geompy.addToStudy( Middle, 'Middle' )
	geompy.addToStudy( Cut_3, 'Pore_'+str(i+1) )
	#geompy.addToStudy( Pore, 'Pore' )
	#geompy.addToStudy( Pore_2, 'Pore_2' )
	#geompy.addToStudy( Rotation_2, 'Rotation_2' )
	#geompy.addToStudy( Translation_4, 'Translation_4' )
	#geompy.addToStudy( Cut_4, 'Cut_'+str(i+1) )
	i = i + 1
	if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(True)

