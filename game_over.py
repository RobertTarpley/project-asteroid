import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def show_game_over(screen, score, high_score):
    if score > high_score:
        high_score = score

    font = pygame.font.SysFont("Viga", 48)
    screen.fill((0, 0, 0))
    text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 0))
    
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 60))

    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()
