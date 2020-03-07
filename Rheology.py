#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Rheology:
    '''For rheology  calculation'''

    def __init__(self):
        # __coef  - conversion factor
        # __coef  - коэфициент перевода единиц
        self.__coef = 0.48
        # fann600 -
        self.rpm_600 = 0
        # fann300 -
        self.rpm_300 = 0
        # fann200 -
        self.rpm_200 = 0
        # fann100 -
        self.rpm_100 = 0
        # fann60 -
        self.rpm_60 = 0
        # fann30 -
        self.rpm_30 = 0
        # fann6 -
        self.rpm_6 = 0
        # fann3 -
        self.rpm_3 = 0
        # sns
        self.sns_10s = 0
        self.sna_10m = 0

    def sns_1(self):
        ''' For SNS  calculation'''
        return self.sns_10s * self.__coef, self.sns_10m * self.__coef

    def reo(self):
        PV = self.rpm_600 - self.rpm_300
        YV = (self.rpm_300 - PV) * self.__coef
        return PV, YV
