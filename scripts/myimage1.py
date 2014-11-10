import math
import random
import numpy as np
import pytweening
import gizeh
import moviepy.editor as mpy

#W,H = 128,128 # width, height, in pixels
W,H = 200,200 # width, height, in pixels
duration = 2 # duration of the clip, in seconds
radius1 = W / 2 - 10
radius3 = 4

# Array containing instances of Star class
particles = []
numParticles = 10

class Particle():
  x = 0.0
  y = 0.0
  radius = 0
  #vecX = 0.0
  #vecY = 0.0


def supersample(clip, d, nframes):
    """ Replaces each frame at time t by the mean of `nframes` equally spaced frames
        taken in the interval [t-d, t+d]. This results in motion blur."""
    def fl(gf, t):
        tt = np.linspace(t-d, t+d, nframes)
        avg = np.mean(1.0*np.array([gf(t_) for t_ in tt]),axis=0)
        return avg.astype("uint8")
    return clip.fl(fl)

# Initialize particles
def init():
  for i in range(numParticles):
    particle = Particle()
    particle.direction = random.choice([-1, 1])
    particle.radius = random.uniform(0.1, 2.5)
    particle.orbit_radius = random.uniform(1, H/2)
    particle.color = [random.random(), random.random(), random.random()]
    particle.easing = random.choice([1, 2, 3])
    particles.append(particle)


def make_frame(t):
    #colorDiv = t + 0.01
    #color1= [1.0 / colorDiv, 0.0, 0.0]
    #color2 = [0.0, 1.0 / colorDiv, 0.0]

    #gradient= gizeh.ColorGradient("linear",((0,(0,.5,1)),(1,(0,1,1))), xy1=(-cosR,-sinR), xy2=(cosR,sinR))

    #gradRad1 = radius1 - 20
    #gradRad2 = radius1 + 20
    #gradient = gizeh.ColorGradient(type="radial",
    #                               stops_colors = [(0,color1),(1,color2)],
    #                               xy1=[0.0,0.0], xy2=[gradRad1,0.0], xy3 = [0.0,gradRad2])
    surface = gizeh.Surface(W,H)

    # orbit halo
    #circle1 = gizeh.circle(radius1, xy = (W/2, H/2), stroke=gradient, stroke_width=5)
    #circle1.draw(surface)

    for i in range(numParticles):
      # Orbiting planet
      particle = particles[i]

      if (particle.easing == 1):
        angle = pytweening.linear((duration - t) / duration) * 360 * particle.direction
      elif (particle.easing == 2):
        angle = pytweening.easeInQuad((duration - t) / duration) * 360 * particle.direction
      elif (particle.easing == 3):
        angle = pytweening.easeOutQuad((duration - t) / duration) * 360 * particle.direction
      elif (particle.easing == 4):
        angle = pytweening.easeInOutQuad((duration - t) / duration) * 360 * particle.direction
      elif (particle.easing == 5):
        angle = pytweening.easeInSine((duration - t) / duration) * 360 * particle.direction
      elif (particle.easing == 6):
        angle = pytweening.easeOutSine((duration - t) / duration) * 360 * particle.direction
      elif (particle.easing == 7):
        angle = pytweening.easeInOutSine((duration - t) / duration) * 360 * particle.direction
      radians = math.radians(angle)
      cosR = math.cos(radians)
      sinR = math.sin(radians)
      x = W/2 + cosR * particle.orbit_radius
      y = H/2 + sinR * particle.orbit_radius
      fill = particle.color
      #circle = gizeh.circle(particle.radius, xy = (x, y), fill=(1,0,1))
      circle = gizeh.circle(particle.radius, xy = (x, y), fill=fill)
      circle.draw(surface)

    return surface.get_npimage()

init()
clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif('myimage1.gif',fps=15)

#new_clip = supersample(clip, d=0.05, nframes=5)
#new_clip.write_gif('myimage1.gif',fps=15, opt="OptimizePlus", fuzz=10)
