""" Libraries """
try:
    import wx
except:
    print "wx package missing. Please install wxPython"
    exit()
try:
    import numpy
except:
    print "numpy Package missing. Please install numpy"
    exit()
    
try:
    import scipy
except:
    print "scipy Package missing. Please install scipy"
    exit()
    
""" Packages """
    
try:
    from Fachwerte import inputValues, outputValues, valProp, values
except:
    print "Fachwerte or Fachwert Class missing"
    exit()

try:
    from Services import spline, abbildungsgeometrie, diffraction, linse, ioService
except:
    print "Services or Service Class missing. Please add the package or the file to the path"
    exit()
    
try:
    from UI import crlcalcUI, gui_builder, observable
except:
    print "UI missing or UI class missing. PLease add the Package or the file to the path"
    exit()

try:
    from Werkzeuge import crlcalcWerkzeug
except:
    print "crlcalcWerkzeug missing. Maybe in another directory?"
    exit()


"""
TODO: Bilder auf Homepage
"""

app = wx.PySimpleApp()
instance_of_Werkzeug = crlcalcWerkzeug.CrlcalcWerkzeug()
app.MainLoop()
