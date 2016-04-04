'''
Created on 25.06.2015

@author: Woehnert
'''

# import the used classes
import Services.abbildungsgeometrie as abbildungsgeometrie
import Services.linse as linse
import Services.diffraction as diffraction
import Services.spline as spline
import Services.ioService as ioService
import Fachwerte.inputValues as inVal
import Fachwerte.outputValues as outVal
import UI.crlcalcUI as UI



class CrlcalcWerkzeug(object):
    '''
    Interface between GUI and Calculation
    This class holds objects from all classes necessary
    '''


    def __init__(self):
        '''
        Constructor for Main Class.
        Create Instances of all used Subclasses and displays the GUI
        '''
        # instance of values
        self.inVal = inVal.InputValues()
        self.outVal = outVal.OutputValues()
        
        # load custom start values
        io = ioService.IO
        io.loadFromFile(self.inVal, self.outVal)
        
        #instance of Gui and register as observer of the Gui
        self.gui = UI.Gui()
        self.gui.myobservable.registerObserver(self)
        
        # instance of spline
        self.spline = None
        self.calcNewSpline()
        
        # set Input and Output Values
        self.setInputParameters()
        self.calcNewWavelength()
        self.calcOutput()
        self.setOutputParameters()
        
        self.gui.Show()
        
    def observableChanged(self, reason): 
        """
        Called if gui changed.
        Proceeds with reasonable method due to reason
        @param reason: (String) defines the further procedure
        """
        if (reason == "onChangeMaterial"):
            if self.inVal.setValue('material_choice', self.gui.Box_Material.GetSelection()) == True:
                validness = self.calcNewSpline()
                self.FieldFactoring('material_choice', "Material files not found. No files for chosen index",
                                 successful = validness, color=False)
            else:
                self.gui.statusBarPush("invalid index", 'material_choice')
        elif (reason == "onEnergyChanged"):
            validness = self.calcNewEnergy()
            self.FieldFactoring('energy', "energy has not a valid value", successful=validness)
        elif (reason == "onCheckChanged"):
            self.calcCheckChanged()
            self.calcOutput()
        elif (reason == "onWChanged"):
            validness = self.calcWChanged()
            self.FieldFactoring('W', "W has not a valid value", successful=validness)
        elif (reason == "save"):
            io = ioService.IO
            io.saveToFile(self.inVal, self.outVal)
        else:
            validness = self.inVal.setValue(reason, self.gui.getFieldInputValue(reason))
            mymessage = reason + " has not a valid value"
            self.FieldFactoring(reason, message = mymessage, successful = validness)
                
    def FieldFactoring(self, myfield, message, successful=True, color=True):
        """
        Help method to deal with the consequences of user input
        @param myfield: (string) dict key for a gui object
        @param message: (string) message for the statusbar in case of invalid input
        @param successful: (bool) indicates value validness
        @param color: (bool) indicates if color of Field is changeable
        """
        if color == True:
            self.gui.setFieldValidnessIndicator(myfield, successful)
        if successful == True:
            self.gui.statusBarPop(myfield)
            if (myfield in ["density","delta","mu"]):
                self.calcOutputNoSpline()
            else:
                self.calcOutput()
        else:
            newmessage = message + " " + self.inVal.getValueRequirements(myfield)
            self.gui.statusBarPush(newmessage, myfield)
            
        
               
        
    def setInputParameters(self):
        """
        Set Input Parameters to the Fields of the Gui
        """
        Fields = self.gui.getFieldInputList()
        for bezeichner in Fields:
            self.gui.setFieldInputValue(bezeichner, self.inVal.getValueForUI(bezeichner))
            #Values set in self.inVal are always valid
            self.gui.setFieldValidnessIndicator(bezeichner, isValid=True)
            
    def setOutputParameters(self):
        """
        Set Output Parameters to the Fields of the Gui
        """
        Fields = self.gui.getFieldOutputList()
        for bezeichner in Fields:
            self.gui.setFieldOutputValue(bezeichner, self.outVal.getValueForUI(bezeichner))
      
    # Not used in any way. Maybe in case of debugging/refactoring         
