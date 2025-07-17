import os
import random
import pygame
import time

# Hardcoded path to the folder containing MP3 files
MP3_FOLDER = "C:/Users/YourUsername/Music/MyMP3s"  # 🔁 Replace with your actual path

def get_mp3_files(folder_path):
    """Return a list of all .mp3 files in the folder."""
    return [file for file in os.listdir(folder_path) if file.endswith('.mp3')]

def play_random_mp3(folder_path):
    mp3_files = get_mp3_files(folder_path)
    if not mp3_files:
        print("No MP3 files found in the folder.")
        return
    
    random_file = random.choice(mp3_files)
    file_path = os.path.join(folder_path, random_file)
    
    print(f"Now playing: {random_file}")
    
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    play_random_mp3('/home/username/my_project/mp3Files')
