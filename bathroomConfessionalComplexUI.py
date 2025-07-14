import pygame

def display_text(filepath, duration=10):
    with open(filepath, "r") as file:
        content = file.read()

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()
    pygame.display.set_caption("Confession Booth")
    screen.fill((0, 0, 0))

    # Function to dynamically calculate best font size to fit text on screen
    def get_best_font_size(text, max_width, max_height, font_name="Georgia"):
        font_size = 80
        while font_size > 10:
            font = pygame.font.SysFont(font_name, font_size)
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

            total_height = len(lines) * (font.get_height() + 10)
            if total_height <= max_height - 100:
                return font, lines

            font_size -= 2
        return pygame.font.SysFont(font_name, 20), [text]

    font, lines = get_best_font_size(content, screen_width, screen_height)

    y = (screen_height - (len(lines) * (font.get_height() + 10))) // 2
    for line in lines:
        rendered_text = font.render(line, True, (255, 255, 255))
        x = (screen_width - rendered_text.get_width()) // 2
        screen.blit(rendered_text, (x, y))
        y += font.get_height() + 10

    pygame.display.flip()

    # Wait for `duration` seconds or ESC key
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration * 1000:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return
        clock.tick(60)

    pygame.quit()

display_text("introductionText.txt")
