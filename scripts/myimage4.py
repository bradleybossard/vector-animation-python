#import random
import numpy as np
import pytweening
import gizeh as gz
import moviepy.editor as mpy

# Width/Height, Duration, framerate
W,H = 400, 400
duration = 3
fps = 25
numBalls = 10
radius = 10.0
circleRadius = 30.0
alpha = 1.0

# Init function
def init():
  return 0

# Draw a single frame based on time t
def make_frame(t):
  surface = gz.Surface(W,H, bg_color=(1,1,1))

  gradient = gz.ColorGradient(type="radial",
                  stops_colors = [(0,(1,0,0, alpha)),(1,(0.9,0,0,alpha))],
                  xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])
  for i in range(numBalls):
    if (t < duration/2):
      newRadius = pytweening.easeInOutBounce(2 * t / duration) * radius
      newCircleRadius = pytweening.easeInOutBounce(2 * t / duration) * circleRadius
    else:
      newRadius = pytweening.easeInOutBounce(1 - (t / duration)) * radius
      newCircleRadius = pytweening.easeInOutBounce(1 - (t / duration)) * circleRadius

    angle = (2 * np.pi / numBalls) * i
    #center = (W/2) + gz.polar2cart(newCircleRadius, angle)
    center = (W/2) + gz.polar2cart(circleRadius, angle)

    #ball = gz.circle(r=newRadius, fill=gradient).translate((x, y))
    ball = gz.circle(r=newRadius, fill=gradient).translate(center)
    ball.draw(surface)

  return surface.get_npimage()

init()
clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("gifs/myimage4.gif", fps=fps, opt="OptimizePlus")
