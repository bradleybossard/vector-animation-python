import math
import gizeh
import moviepy.editor as mpy

W,H = 128,128 # width, height, in pixels
duration = 2 # duration of the clip, in seconds
radius1 = W / 2 - 10
radius2 = radius1 - 2
radius3 = 4

def make_frame(t):
    surface = gizeh.Surface(W,H)
    circle1 = gizeh.circle(radius1, xy = (W/2,H/2), fill=(1,0,0))
    circle1.draw(surface)
    circle2 = gizeh.circle(radius2, xy = (W/2,H/2), fill=(0,0,0))
    circle2.draw(surface)
    angle = (duration - t)/duration * 360
    radians = math.radians(angle)

    # Orbiting planet
    circle3 = gizeh.circle(radius3, xy = (W/2 + math.cos(radians) * radius1, H/2 + math.sin(radians) * radius1), fill=(1,0,1))
    circle3.draw(surface)

    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif('myimage1.gif',fps=15, opt="OptimizePlus", fuzz=10)
