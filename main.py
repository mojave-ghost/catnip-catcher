import pygame
import sys
import random
import images

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock() # Set up an fps

# define classes
class Catnip:
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
game_over = False
game_over_sound_played = False

# constants
TILESIZE = 32

# load images
images = images.load_images()

cloud1_1_white = images['cloud1_1_white']
cloud1_1_grey = images['cloud1_1_grey']
cloud2_1_white = images['cloud2_1_white']
cloud2_1_grey = images['cloud2_1_grey']
cloud3_4_white = images['cloud3_4_white']
cloud3_4_grey = images['cloud3_4_grey']

# cloud rects
cloud1_1_white_rect = cloud1_1_white.get_rect(topleft=(20,150))
cloud1_1_grey_rect = cloud1_1_grey.get_rect(topleft=(25,155))
cloud2_1_white_rect = cloud2_1_white.get_rect(topleft=(80,60))
cloud2_1_grey_rect = cloud2_1_grey.get_rect(topleft=(85,65))
cloud3_4_white_rect = cloud3_4_white.get_rect(topleft=(220,250))
cloud3_4_grey_rect = cloud3_4_grey.get_rect(topleft=(225,255))


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
player_image = pygame.image.load('assets/cat.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE*2, TILESIZE*2))
player_rect = player_image.get_rect(center = (screen.get_width()//2, 
                                              screen.get_height()-floor_image.get_height()-(player_image.get_height())/2))

# catnip
catnip_image = pygame.image.load('assets/catnip.png').convert_alpha()
catnip_image = pygame.transform.scale(catnip_image, (TILESIZE*1.5, TILESIZE*1.25))
catnips = [
  Catnip(catnip_image, (100,0), 3), 
  Catnip(catnip_image, (300,0), 3),
]

# sound fx
bg_music = pygame.mixer.Sound('assets/sound-fx/Sakura-Girl-Motivation.mp3')
bg_music.set_volume(0.080)
pickup = pygame.mixer.Sound('assets/sound-fx/powerup.mp3')
pickup.set_volume(0.1)
drop = pygame.mixer.Sound('assets/sound-fx/pkmn_emerald_drop.wav')
drop.set_volume(0.3)
game_over_sound = pygame.mixer.Sound('assets/sound-fx/pkmn_emerald_game_over.wav')
game_over_sound.set_volume(0.1)

# fonts
font = pygame.font.Font('assets/fonts/PixeloidMono.ttf', TILESIZE//2)

def start_game():
  global speed
  global score
  global game_over
  global catnips
  global hearts
  global player_rect
  global game_over_sound_played
  
  bg_music.play(-1)
  
  speed = 3
  score = 0
  game_over = False
  game_over_sound_played = False
  player_rect = player_image.get_rect(center = (screen.get_width()//2, 
                                              screen.get_height()-floor_image.get_height()-(player_image.get_height())/2))
  catnips = [
    Catnip(catnip_image, (100,0), 3), 
    Catnip(catnip_image, (300,0), 3),
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
  
  # general 
  screen.fill('lightblue')
  screen.blit(player_image, player_rect)
  screen.blit(floor_image, floor_rect)
  
  # clouds
  screen.blit(cloud1_1_grey, cloud1_1_grey_rect)
  screen.blit(cloud1_1_white, cloud1_1_white_rect)
  screen.blit(cloud2_1_grey, cloud2_1_grey_rect)
  screen.blit(cloud2_1_white, cloud2_1_white_rect)
  screen.blit(cloud3_4_grey, cloud3_4_grey_rect)
  screen.blit(cloud3_4_white, cloud3_4_white_rect)
  
  # catnips
  for catnip in catnips:
    screen.blit(catnip.image, catnip.rect)
  for heart in hearts:
    screen.blit(heart.image, heart.rect)
  
  # score
  score_text = font.render(f'Score: {score}', True, 'white')
  screen.blit(score_text, (10,10))
  
  # game over screen
  if game_over:
    game_over_text = font.render('Game over!', True, 'white')
    screen.blit(game_over_text, (125, screenHeight / 4))
    # create a button to start the game
    start_button = pygame.Rect(100, 200, 150, 50)
    pygame.draw.rect(screen, 'black', start_button)
    start_text = font.render('start', True, 'white')
    screen.blit(start_text, (138, 215))
    # start the game
    if pygame.mouse.get_pressed()[0]:
      if start_button.collidepoint(pygame.mouse.get_pos()):
        start_game()

def update():
  global speed
  global score
  global game_over
  global game_over_sound_played
  
  keys = pygame.key.get_pressed()
  
  # player movement
  if keys[pygame.K_LEFT]:
    player_rect.x -= 9.5
  if keys[pygame.K_RIGHT]:
    player_rect.x += 9.5
  if player_rect.left < 0:
    player_rect.left = 0
  if player_rect.right > screen.get_width():
    player_rect.right = screen.get_width()
 
    
  # catnip movement
  for catnip in catnips:
    catnip.move()
    if catnip.rect.colliderect(floor_rect):
      catnips.remove(catnip)
      catnips.append(Catnip(catnip_image, (random.randint(50, 300), -50), speed))
      drop.play()
      # if catnip hits floor, remove heart
      if hearts:
        hearts.pop()
      if len(hearts) == 0:
        game_over = True
        speed = 0
        player_rect.x = 1000
        player_rect.y = 1000
        for catnip in catnips:
          catnip.rect.y = 1000
        for heart in hearts:
          heart.rect.y = 1000
    elif catnip.rect.colliderect(player_rect):
      catnips.remove(catnip)
      catnips.append(Catnip(catnip_image, (random.randint(50, 300), -50), speed))
      speed += 0.1
      score += 1
      pickup.play()
  
  if game_over and not game_over_sound_played:
    game_over_sound.play()
    bg_music.stop()
    game_over_sound_played = True
  
def main_menu():
    while True:
        screen.fill('lightblue')
        title_text = font.render('Catnip Catcher', True, 'white')
        screen.blit(title_text, (80, 50))
        
        # Buttons
        play_button = pygame.Rect(100, 150, 150, 50)
        instructions_button = pygame.Rect(100, 225, 150, 50)
        credits_button = pygame.Rect(100, 300, 150, 50)
        quit_button = pygame.Rect(100, 375, 150, 50)
        
        pygame.draw.rect(screen, 'black', play_button)
        pygame.draw.rect(screen, 'black', instructions_button)
        pygame.draw.rect(screen, 'black', credits_button)
        pygame.draw.rect(screen, 'black', quit_button)
        
        play_text = font.render('Play', True, 'white')
        instructions_text = font.render('Instructions', True, 'white')
        credits_text = font.render('Credits', True, 'white')
        quit_text = font.render('Quit', True, 'white')
        
        screen.blit(play_text, (138, 165))
        screen.blit(instructions_text, (110, 240))
        screen.blit(credits_text, (138, 315))
        screen.blit(quit_text, (138, 390))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return 'play'
                elif instructions_button.collidepoint(event.pos):
                    return 'instructions'
                elif credits_button.collidepoint(event.pos):
                    return 'credits'
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def show_instructions():
    while True:
        screen.fill('lightblue')
        instructions_text = font.render('Use arrow keys to move', True, 'white')
        back_button = pygame.Rect(100, 450, 150, 50)
        
        pygame.draw.rect(screen, 'black', back_button)
        back_text = font.render('Back', True, 'white')
        
        screen.blit(instructions_text, (50, 250))
        screen.blit(back_text, (138, 465))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return

def show_credits():
    while True:
        screen.fill('lightblue')
        credits_text = font.render('Game by Your Name', True, 'white')
        back_button = pygame.Rect(100, 450, 150, 50)
        
        pygame.draw.rect(screen, 'black', back_button)
        back_text = font.render('Back', True, 'white')
        
        screen.blit(credits_text, (90, 250))
        screen.blit(back_text, (138, 465))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return

# Game loop
running = True

while running:
  main_menu()
  start_game()
  while not game_over:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
      
      update()
      draw()
      
      clock.tick(60)
      pygame.display.update()
  