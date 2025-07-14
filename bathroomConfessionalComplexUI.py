import pygame

def display_text(filepath):
    with open(filepath, "r") as file:
        content = file.read()

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Confession Booth")
    font = pygame.font.SysFont("Georgia", 48)
    screen.fill((0, 0, 0))

    # Word-wrap and render text
    words = content.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word
        if font.size(test_line)[0] < screen.get_width() - 100:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    y = 100
    for line in lines:
        rendered_text = font.render(line.strip(), True, (255, 255, 255))
        screen.blit(rendered_text, ((screen.get_width() - rendered_text.get_width()) // 2, y))
        y += rendered_text.get_height() + 20

    pygame.display.flip()

    # Wait for 10 seconds or keypress
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 10000:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                return

    pygame.quit()

display_text("introductionText.txt")
