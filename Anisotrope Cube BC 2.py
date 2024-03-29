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

L = 1.0
r0 = L*math.sqrt(3)/4
d1 = L*math.sqrt(2)
Pi_4 = 45*math.pi/180.0
n = 3

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(0, 0, 2*L)                                                 # Vertex_1 of Rombus
sk.addPointsAbsolute(L, 0, L)                                                   # Vertex_2 of Rombus
sk.addPointsAbsolute(L, L, 0)                                                   # Vertex_3 of Rombus
sk.addPointsAbsolute(0, L, L)                                                   # Vertex_4 of Rombus
sk.addPointsAbsolute(0, 0, 2*L)                                                 # Vertex_1 of Rombus
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Extrusion_1 = geompy.MakePrismDXDYDZ(Face_1, L/2, L/2, L/2)

sk2 = geompy.Sketcher3D()
sk2.addPointsAbsolute(L/3, L/3, 4*L/3)                                          # Vertex_1 of Triangle
sk2.addPointsAbsolute(L, 0, L)                                                  # Vertex_2 of Triangle
sk2.addPointsAbsolute(2*L/3, 2*L/3, 2*L/3)                                      # Vertex_3 of Triangle
sk2.addPointsAbsolute(L/3, L/3, 4*L/3)                                          # Vertex_1 of Triangle
a3D_Sketcher_2 = sk2.wire()
Face_2 = geompy.MakeFaceWires([a3D_Sketcher_2], 1)
Extrusion_2 = geompy.MakePrismDXDYDZ(Face_2, L/2, L/2, L/2)

sk3 = geompy.Sketcher3D()
sk3.addPointsAbsolute(L/3, L/3, 4*L/3)                                          # Vertex_1 of Hexagon
sk3.addPointsAbsolute(L, 0, L)                                                  # Vertex_2 of Hexagon
sk3.addPointsAbsolute(4*L/3, L/3, L/3)                                          # Vertex_3 of Hexagon
#sk3.addPointsAbsolute(2*L/3, 2*L/3, 2*L/3)                                     # Vertex_3 of Hexagon
sk3.addPointsAbsolute(L, L, 0)                                                  # Vertex_4 of Hexagon
sk3.addPointsAbsolute(L/3, 4*L/3, L/3)                                          # Vertex_5 of Hexagon
sk3.addPointsAbsolute(0, L, L)                                                  # Vertex_6 of Hexagon
sk3.addPointsAbsolute(L/3, L/3, 4*L/3)                                          # Vertex_1 of Hexagon
a3D_Sketcher_3 = sk3.wire()
Face_3 = geompy.MakeFaceWires([a3D_Sketcher_3], 1)
Extrusion_3 = geompy.MakePrismDXDYDZ(Face_3, L/2, L/2, L/2)

a3D_Sketcher_4 = geompy.MakeTranslation(a3D_Sketcher_3, -L/4, -L/4, -L/4)
Face_4 = geompy.MakeFaceWires([a3D_Sketcher_4], 1)
#Extrusion_4 = geompy.MakePrismDXDYDZ(Face_4, (n-1.5)*L, (n-1.5)*L, (n-1.5)*L)   # Extrusion_3Direction
Vector_1 = geompy.MakeVectorDXDYDZ(1, 1, 1)
Extrusion_4 = geompy.MakePrismVecH(Face_4, Vector_1, 4*(n-1.5)*r0)              # Extrusion_3Direction

Box_1 = geompy.MakeBoxDXDYDZ(d1, d1, L)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, Pi_4)
Translation_1 = geompy.MakeTranslation(Rotation_1, L, 0, 0)
Translation_2 = geompy.MakeTranslation(Translation_1, 0, 0, L/4)

Box_2 = geompy.MakeBoxDXDYDZ(d1/2, d1/2, L)
Rotation_2 = geompy.MakeRotation(Box_2, OZ, Pi_4)
Translation_3 = geompy.MakeTranslation(Rotation_2, L, 0, L/4)

