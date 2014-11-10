import random
import gizeh as gz
import moviepy.editor as mpy

# Width/Height, Duration, framerate
W,H = 400, 400
D = 3
fps = 25

# Array containing instances of Star class
stars = []
numStars = 50

class Star():
  x = 0.0
  y = 0.0
  vecX = 0.0
  vecY = 0.0

# Initialize stars with position and random sizes/vectors
def init():
  for i in range(numStars):
    star = Star()
    star.x = W / 2;
    star.y = H / 2;
    star.radius = random.uniform(-3, 3)
    star.vecX = random.uniform(-3, 3)
    star.vecY = random.uniform(-3, 3)
    print star.x, star.y, star.vecX, star.vecY
    stars.append(star)

def make_frame(t):

  alpha = 0.8
  surface = gz.Surface(W,H, bg_color=(1,1,1))

  gradient = gz.ColorGradient(type="radial",
                  stops_colors = [(0,(1,0,0, alpha)),(1,(0.1,0,0,alpha))],
                  xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])
  for i in range(numStars):
    star = stars[i]
    star.x += star.vecX;
    star.y += star.vecY;
    ball = gz.circle(r=star.radius, fill=gradient).translate((star.x, star.y))
    ball.draw(surface)
  return surface.get_npimage()

init()
clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("gifs/myimage3.gif", fps=fps, opt="OptimizePlus")
