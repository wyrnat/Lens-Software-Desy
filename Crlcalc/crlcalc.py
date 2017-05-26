'''
Created on 3.06.2015

@author: Woehnert
'''
from Fachwerte import materials

print "start crlcalc.py"

""" Libraries """
print "--- load libraries ---"
wxbool = True
try:
    import wx
    print "using wxPython as User Interface"
except:
    print "wx package not found. Searching for PyQt4"
    print "QT-GUI not implemented yet"
    raw_input("close crlcalc...")
    exit()
    
""" Qt-GUI not yet implemented """
#     try:
#         import PyQt4
#         print "Using PyQT4 as User Interface"
#         wxbool = False
#     except:
#         print "wx and PyQt4 package missing. Please install wxPython or PyQt4"
#         exit()
#         
try:
    import numpy
except:
    print "numpy Package missing. Please install numpy"
    raw_input("close crlcalc...")
    exit()
    
    
try:
    import scipy
except:
    print "scipy Package missing. Please install scipy"
    raw_input("close crlcalc...")
    exit()
print "--- libraries check ---"
    
""" Packages """
print "--- load internal packages ---"

try:
    from Fachwerte import units, toolTips, materials
except:
    print "Error in import *Fachwerte* package"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Steps for Solution"
    print "1) Make sure that the files *units.py*, *materials.py* and *tooltips.py* exists"
    print "2) Check the code for logical and syntax errors"
    print "3) Check the internal imported packages for 1) and 2)"
    raw_input("close crlcalc...")
    exit()
    
try:
    from Materialien import inputValues, outputValues, valProp, values
except:
    print "Error in import *Materialien* package"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Steps for Solution"
    print "1) Make sure that the files *inputValues.py*, *outputValues.py*, *valProp.py* and *values.py* exists"
    print "2) Check the code for logical and syntax errors"
    print "3) Check the internal imported packages for 1) and 2)"
    raw_input("close crlcalc...")
    exit()

try:
    from Services import spline, abbildungsgeometrie, diffraction, linse, ioService
except:
    print "Error in import *Services* package"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Steps for Solution"
    print "1) Make sure that the files *spline.py*, *abbildungsgeometrie.py*, *diffraction.py*, *linse.py* and *ioService.py* exists"
    print "2) Check the code for logical and syntax errors"
    print "3) Check the internal imported packages for 1) and 2)"
    raw_input("close crlcalc...")
    exit()
    
try:
    if wxbool == True:
        from UI import crlcalcUI, gui_builder, observable
    else:
        from UI import qt_builder, crlcalcQT
except:
    print "Error in import *UI* package"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Steps for Solution"
    if wxbool == True:
        print "1) Make sure that the files *crlcalcUI.py*, *gui_builder.py* and *observable.py* exists"
    else:
        print "1) Make sure that the files *crlcalcQT.py* and *qt_builder.py* exists"
    print "2) Check the code for logical and syntax errors"
    print "3) Check the internal imported packages for 1) and 2)"
    raw_input("close crlcalc...")
    exit()

try:
    from Werkzeuge import crlcalcWerkzeug
except:
    print "Error in import *Werkzeuge* package"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Steps for Solution"
    print "1) Make sure that the files *crlcalcWerkzeug.py* exists"
    print "2) Check the code for logical and syntax errors"
    print "3) Check the internal imported packages for 1) and 2)"
    raw_input("close crlcalc...")
    exit()

print "--- internal packages check ---"

""" Check Files """
print "--- Check Files for Errors ---"
absolutlen = len(materials.material_list)
if (len(materials.delta_fileList) != absolutlen or
    len(materials.mu_fileList) != absolutlen or
    len(materials.density_list) != absolutlen
    ):
    print "Error in Fachwerte.materials:"
    print "Array length not synchronised"
    raw_input("close crlcalc...")
    exit()
    
print "--- Files check ---"


"""
TODO: alternativen W-Parameter einfuegen
TODO: QT-GUI
TODO: Manual schreiben
"""
if wxbool == True:
    app = wx.PySimpleApp()
    instance_of_Werkzeug = crlcalcWerkzeug.CrlcalcWerkzeug()
    app.MainLoop()
# else:
#     import sys
#     app = PyQt4.QtGui.QApplication(sys.argv)
#     form = crlcalcQT.CrlcalcQT()
#     form.show()
#     app.exec_()
