import numpy

class Linse (object):
    """
    Calculate all lens correlated Values
    Values needed for Calculation:
    --Input Values: energy, R, R_0, delta, mu, density, N, d, rough, W
    """

    def __init__(self):
        
        #self.calc(inVal, outVal)

        """Input Fachwerte"""
        # R >> Radius of curvature
        # R_0 >> Lens aperture
        # delta >> index of refraction: real part
        # mu >> index of refraction: imaginary part
        # N >> Number of lenses
        # d >> lens thickness at the tightest point
        # rough >> surface roughness of lens
        # energy >> light energy
        # W >> lens total thickness along beam axis
        
        """Output Fachwerte"""
        # f >> uncorrelated focal length 
        # f_corr >> correlated focal length >> 'f'
        # T >> Transmission per area >> 'T'
        # Tr >> all-of-lens transmission
        # a >> transmission exponent
        # a_eff >> effective aperture for absorption
        # D_eff >> effective aperture for diffraction and roughness >> 'Deff'
        # sigma >> cross section of the focus >> 'CrossSection'
        


    def calc(self, inVal, outVal):
        """
        calculate lens parameters. f, T, Tr, a, a_eff, D_eff, sigma
        Returns True if all parameters have been calulated
        """
        
        if (inVal==None or outVal==None):
            return False
        
        # local input variables for shorter calls
        energy = inVal.getValue('energy')
        R = inVal.getValue('R')
        R_0 = inVal.getValue('R_0')
        #TODO nachfragen
        delta = inVal.getValue('delta') * inVal.getValue('density')
        mu = inVal.getValue('mu') * inVal.getValue('density') /10. # factor 10 due to units [mm/cm]
        N = inVal.getValue('N')
        d = inVal.getValue('d')
        rough = inVal.getValue('rough')
        W = inVal.getValue('W')
        
        #local output variables for shorter call
        f = self.getf_corr(R, N, delta, W)
        H = self.getH(N, W, R, delta)
        Deff = self.getD_eff(mu, N, R, R_0, delta, rough, energy)
        T_p = self.getT(mu, N, R_0, R, d, delta, rough, energy)
        CrossSection = self.getsigma(mu, N, R_0, R, d, delta, rough, energy)
        
        
        # set output Values and return True if set sucessful
        if (
            outVal.setValue('f',f) and
            outVal.setValue('H', H) and # Wert muss noch ueberprueft werden
            outVal.setValue('Deff', Deff) and
            outVal.setValue('T_p',T_p) and
            outVal.setValue('CrossSection', CrossSection)
            ):
            return True
        else:
            return False

        
    # intermediate Methods
        
    def getAp(self, mu, N, R_0, R, delta, rough, energy):
        assert (R!=0), "R = 0 leads to division by zero"
        e2k = self.gete2k(energy)
        return mu * N * R_0**2 / 2. / R + N * delta * e2k * rough * (R_0/R)**2
    
    def gete2k(self, energy):
        return 2 * numpy.pi * energy / 12398.52 * 1e7
    
    def getDeff_part(self, mu, N, R, delta, rough, energy):
        e2k = self.gete2k(energy)
        return mu * N * R + 2*N*(e2k * delta * rough)**2
    
    # ---Methods---
        
    def getf(self, R, N, delta):
        assert (N!=0), "N = 0 leads to division by zero"
        assert (delta!=0), "delta = 0 leads to division by zero"
        #TODO: delta ohne dichte-normierung oder mit
        return R/(2. * N * delta)
    
    def getf_corr_approx(self, R, N, delta, W):
        f = self.getf(R, N, delta)
        assert (f!=0), "f = 0 leads to division by zero"
        assert (N**2 != 1 + 1/W), "Bad Luck, Choice of N and W leads to division by zero"
        return f / ( 1 - W * (N**2-1) / (6. * f * N ) )
    
    def getf_corr(self, R, N, delta, W):
        f = self.getf(R, N, delta)
        L = N*W
        assert (L > 0), "N*W needs to be bigger than 0"
        factor = float(numpy.sqrt(f/(L*1.0)))
        assert (factor % numpy.pi != 0), "sin(x) = 0 leads to division by zero"
        return float(L * factor / numpy.sin(1/factor))
    
    
    def getH(self, N, W, R, delta):
        f = self.getf(R, N, delta)
        assert (f!=0), "f=0 leads to division by zero"
        L = N * W
        return - L**2 / f / 24
    
    def getT(self, mu, N, R_0, R, d, delta, rough, energy):
        a_p = self.getAp(mu, N, R_0, R, delta, rough, energy)
        assert (a_p!=0), "a_p-Value = 0 leads to division by zero "
        return float( (numpy.exp(-mu * N * d) * (1 - numpy.exp(-2 * a_p)) / (2* a_p) ) )
        
    def getTr(self, mu, N, R_0, R, d, delta, rough, energy):
        return self.getT(mu, N, R_0, R, d, delta, rough, energy) * numpy.pi * R_0**2
    
    def geta(self, mu, N, R_0, R, delta, rough, energy):
        return self.getAp(mu, N, R_0, R, delta, rough, energy)
    
    def geta_eff(self, mu, N, R_0, R, delta, rough, energy):
        a_p = self.getAp(mu, N, R_0, R, delta, rough, energy)
        assert(a_p<0), "negative a_p-Value leads imaginary result"
        assert(mu>0), "mu has to be greater than zero"
        assert(N>0), "N has to be greater than zero"
        assert(R>=0), "R needs to be positive"
        return 2 * float( numpy.sqrt( R / mu / N *  (1 - numpy.exp(-a_p)) ) )
    
    def getD_eff_old(self, mu, N, R, R_0, delta, rough, energy):
        deff_part = self.getDeff_part(mu, N, R, delta, rough, energy)
        assert (deff_part>0), "deff_part has to be greater than zero"
        assert (R>=0), "R shall not be negative"
        return 2 * float( numpy.sqrt(2*R**2 / deff_part * (1 - numpy.exp(-deff_part / 2. * (R_0/R)**2)) ) )
    
    def getD_eff(self, mu, N, R, R_0, delta, rough, energy):
        a_p = self.getAp(mu, N, R_0, R, delta, rough, energy)
        return 2*R_0 * float( numpy.sqrt((1-numpy.exp(-a_p)) /a_p ) )
    
    def getsigma(self, mu, N, R_0, R, d, delta, rough, energy):
        T = self.getT(mu, N, R_0, R, d, delta, rough, energy)
        return numpy.pi * R_0**2 * T
                                    
    # get methods for important values
    def getR_0Lock(self, R, W, d):
        assert (W>=d), "negative squareroot due to W<d"
        return float(numpy.sqrt(R*(W-d)))                                                                        
