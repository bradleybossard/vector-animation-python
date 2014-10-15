from moviepy.editor import VideoFileClip
import moviepy.video.tools.cuts as cuts
import moviepy.editor as mpy

clip = mpy.VideoFileClip("bunny.mp4").resize(0.2).subclip((4,32),(4,33))
# error, can
t_loop = cuts.find_video_period(clip) # gives t=0.56
clip.subclip(0,t_loop).write_gif('example10.gif')
