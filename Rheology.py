#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math


class Rheology:
    '''For rheology  calculation'''

    def __init__(self):
        '''
        __coef  - conversion factor
        __coef  - коэфициент перевода единиц
        '''

        self.__coef = 0.48


        ''' Type of models:
 0 - Bingham Plastic Model (bh)—This model describes fluids in which
the shear stress shear rate ratio is linear
once a specific shear stress has been exceeded.

1 - Power Law (pl) —The Power Law is used to describe the flow of
shear thinning or pseudoplastic drilling fluids.

2 - Herschel-Bulkley Model (hb) —Also called the “modified” power law and
yield-pseudoplastic model, the Herschel-Bulkley model is used to describe
the flow of pseudoplastic drilling fluids which require a yield stress
to initiate flow. Defoult model
        '''

    def hbModel(self, data):
        '''Herschel-Bulkley Model'''

        _dict = {}
        try:
            plastic_viscosity = data['600'] - data['300']
            _dict['plastic_viscosity'] = plastic_viscosity

            yield_point = (data['300'] - plastic_viscosity) * self.__coef
            _dict['yield_point'] = yield_point

            yield_stress = 2 * data['3'] - data['6']
            _dict['yield_stress'] = yield_stress

            flow_index = 3.32 * \
                math.log10((data['600'] - yield_stress) /
                           (data['300'] - yield_stress))
            _dict['flow_index'] = flow_index

            consistency_index = (
                data['300'] - yield_stress) / math.pow(511, flow_index)
            _dict['consistency_index'] = consistency_index

            return _dict
        except Exception as e:
            print(f'\nОшибка: {e}\n')
            return _dict

    def powerLowModel(self, data):
        '''Power Low Model'''

        _dict = {}
        try:
            plastic_viscosity = data['600'] - data['300']
            _dict['plastic_viscosity'] = plastic_viscosity

            yield_point = (data['300'] - plastic_viscosity) * self.__coef
            _dict['yield_point'] = yield_point

            yield_stress = 2 * data['3'] - data['6']
            _dict['yield_stress'] = yield_stress

            '''For Pipe flow'''

            pipe_flow_flow_index = 3.32 * \
                    math.log10(data['600'] / data['300'])
            _dict['pipe_flow_flow_index'] = pipe_flow_flow_index

            pipe_flow_consistency_index = (
                    data['300']) / math.pow(511, pipe_flow_flow_index)
            _dict['pipe_flow_consistency_index'] = pipe_flow_consistency_index

            '''For Annular flow  '''
            annular_flow_index = 3.32 * \
                    math.log10((data['600'] - yield_stress) /
                               (data['300'] - yield_stress))
            _dict['annular_flow_index'] = annular_flow_index

            annular_flow_consistency_index = (
                    data['300'] - yield_stress) / math.pow(511, annular_flow_index)
            _dict['afci'] = annular_flow_consistency_index

            try:
                '''Расчитываем срднюю скорость'''
                '''Fluid velocity'''
                velocity_pipe = 24.21 * data['Q'] / math.pow(data['di'], 2)
                _dict['Vp'] = velocity_pipe

                '''Fluid velocity'''
                velocity_annulus = 24.21 * data['Q'] / (math.sqrt(data['dh']) - math.pow(data['dp'], 2))
                _dict['Va'] = velocity_annulus

                '''Hydraulic diameter'''

                '''Hydraulic diameter Pipe'''
                Dhydp = data['di']
                _dict['Dhydp'] = Dhydp

                '''Hydraulic diameter Annulus '''
                Dhyda = data['dh'] - data['dp']
                _dict['Dhyda'] = Dhyda

                return _dict
            except Exception as e:
                print(f'\nОшибка: {e}\n')
                return _dict




            return _dict
        except Exception as e:
            print(f'\nОшибка: {e}\n')
            return _dict


    def sns_1(self, data):
        ''' For SNS  calculation'''
        _sns = {}
        sns_10s = data['sns_10s'] * self.__coef
        _sns['sns_10s'] = sns_10s
        sns_10m = data['sns_10m'] * self.__coef
        _sns['sns_10m'] = sns_10m
        return _sns
