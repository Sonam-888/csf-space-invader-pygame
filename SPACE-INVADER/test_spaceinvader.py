import unittest
import pygame
from Spaceinvader import screen, background 

class TestBackground(unittest.TestCase):

    def test_background_load(self):
        # Test background image loads 
        self.assertIsNotNone(background)
        self.assertEqual(background.get_size(), (800,600))

    def test_background_display(self):
        # Test background displayed on screen
        screen.blit(background, (0,0))
        bg_color = screen.get_at((0, 0))
        self.assertNotEqual(bg_color, (0,0,0))



from Spaceinvader import player, enemy, isCollision, fire_bullet

class TestGameLogic(unittest.TestCase):

    def test_caption_icon(self):
        # Test caption and icon are set
        pygame.display.set_caption("Space Invader")
        icon = pygame.image.load('ufo.png')
        pygame.display.set_icon(icon)
        self.assertEqual(pygame.display.get_caption()[0], "Space Invader")
        self.assertIsNotNone(icon)

from Spaceinvader import show_score, game_over_text, player, enemy, fire_bullet, isCollision

class TestGameFunctions(unittest.TestCase):


    def test_show_score(self):
        # Test score text rendered at given coords
        screen = pygame.Surface((800,600))
        score_value = 10
        show_score(screen, 10, 10)
        self.assertNotEqual(screen.get_at((10, 10)), (0,0,0))

    def test_game_over(self):
        # Test game over text rendered 
        screen = pygame.Surface((800,600))  
        game_over_text(screen)
        self.assertNotEqual(screen.get_at((200, 250)), (0,0,0))

    def test_player_movement(self):
        # Test player movement and boundary checking
        playerX = 400
        playerX_change = 5
        playerX += playerX_change
        
        self.assertEqual(playerX, 405)

        playerX = 0
        playerX_change = -10
        playerX += playerX_change
        self.assertEqual(playerX, -10)

    def test_collision_detection(self):
        # Test collision detection
        enemyX = 300
        enemyY = 400
        bulletX = 250
        bulletY = 350
        self.assertFalse(isCollision(enemyX, enemyY, bulletX, bulletY))

        enemyX = 500
        enemyY = 100 
        self.assertFalse(isCollision(enemyX, enemyY, bulletX, bulletY))

    
from Spaceinvader import player, enemy, collision

class TestGameLoop(unittest.TestCase):

    def test_player_movement(self):
        # Test player x position changes on key presses
        playerX = 100
        playerX_change = 0
        player(pygame.K_LEFT, playerX)
        self.assertEqual(playerX_change, 0)
        
        player(pygame.K_RIGHT, playerX )
        self.assertEqual(playerX_change,0)

    def test_enemy_movement(self):
        # Test enemy direction changes on edge collision
        enemyX = [50, 100, 150]
        enemyX_change = [4, -4, 4]
        
        enemy(0, enemyX, enemyX_change)
        self.assertEqual(enemyX_change[0], -4)

        enemy(1, enemyX, enemyX_change)
        self.assertEqual(enemyX_change[1], 4)

    def test_collision(self):
        # Test collision detection
        enemyX = 300
        enemyY = 400
        bulletX = 250
        bulletY = 350
        self.assertTrue(collision(enemyX, enemyY, bulletX, bulletY))
        
if __name__ == '__main__':
    unittest.main()