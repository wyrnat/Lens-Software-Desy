'''
Created on 25.06.2015

@author: Woehnert
'''

class Values(object):
    '''
    Abstract Class for InputValues and OutputValues. Provides elementary functionality
    '''


    def __init__(self):
        '''
        Creates the dict params with all parameters necessary
        '''
        self.params = {}
        
        
    def setValue(self, name, val):
        '''
        Try to set Value and returns bool
        >> True: name exist in self.params and value is settable due to valProp conditions
        >> False: else
        @param name: (String) the key for the dictionary 'list'
        @param val: the value to be set
        @return: bool indicates if set was sucessful
        '''
        if name in self.params:
            if (self.params[name].setValue(val)):
                return True
        return False
                
    def getValue(self, name):
        '''
        Returns the value in case of existence, else None
        @param name: (String) the key for the dictionary 'list'
        @return: The Value or None if Value not found
        '''
        if name in self.params:
            return self.params[name].getValue()
        else:
            return None
    
    def getValues(self):
        """
        Debug Method. No implicite use
        """
        mylist = []
        for val in self.params:
            mylist.append( str(val) + str(self.getValue(val)) )
        return mylist
            
        
    def getValueForUI(self, name):
        '''
        Returns the value prepared for wxObjects-Setters
        @param name: (String) the key for the dictionary 'list'
        @return: value converted to String or bool
        '''
        if name in self.params:
            if self.params[name].getType() == bool:
                return self.params[name].getValue()
            else:
                return "%.3g" % self.params[name].getValue()
            
            
    def getObj(self, name):
        '''
        Returns the valProp-Object itself
        @param name: (String) the key for the dictionary 'list'
        @return: ValProp Object from dictionary 'list'
        '''
        return self.params[name]
            