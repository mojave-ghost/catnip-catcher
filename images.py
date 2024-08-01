import pygame

# constants
TILESIZE = 32

def load_images():
    # cloud1
    cloud1_1_white = pygame.image.load('assets/clouds/cloud_shape1_1.png').convert_alpha()
    cloud1_1_white = pygame.transform.scale(cloud1_1_white, (TILESIZE, TILESIZE))
    cloud1_1_gray = pygame.image.load('assets/clouds/cloud_shape1_1_gray.png').convert_alpha()
    cloud1_1_gray = pygame.transform.scale(cloud1_1_gray, (TILESIZE, TILESIZE))

    # cloud2
    cloud2_1_white = pygame.image.load('assets/clouds/cloud_shape2_1.png').convert_alpha()
    cloud2_1_white = pygame.transform.scale(cloud2_1_white, (TILESIZE, TILESIZE))
    cloud2_1_gray = pygame.image.load('assets/clouds/cloud_shape2_1_gray.png').convert_alpha()
    cloud2_1_gray = pygame.transform.scale(cloud2_1_gray, (TILESIZE, TILESIZE))
    cloud2_4_white = pygame.image.load('assets/clouds/cloud_shape2_4.png').convert_alpha()
    cloud2_4_white = pygame.transform.scale(cloud2_4_white, (TILESIZE, TILESIZE))
    cloud2_4_gray = pygame.image.load('assets/clouds/cloud_shape2_4_gray.png').convert_alpha()
    cloud2_4_gray = pygame.transform.scale(cloud2_4_gray, (TILESIZE, TILESIZE))

    # cloud3
    cloud3_4_white = pygame.image.load('assets/clouds/cloud_shape3_4.png').convert_alpha()
    cloud3_4_white = pygame.transform.scale(cloud3_4_white, (TILESIZE, TILESIZE))
    cloud3_4_gray = pygame.image.load('assets/clouds/cloud_shape3_4_gray.png').convert_alpha()
    cloud3_4_gray = pygame.transform.scale(cloud3_4_gray, (TILESIZE, TILESIZE))

    return {
        'cloud1_1_white': cloud1_1_white,
        'cloud1_1_gray': cloud1_1_gray,
        'cloud2_1_white': cloud2_1_white,
        'cloud2_1_gray': cloud2_1_gray,
        'cloud2_4_white': cloud2_4_white,
        'cloud2_4_gray': cloud2_4_gray,
        'cloud3_4_white': cloud3_4_white,
        'cloud3_4_gray': cloud3_4_gray,
    }