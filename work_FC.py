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
sys.path.insert( 0, r'/home/igoshin/Salome_scripts/WORK')

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
Vertex_1 = geompy.MakeVertex(-0.7071067811865475, -0.7071067811865475, -0.5)
Vertex_2 = geompy.MakeVertex(0.7071067811865475, 0.7071067811865475, 0.5)
Vertex_3 = geompy.MakeVertex(-1, 0, -0.5)
Vertex_4 = geompy.MakeVertex(-0.5, 0, 0)
geomObj_1 = geompy.MakeVertex(0, 0, -0.5)
Box_1 = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Box_2 = geompy.MakeBoxTwoPnt(geomObj_1, Vertex_2)
Rotation_2 = geompy.MakeRotation(Box_2, OZ, 45*math.pi/180.0)
geomObj_2 = geompy.MakeSpherePntR(Vertex_3, 0.4063832075784756)
geomObj_3 = geompy.MakeMultiTranslation2D(geomObj_2, V_1, 0.7071067811865475, 3, V_2, 0.7071067811865475, 3)
Up_Down_1 = geompy.MakeMultiTranslation1D(geomObj_3, OZ, 1, 2)
Cut_1_1 = geompy.MakeCutList(Rotation_1, [Up_Down_1], True)
geomObj_4 = geompy.MakeSpherePntR(Vertex_4, 0.4063832075784756)
Middle_1 = geompy.MakeMultiTranslation2D(geomObj_4, V_1, 0.7071067811865475, 2, V_2, 0.7071067811865475, 2)
Pore_1 = geompy.MakeCutList(Cut_1_1, [Middle_1], True)
Pore_2_1 = geompy.MakeCommonList([Pore_1, Rotation_2], True)
Vertex_5 = geompy.MakeVertex(1, 1, 1)
Line_1 = geompy.MakeLineTwoPnt(O, Vertex_5)
Plane_1 = geompy.MakePlane(Vertex_5, Line_1, 2)
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
geompy.addToStudy( Rotation_2, 'Rotation_2' )
geompy.addToStudy( Up_Down_1, 'Up_Down_1' )
geompy.addToStudy( Cut_1_1, 'Cut_1_1' )
geompy.addToStudy( Middle_1, 'Middle_1' )
geompy.addToStudy( Pore_1, 'Pore_1' )
geompy.addToStudy( Pore_2_1, 'Pore_2_1' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Plane_1, 'Plane_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
