label chapter1:
    scene black
    with Pause(1)

    show text "{color=[gui.accent_color]}CHAPTER 1{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show temp_bigby_wolf with dissolve

    $ variableBox = "gui/normal.png"

    bigby "{color=#000000}[variableBox] We have access to images and variables defined in other files, as well.{/color}"

    # ... more code goes here ...
    # This ends the game.

    scene black

    "So Lets start with items"

    jump listItems

label listItems:

    "Current you have the folloing Items"

    python:
        listOfItems = ""
        for i in playerIventory.listItems():
            listOfItems += "{} ".format(i.name)

        if listOfItems == "":
            listOfItems = "None"

    "[listOfItems]"

    "Now what you want to do?"

    menu:
        "Add New Item":
            jump addItem

        "List Items":            
            jump listItems

        "End Game":
            return

label addItem:
    "What is the item that you want to add"

    menu:
        "Knife":
            $ playerIventory.addItem(item(1, "Knife"))
            jump listItems

        "Rifle":
            $ playerIventory.addItem(item(3, "Rifle"))
            jump listItems
            
        "Banana":
            $ playerIventory.addItem(item(4, "Banana"))
            jump listItems
        
        "Hat":
            $ playerIventory.addItem(item(4, "Hat"))
            jump listItems
