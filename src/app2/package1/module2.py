#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import os


class Plot_Maker:

    @staticmethod
    def Test():
        mseg = f'function {Plot_Maker.Test.__name__}() from  {os.path.basename(__file__)} inside Package-1'
        return mseg

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
            return None

        # define the mathematical operation to apply on the input data set
        f_data_set = list(map(Plot_Maker.Operation, data_set))
        return f_data_set

    @staticmethod
    def Create_Data_Set():
        try:
            x_data_set = np.arange(0, 110, 10)
            fx_data_set = Plot_Maker.Math_Function(x_data_set)
        except Exception:
            result = [None, None]
        else:
            result = [x_data_set, fx_data_set]
        return result

    @staticmethod
    def Make_Plot(plot_file):
        do_plot = 0

        try:
            data = Plot_Maker.Create_Data_Set()
            assert type(data[0]) != None and type(data[1]) != None
        except AssertionError:
            do_plot = 0
        else:
            do_plot = 1

        x = data[0]
        y = data[1]

        if(do_plot):
            try:
                plt.plot(x, y, '-or', label=r'f(x)')
                plt.legend(loc='best')
                plt.xlabel(r'x')
                plt.ylabel(r'f(x)')
                plt.savefig(plot_file, bbox_inches='tight')
                plt.close()
            except Exception:
                return -1
            else:
                return 1
        else:
            return -1


def Main():
    print(Plot_Maker.Test())


if __name__ == '__main__':
    Main()
