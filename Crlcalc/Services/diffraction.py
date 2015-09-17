'''
Created on 16.07.2015

@author: Woehnert
'''

import numpy

class Diffraction(object):
    '''
    Calculate the diffraction corrected values
    
    Values needed for calculation:
    --Input Values: f, g, b_v, b_h, R_0, R, N, delta, T, Energy, Deff
    --Output Values: diff_limit_corr, bgv_corr, bgh_corr, NA_corr
    --Abbildungsgeometrie: diff_limit (uncorrelated)
    
    Returned Values: dof, mb_dof, Isv_corr, ISh_corr, gain_corr
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def calc(self, inVal, outVal):
        
        # used input values
        R_0 = inVal.getValue('R_0')
        
        #TODO: klaeren, wann diff_limit_corr und wann diff_limit
        diff_limit_corr = outVal.getValue('diff_limit')
        bgv_corr = outVal.getValue('ISv')
        bgh_corr = outVal.getValue('ISh')
        NA_corr = outVal.getValue('NA')
        T = outVal.getValue('T_p')
        
        dof = self.getDOF_corr(diff_limit_corr, NA_corr)
        mb_dof = self.getDOF_Microbeam_corr(diff_limit_corr, bgh_corr, bgv_corr, NA_corr)
        ISv_corr = self.getBbgv_corr(diff_limit_corr, bgv_corr)
        ISh_corr = self.getBbgh_corr(diff_limit_corr, bgh_corr)
        gain_corr = self.getBgain_corr(diff_limit_corr, bgh_corr, bgv_corr, R_0, T)
        
        if (
            outVal.setValue('dof', dof) and
            outVal.setValue('mb_dof', mb_dof) and
            outVal.setValue('ISv_corr', ISv_corr) and
            outVal.setValue('ISh_corr', ISh_corr) and
            outVal.setValue('gain_corr', gain_corr)
            ):
            return True
        else:
            return False
                               

    """Help Methods"""
        
    def calcBGain(self, R_0, T, Bbgv, Bbgh):
        return 4 * T * R_0**2 / Bbgv / Bbgh
    
    def calcRMS(self, sigma):
        return sigma / 2. / float( numpy.sqrt(2 * numpy.log(2)) )

    def calcRMS_u(self, NA, Bbgv, Bbgh):
        """boolean expression as integer: if true, expression equals 1, else 0"""
        return((Bbgv >= Bbgh) * self.calcRMS(Bbgh / NA)
                + (Bbgv < Bbgh) * self.calcRMS(Bbgv / NA)
                )
    def calcBbg(self, diff_limit, bg, dpsf = 0):
        return float( numpy.sqrt(diff_limit ** 2 + bg ** 2 + dpsf ** 2) )
    
    """Return Methods"""
        
    def getBbgv_corr(self, diff_limit_corr, bgv_corr):
        return self.calcBbg(diff_limit_corr, bgv_corr)
    
    def getBbgh_corr(self, diff_limit_corr, bgh_corr):
        return self.calcBbg(diff_limit_corr, bgh_corr)
    
    def getBbgv(self, diff_limit, bgv):
        return self.calcBbg(diff_limit, bgv)
    
    def getBbgh(self, diff_limit, bgh):
        return self.calcBbg(diff_limit, bgh)

    def getBbgvDpsf_corr(self, diff_limit_corr, bgv_corr, dpsf):
        return self.calcBbg(diff_limit_corr, bgv_corr, dpsf)
    
    def getBbghDpsf_corr(self, diff_limit_corr, bgh_corr, dpsf):
        return self.calcBbg(diff_limit_corr, bgh_corr, dpsf)
        
    def getBbgvDpsf(self, diff_limit, bgv, dpsf):
        return self.calcBbg(diff_limit, bgv, dpsf)
    
    def getBbghDpsf(self, diff_limit, bgh, dpsf):
        return self.calcBbg(diff_limit, bgh, dpsf)
    
    
    def getBgain_corr(self, diff_limit_corr, bgh_corr, bgv_corr, R_0, T):
        Bbgh_corr = self.getBbgh_corr(diff_limit_corr, bgh_corr)
        Bbgv_corr = self.getBbgv_corr(diff_limit_corr, bgv_corr)
        return self.calcBGain(R_0, T, Bbgv_corr, Bbgh_corr)
    
    def getBgain(self, diff_limit, bgh, bgv, R_0, T):
        Bbgh = self.getBbgh_corr(diff_limit, bgh)
        Bbgv = self.getBbgv_corr(diff_limit, bgv)
        return self.calcBGain(R_0, T, Bbgv, Bbgh)
    
    def getBgainDpsf_corr(self, diff_limit_corr, bgh_corr, bgv_corr, dpsf, R_0, T):
        BbghDpsf_corr = self.getBbgh_corr(diff_limit_corr, bgh_corr, dpsf)
        BbgvDpsf_corr = self.getBbgv_corr(diff_limit_corr, bgv_corr, dpsf)
        return self.calcBGain(R_0, T, BbgvDpsf_corr, BbghDpsf_corr)
    
    def getBgainDpsf(self, diff_limit, bgh, bgv, dpsf, R_0, T):
        BbghDpsf = self.getBbgh_corr(diff_limit, bgh, dpsf)
        BbgvDpsf = self.getBbgv_corr(diff_limit, bgv, dpsf)
        return self.calcBGain(R_0, T, BbgvDpsf, BbghDpsf)
    
    def getDOF_corr(self, diff_limit_corr, NA_corr):
        assert (NA_corr!=0), "NA_corr = 0 leads to divison by zero"
        return 4 * self.calcRMS(diff_limit_corr / NA_corr)
    
    def getDOF(self, diff_limit, NA):
        assert (NA!=0), "NA=0 leads to division by zero"
        return 4 * self.calcRMS(diff_limit / NA)
    
    def getDOF_Microbeam_corr(self, diff_limit_corr, bgh_corr, bgv_corr, NA_corr):
        Bbgh_corr = self.getBbgh_corr(diff_limit_corr, bgh_corr)
        Bbgv_corr = self.getBbgv_corr(diff_limit_corr, bgv_corr)
        return 4 * self.calcRMS_u(NA_corr, Bbgv_corr,Bbgh_corr)
    
    def getDOF_Microbeam(self, diff_limit, bgh, bgv, NA):
        Bbgh = self.getBbgh_corr(diff_limit, bgh)
        Bbgv = self.getBbgv_corr(diff_limit, bgv)
        return 4 * self.calcRMS_u(NA, Bbgv,Bbgh)
    
    
    