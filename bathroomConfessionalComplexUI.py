import pygame

def display_text(filepath, duration=10):
    with open(filepath, "r") as file:
        content = file.read()

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()
    pygame.display.set_caption("Confession Booth")
    screen.fill((0, 0, 0))

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

    # Try from large font size down until text fits
    max_font_size = 150
    min_font_size = 10
    best_font = None
    best_lines = []

    for font_size in range(max_font_size, min_font_size - 1, -2):
        font = pygame.font.SysFont("Apple Chancery", font_size)
        lines = wrap_text(font, content, screen_width)
        total_height = len(lines) * (font.get_height() + 10)

        if total_height <= screen_height - 100:
            best_font = font
            best_lines = lines
            break

    # Fallback
    if not best_font:
        best_font = pygame.font.SysFont("Apple Chancery", 20)
        best_lines = wrap_text(best_font, content, screen_width)

    # Display text centered
    screen.fill((0, 0, 0))
    y = (screen_height - (len(best_lines) * (best_font.get_height() + 10))) // 2
    for line in best_lines:
        rendered_text = best_font.render(line, True, (255, 255, 255))
        x = (screen_width - rendered_text.get_width()) // 2
        screen.blit(rendered_text, (x, y))
        y += best_font.get_height() + 10

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
