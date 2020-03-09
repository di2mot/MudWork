#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import numpy

class Rheology:
    '''For rheology  calculation'''

    def __init__(self, kwargs):

        # __coef  - conversion factor
        # __coef  - коэфициент перевода единиц
        self.__coef = 0.48
        # fann600 -
        self.rpm_600 = kwargs['600 prm']
        # fann300 -
        self.rpm_300 = kwargs['300 prm']
        # fann200 -
        self.rpm_200 = kwargs['200 prm']
        # fann100 -
        self.rpm_100 = kwargs['100 prm']
        # fann60 -
        # self.rpm_60 = kwargs['60 prm']
        # # fann30 -
        # self.rpm_30 = kwargs['30 prm']
        # fann6 -
        self.rpm_6 = kwargs['6 prm']
        # fann3 -
        self.rpm_3 = kwargs['3 prm']


    def sns_1(self, sns_10s, sns_10m):
        ''' For SNS  calculation'''
        return sns_10s * self.__coef, sns_10m * self.__coef

    def reo(self, model = 'hb'):
        ''' Type of models:
Bingham Plastic Model (bingham)—This model describes fluids in which the shear stress/shear rate ratio is linear
once a specific shear stress has been exceeded.

Power Law (power_low) —The Power Law is used to describe the flow of shear thinning or pseudoplastic drilling
fluids.

Herschel-Bulkley Model (bh) —Also called the “modified” power law and yield-pseudoplastic model, the
Herschel-Bulkley model is used to describe the flow of pseudoplastic drilling fluids which require a yield stress to
initiate flow. Defoult model
        '''
        _list = {}
        if model == 'hb':

            plastic_viscosity = self.rpm_600 - self.rpm_300
            _list['plastic_viscosity'] = plastic_viscosity

            yield_point = (self.rpm_300 - plastic_viscosity) * self.__coef
            _list['yield_point'] = yield_point

            yield_stress = 2*self.rpm_3 - self.rpm_6
            _list['yield_stress'] = yield_stress

            flow_index = 3.32*math.log10((self.rpm_600- yield_stress)/(self.rpm_300 - yield_stress))
            _list['flow_index'] = flow_index

            consistency_index = (self.rpm_300 - yield_stress)/511**flow_index
            _list['consistency_index'] = consistency_index

            return _list

        elif model == 'power_low':

            plastic_viscosity = self.rpm_600 - self.rpm_300
            _list['plastic_viscosity'] = plastic_viscosity

            yield_point = (self.rpm_300 - plastic_viscosity) * self.__coef
            _list['yield_point'] = yield_point

            yield_stress = 2 * self.rpm_3 - self.rpm_6
            _list['yield_stress'] = yield_stress

            _list.append(plastic_viscosity, yield_point, yield_stress)

            '''For Pipe flow'''
            pipe_flow_flow_index = 3.32 * math.log10((self.rpm_600) / (self.rpm_300))
            _list['pipe_flow_flow_index'] = pipe_flow_flow_index

            pipe_flow_consistency_index = (self.rpm_300) / 511 ** pipe_flow_flow_index
            _list['pipe_flow_consistency_index'] = pipe_flow_consistency_index

            '''For Annular flow  '''
            annular_flow_flow_index = 3.32 * math.log10((self.rpm_600 - yield_stress) / (self.rpm_300 - yield_stress))
            _list['annular_flow_flow_index'] = annular_flow_flow_index

            annular_flow_consistency_index = (self.rpm_300 - yield_stress) / 511 ** annular_flow_flow_index
            _list['annular_flow_consistency_index'] = annular_flow_consistency_index

            return _list

