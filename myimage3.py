import gizeh as gz
import moviepy.editor as mpy


W,H = 200,75
D = 3
fps = 25

stars = []

"""
def make_ball(t, alpha):

    gradient = gz.ColorGradient(type="radial",
                    stops_colors = [(0,(1,0,0, 0.8)),(1,(0.1,0,0,alpha))],
                    xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])
    x = (-W/3)+(5*W/3)*(t/D)
    y = ground - HJ*4*(x % DJ)*(DJ-(x % DJ))/DJ**2
    coef = (HJ-y)/HJ

    return ball
"""

def make_frame(t):
    alpha = 0.8
    radius = 10.0
    surface = gz.Surface(W,H, bg_color=(1,1,1))
    """
    #spacer = 3.0 / num_balls
    spacer = 1.0 / fps
    alpha_dec = 1.0 / num_balls
    for i in range(num_balls):
      tracer_t = t - (i * spacer)
      alpha = 1.0 - (i * alpha_dec)
      print "  " + str(alpha)
      #tracer_ball = make_bawll(tracer_t, 1.0 - spacer)
      tracer_ball = make_ball(tracer_t, alpha)
      tracer_ball.draw(surface)


    ball = make_ball(t, 1.0)
    ball.draw(surface)
    #shadow = make_shadow(t)
    #shadow.draw(surface)
    """

    gradient = gz.ColorGradient(type="radial",
                    stops_colors = [(0,(1,0,0, alpha)),(1,(0.1,0,0,alpha))],
                    xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])
    #ball = gz.circle(r=1, fill=gradient).scale(r).translate((x,y))
    ball = gz.circle(r=radius, fill=gradient).translate((W/2, H/2))
    ball.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("myimage3.gif", fps=fps, opt="OptimizePlus")
