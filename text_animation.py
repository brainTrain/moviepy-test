from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

def create_text_animation():
    # Background settings
    width, height = 1280, 720
    duration = 10  # Total video duration in seconds
    
    # Create background
    background = ColorClip(size=(width, height), color=(25, 25, 25))  # Dark background
    background = background.set_duration(duration)
    
    # Text to animate
    words = "Welcome to MoviePy Text Animation Demo!".split()
    text_clips = []
    
    # Animation timing settings
    word_duration = 2.0  # How long each word stays on screen
    fade_duration = 0.5  # Duration of fade in/out effects
    word_spacing = 1.5   # Time between start of each word
    
    # Create a clip for each word
    for i, word in enumerate(words):
        # Calculate timing
        start_time = i * word_spacing
        
        # Create text clip for the word
        txt_clip = TextClip(word, fontsize=70, color='white', font='Courier')
        
        # Position text vertically based on its index
        txt_clip = txt_clip.set_position(('center', 300 + (i % 2) * 100))
        
        # Set timing: word appears for word_duration seconds
        txt_clip = txt_clip.set_start(start_time).set_duration(word_duration)
        
        # Add fade in and fade out effects
        txt_clip = txt_clip.crossfadein(fade_duration)
        txt_clip = txt_clip.crossfadeout(fade_duration)
        
        text_clips.append(txt_clip)
    
    # Calculate total duration needed
    total_duration = (len(words) - 1) * word_spacing + word_duration
    background = background.set_duration(total_duration)
    
    # Combine all clips
    final_video = CompositeVideoClip([background] + text_clips)
    
    # Write the result
    final_video.write_videofile("text_animation.mp4", fps=24)

if __name__ == "__main__":
    create_text_animation() 