# -*- coding: utf-8 -*-
""" Contains the Base Class of TWAU.
 
    This package contains the base classes to be used in the TWAU game for example Player.
     
    The Programmer will use the classes and update this file in order to have all changes
     in one place and know where the changes will be done.
 
    Tested and build in: Renpy X
     
    Example of use
     
    #Player Creation
    newPlayer = Player()
         
        # get the health of the player
         
        newPlaner.getHealth()    
     
"""

__author__ = "Tanix"
__copyright__ = "Copyright 2019, by Tanix"
__credits__ = "TWAU 2 Project"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "Tanix"
__email__ = "keitaro.haitou@gmail.com"
__status__ = "Prototype"

import copy

class player(object):
    ''' Player Class where we can init the player
    '''

    def __init__(self):
        """ Init of the Player

        The following attributes will be instantiated:
         iventory
         
        """
        self.inventory = inventory()
        self.health = 100
        self.actionPoints = 100

class inventory(object):
    ''' Iventory Class where inventory is defined
    '''

    def __init__(self):
        ''' Init Iventory
            set items attribute
        '''
        self.items = []

    def addItem(self, item):
        ''' Add one item to the list
        '''
        self.items.append(item)

    def useItem(self, itemID):
        ''' Pop one item from the list
        
        Return the item that it's pop
        Return False if there is no item in the list
        '''
        if itemID < len(self.items):
            return self.items.pop(itemID)
        else:
            return False

    def listItems(self):
        ''' Return one item from the list
        '''
        return self.items

class item(object):

    def __init__(self, id, name):
        '''
        Init Variables
        '''
        self.id = id
        self.name = name
        self.quantity = 1
