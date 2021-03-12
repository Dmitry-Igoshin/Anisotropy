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
geomObj_4 = geompy.MakeVertex(-0.7071067811865476, 0, 0.25)
geomObj_5 = geompy.MakeVertex(1, 1, 1)

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(0.0000000, 0.0000000, 2.0000000)
sk.addPointsAbsolute(1.0000000, 0.0000000, 1.0000000)
sk.addPointsAbsolute(1.0000000, 1.0000000, 0.0000000)
sk.addPointsAbsolute(0.0000000, 1.0000000, 1.0000000)
sk.addPointsAbsolute(0.0000000, 0.0000000, 2.0000000)
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Extrusion_1 = geompy.MakePrismDXDYDZ(Face_1, 0.5, 0.5, 0.5)
Box_1 = geompy.MakeBoxDXDYDZ(1.414213562373095, 1.414213562373095, 1)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Translation_1 = geompy.MakeTranslation(Rotation_1, 1, 0, 0)
Translation_2 = geompy.MakeTranslation(Translation_1, 0, 0, 0.25)
Box_2 = geompy.MakeBoxDXDYDZ(0.7071067811865476, 0.7071067811865476, 1)
Rotation_2 = geompy.MakeRotation(Box_2, OZ, 45*math.pi/180.0)
Translation_3 = geompy.MakeTranslation(Rotation_2, 1, 0, 0.25)
geomObj_6 = geompy.MakeBoxDXDYDZ(0.7071067811865476, 0.7071067811865476, 0.5)
Rotation_3 = geompy.MakeRotation(geomObj_6, OZ, 45*math.pi/180.0)
Translation_4 = geompy.MakeTranslation(Rotation_3, 1, 0, 0.25)
Sphere_1 = geompy.MakeSphereR(0.5000146673120315)
Down_1 = geompy.MakeMultiTranslation2D(Sphere_1, OX, 1, 3, OY, 1, 3)
Up_Down_1 = geompy.MakeMultiTranslation1D(Down_1, OZ, 1, 3)
Cut_1a_1 = geompy.MakeCutList(Translation_1, [Up_Down_1])
Cut_1b_1 = geompy.MakeCutList(Translation_2, [Up_Down_1])
geomObj_7 = geompy.MakeCutList(Translation_3, [Up_Down_1])
geomObj_8 = geompy.MakeCutList(Translation_4, [Up_Down_1])
geomObj_9 = geompy.MakeCutList(Extrusion_1, [Up_Down_1])
Middle_1 = geompy.MakeTranslation(Up_Down_1, 0.5, 0.5, 0.5)
Pore_1a_1 = geompy.MakeCutList(Cut_1a_1, [Middle_1])
Pore_1b_1 = geompy.MakeCutList(Cut_1b_1, [Middle_1])
Pore_2a_1 = geompy.MakeCutList(geomObj_7, [Middle_1])
Pore_2b_1 = geompy.MakeCutList(geomObj_8, [Middle_1])
Pore_3a_1 = geompy.MakeCutList(geomObj_9, [Middle_1])
Translation_5 = geompy.MakeTranslation(Down_1, 0, 0, 2)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( V_1, 'V_1' )
geompy.addToStudy( V_2, 'V_2' )
geompy.addToStudy( a3D_Sketcher_1, 'a3D_Sketcher_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Translation_2, 'Translation_2' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Rotation_2, 'Rotation_2' )
geompy.addToStudy( Translation_3, 'Translation_3' )
geompy.addToStudy( Rotation_3, 'Rotation_3' )
geompy.addToStudy( Translation_4, 'Translation_4' )
geompy.addToStudy( Sphere_1, 'Sphere_1' )
geompy.addToStudy( Down_1, 'Down_1' )
geompy.addToStudy( Up_Down_1, 'Up_Down_1' )
geompy.addToStudy( Cut_1a_1, 'Cut_1a_1' )
geompy.addToStudy( Cut_1b_1, 'Cut_1b_1' )
geompy.addToStudy( Middle_1, 'Middle_1' )
geompy.addToStudy( Pore_1a_1, 'Pore_1a_1' )
geompy.addToStudy( Pore_1b_1, 'Pore_1b_1' )
geompy.addToStudy( Pore_2a_1, 'Pore_2a_1' )
geompy.addToStudy( Pore_2b_1, 'Pore_2b_1' )
geompy.addToStudy( Pore_3a_1, 'Pore_3a_1' )
geompy.addToStudy( Translation_5, 'Translation_5' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
