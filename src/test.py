"""# Test file for challenges
elif event.type == pygame.KEYDOWN:
if event.key == pygame.K_a:
    x_speed = -3
elif event.key == pygame.K_d:
    x_speed = 3
elif event.key == pygame.K_w:
    y_speed = -3
elif event.key == pygame.K_s:
    y_speed = 3
elif event.type == pygame.KEYUP:
    if event.key == pygame.K_a or event.key == pygame.K_d:
        x_speed = 0
    elif event.key == pygame.K_w or event.key == pygame.K_s:
        y_speed = 0

x_coord += x_speed
y_coord += y_speed"""
