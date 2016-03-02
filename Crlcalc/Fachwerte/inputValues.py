'''
Created on 25.06.2015

@author: Woehnert
'''
from .values import Values
from .valProp import ValProp

class InputValues(Values):
    '''
    Saves Input Values in a dictionary. Inherits functionality from values.Fachwerte
    '''

    def __init__(self):
        '''
        Auto-creates all input values
        @note: delta and mu are still divided by density. 
        @note: Raw values appear in Services
        '''
        # Initial Fachwerte
        self.params = {'energy': ValProp(15000.0, float, 499., 200001.),        #eV
                       'wavelength': ValProp(0., float),                        #Angstroem
                       'b_v': ValProp(0.060, float, min_value=0.),               #mm
                       'b_h': ValProp(0.700, float, min_value=0.),               #mm
                       'g': ValProp(41000., float),                             #mm
                       'dpsf': ValProp(0., float),                              #mm
                       'intensity': ValProp(1e12, float),                       #ph/s/mm**2
                       'R': ValProp(0.2, float, min_value=0.),                                #mm
                       'R_0': ValProp(0.447, float, min_value=0.),                            #mm
                       'lockR0toW': ValProp(False, bool),
                       'material_choice': ValProp(3, int, min_value=-1, max_value=14),
                       'density': ValProp(1., float, min_value=0.),                           #g/cm**3
                       'delta': ValProp(1., float, min_value=0.),                             #cm**3/g
                       'mu': ValProp(1., float, min_value=0.),                                #cm**2/g
                       'N': ValProp(50, int, min_value = 0),
                       'd': ValProp(0.010, float),                              #mm
                       'rough': ValProp(0.1, float),                            #mm
                        'W': ValProp(1., float)                                 #mm
                       }
