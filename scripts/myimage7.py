import numpy as np
import moviepy.editor as mpy
import colorsys
import gizeh as gz

W,H = 256,256
NFACES = 5
NSQUARES = 6
DURATION = 2

#def polar_polygon(nfaces,radius, npoints):
def polar_ngon_to_cart(nfaces, radius, angle):
    """ Returns the (x,y) coordinates of n points regularly spaced
    along a regular polygon of `nfaces` faces and given radius.
    """
    #theta=np.linspace(0,2*np.pi,npoints)[:-1]
    theta = angle
    cos, pi, n = np.cos, np.pi, nfaces
    r = cos( pi / n ) / cos((theta % (2 * pi/n)) - pi/n)
    #d = np.cumsum(np.sqrt(((r[1:]-r[:-1])**2)))
    #d = [0] + list( d / d.max())
    return gz.polar2cart(radius*r, theta)
    #return zip(radius*r, theta, d)

def make_frame(t):
    surface = gz.Surface(W,H)

    centerPoints = []
    r = W / 2 * 0.8
    for i in range(NFACES*2):
        th = float(i) * ((2 * np.pi) / float(NFACES * 2))
        #center = gz.polar2cart(r, th)
        #center = gz.polar2cart(r, th)
        center = polar_ngon_to_cart(NFACES, r, th)
        print "center",center
        centerPoints.append(center)
        color= (0.9, 0.9, 0.9)
        dot = gz.circle(r=4.0, xy= center, fill=color).translate((W/2, H/2))
        dot.draw(surface)

    line = gz.polyline(points=centerPoints, stroke_width=1, stroke=(1, 0, 0)).translate((W/2, H/2))
    line.draw(surface)

    im = surface.get_npimage()
    return im

clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("gifs/myimage7.gif",fps=15, opt="OptimizePlus")
