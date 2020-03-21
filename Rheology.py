#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math


class Rheology:
    '''
    For rheology  calculation

    '''

    def __init__(self):
        '''
        __coef  - conversion factor
        __coef  - коэфициент перевода единиц
        '''

        self.__coef = 0.48
        self._dict = {}

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

        try:
            plastic_viscosity = data['600'] - data['300']
            self._dict['plastic_viscosity'] = plastic_viscosity

            yield_point = (data['300'] - plastic_viscosity) * self.__coef
            self._dict['yield_point'] = yield_point

            yield_stress = 2 * data['3'] - data['6']
            self._dict['yield_stress'] = yield_stress

            flow_index = 3.32 * \
                math.log10((data['600'] - yield_stress) /
                           (data['300'] - yield_stress))
            self._dict['flow_index'] = flow_index

            consistency_index = (
                data['300'] - yield_stress) / math.pow(511, flow_index)
            self._dict['consistency_index'] = consistency_index

            return self._dict
        except Exception as e:
            print(f'\nОшибка: {e}\n')
            return self._dict

    def powerLowModel(self, data):
        '''Power Low Model'''

        self._dict = {}
        try:
            plastic_viscosity = data['600'] - data['300']
            self._dict['PV'] = plastic_viscosity

            yield_point = (data['300'] - plastic_viscosity) * self.__coef
            self._dict['YP'] = yield_point

            yield_stress = 2 * data['3'] - data['6']
            self._dict['ys'] = yield_stress

            '''For Pipe flow'''

            pipe_flow_index = 3.32 * \
                math.log10(data['600'] / data['300'])
            self._dict['pfi'] = pipe_flow_index

            pipe_flow_consistency_index = (
                data['300']) / math.pow(511, pipe_flow_index)
            self._dict['pfci'] = pipe_flow_consistency_index

            '''For Annular flow  '''
            annular_flow_index = 3.32 * \
                math.log10((data['600'] - yield_stress) /
                           (data['300'] - yield_stress))
            self._dict['afi'] = annular_flow_index

            annular_flow_consistency_index = (
                data['300'] - yield_stress) / math.pow(511, annular_flow_index)
            self._dict['afci'] = annular_flow_consistency_index

            return self._dict

        except Exception as e:
            print(f'\nОшибка: {e}\n')
            return self._dict

    def binghamModel(self, data):
        '''Bingham Model'''

        self._dict = {}
        try:
            plastic_viscosity = data['600'] - data['300']
            self._dict['PV'] = plastic_viscosity

            yield_point = (data['300'] - plastic_viscosity) * self.__coef
            self._dict['YP'] = yield_point

            yield_stress = 2 * data['3'] - data['6']
            self._dict['ys'] = yield_stress

            '''For Pipe flow'''

            pipe_flow_index = 3.32 * \
                math.log10(data['600'] / data['300'])
            self._dict['pfi'] = pipe_flow_index

            pipe_flow_consistency_index = (
                data['300']) / math.pow(511, pipe_flow_index)
            self._dict['pfci'] = pipe_flow_consistency_index

            '''For Annular flow  '''
            annular_flow_index = 3.32 * \
                math.log10((data['600'] - yield_stress) /
                           (data['300'] - yield_stress))
            self._dict['afi'] = annular_flow_index

            annular_flow_consistency_index = \
                (data['300'] - yield_stress) / math.pow(511, annular_flow_index)
            self._dict['afci'] = annular_flow_consistency_index

            return self._dict

        except Exception as e:
            print(f'\nОшибка: {e}\n')
            return self._dict
        pass

    def sns_1(self, data):
        ''' For SNS  calculation'''
        _sns = {}
        sns_10s = data['sns_10s'] * self.__coef
        _sns['sns_10s'] = sns_10s
        sns_10m = data['sns_10m'] * self.__coef
        _sns['sns_10m'] = sns_10m
        return _sns

    def hydro(self, data):
        try:
            '''Проводим расчёт для трубного пространства'''

            '''Расчитываем срднюю скорость
            Fluid velocity Pipe/ Скорость потока в трубном пространстве'''
            velocity_pipe = 24.21 * data['Q'] / math.pow(data['di'], 2)
            self._dict['Vp'] = velocity_pipe

            '''Hydraulic diameter Pipe'''
            Dhydp = data['di']
            self._dict['Dhydp'] = Dhydp

            '''Shear rate pipe / расчитываем скорость сдвига у стенок трубы, с-1'''
            yp = ( (3 * self._dict['pipe_flow_index'] + 1) / (4 * self._dict['pipe_flow_index']) ) \
                 * (8 * velocity_pipe / data['dh'] )
            self._dict['yp'] = yp

            '''effective viscosity / Определяем эффективную вязкость'''
            mea = (self._dict['pfci'] * math.pow(yp, self._dict['pipe_flow_index'])) / yp
            self._dict['mea'] = mea

            '''Определяем режим течения'''
            Re = (data['dh'] * velocity_pipe * data['g']) / mea
            self._dict['Re'] = Re



            '''Проводим расчёт для кольцевого пространства'''
            '''Fluid velocity Annulus/ Скорость потока в кольцвом пространстве'''
            velocity_annulus = 24.21 * \
                data['Q'] / (math.pow(data['dh'], 2) - math.pow(data['dp'], 2))
            self._dict['Va'] = velocity_annulus


            '''Hydraulic diameter Annulus '''
            Dhyda = data['dh'] - data['dp']
            self._dict['Dhyda'] = Dhyda



            return self._dict

        except Exception as e:
            print(f'\nОшибка: {e}\n')
            return self._dict
