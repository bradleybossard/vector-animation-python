import gizeh as gz
import numpy as np
import moviepy.editor as mpy
from fractions import gcd

rose_radius = 10
num_roses = 0

# Width/Height, Duration, framerate
W,H = 400, 400
D = 3
fps = 25


"""
We will draw several varieties of beautiful mathematical roses, which are
defined by the polar equation r = cos (n*a/d) where r=radius, a=angle, and
d,n are the parameters of the curve. We will trace roses for a few d and n.
http://en.wikipedia.org/wiki/Rose_mathematics
"""
def rose(d, n):
    """ Returns a polyline representing a rose of radius 1 """
    n_cycles = 1.0 * d / gcd(n,d) # <- number of cycles to close the rose
    aa = np.linspace(0, 2 * np.pi * n_cycles, 1000)
    rr = np.cos( n*aa/d)
    points = gz.polar2cart(rr, aa)
    return gz.polyline(points, stroke=[0,0,0], stroke_width=.05)


# Init function
def init():
  return 0

# Draw a single frame based on time t
def make_frame(t):
  surface = gz.Surface(W,H, bg_color=(1,1,1))

  n = 1
  d = 6

  x = W / 2
  y = H / 2

  global num_roses
  num_roses += 1

  for i in range(1, num_roses):
    rose_nd = rose(n, d).scale(i * rose_radius).translate((x,y))
    rose_nd.draw(surface)

  return surface.get_npimage()

init()
clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("gifs/myimage8.gif", fps=fps, opt="OptimizePlus")
