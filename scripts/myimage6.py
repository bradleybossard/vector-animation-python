import numpy as np
import moviepy.editor as mpy
import colorsys
import gizeh as gz

W,H = 256,256
NFACES = 6
R = 0.3
NSQUARES = 6
DURATION = 2

def half(t, side="left"):
    points = gz.geometry.polar_polygon(NFACES, R, NSQUARES)
    #ipoint = 0 if side=="left" else NSQUARES/2
    #points = (points[ipoint:]+points[:ipoint])[::-1]

    #for point in points:
    #  print point

    surface = gz.Surface(W,H)

    centerPoints = []
    for (r, th, d) in points:
        center = W * (0.5 + gz.polar2cart(r, th))
        angle = -(6 * np.pi * d + t * np.pi / DURATION)
        #color= colorsys.hls_to_rgb((2*d+t/DURATION)%1,.5,.5)
        centerPoints.append(center)
        color= (0.9, 0.9, 0.9)
        square = gz.circle(r=4.0, xy= center, fill=color)
        #square = gz.square(l=0.17*W, xy= center, angle=angle,
        #           fill=color, stroke_width= 0.005*W, stroke=(1,1,1))

        square.draw(surface)

    line = gz.polyline(points=centerPoints, stroke_width=1, stroke=(1, 0, 0))
    line.draw(surface)

    im = surface.get_npimage()
    return (im[:,:W/2] if (side=="left") else im[:,W/2:])


def make_frame(t):
    return np.hstack([half(t,"left"),half(t,"right")])

clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("gifs/myimage6.gif",fps=15, opt="OptimizePlus")
