#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Rheology:
    '''For rheology  calculation'''

    def __init__(self):
        # __coef  - conversion factor
        # __coef  - коэфициент перевода единиц
        self.__coef = 0.48
        # fann600 -
        self.rpm_600 = rpm_600
        # fann300 -
        self.rpm_300 = rpm_300
        # fann200 -
        self.rpm_200 = rpm_00
        # fann100 -
        self.rpm_100 = rpm_100
        # fann60 -
        self.rpm_60 = rpm_60
        # fann30 -
        self.rpm_30 = rpm_0
        # fann6 -
        self.rpm_6 = rpm_6
        # fann3 -
        self.rpm_3 = rpm_3

    def sns(self, sns):
        ''' For SNS  calculation'''
        return sns * self.__coef
