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
sys.path.insert( 0, r'/home/igoshin/Anisotropy')

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
geomObj_1 = geompy.MakeVertex(-0.7071067811865475, -0.7071067811865475, -0.5)
geomObj_2 = geompy.MakeVertex(0.7071067811865475, 0.7071067811865475, 0.5)
geomObj_3 = geompy.MakeVertex(-1, 0, -0.5)
geomObj_4 = geompy.MakeVertex(-0.5, 0, 0)
geomObj_5 = geompy.MakeVertex(0, 0, -0.5)

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(-0.5000000, -0.5000000, 0.5000000)
sk.addPointsAbsolute(0.0000000, -0.5000000, 0.0000000)
sk.addPointsAbsolute(0.0000000, 0.0000000, -0.5000000)
sk.addPointsAbsolute(-0.5000000, 0.0000000, 0.0000000)
sk.addPointsAbsolute(-0.5000000, -0.5000000, 0.5000000)
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Face_2 = geompy.MakeTranslation(Face_1, 0.5, 0.5, 0)
Rhombohedron = geompy.MakeHexa2Faces(Face_1, Face_2)
Box_1 = geompy.MakeBoxTwoPnt(geomObj_1, geomObj_2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Box_2 = geompy.MakeBoxTwoPnt(geomObj_5, geomObj_2)
Rotation_2_ = geompy.MakeRotation(Box_2, OZ, 45*math.pi/180.0)
geomObj_6 = geompy.MakeSpherePntR(geomObj_3, 0.3721614637823935)
geomObj_7 = geompy.MakeMultiTranslation2D(geomObj_6, V_1, 0.7071067811865475, 3, V_2, 0.7071067811865475, 3)
geomObj_8 = geompy.MakeMultiTranslation1D(geomObj_7, OZ, 1, 2)
geomObj_9 = geompy.MakeCutList(Rotation_1, [geomObj_8], True)
geomObj_10 = geompy.MakeSpherePntR(geomObj_4, 0.3721614637823935)
geomObj_11 = geompy.MakeMultiTranslation2D(geomObj_10, V_1, 0.7071067811865475, 2, V_2, 0.7071067811865475, 2)
Pore_1 = geompy.MakeCutList(geomObj_9, [geomObj_11], True)
Pore_2_1 = geompy.MakeCommonList([Pore_1, Rotation_2_], True)
Pore_3_1 = geompy.MakeCommonList([Rhombohedron, Pore_1], True)
geomObj_12 = geompy.MakeSpherePntR(geomObj_3, 0.3928371006591931)
geomObj_13 = geompy.MakeMultiTranslation2D(geomObj_12, V_1, 0.7071067811865475, 3, V_2, 0.7071067811865475, 3)
geomObj_14 = geompy.MakeMultiTranslation1D(geomObj_13, OZ, 1, 2)
geomObj_15 = geompy.MakeCutList(Rotation_1, [geomObj_14], True)
geomObj_16 = geompy.MakeSpherePntR(geomObj_4, 0.3928371006591931)
geomObj_17 = geompy.MakeMultiTranslation2D(geomObj_16, V_1, 0.7071067811865475, 2, V_2, 0.7071067811865475, 2)
Pore_2 = geompy.MakeCutList(geomObj_15, [geomObj_17], True)
Pore_2_2 = geompy.MakeCommonList([Pore_2, Rotation_2_], True)
Pore_3_2 = geompy.MakeCommonList([Rhombohedron, Pore_2], True)
Cut_1 = geompy.MakeCutList(Pore_3_1, [Pore_2_1], True)
Rhombohedron.SetColor(SALOMEDS.Color(0,0,0))
Rotation_2_.SetColor(SALOMEDS.Color(0,0,0))
Pore_2_1.SetColor(SALOMEDS.Color(0.333333,0.333333,0))
Pore_3_1.SetColor(SALOMEDS.Color(0,0.333333,1))
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( V_1, 'V_1' )
geompy.addToStudy( V_2, 'V_2' )
geompy.addToStudy( a3D_Sketcher_1, 'a3D_Sketcher_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Rhombohedron, 'Rhombohedron' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Rotation_2_, 'Rotation_2_' )
geompy.addToStudy( Pore_1, 'Pore_1' )
geompy.addToStudy( Pore_2_1, 'Pore_2_1' )
geompy.addToStudy( Pore_3_1, 'Pore_3_1' )
geompy.addToStudy( Pore_2, 'Pore_2' )
geompy.addToStudy( Pore_2_2, 'Pore_2_2' )
geompy.addToStudy( Pore_3_2, 'Pore_3_2' )
geompy.addToStudy( Cut_1, 'Cut_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
