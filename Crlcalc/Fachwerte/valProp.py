'''
Created on 28.06.2015
@author: Woehnert
'''

class ValProp(object):
    '''
    Contains A value and provides type test and boarder values
    '''


    def __init__(self, value, mytype, min_value = None, max_value = None, tooltip=None):
        '''
        Set value and type of the value.
        min_value and max_value are optional
        @param value: value to be set
        @param mytype: Type of value, e.g. float, bool
        @param min_value: lower boarder of value range
        @param max_value: higher boarder of value range
        '''
        #set type
        self.mytype = mytype
        
        #set min and max value
        if (type(max_value)==self.mytype or max_value==None):
            self.max_value = max_value
        else:
            print "max_value "+str(max_value)+" not of type "+str(mytype)
        if (type(min_value)==self.mytype or min_value==None):
            self.min_value = min_value
        else:
            print "min_value "+str(min_value)+" not of type "+str(mytype)
        
        #set value
        if not (self.setValue(value)):
            print "value "+ str(value)+ " not settable"
        
        #set tooltip    
        if tooltip==None:
            self.tooltip = (
                            '['+str(self.mytype)+
                            '|min value: '+str(self.min_value)+
                            '|max value: '+str(self.max_value)+
                            ']'
                            )
        elif type(tooltip) == str:
            self.tooltip = tooltip
        else:
            print "tooltip "+str(tooltip)+" not of type "+str(type(str))
                
            
            
    def getValue(self):
        """
        returns the Value
        @return: value
        """
        return self.value
            
    
    def setValue(self, value):
        """
        sets Value and returns True if value is settable,
        else returns False
        @param value: new value to be set
        @return: bool indicates if value is valid
        @attention: convert to float at first, int can not handle literals
        """
        
        if self.isValueSettable(value):
            self.value = (self.mytype)(float(value))
            return True
        else:
            return False
        
    def getType(self):
        """
        returns the type.
        @return: mytype
        """
        return self.mytype
        
    def getMinValue(self):
        """
        returns min_value
        @return: min_value
        """
        return self.min_value
    
    def getMaxValue(self):
        """
        returns max_value
        @return: max_value
        """
        return self.max_value
    
    def getTooltip(self):
        """
        returns value information
        @return tooltip
        """
        return self.tooltip
    
    def setTooltip(self, tooltip):
        """
        Sets value information if from type <str>
        @param tooltip: (str) value information
        """
        if type(tooltip) == str:
            self.tooltip=tooltip
    
    def isValueSettable(self, value):
        """
        Returns true if min_value < value < max_value or
        if boarders are None and
        value from type mytype or related
        @param value: the value needed to be checked
        @return: bool indicates if above conditions are fulfilled
        @attention: converting at first to float. int can not handle literals
        """
        try:
            value = (float)(value)
        except:
            return False
        return  (value == (self.mytype)(float(value)) and 
                (value > self.min_value or self.min_value == None) and 
                (value < self.max_value or self.max_value == None)
                )
        
