import math
import numpy as np
import gizeh
import moviepy.editor as mpy

#W,H = 128,128 # width, height, in pixels
W,H = 200,200 # width, height, in pixels
duration = 2 # duration of the clip, in seconds
radius1 = W / 2 - 10
radius2 = radius1 - 2
radius3 = 4


def supersample(clip, d, nframes):
    """ Replaces each frame at time t by the mean of `nframes` equally spaced frames
        taken in the interval [t-d, t+d]. This results in motion blur."""
    def fl(gf, t):
        tt = np.linspace(t-d, t+d, nframes)
        avg = np.mean(1.0*np.array([gf(t_) for t_ in tt]),axis=0)
        return avg.astype("uint8")
    return clip.fl(fl)

def make_frame(t):
    colorDiv = t + 0.01
    color1= [1.0 / colorDiv, 0.0, 0.0]
    color2 = [0.0, 1.0 / colorDiv, 0.0]

    angle = (duration - t)/duration * 360
    radians = math.radians(angle)
    cosR = math.cos(radians)
    sinR = math.sin(radians)
    gradient= gizeh.ColorGradient("linear",((0,(0,.5,1)),(1,(0,1,1))), xy1=(-cosR,-sinR), xy2=(cosR,sinR))
    #gradient=color2

    gradRad1 = radius1 - 20
    gradRad2 = radius1 + 20
    gradient = gizeh.ColorGradient(type="radial",
                                   stops_colors = [(0,color1),(1,color2)],
                                   #xy1=[0.2,-0.2], xy2=[0.1,0.0], xy3 = [0.0,0.99])
                                   xy1=[0.0,0.0], xy2=[gradRad1,0.0], xy3 = [0.0,gradRad2])
    surface = gizeh.Surface(W,H)

    #circle1 = gizeh.circle(r=1, xy = (0, 0), stroke=gradient, stroke_width=0.3).scale(50.0).translate(xy=(W/2, H/2))
    #circle1 = gizeh.circle(radius1, xy = (W/2, H/2), fill=gradient)
    circle1 = gizeh.circle(radius1, xy = (W/2, H/2), stroke=gradient, stroke_width=5)
    circle1.draw(surface)

    #circle4 = gizeh.circle(r=1, xy = (W/2,H/2), fill=color1)
    #circle4.draw(surface)

    # Orbiting planet
    circle3 = gizeh.circle(radius3, xy = (W/2 + cosR * radius1, H/2 + sinR * radius1), fill=(1,0,1))
    circle3.draw(surface)

    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
#clip.write_gif('myimage1.gif',fps=15, opt="OptimizePlus", fuzz=10)
#clip.write_gif('myimage1.gif',fps=15, opt="OptimizePlus")
clip.write_gif('myimage1.gif',fps=15)

#new_clip = supersample(clip, d=0.05, nframes=5)
#new_clip.write_gif('myimage1.gif',fps=15, opt="OptimizePlus", fuzz=10)
