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
c=b/2
d=math.sqrt(3)/8

Vertex_1 = geompy.MakeVertex(-a, -a, -b)
Vertex_2 = geompy.MakeVertex(a, a, b)
Vertex_3 = geompy.MakeVertex(-1, 0, -b)
Vertex_4 = geompy.MakeVertex(-b, 0, -0)
Vertex_5 = geompy.MakeVertex(0, 0, -b)
Vertex_6 = geompy.MakeVertex(c, c, c)
Vertex_7 = geompy.MakeVertex(-d, -d, -d)

Line_1 = geompy.MakeLineTwoPnt(O, Vertex_6)
Plane_1 = geompy.MakePlane(Vertex_6, Line_1, 3)
Line_2 = geompy.MakeLineTwoPnt(O, Vertex_7)
Plane_2 = geompy.MakePlane(Vertex_7, Line_2, 3)

Box_1 = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Box_2 = geompy.MakeBoxTwoPnt(Vertex_5, Vertex_2)
Rotation_2 = geompy.MakeRotation(Box_2, OZ, 45*math.pi/180.0)

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
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Rotation_2, 'Rotation_2_' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Line_1, 'Line_1_' )
geompy.addToStudy( Plane_1, 'Plane_1' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Plane_2, 'Plane_2' )

i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12]
alpha=[0.1]
for element in alpha:
	Radius = math.sqrt(2)/4/(1-alpha[i])
	Sphere_1 = geompy.MakeSpherePntR(Vertex_3, Radius)
	Down = geompy.MakeMultiTranslation2D(Sphere_1, V_1, a, 3, V_2, a, 3)
	Up_Down = geompy.MakeMultiTranslation1D(Down, OZ, 1, 2)
	Cut_1 = geompy.MakeCutList(Rotation_1, [Up_Down], True)
	
	Sphere_2 = geompy.MakeSpherePntR(Vertex_4, Radius)
	Middle = geompy.MakeMultiTranslation2D(Sphere_2, V_1, a, 2, V_2, a, 2)
	Cut_2 = geompy.MakeCutList(Cut_1, [Middle], True)

	Common = geompy.MakeCommonList([Cut_2, Rotation_2], True)
	
	#geompy.addToStudy( Sphere_, 'Sphere_1'+str(i+1) )
	#geompy.addToStudy( Down, 'Down_'+str(i+1) )
	geompy.addToStudy( Up_Down, 'Up_Down_'+str(i+1) )
	geompy.addToStudy( Cut_1, 'Cut_1_'+str(i+1) )
	geompy.addToStudy( Middle, 'Middle_'+str(i+1) )
	geompy.addToStudy( Cut_2, 'Pore_'+str(i+1) )
	geompy.addToStudy( Common, 'Pore_2_'+str(i+1) )
	
	i = i + 1
	if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(True)