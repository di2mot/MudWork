#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Rheology:
    '''For rheokogy  calculation'''

    def __init__(self):
        # __coef  - conversion factor
        # __coef  - коэфициент перевода единиц
        self.__coef = 0.48

    def sns(self, sns):
        ''' For SNS  calculation'''
        return sns * self.__coef
