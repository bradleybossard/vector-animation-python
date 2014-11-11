import random
import gizeh as gz
import moviepy.editor as mpy

# Width/Height, Duration, framerate
W,H = 400, 400
D = 3
fps = 25
rects = []
numRects = 20

class Rect():
  height = 0.0

# Init function
def init():
  for i in range(numRects):
    rect = Rect()
    rect.height = random.uniform(0, H * 0.8)
    rects.append(rect)
  return 0

# Draw a single frame based on time t
def make_frame(t):
  surface = gz.Surface(W,H, bg_color=(1,1,1))
  #rect = gizeh.rectangle(lx=60.3, ly=45, xy=(60,70), fill=(0,1,0), angle=Pi/8)
  for i in range(numRects):
    rect = rects[i]
    x = i * 15.0
    #y = H - rect.height
    y = H
    #y = 40
    #rectShape = gz.rectangle(lx=10.0, ly=rect.height, xy=(x, y), fill=(0,1,0), angle=0)
    rectShape = gz.rectangle(lx=10.0, ly=rect.height, fill=(0,1,0), angle=0).translate((x,y))
    rectShape.draw(surface)

  return surface.get_npimage()

init()
clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("gifs/myimage5.gif", fps=fps, opt="OptimizePlus")
