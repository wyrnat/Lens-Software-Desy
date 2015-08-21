'''
Created on 25.0.6.20.15

@author: Woehnert
'''
from .values import Values
from .valProp import ValProp

class OutputValues(Values):
    '''
    Saves Output Values in a dictionary. Inherits functionality from values.Fachwerte
    '''


    def __init__(self):
        '''
        Provides 'Empty' ValProp Instances for the Fachwerte
        '''
        self.params = {'f': ValProp(0.,float),              #mm
                       'H': ValProp(0.,float),              #mm
                       'Deff': ValProp(0.,float),           #mm
                       'NA': ValProp(0.,float),
                       'T_p': ValProp(0.,float),
                       'CrossSection': ValProp(0.,float),   #mm**2
                       'b': ValProp(0.,float),              #mm
                       'L1': ValProp(0.,float),             #mm
                       'L2': ValProp(0.,float),             #mm
                       'ISh': ValProp(0.,float),            #mm
                       'ISv': ValProp(0.,float),            #mm
                       'magn': ValProp(0.,float),
                       'gain': ValProp(0.,float),
                       'flux': ValProp(0.,float),           #ph/s
                       'diff_limit': ValProp(0.,float),     #mm
                       'dof': ValProp(0.,float),            #mm
                       'mb_dof': ValProp(0.,float),         #mm
                       'ISh_corr': ValProp(0.,float),       #mm
                       'ISv_corr': ValProp(0.,float),       #mm
                       'gain_corr': ValProp(0.,float)
                       }
        

        
