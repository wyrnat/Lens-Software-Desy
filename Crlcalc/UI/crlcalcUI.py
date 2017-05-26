'''
Created on 02.07.2015

@author: Woehnert
'''

from gui_builder import BuilderFrame
from UI import observable
from wx import ToolTip

class Gui(BuilderFrame):
    """
    Inherits from the GuiBilder-Frame
    Holds all Fields and objects related to User Interface
    Implements Event Metods
    """

    def __init__(self):
        """
        Initialize superclass and creates Object from observable
        """
        
        BuilderFrame.__init__(self,parent=None)

        #Watch Out, double connection!
        self.myobservable = observable.Observable()
        
        #set the Frame title to show actual Version name
        self.SetTitle("CrlCalc - Version 2.51 (26.5.2017) - Created by Jannik Woehnert")
        
        #StatusBar
        self.StatusBar.PushStatusText("Ready!")
        self.statusSource = []
        self.statusMessage = []
        
        #Disable all output fields
        for field in self.getFieldOutputList():
            self.getFieldOutputList()[field].Enable(False)
            self.getFieldOutputList()[field].SetBackgroundColour('white')
        self.getFieldInputList()['wavelength'].Enable(False)
        self.getFieldInputList()['wavelength'].SetBackgroundColour('white')


    def getFieldInputList(self):
        """
        Returns a List of the Input Field Objects
        @return: List<TextCtrl> A list of the Fields
        """
        FieldInput_List = {'energy': self.Field_Energy,
                           'wavelength': self.Field_WaveLength,
                           'b_v': self.Field_SSv,
                           'b_h': self.Field_SSh,
                           'g': self.Field_g,
                           'intensity': self.Field_Intensity,
                           'dpsf': self.Field_dpsf,
                           'density':self.Field_Density,
                           'delta': self.Field_delta,
                           'mu': self.Field_mu,
                           'R': self.Field_R,
                           'R_0': self.Field_R_0,
                           'lockR0toW': self.Check_RWLock,
                           'd': self.Field_d,
                           'N': self.Field_N,
                           'rough': self.Field_rough,
                           'W': self.Field_W
                           }
        return FieldInput_List
    
    def getFieldInputValue(self, name):
        """
        Returns the value of the Field corresponding to name
        @param name: (String) the key for the dictionary 'list'
        @return: The Value of the Field corresponding to name
        """
        
        return self.getFieldInputList()[name].GetValue()
    
    def setFieldInputValue(self, name, val):
        """
        sets the value of the Field corresponding to name
        @param name: (String) the key for the dictionary 'list'
        @param val: The value to be set
        """
        if name != 'lockR0toW':
            val = str(val)
        else:
            val = bool(val)
            
        self.getFieldInputList()[name].SetValue(val)
    
    def getFieldOutputList(self):
        """
        Returns a List of the Output Field Objects
        @return: List<TextCtrl> A list of the Fields
        """
        FieldOutput_List = {'f': self.Field_f,
                            'H': self.Field_H,
                            'Deff': self.Field_Deff,
                            'NA': self.Field_NA,
                            'T_p': self.Field_Tp,
                            'CrossSection': self.Field_CrossSection,
                            'b': self.Field_b,
                            'L1': self.Field_L1,
                            'L2': self.Field_L2,
                            'ISh': self.Field_ISh,
                            'ISv': self.Field_ISv,
                            'magn': self.Field_magn,
                            'gain': self.Field_gain,
                            'flux': self.Field_flux,
                            'diff_limit': self.Field_DiffLimit,
                            'dof': self.Field_dof,
                            'mb_dof': self.Field_mdof,
                            'ISh_corr': self.Field_IShCorr,
                            'ISv_corr': self.Field_ISvCorr,
                            'gain_corr': self.Field_gainCorr
                            }
        return FieldOutput_List
    
    def getFieldOutputValue(self, name):
        """
        Returns the value of the Field corresponding to name
        @param name: (String) the key for the dictionary 'list'
        @return: The Value of the Field corresponding to name
        """
        return self.getFieldOutputList()[name].GetValue()
    
    def setFieldOutputValue(self, name, val):
        """
        sets the value of the Field corresponding to name
        @param name: (String) the key for the dictionary 'list'
        @param val: The value to be set
        """
        self.getFieldOutputList()[name].SetValue(str(val))
        
    def setFieldOutTooltip(self, name, mytooltip):
        """
        Sets the tooltip of the OutputField
        @param name: (String) the key for the dictionary 'list'
        @param tooltip: (str) Information about the field parameter
        """
        self.getFieldOutputList()[name].SetToolTip(ToolTip(mytooltip))
        
    def setFieldInTooltip(self, name, mytooltip):
        """
        Sets the tooltip of the InputField
        @param name: (String) the key for the dictionary 'list'
        @param tooltip: (str) Information about the field parameter
        """
        self.getFieldInputList()[name].SetToolTip(ToolTip(mytooltip))
    
    def setFieldValidnessIndicator(self, myField, isValid=True):
        """
        change the Foreground color respective
        to the validness of the latest input change
        @param myField: (String) key of the Field to be changed
        @param isValid: decides which color should be set
        """
        Field = self.getFieldInputList()[myField]
        if isValid==True:
            Field.SetForegroundColour((0,0,0))
        else:
            Field.SetForegroundColour((255,0,0))
            
    """ Status Bar """
    
    def statusBarPush(self, s, field):
        """
        saves message and cause to an array.
        pushes message to statusbar stack
        @param s: (string) message
        @param field: (string) key for a Field in the dictionary
        """
        if s != self.StatusBar.GetStatusText():
            self.statusSource.append(field)
            self.statusMessage.append(s)
            self.StatusBar.PushStatusText(s)
        
    def statusBarPop(self, field):
        """
        delete the statusbar stack.
        delete all entries in the array related to the field
        refill the stack with the cleared array
        @param field: (string) key for a Field in the dictionary
        """
        index_list = []
        for i, myfield in enumerate(self.statusSource):
            if field == myfield:
                index_list.append(i)
        index_list.reverse()
        
        for i in index_list:
            self.statusSource.pop(i)
            self.statusMessage.pop(i)
        self.refreshStatusBar()
                
    def refreshStatusBar(self):
        """
        Help method for statusBarPop
        deleting and refilling the stack
        """
        e = self.StatusBar.GetStatusText()
        while e != "Ready!":
            self.StatusBar.PopStatusText()
            e = self.StatusBar.GetStatusText()
            
        for text in self.statusMessage:
            self.StatusBar.PushStatusText(text)


    """ Event Handling """       
            
    def onCheckChanged(self, event):
        self.myobservable.informObserver("onCheckChanged")

    
    def onEnergyChanged(self, event):
        self.myobservable.informObserver("onEnergyChanged")

    
    def onChangeMaterial(self, event):
        self.myobservable.informObserver("onChangeMaterial")
        
    def onDensityChange(self, event):
        self.myobservable.informObserver("density")
        
    def onDeltaChanged(self, event):
        self.myobservable.informObserver("delta")
        
    def onmuChanged(self, event):
        self.myobservable.informObserver("mu")
        
    def onSSHChanged(self, event):
        self.myobservable.informObserver("b_h")
    def onSSVChanged(self, event):
        self.myobservable.informObserver("b_v")
        
    def ongChanged(self, event):
        self.myobservable.informObserver("g")
        
    def onIChanged(self, event):
        self.myobservable.informObserver("intensity")
        
    def ondpsfChanged(self, event):
        self.myobservable.informObserver("dpsf")
        
    def onRChanged(self, event):
        self.myobservable.informObserver("R")
        
    def onR_0Changed(self, event):
        self.myobservable.informObserver("R_0")
        
    def ondChanged(self, event):
        self.myobservable.informObserver("d")
        
    def onNChanged(self, event):
        self.myobservable.informObserver("N")
        
    def onroughnessChanged(self, event):
        self.myobservable.informObserver("rough")
        
    def onWChanged(self, event):
        self.myobservable.informObserver("W")
        
    def onSave(self, event):
        self.myobservable.informObserver("save")
        
        
        
