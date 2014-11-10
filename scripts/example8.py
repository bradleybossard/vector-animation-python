import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 256,256
R=1.0*W/3
D = 4
yingyang = gz.Group( [
      gz.arc(R,0,np.pi, fill=(0,0,0)),
      gz.arc(R,-np.pi,0, fill=(1,1,1)),
      gz.circle(R/2,xy=(-R/2,0), fill=(0,0,0)),
      gz.circle(R/2,xy=(R/2,0), fill=(1,1,1))])

fractal = yingyang
for i in range(5):
    fractal = gz.Group([yingyang,
                fractal.rotate(np.pi).scale(0.25).translate([R/2,0]),
                fractal.scale(0.25).translate([-R/2,0]),
                gz.circle(0.26*R, xy=(-R/2,0),
                    stroke=(1,1,1), stroke_width=1),
                gz.circle(0.26*R, xy=(R/2,0),
                    stroke=(0,0,0), stroke_width=1)])

# Go one level deep into the fractal
fractal = fractal.translate([(R/2),0]).scale(4)

def make_frame(t):
    surface = gz.Surface(W,H)
    G = 2**(2*(t/D)) # zoom coefficient
    (fractal.translate([R*2*(1-1.0/G)/3,0]).scale(G) # zoom
     .translate(W/2+gz.polar2cart(W/12,2*np.pi*t/D)) # spiral effect
     .draw(surface))
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("gifs/example8.gif",fps=15, fuzz=30, opt="OptimizePlus")
