'''
Created on 02.03.2016

@author: jannik
'''

import os

class IO(object):
    '''
    Save and load values from data files
    '''
    

    @staticmethod
    def saveToFile(inval, outval):
        """
        Saves input and output values into a human and machine readable data file
        @param inval: input values
        @param outval: output values
        @note: creates file of "params.dat does not exists
        """
        path = os.getcwd()+"/Werkzeuge/params.dat"
        myfile = open(path, 'w+')
        
        # write the file
        myfile.write("***** Crlcalc Value File *****\n")
        myfile.write("\n> Input Values\n")
        for value in inval.params:
            myfile.write(value + "   " + str(inval.getValueForUI(value)) + "\n")
        myfile.write("\n> Output Values\n")
        for value in outval.params:
            myfile.write(value + "   " + str(outval.getValueForUI(value)) + "\n")
            
        myfile.close()
        
    @staticmethod
    def loadFromFile(inval, outval):
        """
        Load data into input Value object from data file
        @param inval: input values
        @param outval: output values
        @note: if file do not exists, method returns to the calling block
        """
        path = os.getcwd()+"/Werkzeuge/params.dat"
        if not os.path.exists(path):
            return
        myfile = open(path, 'r')
        
        # read from file
        data = myfile.readlines()
        for line in data:
            split = line.split('   ')
            if len(split) != 2:
                continue
            inval.setValue(split[0], split[1].strip('\n'))
            
        myfile.close()
            