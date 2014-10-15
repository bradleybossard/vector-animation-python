import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 200,75
D = 3
r = 10 # radius of the ball
DJ, HJ = 50, 35 # distance and height of the jumps
ground = 0.75*H # y-coordinate of the ground


gradient = gz.ColorGradient(type="radial",
                stops_colors = [(0,(1,0,0)),(1,(0.1,0,0))],
                xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])

def make_frame(t):
    surface = gz.Surface(W,H, bg_color=(1,1,1))
    x = (-W/3)+(5*W/3)*(t/D)
    y = ground - HJ*4*(x % DJ)*(DJ-(x % DJ))/DJ**2
    coef = (HJ-y)/HJ
    shadow_gradient = gz.ColorGradient(type="radial",
                stops_colors = [(0,(0,0,0,.2-coef/5)),(1,(0,0,0,0))],
                xy1=[0,0], xy2=[0,0], xy3 = [0,1.4])
    shadow = (gz.circle(r=(1-coef/4), fill=shadow_gradient)
               .scale(r,r/2).translate((x,ground+r/2)))
    shadow.draw(surface)
    ball = gz.circle(r=1, fill=gradient).scale(r).translate((x,y))
    ball.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("example4.gif",fps=25, opt="OptimizePlus")
