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

a=math.sqrt(2)
b=0.5
r0=math.sqrt(3)/4
h4=0.25

Vertex_1 = geompy.MakeVertex(-a/2, -a/2, 0)                         #Vertex_1 of Box_1
Vertex_2 = geompy.MakeVertex(a/2, a/2, 1)                           #Vertex_2 of Box_1
Vertex_3 = geompy.MakeVertex(-a, 0, 0)                              #Center of Sphere_1
Vertex_4 = geompy.MakeVertex(-a/2, 0, b)                            #Center of Sphere_2
Vertex_5 = geompy.MakeVertex(1, 1, 1)                               #Vertex_2 of Box_2

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(-a/2, -a/2, b)                                 #Vertex_1 of Rombus
sk.addPointsAbsolute(0, -a/2, 0)                                    #Vertex_2 of Rombus
sk.addPointsAbsolute(0, 0, -b)                                      #Vertex_3 of Rombus
sk.addPointsAbsolute(-a/2, 0, 0)                                    #Vertex_4 of Rombus
sk.addPointsAbsolute(-a/2, -a/2, b)                                 #Vertex_1 of Rombus
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Face_2 = geompy.MakeTranslation(Face_1, a/2, a/2, 0)
Rhombohedron = geompy.MakeHexa2Faces(Face_1, Face_2)

Box_1 = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Box_2 = geompy.MakeBoxTwoPnt(O, Vertex_5)
Rotation_2 = geompy.MakeRotation(Box_2, OZ, 45*math.pi/180.0)
Translation_1 = geompy.MakeTranslation(Rotation_2, 0, 0, h4)

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( V_1, 'V_1' )
geompy.addToStudy( V_2, 'V_2' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Rotation_2, 'Rotation_2_' )

geompy.addToStudy( a3D_Sketcher_1, 'a3D_Sketcher_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Rhombohedron, 'Rhombohedron' )
geompy.addToStudy( Translation_1, 'Translation_1' )
 
i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12]
alpha=[0.15]
for element in alpha:
	Radius = r0/(1-alpha[i])
	Sphere_1 = geompy.MakeSpherePntR(Vertex_3, Radius)
	Down = geompy.MakeMultiTranslation2D(Sphere_1, V_1, 1, 3, V_2, 1, 3)
	Up_Down = geompy.MakeMultiTranslation1D(Down, OZ, 1, 2)
	Cut_1 = geompy.MakeCutList(Translation_1, [Up_Down])
	
	Sphere_2 = geompy.MakeSpherePntR(Vertex_4, Radius)
	Middle = geompy.MakeMultiTranslation2D(Sphere_2, V_1, 1, 2, V_2, 1, 2)
	Middle_2 = geompy.MakeMultiTranslation1D(Middle, OZ, 1, 2)
	Cut_2 = geompy.MakeCutList(Cut_1, [Middle_2])

	Pore_2 = geompy.MakeCommonList([Up_Down, Middle, Rotation_2], True)
	Pore_3 = geompy.MakeCommonList([Rhombohedron, Cut_2], True)

	geompy.addToStudy( Sphere_1, 'Sphere_'+str(i+1) )
	geompy.addToStudy( Down, 'Down_'+str(i+1) )
	geompy.addToStudy( Up_Down, 'Up_Down_'+str(i+1) )
	geompy.addToStudy( Cut_1, 'Cut_1_'+str(i+1) )
	geompy.addToStudy( Middle, 'Middle_'+str(i+1) )
	geompy.addToStudy( Middle_2, 'Middle_2_'+str(i+1) )
	geompy.addToStudy( Cut_2, 'Pore_'+str(i+1) )
	geompy.addToStudy( Pore_2, 'Pore_2_'+str(i+1) )
	geompy.addToStudy( Pore_3, 'Pore_3_'+str(i+1) )

	i = i + 1
	if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(True)
