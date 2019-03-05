# Declare characters used by this game. The color argument colorizes the
# name of the character.
#define bigby = Character("Bigby", window_background="gui/regular.png", image="bigby")
define bigby = Character("Bigby", image="bigby")
define bigbyShouting = Character("Bigby", window_background="gui/dialog/Dialogue Shout Speech.png", image="bigby")

image side bigby normal = im.Scale("images/temp_bigby_wolf.png", 600, 450, xoffset=-200, yoffset=100)
image side bigby thinking = im.Scale("images/ThinkingSprite.png", 600, 450, xoffset=-200, yoffset=100)
