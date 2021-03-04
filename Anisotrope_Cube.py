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

d1 = 2*math.sqrt(2)
d2 = 2*math.sqrt(3)
d = 1/math.sqrt(3)
h = 2
h2 = 2*h
pi_4 = 45*math.pi/180.0
pi_2 = 90*math.pi/180.0

Box_1 = geompy.MakeBoxDXDYDZ(d1, d1, h)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, pi_4)
Translation_2 = geompy.MakeTranslation(Rotation_1, h, 0, 0)
Vertex_1 = geompy.MakeVertex(h, 0, 0)
Vertex_2 = geompy.MakeVertex(h, h, 0)
Vertex_3 = geompy.MakeVertex(h, h, h)
Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)

#sk = geompy.Sketcher3D()
#sk.addPointsAbsolute(h, h, h)                                      #Vertex_1 of Rombus
#sk.addPointsAbsolute(h, h2, 0)                                     #Vertex_2 of Rombus
#sk.addPointsAbsolute(h2, h, 0)                                     #Vertex_3 of Rombus
#sk.addPointsAbsolute(h2, 0, h)                                     #Vertex_4 of Rombus
#sk.addPointsAbsolute(h, h, h)                                      #Vertex_1 of Rombus
#a3D_Sketcher_1 = sk.wire()

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(h, 0, 0)                                      #Vertex_1 of Rombus
sk.addPointsAbsolute(0, h, 0)                                      #Vertex_2 of Rombus
sk.addPointsAbsolute(0, 0, h)                                      #Vertex_3 of Rombus
sk.addPointsAbsolute(h, 0, 0)                                      #Vertex_1 of Rombus
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Translation_1 = geompy.MakeTranslation(Face_1, d, d, d)
Vector_1 = geompy.MakeVectorDXDYDZ(1, 1, 1)
Extrusion_1 = geompy.MakePrismVecH(Translation_1, Vector_1, -d2)

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
geompy.addToStudy( a3D_Sketcher_1, 'a3D_Sketcher_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Translation_1, 'Translation_1' )

i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28]
alpha=[0.1]
for element in alpha:
    Sphere_1 = geompy.MakeSpherePntR(Vertex_1, 1/(1-alpha[i]))
    Multi_Translation_1 = geompy.MakeMultiTranslation1D(Sphere_1, OY, h, 3)
    Cut_1 = geompy.MakeCutList(Translation_2, [Multi_Translation_1], True)
    Translation_3 = geompy.MakeTranslation(Multi_Translation_1, 0, 0, h)
    Cut_2 = geompy.MakeCutList(Cut_1, [Translation_3], True)
    Rotation_2 = geompy.MakeRotation(Multi_Translation_1, Line_1, pi_2)
    Cut_3 = geompy.MakeCutList(Cut_2, [Rotation_2], True)
    Translation_4 = geompy.MakeTranslation(Rotation_2, 0, 0, h)
    Cut_4 = geompy.MakeCutList(Cut_3, [Translation_4], True)

    Sphere_2 = geompy.MakeSphereR(1/(1-alpha[i]))
    Multi_Translation_2 = geompy.MakeMultiTranslation2D(Sphere_2, OX, 2, 3, OY, 2, 3)
    Multi_Translation_3 = geompy.MakeMultiTranslation1D(Multi_Translation_2, OZ, 2, 3)
    Cut_5 = geompy.MakeCutList(Translation_2, [Multi_Translation_3])

    geompy.addToStudy( Sphere_1, 'Sphere_1' )
    geompy.addToStudy( Multi_Translation_1, 'Multi-Translation_1' )
    geompy.addToStudy( Cut_1, 'Cut_1' )
    geompy.addToStudy( Translation_3, 'Translation_3' )
    geompy.addToStudy( Cut_2, 'Cut_2' )
    geompy.addToStudy( Rotation_2, 'Rotation_2' )
    geompy.addToStudy( Cut_3, 'Cut_3' )
    geompy.addToStudy( Translation_4, 'Translation_4' )
    geompy.addToStudy( Cut_4, 'Pore_'+str(i+1) )
    geompy.addToStudy( Sphere_2, 'Sphere_2' )
    geompy.addToStudy( Multi_Translation_2, 'Multi-Translation_2' )
    geompy.addToStudy( Multi_Translation_3, 'Multi-Translation_3' )
    geompy.addToStudy( Cut_5, 'Pore2_' )

    i = i + 1
    if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(True)

