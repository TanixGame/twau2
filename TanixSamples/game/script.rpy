init python:
    from baseClasses import *
    #Define and Init Python
    config.developer = True
    #config.gamedir
    config.main_menu_music = "music/intro_game.mp3"
    introLines = """
    {size=+10}THE TAW2{color=#303030}
    \n\n
    {color=#303030}TELL ME WHAT IS TAW2{/color}
    {color=#d92626}this is a TAW2 text to be done\n\n{/color}
    {color=#303030}Sample TAW2, Sample TAW2, Sample TAW2 ,Sample TAW2{/color}
    {color=#d92626}Sample TAW2, Sample TAW2, Sample TAW2, Sample TAW2\n\n{/color}
    {color=#303030}Sample TAW2,Sample TAW2,Sample TAW2{/color}
    {color=#d92626}Sample TAW2 , Sample TAW2 , Sample TAW2, Sample TAW2 ,Sample TAW2\n\n{/color}
    {color=#cc9900}Sample TAW2, Sample TAW2
    Sample TAW2
    Sample TAW2
    Sample TAW2\n\n
    {/color}
    {color=#d92626}Sample TAW2 , Sample TAW2 , Sample TAW2, Sample TAW2 ,Sample TAW2\n\n{/color}
    {color=#d92626}Sample TAW2 , Sample TAW2 , Sample TAW2, Sample TAW2 ,Sample TAW2\n\n{/color}
    {color=#d92626}Sample TAW2, Sample TAW2, Sample TAW2, Sample TAW2\n\n{/color}
    {color=#303030}Sample TAW2,Sample TAW2,Sample TAW2{/color}
    {color=#d92626}Sample TAW2 , Sample TAW2 , Sample TAW2, Sample TAW2 ,Sample TAW2\n\n{/color}
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n"""

    
    playerIventory = inventory()

    variableBox = "gui/narrator.png"


#Defining images

image black = '#000000'
image white = '#FFFFFF'

image TAW2TILE = Text("{size=+20}*{color=#252525}* TAW2 *{/color}*{/size}", text_align=0.5)

image introText = Text(introLines, text_align=0.5)

label splashscreen:
    scene black
    with Pause(1)

    show text "TAW2 PROJECT PRESENTS" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    nvl clear

    play music "music/intro_game.mp3" loop

    show TAW2TILE:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide TAW2TILE

    $ speed = 45  # scrolling speed in seconds
    show introText at Move((0.5, 5.0), (0.5, 0.0), speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")

    with Pause(25)
    
    show text "{size=+10}{color=#FFFFFF}PRODUCT MANAGER: RACHEL{/color}{/size}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show temp_bigby_wolf at left
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{size=+10}{color=#FFFFFF}ARTISTS: KASSIA/LUE/XEEN{/color}{/size}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{size=+10}{color=#FFFFFF}DEVELOPER LEAD: RENEE{/color}{/size}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{size=+10}{color=#FFFFFF}DEVELOPER: TANIX/ZORP{/color}{/size}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{size=+10}{color=#FFFFFF}WRITER: GRAY{/color}{/size}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show temp_bigby_wolf at right
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{size=+10}{color=#FFFFFF}MUSIC: BRUNO{/color}{/size}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{size=+10}{color=#FFFFFF}Whaterver is needed to add{/color}{/size}"
    with dissolve
    pause 3
    hide text
    with dissolve

    show temp_bigby_wolf at center
    with dissolve
    pause 5
    hide text
    with dissolve

    return

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite with the corresponding [filename].png.
    # For example, this is images/temp_bigby_wolf.png

    show temp_bigby_wolf

    # These display lines of dialogue.

    bigby "{color=#000000}You've created a new Ren'Py game.{/color}"

    bigby "{color=#000000}Once you add a story, pictures, and music, you can release it to the world!{/color}"

    jump chapter1

