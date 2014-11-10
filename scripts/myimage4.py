import random
import gizeh as gz
import moviepy.editor as mpy

# Width/Height, Duration, framerate
W,H = 400, 400
D = 3
fps = 25

# Init function
def init():
  return 0

# Draw a single frame based on time t
def make_frame(t):
  surface = gz.Surface(W,H, bg_color=(1,1,1))

  return surface.get_npimage()

init()
clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("gifs/myimage.gif", fps=fps, opt="OptimizePlus")
