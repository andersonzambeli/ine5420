from typing import List
from structs import *
from math import sin, cos, degrees, radians
from numpy import *

def viewport_transformation(point: Point, window_size: List[float]) -> Point:    
    x = (point.x - window_size[0]) / (window_size[2] - window_size[0]) * (570 - 0)
    y = (1 - ((point.y - window_size[1]) / (window_size[3] - window_size[1]))) * (420 - 0)
    colour = point.colour
    return Point(x, y, colour)



def find_center(obj):
    cx = 0
    cy = 0
    if(isinstance(obj, Wireframe)):
        for i in range(0,len(obj.pontos)):
            cx = cx + obj.pontos[i].x
            cy = cy + obj.pontos[i].y
        cx = cx / len(obj.pontos)
        cy = cy / len(obj.pontos)
        return cx, cy
    if(isinstance(obj, Line)):
        cx = (obj.xf + obj.xi)/2
        cy = (obj.yf + obj.yi)/2
        return cx, cy
    
    if(isinstance(obj, Point)):
        cx = obj.x
        cy = obj.y
        return cx, cy

def translation(obj, dx, dy):
    colour = obj.colour
    
    if(isinstance(obj, Wireframe)):
        
        new_obj = Wireframe(colour)
        for i in range(0,len(obj.pontos)):
            x = obj.pontos[i].x * 1 + obj.pontos[i].y * 0 + obj.pontos[i].z * dx
            y = obj.pontos[i].x * 0 + obj.pontos[i].y * 1 + obj.pontos[i].z * dy
            z = obj.pontos[i].x * 0 + obj.pontos[i].y * 0 + obj.pontos[i].z * 1
            p = Point(x,y,colour)
            new_obj.add_ponto(p)
        return new_obj
    
    if(isinstance(obj, Line)):
        xi = obj.xi * 1 + obj.yi * 0 + obj.zi * dx
        xf = obj.xf * 1 + obj.yf * 0 + obj.zf * dx
        yi = obj.xi * 0 + obj.yi * 1 + obj.zi * dy
        yf = obj.xf * 0 + obj.yf * 1 + obj.zf * dy
        zi = obj.xi * 0 + obj.yi * 0 + obj.zi * 1
        zf = obj.xf * 0 + obj.yi * 0 + obj.zf * 1
        pi = Point(xi,yi, colour)
        pf = Point(xf,yf, colour)
        l = Line(pi,pf, colour)
        return l
    
    if(isinstance(obj, Point)):
        x = obj.x * 1 + obj.y * 0 + obj.z * dx
        y = obj.x * 0 + obj.y * 1 + obj.z * dy
        z = obj.x * 0 + obj.y * 0 + obj.z * 1
        p = Point(x, y, colour)
        return p

def rotation(obj, ang):
    colour = obj.colour
    
    ang = radians(ang)
    if(isinstance(obj, Wireframe)):
        new_obj = Wireframe(colour)
        for i in range(0,len(obj.pontos)):
            x = obj.pontos[i].x * cos(ang) + obj.pontos[i].y * -sin(ang) + obj.pontos[i].z * 0
            y = obj.pontos[i].x * sin(ang) + obj.pontos[i].y * cos(ang) + obj.pontos[i].z * 0
            z = obj.pontos[i].x * 0 + obj.pontos[i].y * 0 + obj.pontos[i].z * 1
            p = Point(x,y, colour)
            new_obj.add_ponto(p)
        return new_obj
    
    if(isinstance(obj, Line)):
        xi = obj.xi * cos(ang) + obj.yi * -sin(ang) + obj.zi * 0
        xf = obj.xf * cos(ang) + obj.yf * -sin(ang) + obj.zf * 0
        yi = obj.xi * sin(ang) + obj.yi * cos(ang) + obj.zi * 0
        yf = obj.xf * sin(ang) + obj.yf * cos(ang) + obj.zf * 0
        zi = obj.xi * 0 + obj.yi * 0 + obj.zi * 1
        zf = obj.xf * 0 + obj.yi * 0 + obj.zf * 1
        pi = Point(xi,yi,colour)
        pf = Point(xf,yf,colour)
        print(pi, pf)
        l = Line(pi,pf, colour)
        return l
    
    if(isinstance(obj, Point)):
        x = obj.x * cos(ang) + obj.y * -sin(ang) + obj.z * 0
        y = obj.x * sin(ang) + obj.y * cos(ang) + obj.z * 0
        z = obj.x * 0 + obj.y * 0 + obj.z * 1
        p = Point(x, y, colour)
        return p

def scaling(obj, sx, sy):
    
    colour = obj.colour
    
    if(isinstance(obj, Wireframe)):
        new_obj = Wireframe(colour)
        for i in range(0,len(obj.pontos)):
            
            
            x = obj.pontos[i].x * sx + obj.pontos[i].y * 0 + obj.pontos[i].z * 0
            y = obj.pontos[i].x * 0 + obj.pontos[i].y * sy + obj.pontos[i].z * 0
            z = obj.pontos[i].x * 0 + obj.pontos[i].y * 0 + obj.pontos[i].z * 1
            p = Point(x,y, colour)
            new_obj.add_ponto(p)
        return new_obj
    
    if(isinstance(obj, Line)):
        xi = obj.xi * sx #+ obj.yi * 0 + obj.zi * 0
        xf = obj.xf * sx + obj.yf * 0 + obj.zf * 0
        yi = obj.xi * 0 + obj.yi * sy + obj.zi * 0
        yf = obj.xf * 0 + obj.yf * sy + obj.zf * 0
        zi = obj.xi * 0 + obj.yi * 0 + obj.zi * 1
        zf = obj.xf * 0 + obj.yi * 0 + obj.zf * 1
        pi = Point(xi,yi,colour)
        pf = Point(xf,yf,colour)
        l = Line(pi,pf,colour)
        return l
    
    if(isinstance(obj, Point)):
        x = obj.x * sx + obj.y * 0 + obj.z * 0
        y = obj.x * 0 + obj.sy * 1 + obj.z * 0
        z = obj.x * 0 + obj.y * 0 + obj.z * 1
        p = Point(x, y,colour)
        return p

def self_rotation(obj, ang):

    cx , cy = find_center(obj)
    obj = translation(obj, -cx,-cy)
    obj = rotation(obj, ang)
    obj = translation(obj,cx,cy)
    return obj

def rotation_around_point(obj, ang, p):
    obj = translation(obj,-p.x, -p.y)
    obj = rotation(obj, ang)
    obj = translation(obj, p.x, p.y)
    return obj

def scale(obj, sx, sy):
    cx , cy = find_center(obj)
    obj = translation(obj, -cx,-cy)
    obj = scaling(obj,sx,sy)
    obj = translation(obj,cx,cy)
    return obj