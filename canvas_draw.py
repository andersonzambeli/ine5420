from cProfile import label
import sys
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from structs import *
from transforms import viewport_transformation

def draw_point(scene, p, window_size):
    pen = QtGui.QPen()
    pen.setWidth(1)

    p_vp = viewport_transformation(p, window_size)    
    scene.addLine(p_vp.x,p_vp.y,p_vp.x,p_vp.y, pen)

    scene.update()

def draw_line(scene, line, window_size):
    
    pen = QtGui.QPen()
    pen.setWidth(1)
    pi = Point(line.xi, line.yi)
    pf = Point(line.xf, line.yf)
    pi_vp = viewport_transformation(pi, window_size)
    pf_vp= viewport_transformation(pf, window_size)

    
    scene.addLine(pi_vp.x,pi_vp.y,pf_vp.x,pf_vp.y, pen)   
    scene.update()

def draw_wireframe(scene, wireframe, window_size):
    
    pen = QtGui.QPen()
    pen.setWidth(1)
    wireframe_vp = Wireframe()

    for j in range(0, len(wireframe.pontos)):
        p = wireframe.pontos[j]
        p = viewport_transformation(p, window_size)
        wireframe_vp.add_ponto(p)

    for j in range(0, len(wireframe_vp.pontos)):
                
                if(j == 0):                                    
                    scene.addLine(wireframe_vp.pontos[j].x,wireframe_vp.pontos[j].y,wireframe_vp.pontos[j].x,wireframe_vp.pontos[j].y, pen)
                else:
                    scene.addLine(wireframe_vp.pontos[j - 1].x,wireframe_vp.pontos[j - 1].y,wireframe_vp.pontos[j].x,wireframe_vp.pontos[j].y, pen)
    scene.update()

def draw_objects(scene, objs, window_size):
    pen = QtGui.QPen()
    pen.setWidth(3)
    for i in range(0, len(objs)):

        if(isinstance(objs[i][1], Wireframe)):
            
            wireframe_vp = Wireframe(QtGui.QColor(objs[i][1].colour))
            pen.setColor(QtGui.QColor(objs[i][1].colour))
            for j in range(0, len(objs[i][1].pontos)):
                p = objs[i][1].pontos[j]
                p = viewport_transformation(p, window_size)
                wireframe_vp.add_ponto(p)

            for j in range(0, len(wireframe_vp.pontos)):
                
                if(j == 0):                                    
                    scene.addLine(wireframe_vp.pontos[j].x,wireframe_vp.pontos[j].y,wireframe_vp.pontos[j].x,wireframe_vp.pontos[j].y, pen)
                else:
                    scene.addLine(wireframe_vp.pontos[j - 1].x,wireframe_vp.pontos[j - 1].y,wireframe_vp.pontos[j].x,wireframe_vp.pontos[j].y, pen)
        
        if(isinstance(objs[i][1], Line)):
            
            pen.setColor(QtGui.QColor(objs[i][1].colour))
            pi = Point(objs[i][1].xi, objs[i][1].yi, QtGui.QColor(objs[i][1].colour))
            pf = Point(objs[i][1].xf, objs[i][1].yf, QtGui.QColor(objs[i][1].colour))
            pi_vp = viewport_transformation(pi, window_size)
            pf_vp = viewport_transformation(pf, window_size)

    
            scene.addLine(pi_vp.x,pi_vp.y,pf_vp.x,pf_vp.y, pen)        
    
        if(isinstance(objs[i][1], Point)):
            pen.setColor(QtGui.QColor(objs[i][1].colour))
            p_vp = viewport_transformation(objs[i][1], window_size)
            scene.addLine(p_vp.x, p_vp.y, p_vp.x, p_vp.y, pen)
    scene.update()
