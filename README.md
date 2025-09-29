while run == True:
    screen.fill(HG)
    screen.blit(sprite_sheet_image, (0,0))
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                move_right = True
            if(event.key == pygame.K_LEFT):
                move_left = True
            if(event.key == pygame.K_UP):
                move_up = True
            if(event.key == pygame.K_DOWN):
                move_down = True
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                move_right = True
            if(event.key == pygame.K_LEFT):
                move_left = True
            if(event.key == pygame.K_UP):
                move_up = True
            if(event.key == pygame.K_DOWN):
                move_down = True
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()
        
pygame.quit
                
