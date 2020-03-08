#!/usr/bin/python3
# -*- coding: utf-8 -*-


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

    def reo(self):
        pv = self.rpm_600 - self.rpm_300
        yv = (self.rpm_300 - pv) * self.__coef
        return pv, yv
