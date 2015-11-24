'''
Created on 2.06.2015

@author: Woehnert
'''

import linse
import numpy

class Abbildungsgeometrie(object):

    def __init__(self):
        pass

#         self.b_v = b_v  # Image size vertical
#         self.b_h = b_h  # Image size horizontal
#         self.g = g  # distance source to lens mirror plane >> L1
#         self.energy = energy  # light energy
#         self.dpsf = dpsf  # detector point spread function
#         self.intensity = intensity  # intensity before lens
#         self.delta = delta  # index of refraction: real part
#         self.mu = mu  # index of refraction: imaginary part


        # self.gain >> gain >> 'gain'
        # self.flux >> flux in microbeam >> 'flux'
        # self.bgv >> image size: vertical >> 'ISv'
        # self.bgh >> image size: horizontal >> 'ISh'
        # self.imDistance >> image distance (former babst) >> 'L2
        # self.ds >> diffraction slices (former beug = beugungsscheibchen) >> 'diff_limit'
        
        # self.Bbgv >> theoretical image size (vertical) after correction by diffraction (psf) >> 'ISv_corr'
        # self.Bbgh >> theoretical image size (horizontal) after correction by diffraction (psf) >> 'ISh_corr'
        # self.BbgvDpsf >> -"- (dpsf)
        # self.BbghDpsf >> -". (dpsf)
        
        # self.Bgain >> therorethical gain after correction by diffraction (psf) >> 'gain_corr'
        # self.BgainDpsf >> therorethical gain after correction by diffraction (dpsf)
        
        # self.mag >> magnification of the image setup
        # self.wavelength >> energy shown as wavelength
        # self. effectivity >> Quantum effictivity of setup for X-ray tube
        # self.NA >> Numeric aperture
        # self.DOF >> Depth of field
        # TODO Was ist der microbeam
        # self.DOF_microbeam >> 
        
        



    # TODO: Corr und Uncorr trennen -> reduzierung der Zustandsfelder um 50%
    def calc(self, inVal, outVal):
        
        # used input Values
        energy = inVal.getValue('energy')
        b_v = inVal.getValue('b_v')
        b_h = inVal.getValue('b_h')
        g = inVal.getValue('g')
        intensity = inVal.getValue('intensity')
        R_0 = inVal.getValue('R_0')
        
        # used output values
        f_corr = outVal.getValue('f') #TODO check
        T = outVal.getValue('T_p')
        H = outVal.getValue('H')
        Deff = outVal.getValue('Deff')
        sigma = outVal.getValue('CrossSection')
        
        # create the values to override Output Values
        b = self.getb_corr(f_corr, g, H)
        L1 = self.getL1(g, H)
        L2 = self.getL2_corr(f_corr, g)
        ISh = self.getbgh_corr(f_corr, L1, b_h)
        ISv = self.getbgv_corr(f_corr, L1, b_v)
        magn = self.getmag_corr(L1, L2)
        gain = self.getgain_corr(R_0, f_corr, T, g, b_v, b_h)
        flux = self.getflux(sigma, intensity)
        NA = self.getNa_corr(f_corr, g, Deff)
        diff_limit = self.getdiff_limit_corr(energy, f_corr, g, Deff)
        
        #TODO: if Bedingung ueberdenken. Schlechte Fehlerbehandlung. Werte werden uU. nicht belegt
        if (
            outVal.setValue('b', b) and
            outVal.setValue('L1', L1) and
            outVal.setValue('L2',L2) and
            outVal.setValue('ISh', ISh) and
            outVal.setValue('ISv', ISv) and
            outVal.setValue('magn', magn) and
            outVal.setValue('gain', gain) and
            outVal.setValue('flux', flux) and
            outVal.setValue('NA', NA) and
            outVal.setValue('diff_limit', diff_limit)
            ):
            return True
        else:
            return False
        

    def getgain_corr(self, R_0, f_corr, T, g, b_v, b_h):
        return self.calcGain(R_0, f_corr, T, g, b_v, b_h)
    
    def getgain(self, R_0, T, g, b_v, b_h, R, N, delta):
        f = linse.Linse.getf(R, N, delta)
        return self.calcGain(R_0, f, T, g, b_v, b_h)  
    
    def getflux(self, sigma, intensity):
        return sigma * intensity
    
    def getbgv_corr(self, f_corr, L1, b_v):
        return self.calcImageSize(f_corr, L1, b_v)
        
    def getbgh_corr(self, f_corr, L1, b_h):
        return self.calcImageSize(f_corr, L1, b_h)
        
    def getbgv(self, g, b_v, R, N, delta):
        f = linse.Linse.getf(R, N, delta)
        return self.calcImageSize(f, g, b_v)
        
    def getbgh(self, g, b_h, R, N, delta):
        f = linse.Linse.getf(R, N, delta)
        return self.calcImageSize(f, g, b_h)
        
    def getL1(self, g, H):
        return g - H
        
    # TODO: im Skript: Berechnung aus L1. Hier: Berechnung aus g ???
    def getL2_corr(self, f_corr, g):
        return self.calcImDist(f_corr, g)
        
    def getL2(self, g, R, N, delta):
        f = linse.Linse.getf(R, N, delta)
        return self.calcImDist(f, g)
        
    def getb_corr(self, f_corr, g, H):
        L2 = self.getL2_corr(f_corr, g)
        return L2 + H
    
    def getb(self, g, H, R, N, delta):
        f = linse.Linse.getf(R, N, delta)
        L2 = self.getL2(f, g)
        return L2 + H
    
    # Vorher imDistance_corr
    def getdiff_limit_corr(self, energy, f_corr, g, Deff):
        e2k = self.E2k(energy)
        L2_corr = self.getL2_corr(f_corr, g)
        return self.FWHM(2 / e2k * L2_corr/ Deff)
        
    def getdiff_limit(self, energy, g, Deff, R, N, delta):
        f = linse.Linse.getf(R, N, delta)
        e2k = self.E2k(energy)
        L2 = self.getL2(f, g)
        return self.FWHM(2 / e2k * L2/ Deff)
    
    def getmag_corr(self, L1, L2):
        return self.calcmag(L1, L2)
        
    def getmag(self, g, b):
        return self.calcmag(g, b)
        
    def getwavelength(self, energy):
        return self.calcLambda(energy)
        
    def geteffectivity(self, R_0, g, T):
        assert (g!=0), "g = 0 leads to division by zero"
        return (R_0 / g) ** 2 * T / 4.
        
    def getNa(self, g, Deff, R, N, delta):
        f = linse.Linse.getf(self, R, N, delta)
        L2 = self.getL2(f, g)
        return self.calcNA(Deff, L2)
        
    def getNa_corr(self, f_corr, g, Deff):
        L2_corr = self.getL2_corr(f_corr, g)
        return self.calcNA(Deff, L2_corr)

    # Help methods

    def calcGain(self, R_0, f, T, g, b_v, b_h):
        assert (b_v!=0), "b_v = 0 leads to division by zero"
        assert (b_h!=0), "b_h = 0 leads to division by zero"
        return 4 * R_0 ** 2 * T / b_v / b_h * (g - f) ** 2 / f ** 2

    def calcImageSize(self, f, L1, b_x):
        assert (f!=L1), "f=g leads to division by zero"
        return b_x * f / (L1 - f)

    def calcImDist(self, f, g):
        assert (f!=g), "f=g leads to divison by zero"
        return (g * f) / (g - f)

    def FWHM(self, s):
        """ Calculate Full Width Half Maximum from Sigma"""
        return (2 * s * float(numpy.sqrt(2 * numpy.log(2))))

    def E2k(self, e):
        """ Energy to mm^-1"""
        return 2 * numpy.pi * e * 10e7 / 12398.52

    def calcmag_alt(self, L1, f):
        assert (f!=0), "f = 0 leads to division by zero"
        mag = (L1 - f) / f
        return (mag >= 1) * mag + (mag < 1) / mag
    
    def calcmag(self, L1, L2):
        mag = L2/(L1*1.0)
        return (mag >= 1) * mag + (mag < 1) / mag

    def calcLambda(self, energy):
        assert (energy!=0), "energy=0 leads to division by zero"
        c = 2.9979 * 10e8
        h = 6.6256 * 10e-34
        eV = 1.602 * 10e-19
        return h * c * 10e10 / energy / eV

    def calcNA(self, deff, babst):
        assert (babst!=0), "image distance = 0 leads to division by zero"
        return deff / babst / 2.

