#!/usr/bin/env python

import sys
from scipy import io
import pandas as pd
import numpy as np
import pylab

def process_temp(matfile, outcsv):

    #load matlab file
    mat = io.loadmat(matfile)

    #extract and prefix column names
    hist_names = ['hist_{}'.format(model[0]) for model in mat['models'].flatten()]
    rcp45_names = ['rcp45_{}'.format(model[0]) for model in mat['models'].flatten()]
    rcp85_names = ['rcp85_{}'.format(model[0]) for model in mat['models'].flatten()]

    #extract years
    hist_years = mat['yrs_hist'].flatten()
    future_years = mat['yrs_futr'].flatten()

    #extract data and attach column and row names
    hist = pd.DataFrame(mat['tas_historical_yrly'], columns=hist_names, index=hist_years)
    rcp45 = pd.DataFrame(mat['tas_rcp45_yrly'], columns=rcp45_names, index=future_years)
    rcp85 = pd.DataFrame(mat['tas_rcp85_yrly'], columns=rcp85_names, index=future_years)

    # compute ensemble means
    hist['AVG_HIST'] = np.mean(hist,1)
    rcp45['AVG_RCP45'] = np.mean(rcp45,1)
    rcp85['AVG_RCP85'] = np.mean(rcp85,1)

    # compute baseline
    baseline = np.mean(hist['AVG_HIST'])

    # join dataframes
    joined = hist.join(rcp45, how='outer').join(rcp85)

    # convert from deg C to deg F and compute difference from baseline
    joined = (joined - baseline) * 9 / 5.0 + 32

    # plot test chart
    pylab.plot(joined.index, joined['AVG_HIST'], '-')
    pylab.plot(joined.index, joined['AVG_RCP45'], '-')
    pylab.plot(joined.index, joined['AVG_RCP85'], '-')
    pylab.show()

    # dump csv
    joined.index.name = 'year'
    joined.to_csv(outcsv)

if __name__ == "__main__":
    process_temp(*sys.argv[1:])
