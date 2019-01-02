class player(object):
    '''
    player Class
    '''

    def __init__(self, localDB):
        '''
        Init Variables
        '''
        self.items = []   

    def addItem(self, item):
        self.items += item

    def useItem(self, itemID):
        if itemID < len(self.items):
            return self.items.pop(itemID)
        else:
            return False

    def listItems(self):
        return self.items


