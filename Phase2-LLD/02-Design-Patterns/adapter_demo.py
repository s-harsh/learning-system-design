"""
Day 8: Adapter Pattern Demo
Scenario: A Media Player.
- Core System plays MP3s.
- We want to plug in a new "Advanced Audio Player" that plays VLC and MP4.
- But the interface is completely different.
"""

# ==========================================
# 1. The Target Interface (What Client Expects)
# ==========================================
class MediaPlayer:
    def play(self, audio_type, file_name):
        pass

# ==========================================
# 2. The Adaptee (Incompatible 3rd Party Lib)
# ==========================================
class AdvancedMediaPlayer:
    def play_vlc(self, file_name):
        print(f"🎵 Playing vlc file: {file_name}")
        
    def play_mp4(self, file_name):
        print(f"🎬 Playing mp4 file: {file_name}")

# ==========================================
# 3. The Adapter
# ==========================================
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        self.advanced_music_player = AdvancedMediaPlayer()
        
    def play(self, audio_type, file_name):
        if audio_type == "vlc":
            self.advanced_music_player.play_vlc(file_name)
        elif audio_type == "mp4":
            self.advanced_music_player.play_mp4(file_name)

# ==========================================
# 4. The Client (Concrete Class using Adapter)
# ==========================================
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, file_name):
        # Built-in support for mp3
        if audio_type == "mp3":
            print(f"🎶 Playing mp3 file: {file_name}")
            
        # Adapter support for other formats
        elif audio_type == "vlc" or audio_type == "mp4":
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, file_name)
            
        else:
            print(f"❌ Invalid media. {audio_type} format not supported")

# ==========================================
# Usage
# ==========================================
if __name__ == "__main__":
    print("--- Adapter Pattern Demo: Universal Player ---\n")
    
    player = AudioPlayer()
    
    player.play("mp3", "beyond_the_horizon.mp3")
    player.play("mp4", "matrix_trailer.mp4")
    player.play("vlc", "big_buck_bunny.vlc")
    player.play("avi", "my_movie.avi")
