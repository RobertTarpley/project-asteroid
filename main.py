# this allows us to use code from the open-source pygame library throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
from game_over import show_game_over
from high_score import load_high_score, save_high_score

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.font.init()
    font = pygame.font.SysFont(None, 36)
 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (updatable_group, drawable_group, shot_group)

    player = Player(x = SCREEN_WIDTH / 2 , y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # scoring 
    score = 0
    high_score = load_high_score()
    score_animation_timer = 0
    score_changed = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #exit the main function
        
        #fill the screen with black
        screen.fill((0, 0, 0))
        
        for sprite in drawable_group:
            sprite.draw(screen)
        
        # decrease the timer over time:
        if score_animation_timer > 0:
            score_animation_timer -= dt
        else:
            score_changed = False
        
        if score_changed:
            scale = 1.5
        else:
            scale = 1.0
        
        # Render font at scaled size
        font_size = int(24 * scale)
        score_font = pygame.font.SysFont("Courier", font_size)

        score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))

        high_score_surface = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_surface, (10, 40))

        #create the score surface
        #score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        #screen.blit(score_surface, (10, 10))
        # create the high score surface
        #high_score_surface = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        #screen.blit(high_score_surface, (SCREEN_WIDTH - high_score_surface.get_width() - 10, 10))
        
        # refresh the display
        pygame.display.flip()
        
        #cap the frame rate at 60 fps and set dt 
        dt = clock.tick(60) / 1000
       
        updatable_group.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collides_with(player):
                if score > high_score:
                    save_high_score(score)
                    high_score = score        
                show_game_over(screen, score, high_score)
                break

            for bullet in shot_group:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score += int(asteroid.radius) * 10
                    score_changed = True
                    score_animation_timer = 0.15
                    break

if __name__ == "__main__":
    main()
