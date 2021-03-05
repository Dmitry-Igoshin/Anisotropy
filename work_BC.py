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
geomObj_1 = geompy.MakeVertex(-0.7071067811865476, -0.7071067811865476, 0)
geomObj_2 = geompy.MakeVertex(0.7071067811865476, 0.7071067811865476, 1)
geomObj_3 = geompy.MakeVertex(-1.414213562373095, 0, 0)
geomObj_4 = geompy.MakeVertex(-0.7071067811865476, 0, 0.5)
geomObj_5 = geompy.MakeVertex(1, 1, 1)

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(-0.7071068, -0.7071068, 0.5000000)
sk.addPointsAbsolute(0.0000000, -0.7071068, 0.0000000)
sk.addPointsAbsolute(0.0000000, 0.0000000, -0.5000000)
sk.addPointsAbsolute(-0.7071068, 0.0000000, 0.0000000)
sk.addPointsAbsolute(-0.7071068, -0.7071068, 0.5000000)
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Face_2 = geompy.MakeTranslation(Face_1, 0.7071067811865476, 0.7071067811865476, 0)
Rhombohedron = geompy.MakeHexa2Faces(Face_1, Face_2)
Box_1 = geompy.MakeBoxTwoPnt(geomObj_1, geomObj_2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Box_2 = geompy.MakeBoxTwoPnt(O, geomObj_5)
Rotation_2_ = geompy.MakeRotation(Box_2, OZ, 45*math.pi/180.0)
Sphere_1 = geompy.MakeSpherePntR(geomObj_3, 0.4811252243246881)
Down_1 = geompy.MakeMultiTranslation2D(Sphere_1, V_1, 1, 3, V_2, 1, 3)
Up_Down_1 = geompy.MakeMultiTranslation1D(Down_1, OZ, 1, 2)
Cut_1_1 = geompy.MakeCutList(Box_1, [Up_Down_1], True)
geomObj_6 = geompy.MakeSpherePntR(geomObj_4, 0.4811252243246881)
Middle_1 = geompy.MakeMultiTranslation2D(geomObj_6, V_1, 1, 2, V_2, 1, 2)
Pore_1 = geompy.MakeCutList(Cut_1_1, [Middle_1], True)
geomObj_7 = geompy.MakeCommonList([Up_Down_1, Middle_1, Rotation_2_], True)
geomObj_8 = geompy.MakeCommonList([Rhombohedron, Pore_1], True)
Translation_1 = geompy.MakeTranslation(Rotation_2_, 0, 0, 0.25)
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
geompy.addToStudy( Sphere_1, 'Sphere_1' )
geompy.addToStudy( Down_1, 'Down_1' )
geompy.addToStudy( Up_Down_1, 'Up_Down_1' )
geompy.addToStudy( Cut_1_1, 'Cut_1_1' )
geompy.addToStudy( Middle_1, 'Middle_1' )
geompy.addToStudy( Pore_1, 'Pore_1' )
geompy.addToStudy( Translation_1, 'Translation_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
