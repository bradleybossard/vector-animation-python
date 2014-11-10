import moviepy.editor as mpy
import numpy as np
import gizeh as gz

clip = mpy.VideoFileClip("example10.gif")
(w, h), d = clip.size, clip.duration
center=  np.array([w/2, h/2])

def my_filter(get_frame, t):
    """ Transforms a frame (given by get_frame(t)) into a different
    frame, using vector graphics."""

    surface = gz.Surface(w,h)
    fill = (gz.ImagePattern(get_frame(t), pixel_zero=center)
            .scale(1.5, center=center))
    for (nfaces,angle,f) in ([3, 0, 1.0/6],
                              [5, np.pi/3, 3.0/6],
                              [7, 2*np.pi/3, 5.0/6]):
        xy = (f*w, h*(.5+ .05*np.sin(2*np.pi*(t/d+f))))
        shape = gz.regular_polygon(w/6,nfaces, xy = xy,
                fill=fill.rotate(angle, center))
        shape.draw(surface)
    return surface.get_npimage()

clip.fl(my_filter).write_gif("gifs/example11.gif")
