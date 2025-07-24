import os
import random
import time
import pygame
import subprocess
from mutagen.mp3 import MP3
from gpiozero import MotionSensor, Button
from signal import pause

# === Configuration ===
BUTTON_PIN = 2
MOTION_PIN = 4
INTRO_TEXT_FILES = [
    "/home/username/bathroomConfessional/introduction/introductionText1.txt",
    "/home/username/bathroomConfessional/introduction/introductionText2.txt",
    "/home/username/bathroomConfessional/introduction/introductionText3.txt",
]
INTRO_AUDIO_PATH = "/home/username/bathroomConfessional/introduction/introductionAudio.mp3"
INTRO_DURATIONS = [20, 18]  # Only for first two slides
PENANCE_ROOT = "penences"
FONT_NAME = "Apple Chancery"
FONT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# === Helper Functions ===
def wrap_text(font, text, max_width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width - 100:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

def display_text(content, screen, screen_width, screen_height):
    max_font_size = 150
    min_font_size = 10
    best_font = None
    best_lines = []

    for font_size in range(max_font_size, min_font_size - 1, -2):
        font = pygame.font.SysFont(FONT_NAME, font_size)
        lines = wrap_text(font, content, screen_width)
        total_height = len(lines) * (font.get_height() + 10)
        if total_height <= screen_height - 100:
            best_font = font
            best_lines = lines
            break

    if not best_font:
        best_font = pygame.font.SysFont(FONT_NAME, 20)
        best_lines = wrap_text(best_font, content, screen_width)

    screen.fill(BG_COLOR)
    y = (screen_height - (len(best_lines) * (best_font.get_height() + 10))) // 2
    for line in best_lines:
        rendered = best_font.render(line, True, FONT_COLOR)
        x = (screen_width - rendered.get_width()) // 2
        screen.blit(rendered, (x, y))
        y += best_font.get_height() + 10
    pygame.display.flip()

def get_mp3_duration(filepath):
    try:
        audio = MP3(filepath)
        return int(audio.info.length)
    except:
        return 60

def select_random_penance():
    folders = [f for f in os.listdir(PENANCE_ROOT) if os.path.isdir(os.path.join(PENANCE_ROOT, f))]
    if not folders:
        raise Exception("No penance folders found")
    folder = os.path.join(PENANCE_ROOT, random.choice(folders))
    txt = os.path.join(folder, "penance.txt")
    mp3 = next((os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".mp3")), None)
    return txt, mp3

# === Wait for motion to begin ===
pir = MotionSensor(MOTION_PIN)
print("Waiting for motion to start confessional...")
pir.wait_for_motion()
print("Motion detected. Starting...")

# === Main Program ===
button = Button(BUTTON_PIN)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.font.init()

# Start lights
lights_process = subprocess.Popen(["sudo", "python3", "/home/username/bathroomConfessional/lights.py", "--clear"])

# Play intro audio
try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Error initializing mixer: {e}")
else:
    try:
        pygame.mixer.music.load(INTRO_AUDIO_PATH)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing intro audio: {e}")

# Show intro slides
for i in range(len(INTRO_TEXT_FILES) - 1):
    with open(INTRO_TEXT_FILES[i], "r") as f:
        content = f.read()
    display_text(content, screen, screen_width, screen_height)
    time.sleep(INTRO_DURATIONS[i])

# Final slide, wait for button press
with open(INTRO_TEXT_FILES[-1], "r") as f:
    content = f.read()
display_text(content, screen, screen_width, screen_height)
print("Waiting for button press...")
button.wait_for_press()

# Show loading message
screen.fill(BG_COLOR)
font = pygame.font.SysFont(FONT_NAME, 80)
loading = font.render("Penance Loading...", True, FONT_COLOR)
rect = loading.get_rect(center=(screen_width//2, screen_height//2))
screen.blit(loading, rect)
pygame.display.flip()
time.sleep(2)

# Select penance
penance_txt, penance_mp3 = select_random_penance()
if penance_mp3:
    try:
        pygame.mixer.music.load(penance_mp3)
        pygame.mixer.music.play()
        duration = get_mp3_duration(penance_mp3)
    except Exception as e:
        print(f"⚠️ Error playing penance audio: {e}")
        duration = 60
else:
    print("⚠️ No penance audio found. Skipping playback.")
    duration = 60

# Display penance
with open(penance_txt, "r") as f:
    content = f.read()
display_text(content, screen, screen_width, screen_height)

# Wait for duration
start = time.time()
try:
    while time.time() - start < duration:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise KeyboardInterrupt
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

# Cleanup
pygame.quit()
if pygame.mixer.get_init():
    pygame.mixer.music.stop()

subprocess.run(["sudo", "kill", "-TERM", str(lights_process.pid)])
