label chapter1:
    scene black
    with Pause(1)

    show text "{color=[gui.accent_color]}CHAPTER 1{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show temp_bigby_wolf with dissolve
    bigby "We have access to images and variables defined in other files, as well."

    # ... more code goes here ...
    # This ends the game.

    return