#     def getInputParameters(self):
#         """
#         Get the Input Parameters from the Fields
#         and transfer them to the Input Values
#         """
#         Fields = self.gui.getFieldInputList()
#         for bezeichner in Fields:
#             if self.inVal.setValue(bezeichner, Fields[bezeichner].GetValue()) == False:
#                 print bezeichner + " hat keinen zulaessigen Wert"      
                
    def calcOutput(self):
        """ Provides inVal and Outval for spline, linse, abbgeo and dfrag calculation"""

        if self.spline.splinecalc(self.inVal, self.outVal) == False:
            print "Error in Spline. Parameters not settable"
            exit()
            
        temp_linse = linse.Linse()
        if temp_linse.calc(self.inVal, self.outVal) == False:
            print "Error in Linse. Parameters not settable"
            exit()
            
        temp_abbgeo = abbildungsgeometrie.Abbildungsgeometrie()
        if temp_abbgeo.calc(self.inVal, self.outVal) == False:
            print "Error in Abbildungsgeometrie. Parameters not settable"
            exit()
            
        temp_dfrag = diffraction.Diffraction()
        if temp_dfrag.calc(self.inVal, self.outVal) == False:
            print "Error in Diffraction. Parameters not settable"
            exit()
            
        self.setOutputParameters()
        
    def calcOutputNoSpline(self):
        """ Provides the outval Values for changes in density, delta or mu"""
        
        temp_linse = linse.Linse()
        if temp_linse.calc(self.inVal, self.outVal) == False:
            print "Error in Linse. Parameters not settable"
            exit()
            
        temp_abbgeo = abbildungsgeometrie.Abbildungsgeometrie()
        if temp_abbgeo.calc(self.inVal, self.outVal) == False:
            print "Error in Abbildungsgeometrie. Parameters not settable"
            exit()
            
        temp_dfrag = diffraction.Diffraction()
        if temp_dfrag.calc(self.inVal, self.outVal) == False:
            print "Error in Diffraction. Parameters not settable"
            exit()
            
        self.setOutputParameters()
            
    def calcNewSpline(self):
        """
        Creates Instance of class spline
        @return bool True, if object is created and data gained from files
        """
        self.spline = spline.SpLine(self.inVal, self.outVal)
        
        if (self.spline != None and self.spline.checkConstruction()):
            self.gui.setFieldInputValue('density',self.inVal.getValueForUI("density"))
            self.gui.setFieldInputValue('delta',self.inVal.getValueForUI("delta"))
            self.gui.setFieldInputValue('mu',self.inVal.getValueForUI("mu"))
            return True
        else:
            return False
        
        
    def calcNewEnergy(self):
        """
        Event Method for Energy change.
        - set wavelength
        - calculate new delta/mu values with help of spline instance
        - calculate new output values by calling onCalc method
        @return bool decides if energy value is valid
        """
        E = self.gui.getFieldInputValue('energy')
        
        if self.inVal.setValue("energy", E) == True:
            self.calcNewWavelength()
            self.spline.splinecalc(self.inVal, self.outVal)
            
            self.gui.setFieldInputValue('delta',self.inVal.getValueForUI("delta"))
            self.gui.setFieldInputValue('mu',self.inVal.getValueForUI("mu"))
            return True
        else:
            return False
        
    def calcNewWavelength(self):
        """
        Calculates wavelength from energy value
        """
        E = self.inVal.getValue('energy')
        abbgeo = abbildungsgeometrie.Abbildungsgeometrie()
        wl = abbgeo.getwavelength(E)
        
        #convert wavelength
        self.gui.setFieldInputValue('wavelength', "%.3g" % wl)
        
    def calcCheckChanged(self):
        """
        Event function for change of R0toW-Checkbox.
        Enables and disables R_0 Textfield and set value
        @return bool Always True because invalid inputs impossible
        """
        self.inVal.setValue("lockR0toW", self.gui.getFieldInputValue('lockR0toW') )
        if (self.inVal.getValue("lockR0toW") == True):
            self.inVal.setValue("R_0", "%.3g" % self.calcR0toW())
            self.gui.setFieldInputValue('R_0',self.inVal.getValueForUI("R_0"))
            self.gui.getFieldInputList()['R_0'].Enable(False)
        else:
            self.gui.getFieldInputList()['R_0'].Enable(True)
        return True
            
    def calcR0toW(self):
        """
        calculate R_0, if R_0 is correlated to W
        @return float correlated R_0
        """
        lens = linse.Linse()
        R = self.inVal.getValue("R")
        W = self.inVal.getValue("W")
        d = self.inVal.getValue("d")
        return lens.getR_0Lock(R,W,d)
            
        
    def calcWChanged(self):
        """
        Event function for change of W. If R_0 is locked to W, calculate new R_0
        @return bool decides if W value is valid
        """
        if self.inVal.setValue("W", self.gui.getFieldInputValue("W")) == True:
            if self.inVal.getValue("lockR0toW") == True:
                self.inVal.setValue("R_0", "%.3g" % self.calcR0toW())
                self.gui.setFieldInputValue("R_0", self.inVal.getValue("R_0"))
            return True
        else:
            return False
                     
        
    
        
