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
        
    def getTooltip(self, name):
        """
        Returns information about the value in 
        case of existence, else None
        @return: (str) values tooltip
        """
        if name in self.params:
            return self.params[name].getTooltip()
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
                return "%.4g" % self.params[name].getValue()
        return None
            
#     def getValueForWebsite(self, name):
#         if name in self.params:
#             if self.params[name].GetType() == bool:
#                 return self.params[name].getValue()
#             elif 
            
            
    def getObj(self, name):
        '''
        Returns the valProp-Object itself
        @param name: (String) the key for the dictionary 'list'
        @return: ValProp Object from dictionary 'list'
        '''
        return self.params[name]
    
    def getValueRequirements(self, name):
        """
        Returns value conditions for statusbar information
        @param name: (string) the key for the dictionary 'list'
        @return: string object with all information
        """
        vtype = str(self.params[name].getType())
        min_value = "min value: "+str(self.params[name].getMinValue())
        max_value = "max value: "+str(self.params[name].getMaxValue())
        
        return "[ "+vtype+" | "+min_value+" | "+max_value+"]"
            