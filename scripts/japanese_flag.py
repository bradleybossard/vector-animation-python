import gizeh
surface = gizeh.Surface(width=320, height=260) # dimensions in pixel
circle = gizeh.circle (r=40, # radius, in pixels
                       xy= [156, 200], # coordinates of the center
                       fill= (1,0,0)) # 'red' in RGB coordinates
circle.draw( surface ) # draw the circle on the surface
surface.get_npimage() # export as a numpy array (we will use that)
surface.write_to_png("japanese_flag.png") # export as a PNG
