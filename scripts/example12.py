import gizeh as gz
import moviepy.editor as mpy
import numpy as np

def add_zoom(clip, target_center, zoom_center, zoom_radius, zoomx):

    w, h = clip.size

    def fl(im):
        """ transforms the image by adding a zoom """

        surface = gz.Surface.from_image(im)
        fill = gz.ImagePattern(im, pixel_zero=target_center,
                               filter='best')
        line = gz.polyline([target_center, zoom_center],
                           stroke_width=3)
        circle_target= gz.circle(zoom_radius, xy=target_center,
                                 fill=fill, stroke_width=2)
        circle_zoom = gz.circle(zoom_radius, xy=zoom_center, fill=fill,
                       stroke_width=2).scale(zoomx, center=zoom_center)
        for e in line, circle_zoom, circle_target:
            e.draw(surface)
        return surface.get_npimage()

    return clip.fl_image(fl)


clip = mpy.VideoFileClip("example10.gif")
w, h = clip.size
clip_with_zoom = clip.fx(add_zoom, target_center = [w/2, h/3], zoomx=3,
                   zoom_center = [5*w/6, h/4], zoom_radius=15)
clip_with_zoom.write_gif("gifs/example12.gif")
