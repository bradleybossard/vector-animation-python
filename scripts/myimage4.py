#import random
#import numpy as np
import pytweening
import gizeh as gz
import moviepy.editor as mpy

# Width/Height, Duration, framerate
W,H = 400, 400
duration = 3
fps = 25
numBalls = 10
radius = 10.0
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
  y = H / 2
  for i in range(numBalls):
    x = float(i) / numBalls * W
    #newRadius = pytweening.easeInOutSine((duration - t) / duration) * radius
    if (t < duration/2):
    #newRadius = pytweening.easeInOutBounce((duration - t) / duration) * radius
      newRadius = pytweening.easeInOutBounce(2 * t / duration) * radius
    else:
      newRadius = pytweening.easeInOutBounce(1 - (t / duration)) * radius

    ball = gz.circle(r=newRadius, fill=gradient).translate((x, y))
    ball.draw(surface)

  return surface.get_npimage()

init()
clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("gifs/myimage4.gif", fps=fps, opt="OptimizePlus")