Box_3 = geompy.MakeBoxDXDYDZ(d1/2, d1/2, L/2)
Rotation_3 = geompy.MakeRotation(Box_3, OZ, Pi_4)
Translation_4 = geompy.MakeTranslation(Rotation_3, L, 0, L/4)

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( V_1, 'V_1' )
geompy.addToStudy( V_2, 'V_2' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Translation_2, 'Translation_2' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Rotation_2, 'Rotation_2' )
geompy.addToStudy( Translation_3, 'Translation_3' )
geompy.addToStudy( Rotation_3, 'Rotation_3' )
geompy.addToStudy( Translation_4, 'Translation_4' )

#geompy.addToStudy( a3D_Sketcher_1, 'a3D_Sketcher_1' )
#geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( a3D_Sketcher_2, 'a3D_Sketcher_2' )
#geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Extrusion_2, 'Extrusion_2' )
geompy.addToStudy( a3D_Sketcher_3, 'a3D_Sketcher_3' )
#geompy.addToStudy( Face_3, 'Face_3' )
#geompy.addToStudy( Extrusion_3, 'Extrusion_3' )
geompy.addToStudy( a3D_Sketcher_4, 'a3D_Sketcher_4' )
#geompy.addToStudy( Face_4, 'Face_4' )
geompy.addToStudy( Extrusion_4, 'Extrusion_4' )
 
i = 0
#alpha=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12]
#alpha=[0.134]
alpha=[0.1]
for element in alpha:
    Radius = r0/(1-alpha[i])
    Sphere_1 = geompy.MakeSphereR(Radius)
    Down = geompy.MakeMultiTranslation2D(Sphere_1, OX, L, n, OY, L, n)
    Up = geompy.MakeTranslation(Down, 0, 0, (n-1)*L)
    Up_Down = geompy.MakeMultiTranslation1D(Down, OZ, L, n)
    Cut_1a = geompy.MakeCutList(Translation_1, [Up_Down])
    Cut_1b = geompy.MakeCutList(Translation_2, [Up_Down])
    Cut_2a = geompy.MakeCutList(Translation_3, [Up_Down])
    Cut_2b = geompy.MakeCutList(Translation_4, [Up_Down])
    Cut_3a = geompy.MakeCutList(Extrusion_1, [Up_Down])
    Cut_3b = geompy.MakeCutList(Extrusion_2, [Up_Down])
    Cut_3c = geompy.MakeCutList(Extrusion_4, [Up_Down])
    Middle = geompy.MakeTranslation(Up_Down, L/2, L/2, L/2)
    Pore_1a = geompy.MakeCutList(Cut_1a, [Middle])
    Pore_1b = geompy.MakeCutList(Cut_1b, [Middle])
    Pore_2a = geompy.MakeCutList(Cut_2a, [Middle])
    Pore_2b = geompy.MakeCutList(Cut_2b, [Middle])
    Pore_3a = geompy.MakeCutList(Cut_3a, [Middle])
    Pore_3b = geompy.MakeCutList(Cut_3b, [Middle])
    Pore_3c = geompy.MakeCutList(Cut_3c, [Middle])

    geompy.addToStudy( Sphere_1, 'Sphere_'+str(i+1) )
    geompy.addToStudy( Down, 'Down_'+str(i+1) )
    geompy.addToStudy( Up, 'Up_'+str(i+1) )
    geompy.addToStudy( Up_Down, 'Up_Down_'+str(i+1) )
    geompy.addToStudy( Cut_1a, 'Cut_1a_'+str(i+1) )
    geompy.addToStudy( Cut_1b, 'Cut_1b_'+str(i+1) )
    geompy.addToStudy( Middle, 'Middle_'+str(i+1) )
    geompy.addToStudy( Pore_1a, 'Pore_1a_'+str(i+1) )
    geompy.addToStudy( Pore_1b, 'Pore_1b_'+str(i+1) )
    geompy.addToStudy( Pore_2a, 'Pore_2a_'+str(i+1) )
    geompy.addToStudy( Pore_2b, 'Pore_2b_'+str(i+1) )
    geompy.addToStudy( Pore_3a, 'Pore_3a_'+str(i+1) )
    geompy.addToStudy( Pore_3b, 'Pore_3b_'+str(i+1) )
    geompy.addToStudy( Pore_3c, 'Pore_3c_'+str(i+1) )

    i = i + 1
    if salome.sg.hasDesktop():
        salome.sg.updateObjBrowser(True)
