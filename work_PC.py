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
Box_1 = geompy.MakeBoxDXDYDZ(2.82842712474619, 2.82842712474619, 2)
Rotation_1 = geompy.MakeRotation(Box_1, OZ, 45*math.pi/180.0)
Translation_2 = geompy.MakeTranslation(Rotation_1, 2, 0, 0)
Vertex_1 = geompy.MakeVertex(2, 0, 0)
Vertex_2 = geompy.MakeVertex(2, 2, 0)
Vertex_3 = geompy.MakeVertex(2, 2, 2)
Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(0.0000000, 0.0000000, 4.0000000)
sk.addPointsAbsolute(2.0000000, 0.0000000, 2.0000000)
sk.addPointsAbsolute(2.0000000, 2.0000000, 0.0000000)
sk.addPointsAbsolute(0.0000000, 2.0000000, 2.0000000)
sk.addPointsAbsolute(0.0000000, 0.0000000, 4.0000000)
a3D_Sketcher_1 = sk.wire()
Face_1 = geompy.MakeFaceWires([a3D_Sketcher_1], 1)
Vector_1 = geompy.MakeVectorDXDYDZ(2, 2, 0)
Extrusion_1 = geompy.MakePrismVecH(Face_1, Vector_1, 2.82842712474619)
Sphere_ = geompy.MakeSphereR(1.111111111111111)
Multi_Translation_21 = geompy.MakeMultiTranslation2D(Sphere_, OX, 2, 3, OY, 2, 3)
Multi_Translation_31 = geompy.MakeMultiTranslation1D(Multi_Translation_21, OZ, 2, 3)
Pore2_1 = geompy.MakeCutList(Translation_2, [Multi_Translation_31])
Cut_1 = geompy.MakeCutList(Extrusion_1, [Multi_Translation_31])
Cut_1.SetColor(SALOMEDS.Color(0,0,1))
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Translation_2, 'Translation_2' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( a3D_Sketcher_1, 'a3D_Sketcher_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Sphere_, 'Sphere_' )
geompy.addToStudy( Multi_Translation_21, 'Multi-Translation_21' )
geompy.addToStudy( Multi_Translation_31, 'Multi-Translation_31' )
geompy.addToStudy( Pore2_1, 'Pore2_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
