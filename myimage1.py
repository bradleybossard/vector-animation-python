import math
import numpy as np
import gizeh
import moviepy.editor as mpy

W,H = 128,128 # width, height, in pixels
duration = 2 # duration of the clip, in seconds
radius1 = W / 2 - 10
radius2 = radius1 - 2
radius3 = 4
r = 3

def supersample(clip, d, nframes):
    """ Replaces each frame at time t by the mean of `nframes` equally spaced frames
        taken in the interval [t-d, t+d]. This results in motion blur."""
    def fl(gf, t):
        tt = np.linspace(t-d, t+d, nframes)
        avg = np.mean(1.0*np.array([gf(t_) for t_ in tt]),axis=0)
        return avg.astype("uint8")
    return clip.fl(fl)

def make_frame(t):
    gradient= gizeh.ColorGradient("linear",((0,(0,.5,1)),(1,(0,1,1))),
                               xy1=(0,-r), xy2=(0,r))
    surface = gizeh.Surface(W,H)
    #circle1 = gizeh.circle(radius1, xy = (W/2,H/2), fill=(1,0,0))
    circle1 = gizeh.circle(radius1, xy = (W/2,H/2), stroke=gradient, stroke_width=2)
    circle1.draw(surface)
    #circle2 = gizeh.circle(radius2, xy = (W/2,H/2), fill=(0,0,0))
    #circle2.draw(surface)
    angle = (duration - t)/duration * 360
    radians = math.radians(angle)

    # Orbiting planet
    circle3 = gizeh.circle(radius3, xy = (W/2 + math.cos(radians) * radius1, H/2 + math.sin(radians) * radius1), fill=(1,0,1))
    circle3.draw(surface)

    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif('myimage1.gif',fps=15, opt="OptimizePlus", fuzz=10)

#new_clip = supersample(clip, d=0.05, nframes=5)
#new_clip.write_gif('myimage1.gif',fps=15, opt="OptimizePlus", fuzz=10)
