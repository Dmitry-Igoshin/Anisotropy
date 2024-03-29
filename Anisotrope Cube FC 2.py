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
V = geompy.MakeVectorDXDYDZ(1, 1, 1)
V_1 = geompy.MakeVectorDXDYDZ(1, 1, 0)
V_2 = geompy.MakeVectorDXDYDZ(1, -1, 0)

L = 1.0
r0 = L*math.sqrt(2)/4
a=2*r0
b=L/2
#c=b/2
d = L*math.sqrt(3)
h = d/3
Pi_4 = 45*math.pi/180.0
n = 3                                                               # number of cubes in line

Vertex_1 = geompy.MakeVertex(-a, -a, -b)
Vertex_2 = geompy.MakeVertex(a, a, b)
Vertex_3 = geompy.MakeVertex(-b*(n-1), 0, -b*(n-2))                 # Center of Sphere_1
Vertex_4 = geompy.MakeVertex(-b*n, 0, -b*(n-3))                     # Center of Sphere_2
Vertex_5 = geompy.MakeVertex(0, 0, -b)

sk = geompy.Sketcher3D()                                            #             Rombus
sk.addPointsAbsolute(-b, -b, b)                                     # Vertex_1 of Rombus
sk.addPointsAbsolute(0, -b, 0)                                      # Vertex_2 of Rombus
sk.addPointsAbsolute(0, 0, -b)                                      # Vertex_3 of Rombus
sk.addPointsAbsolute(-b, 0, 0)                                      # Vertex_4 of Rombus
sk.addPointsAbsolute(-b, -b, b)                                     # Vertex_1 of Rombus
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Face_1_Up = geompy.MakeTranslation(Face_1, b, b, 0)
Rhombohedron = geompy.MakeHexa2Faces(Face_1, Face_1_Up)

sk_2 = geompy.Sketcher3D()                                          #             Triangle
sk_2.addPointsAbsolute(-2*b/3, -2*b/3, b/3)                         # Vertex_1 of Triangle
sk_2.addPointsAbsolute(0, -b, 0)                                    # Vertex_2 of Triangle
sk_2.addPointsAbsolute(-b/3, -b/3, -b/3)                            # Vertex_3 of Triangle
sk_2.addPointsAbsolute(-2*b/3, -2*b/3, b/3)                         # Vertex_1 of Triangle
a3D_Sketcher_2 = sk_2.wire() 
Face_2 = geompy.MakeFaceWires([a3D_Sketcher_2], 1)
Extrusion_2 = geompy.MakePrismVecH(Face_2, V, h)

sk_3 = geompy.Sketcher3D()                                          #             Hexagon
sk_3.addPointsAbsolute(-2*b/3, -2*b/3, b/3)                         # Vertex_1 of Hexagon
sk_3.addPointsAbsolute(0, -b, 0)                                    # Vertex_2 of Hexagon
sk_3.addPointsAbsolute(b/3, -2*b/3, -2*b/3)                         # Vertex_3 of Hexagon
sk_3.addPointsAbsolute(0, 0, -b)                                    # Vertex_4 of Hexagon
sk_3.addPointsAbsolute(-2*b/3, b/3, -2*b/3)                         # Vertex_5 of Hexagon
sk_3.addPointsAbsolute(-b, 0, 0)                                    # Vertex_6 of Hexagon
sk_3.addPointsAbsolute(-2*b/3, -2*b/3, b/3)                         # Vertex_1 of Hexagon
a3D_Sketcher_3 = sk_3.wire() 
Face_3 = geompy.MakeFaceWires([a3D_Sketcher_3], 1)
Extrusion_3 = geompy.MakePrismVecH(Face_3, V, h)

Translation_1 = geompy.MakeTranslation(a3D_Sketcher_3, -(n-2)*L/3, -(n-2)*L/3, -(n-2)*L/3)
Face_4 = geompy.MakeFaceWires([Translation_1], 1)
Vector_1 = geompy.MakeVectorDXDYDZ(1, 1, 1)
Extrusion_4 = geompy.MakePrismVecH(Face_4, Vector_1, (2*n-3)/3.0*d)   # Extrusion_3Direction

Box_1 = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, Pi_4)
Box_2 = geompy.MakeBoxTwoPnt(Vertex_5, Vertex_2)
Rotation_2 = geompy.MakeRotation(Box_2, OZ, Pi_4)

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
geompy.addToStudy( Face_1_Up, 'Face_1_Up' )
geompy.addToStudy( Rhombohedron, 'Rhombohedron' )
geompy.addToStudy( a3D_Sketcher_2, 'a3D_Sketcher_2' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Extrusion_2, 'Extrusion_2' )
geompy.addToStudy( a3D_Sketcher_3, 'a3D_Sketcher_3' )
geompy.addToStudy( Face_3, 'Face_3' )
geompy.addToStudy( Extrusion_3, 'Extrusion_3' )
geompy.addToStudy( Face_4, 'Face_4' )
geompy.addToStudy( Extrusion_4, 'Extrusion_4' )
 
i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12]
##alpha=[0.134]
alpha=[0.1]
for element in alpha:
    Radius = r0/(1-alpha[i])
    Sphere_1 = geompy.MakeSpherePntR(Vertex_3, Radius)
    Down = geompy.MakeMultiTranslation2D(Sphere_1, V_1, a, n, V_2, a, n)
    Up_Down = geompy.MakeMultiTranslation1D(Down, OZ, 1, n-1)
    Cut_1 = geompy.MakeCutList(Rotation_1, [Up_Down], True)

    Sphere_2 = geompy.MakeSpherePntR(Vertex_4, Radius)
    Middle = geompy.MakeMultiTranslation2D(Sphere_2, V_1, a, n+1, V_2, a, n+1)
    Middle_Up = geompy.MakeMultiTranslation1D(Middle, OZ, 1, n-2)
    Cut_2 = geompy.MakeCutList(Cut_1, [Middle_Up], True)

    Common = geompy.MakeCommonList([Cut_2, Rotation_2], True)
    Pore_3 = geompy.MakeCommonList([Rhombohedron, Cut_2], True)

    Cut_3 = geompy.MakeCutList(Extrusion_2, [Up_Down], True)
    Cut_4 = geompy.MakeCutList(Cut_3, [Middle_Up], True)
    
    Cut_5 = geompy.MakeCutList(Extrusion_3, [Up_Down], True)
    Cut_6 = geompy.MakeCutList(Cut_5, [Middle_Up], True)

    Cut_7 = geompy.MakeCutList(Extrusion_4, [Up_Down], True)
    Cut_8 = geompy.MakeCutList(Cut_7, [Middle_Up], True)

    #geompy.addToStudy( Sphere_1, 'Sphere_'+str(i+1) )
    geompy.addToStudy( Down, 'Down_'+str(i+1) )
    geompy.addToStudy( Up_Down, 'Up_Down_'+str(i+1) )
    geompy.addToStudy( Cut_1, 'Cut_1_'+str(i+1) )
    geompy.addToStudy( Middle_Up, 'Middle_Up_'+str(i+1) )
    geompy.addToStudy( Cut_2, 'Pore_'+str(i+1) )
    geompy.addToStudy( Common, 'Pore_2_'+str(i+1) )
    geompy.addToStudy( Pore_3, 'Pore_3_'+str(i+1) )
    geompy.addToStudy( Cut_4, 'Pore_3a_'+str(i+1) )
    geompy.addToStudy( Cut_6, 'Pore_3b_'+str(i+1) )
    geompy.addToStudy( Cut_8, 'Pore_3c_'+str(i+1) )

    i = i + 1
    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser(True)
