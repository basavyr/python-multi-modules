#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np


class Plot_Maker:

    @staticmethod
    def Operation(argx):
        try:
            op_x = np.sqrt(argx)
        except Exception:
            op_x = 0

        return op_x

    @staticmethod
    def Math_Function(data_set):
        try:
            assert len(data_set) > 0
        except AssertionError:
            return -1

        # define the mathematical operation to apply on the input data set
        f_data_set = list(map(Plot_Maker.Operation, data_set))
        return f_data_set
