import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 300, 75
D = 2 # duration in seconds
r = 22 # size of the letters / pentagons

gradient= gz.ColorGradient("linear",((0,(0,.5,1)),(1,(0,1,1))),
                           xy1=(0,-r), xy2=(0,r))
polygon = gz.regular_polygon(r, 5, stroke_width=3, fill=gradient)

def make_frame(t):
    surface = gz.Surface(W,H, bg_color=(1,1,1))
    for i, letter in enumerate("GIZEH"):
        angle = max(0,min(1,2*t/D-1.0*i/5))*2*np.pi
        txt = gz.text(letter, "Amiri", 3*r/2, fontweight='bold')
        group = (gz.Group([polygon, txt])
                 .rotate(angle)
                 .translate((W*(i+1)/6,H/2)))
        group.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("example6.gif",fps=20, opt="OptimizePlus")
