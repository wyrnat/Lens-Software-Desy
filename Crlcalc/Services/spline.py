import os
import string

class SpLine(object):
    '''
    Support Class for calculating mu and delta values out of material choice
    '''


    def __init__(self, inVal, outVal):
        """
        Init Methods reads out material files and writes all values to lists
        >> In case of Material Change, a new instance of spline has to be called
        >> In case of Energy Change, the method calcSpline has to be called
        """
        
        # Read-out values from .dat-file
        self.delta_values = []
        self.mu_values = []
        self.energy_values = []
        
        
        # location of material files
        path = os.getcwd() + "/Services/elementdata/"
        
        # lists of material files
        delta_fileList = ["AlD.dat", "AlOD.dat", "BD.dat", "BeD.dat",
                          "B4CD.dat", "CD.dat", "LiD.dat",
                          "LiFD.dat", "MgD.dat", "NiD.dat",
                          "PCD.dat", "PEEKD.dat", "SiD.dat"
                          ]
        mu_fileList = ["AlMu.dat", "AlOMu.dat", "BMu.dat", "BeMu.dat",
                          "B4CMu.dat", "CMu.dat", "LiMu.dat",
                          "LiFMu.dat", "MgMu.dat", "NiMu.dat",
                          "PCMu.dat", "PEEKMu.dat", "SiMu.dat"
                          ]
        density_list = [ 2.6941, 3.97, 2.34, 1.845,
                        2.45, 2.26, 0.533, 2.635,
                        1.845, 8.876, 1.20, 1.3, 2.32 ]
        
        
        # import delta values
        try:
            f_delta = open(path + delta_fileList[inVal.getValue('material_choice')], 'r')
        except:
            print "import Error: delta-File (*) not found"
            print "Expected (*): "+ path + delta_fileList[inVal.getValue('material_choice')]
            exit()
            
        lines_delta = f_delta.readlines()
            
        delta_values = []
        for lines in lines_delta:
            delta_values += string.split(lines, ",")
        for i in range(len(delta_values)):
            delta_values[i] = float(string.strip(delta_values[i]))
            
        self.delta_values = delta_values
        
        f_delta.close()
        
        # import mu values
        try:
            f_mu = open(path + mu_fileList[inVal.getValue('material_choice')], 'r')
        except:
            print "import Error: mu-File (*) not found"
            print "Expected (*): " + path + mu_fileList[inVal.getValue('material_choice')]
            exit()
            
        lines_mu = f_mu.readlines()
            
        mu_values = []
        for lines in lines_mu:
            mu_values += string.split(lines, ",")
        for i in range(len(mu_values)):
            mu_values[i] = float(string.strip(mu_values[i]))
            
        self.mu_values = mu_values
        
        f_mu.close()
        
        # import energy values
        try:
            f_e = open(path + "energy.dat", 'r')
        except:
            print "import Error: energy File not found"
            exit()
            
        lines_e = f_e.readlines()
            
        e_values = []
        for lines in lines_e:
            e_values += string.split(lines, ",")
        for i in range(len(e_values)):
            e_values[i] = float(string.strip(e_values[i]))
            
        self.energy_values = e_values
        
        f_e.close()
        
        # set density
        inVal.setValue("density", density_list[inVal.getValue('material_choice')] )
        
        #Calculate Fachwerte for main init
        self.splinecalc(inVal, outVal)
        
    def checkConstruction(self):
        """ Returns True, if all values are correctly imported from file"""
        if (self.delta_values != [] and self.mu_values != [] and self.energy_values != []):
            return True
        else:
            return False
        
        

    def splinecalc(self, inVal, outVal):
        """
        interface for calculating delta mu values from Combobox choice and energy
        """
        delta = self.calcLinearSpline(inVal.getValue('energy'), self.delta_values) / inVal.getValue('density')
        mu = self.calcLinearSpline(inVal.getValue('energy'), self.mu_values) / inVal.getValue('density')

        return ( inVal.setValue('delta', delta) and inVal.setValue('mu', mu ) )
        
        
    def getNearestXvalue(self, x, up = 0):
        """
        Returns the interval the actual x value is in between.
        x = given value
        up = 0: returns lower interval limit
        up = 1: returns upper interval limit
        """
        for i, value in enumerate(self.energy_values):
            if (value > x):
                return i-1 + up
            
        return len(self.energy_values)-1
            
    
    def calcLinearSpline(self, x, value_list):
        """
        returns the interpolated Output Value out of lists of Fachwerte for given Energy with linear Spline.
        """
        i = self.getNearestXvalue(x)
        
        try:
            Xi = self.energy_values[self.getNearestXvalue(x)]
            Xj = self.energy_values[self.getNearestXvalue(x, up=1)]
        except:
            print "Value Error: energy value out of Range"
            return -1
        #assert (Xj != Xi), "Interval length is zero. Energy value out of "
        
        A = (Xj - x)/(Xj -Xi)/1.
        B = (x - Xi)/(Xj -Xi)/1.
        
        F_x = A * value_list[i] + B * value_list[i+1]
        
        return F_x
        
    def calcCubicSpline(self, x, value_list):
        #TODO aus Lecture Funktion einarbeiten
        pass     
        
    