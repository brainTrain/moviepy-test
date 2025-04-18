from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip

def create_sample_video():
    # Create a simple text clip with monospace font for better width control
    text_clip = TextClip("Yooo Vitor!!1 \\o/", fontsize=70, color='white', font='Courier')
    text_clip = text_clip.set_duration(5)  # 5 seconds duration
    
    # Create a wider background color clip (increased width from 640 to 1280)
    color_clip = ColorClip(size=(1280, 480), color=(0, 0, 255))
    color_clip = color_clip.set_duration(5)
    
    # Combine the clips
    video = CompositeVideoClip([color_clip, text_clip.set_position('center')])
    
    # Write the result to a file
    video.write_videofile("output.mp4", fps=24)

if __name__ == "__main__":
    create_sample_video() 