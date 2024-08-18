# Catnip Catcher Game

A simple game built using Pygame where the player catches catnips falling from the top of the screen. The player loses a heart if an catnip hits the floor, and the game ends when all hearts are lost.

## Table of Contents
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)
- [Assets](#assets)
- [Credits](#credits)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/catnip-catcher-game.git
2. Navigate the project directory:
    ```sh
    cd catnip-catcher-game
3. Install the required dependencies
4. Make sure you have the assets floder with all the necessary imgages and sounds

## How to Play
1. Run the game
    ``` sh
    python main.py
2. Use the left and right arrow keys to move the player left and right.
3. Catch the falling catnips with the player to increase your score.
4. Avoid missing catnips, as they will cause you to lose a heart.
5. The game ends when all hearts are lost.

## Game Mechanics

### Player Movement

	•	The player can move left and right using the arrow keys.
	•	The player cannot move beyond the screen boundaries.

### Catnip Movement

	•	Catnips fall from the top of the screen at a constant speed.
	•	When an catnip hits the floor, it is removed, a new catnip is spawned at the top, and the player loses a heart.
	•	When an catnip is caught by the player, it is removed, a new catnip is spawned at the top, the speed of the catnips increases slightly, and the player’s score increases by one.

### Hearts

	•	The player starts with 5 hearts.
	•	A heart is removed each time an catnip hits the floor.
	•	The game prints “Game Over” and stops when all hearts are lost.

## Assets

## Images

	•	assets/pixel-heart-removebg.png: Heart image.
	•	assets/floor.png: Floor image.
	•	assets/player_static.png: Player image.
	•	assets/catnip.png: Catnip image.

## Sounds

	•	assets/powerup.mp3: Sound effect for catching an catnip.

## Fonts

	•	assets/PixeloidMono.ttf: Font used for displaying the score.

## Credits

	•	Game Development: Waldo Salinas AKA mojabi-geist
  • Music: Motivation by Sakura Girl | https://soundcloud.com/sakuragirl_official
            Music promoted by https://www.chosic.com/free-music/all/
            Creative Commons CC BY 3.0
            https://creativecommons.org/licenses/by/3.0/

This project was created for educational purposes and as a fun way to learn and practice Pygame.