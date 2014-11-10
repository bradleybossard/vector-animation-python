import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 256, 256
DURATION = 2.0
NDISKS_PER_CYCLE = 8
SPEED = .05

def make_frame(t):

    dt = 1.0*DURATION/2/NDISKS_PER_CYCLE # delay between disks
    N = int(NDISKS_PER_CYCLE/SPEED) # total number of disks
    t0 = 1.0/SPEED # indicates at which avancement to start

    surface = gz.Surface(W,H)
    for i in range(1,N):
        a = (np.pi/NDISKS_PER_CYCLE)*(N-i-1)
        r = np.maximum(0, .05*(t+t0-dt*(N-i-1)))
        center = W*(0.5+ gz.polar2cart(r,a))
        color = 3*((1.0*i/NDISKS_PER_CYCLE) % 1.0,)
        circle = gz.circle(r=0.3*W, xy = center,fill = color,
                              stroke_width=0.01*W)
        circle.draw(surface)
    contour1 = gz.circle(r=.65*W,xy=[W/2,W/2], stroke_width=.5*W)
    contour2 = gz.circle(r=.42*W,xy=[W/2,W/2], stroke_width=.02*W,
                            stroke=(1,1,1))
    contour1.draw(surface)
    contour2.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("example5.gif",fps=20, opt="OptimizePlus", fuzz=10)
