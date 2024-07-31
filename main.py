import pygame
import sys
import random

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock() # Set up an fps

# define classes
class Apple:
  def __init__(self, image, position, speed):
    self.image = image
    self.rect = self.image.get_rect(topleft = position)
    self.speed = speed
  def move(self):
    self.rect.y += self.speed
    
class Heart:
  def __init__(self, image, position):
    self.image = image
    self.rect = self.image.get_rect(topleft = position)
  def remove(self):
    self.rect.y += 0.1
    
    
# variables
speed = 3
score = 0
screenWidth = screen.get_width()
screenHeight = screen.get_height()
game_over = True

# constants
TILESIZE = 32

# hearts
heart_image = pygame.image.load('assets/pixel-heart-removebg.png').convert_alpha()
heart_image = pygame.transform.scale(heart_image, (TILESIZE, TILESIZE))
hearts = [
  Heart(heart_image, (screenWidth - 40,10)),
  Heart(heart_image, (screenWidth - 80,10)),
  Heart(heart_image, (screenWidth - 120,10)),
  Heart(heart_image, (screenWidth - 160,10)),
  Heart(heart_image, (screenWidth - 200,10))
]

# floor
floor_image = pygame.image.load('assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE*15, TILESIZE*5))
floor_rect = floor_image.get_rect(bottomleft=(0,screen.get_height()))

# player
player_image = pygame.image.load('assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE, TILESIZE*2))
player_rect = player_image.get_rect(center = (screen.get_width()//2, 
                                              screen.get_height()-floor_image.get_height()-(player_image.get_height())/2))

# apple
apple_image = pygame.image.load('assets/apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TILESIZE, TILESIZE))
apples = [
  Apple(apple_image, (100,0), 3), 
  Apple(apple_image, (300,0), 3),
]

# sound fx
pickup = pygame.mixer.Sound('assets/powerup.mp3')
pickup.set_volume(0.1)

# fonts
font = pygame.font.Font('assets/PixeloidMono.ttf', TILESIZE//2)

def restart_game():
  global speed
  global score
  global game_over
  global apples
  global hearts
  global player_rect
  
  speed = 3
  score = 0
  game_over = False
  player_rect = player_image.get_rect(center = (screen.get_width()//2, 
                                              screen.get_height()-floor_image.get_height()-(player_image.get_height())/2))
  apples = [
    Apple(apple_image, (100,0), 3), 
    Apple(apple_image, (300,0), 3),
  ]
  hearts = [
    Heart(heart_image, (screenWidth - 40,10)),
    Heart(heart_image, (screenWidth - 80,10)),
    Heart(heart_image, (screenWidth - 120,10)),
    Heart(heart_image, (screenWidth - 160,10)),
    Heart(heart_image, (screenWidth - 200,10))
  ]
  

def draw():
  global screenWidth
  global screenHeight
  
  screen.fill('lightblue')
  screen.blit(player_image, player_rect)
  screen.blit(floor_image, floor_rect)
  
  for apple in apples:
    screen.blit(apple.image, apple.rect)
  for heart in hearts:
    screen.blit(heart.image, heart.rect)
    
  score_text = font.render(f'Score: {score}', True, 'white')
  screen.blit(score_text, (10,10))
  
  if game_over:
    game_over_text = font.render('Game over!', True, 'white')
    screen.blit(game_over_text, (125, screenHeight / 4))
    # create a button to restart the game
    restart_button = pygame.Rect(100, 200, 150, 50)
    pygame.draw.rect(screen, 'black', restart_button)
    restart_text = font.render('Restart', True, 'white')
    screen.blit(restart_text, (138, 215))
    # restart the game
    if pygame.mouse.get_pressed()[0]:
      if restart_button.collidepoint(pygame.mouse.get_pos()):
        restart_game()

def update():
  global speed
  global score
  global game_over
  
  keys = pygame.key.get_pressed()
  
  # player movement
  if keys[pygame.K_LEFT]:
    player_rect.x -= 8
  if keys[pygame.K_RIGHT]:
    player_rect.x += 8
  if player_rect.left < 0:
    player_rect.left = 0
  if player_rect.right > screen.get_width():
    player_rect.right = screen.get_width()
 
    
  # apple movement
  for apple in apples:
    apple.move()
    if apple.rect.colliderect(floor_rect):
      apples.remove(apple)
      apples.append(Apple(apple_image, (random.randint(50, 300), -50), speed))
      # if apple hits floor, remove heart
      if hearts:
        hearts.pop()
      if len(hearts) == 0:
        game_over = True
        speed = 0
        player_rect.x = 1000
        player_rect.y = 1000
        for apple in apples:
          apple.rect.y = 1000
        for heart in hearts:
          heart.rect.y = 1000
    elif apple.rect.colliderect(player_rect):
      apples.remove(apple)
      apples.append(Apple(apple_image, (random.randint(50, 300), -50), speed))
      speed += 0.1
      score += 1
      pickup.play()
  
# Game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type ==pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  update() 
  draw()
      
  clock.tick(60) 
  pygame.display.update()
  