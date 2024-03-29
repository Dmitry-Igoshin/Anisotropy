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

r0 = 1.0
L = 2*r0
h = L
h2 = 2*h
d1 = L*math.sqrt(2)
d2 = L*math.sqrt(3)
d = r0/math.sqrt(3)
pi_4 = 45*math.pi/180.0
pi_2 = 90*math.pi/180.0
n = 3                                                             # number of cubes in line

Box_1 = geompy.MakeBoxDXDYDZ(d1, d1, h)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, pi_4)
Translation_2 = geompy.MakeTranslation(Rotation_1, h, 0, 0)
Vertex_1 = geompy.MakeVertex(h, 0, 0)
Vertex_2 = geompy.MakeVertex(h, h, 0)
Vertex_3 = geompy.MakeVertex(h, h, h)
Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(0, 0, h2)                                    #             Rombus
sk.addPointsAbsolute(h, 0, h)                                     # Vertex_2 of Rombus
sk.addPointsAbsolute(h, h, 0)                                     # Vertex_3 of Rombus
sk.addPointsAbsolute(0, h, h)                                     # Vertex_4 of Rombus
sk.addPointsAbsolute(0, 0, h2)                                    # Vertex_1 of Rombus
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Vector_1 = geompy.MakeVectorDXDYDZ(1, 1, 0)
Extrusion_1 = geompy.MakePrismVecH(Face_1, Vector_1, d1)

sk_2 = geompy.Sketcher3D()                                        #             Hexagon
sk_2.addPointsAbsolute(L, L, L)                                   # Vertex_1 of Hexagon
sk_2.addPointsAbsolute(5*L/3, 2*L/3, 2*L/3)                       # Vertex_2 of Hexagon
sk_2.addPointsAbsolute(2*L, L, 0)                                 # Vertex_3 of Hexagon
sk_2.addPointsAbsolute(5*L/3, 5*L/3, -L/3)                        # Vertex_4 of Hexagon
sk_2.addPointsAbsolute(L, 2*L, 0)                                 # Vertex_5 of Hexagon
sk_2.addPointsAbsolute(2*L/3, 5*L/3, 2*L/3)                       # Vertex_6 of Hexagon
sk_2.addPointsAbsolute(L, L, L)                                   # Vertex_1 of Hexagon
a3D_Sketcher_2 = sk_2.wire()
Face_2 = geompy.MakeFaceWires([a3D_Sketcher_2], 1)
Vector_2 = geompy.MakeVectorDXDYDZ(1, 1, 1)
Extrusion_2 = geompy.MakePrismVecH(Face_2, Vector_2, d2/3)

Translation_3 = geompy.MakeTranslation(a3D_Sketcher_2, -L-L/6, -L-L/6, 0-L/6)
Face_3 = geompy.MakeFaceWires([Translation_3], 1)
Vector_2 = geompy.MakeVectorDXDYDZ(1, 1, 1)
Extrusion_3 = geompy.MakePrismVecH(Face_3, Vector_2, (n-4.0/3)*d2)    # Extrusion_3Direction

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Translation_2, 'Translation_2' )

geompy.addToStudy( a3D_Sketcher_1, 'a3D_Sketcher_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( a3D_Sketcher_2, 'a3D_Sketcher_2' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Vector_2, 'Vector_2' )
geompy.addToStudy( Extrusion_2, 'Extrusion_2' )
geompy.addToStudy( Translation_3, 'a3D_Sketcher_3' )
geompy.addToStudy( Extrusion_3, 'Extrusion_3' )

i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28]
#alpha=[n*0.01 for n in range(1,28+1) ]
#alpha=[0.2929]
alpha=[0.1]
for element in alpha:
    Sphere_1 = geompy.MakeSphereR(r0/(1-alpha[i]))
    Multi_Translation_2 = geompy.MakeMultiTranslation2D(Sphere_1, OX, L, n, OY, L, n)
    Multi_Translation_3 = geompy.MakeMultiTranslation1D(Multi_Translation_2, OZ, L, n)
    Cut_1 = geompy.MakeCutList(Translation_2, [Multi_Translation_3])
    Cut_2 = geompy.MakeCutList(Extrusion_1, [Multi_Translation_3])
    Cut_3 = geompy.MakeCutList(Extrusion_2, [Multi_Translation_3])
    Cut_V = geompy.MakeCutList(Cut_1, [Cut_3])
    #Cut_2.SetColor(SALOMEDS.Color(0,0,1))
    Cut_4 = geompy.MakeCutList(Extrusion_3, [Multi_Translation_3])

    geompy.addToStudy( Sphere_1, 'Sphere_' )
    geompy.addToStudy( Multi_Translation_2, 'Multi-Translation_2_'+str(i+1)  )
    geompy.addToStudy( Multi_Translation_3, 'Multi-Translation_3_'+str(i+1)  )
    geompy.addToStudy( Cut_1, 'Pore1_'+str(i+1) )
    geompy.addToStudy( Cut_2, 'Pore2_'+str(i+1) )
    geompy.addToStudy( Cut_3, 'Pore3_'+str(i+1) )
    geompy.addToStudy( Cut_V, 'Cut_V_'+str(i+1) )
    geompy.addToStudy( Cut_4, 'Pore4_'+str(i+1) )

    i = i + 1
    if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(True)
