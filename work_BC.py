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
Box_1 = geompy.MakeBoxDXDYDZ(1.414213562373095, 1.414213562373095, 1)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
WorkBox = geompy.MakeTranslation(Rotation_1, 1, 0, 0)
Vertex_1 = geompy.MakeVertex(0, 0, 0)
Vertex_2 = geompy.MakeVertex(2, 2, 0)
Vertex_3 = geompy.MakeVertex(2, 2, 2)
Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)
Sphere_1 = geompy.MakeSpherePntR(Vertex_1, 0.4706659803176296)
Down = geompy.MakeMultiTranslation2D(Sphere_1, OX, 1, 3, OY, 1, 3)
Up_Down = geompy.MakeMultiTranslation1D(Down, OZ, 1, 2)
Cut_1 = geompy.MakeCutList(WorkBox, [Up_Down], True)
MiddleLayer = geompy.MakeTranslation(Down, 0.5, 0.5, 0.5)
Pore = geompy.MakeCutList(Cut_1, [MiddleLayer], True)
Vector_1 = geompy.MakeVectorDXDYDZ(0.5, 0.5, 0.5)
Multi_Translation_1 = geompy.MakeMultiTranslation1D(Down, Vector_1, 0.865, 3)
Cut_2 = geompy.MakeCutList(WorkBox, [Multi_Translation_1])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( WorkBox, 'WorkBox' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Sphere_1, 'Sphere_1' )
geompy.addToStudy( Down, 'Down' )
geompy.addToStudy( Up_Down, 'Up_Down' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( MiddleLayer, 'MiddleLayer' )
geompy.addToStudy( Pore, 'Pore' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Multi_Translation_1, 'Multi-Translation_1' )
geompy.addToStudy( Cut_2, 'Cut_2' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
