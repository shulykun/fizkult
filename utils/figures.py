import numpy as np
from datetime import datetime
from joblib import Parallel, delayed


def draw_mp(i,di):
    
    pixels_in_line = 0
    pixels_per_line = []

    
    dr = (di / 2)

    for j in range(di):
        x = i - dr
        y = j - dr
        if np.abs(x **dg)+ np.abs(y **dg) <= dr ** dg:
            pixels_in_line += 1
        else:
            pass
    pixels_per_line.append(pixels_in_line)
    pixels_in_line = 0
    
    return pixels_per_line


def draw(di,n_jobs):

    results = Parallel(n_jobs=n_jobs)(delayed(draw_mp)(i,di) for i in range(di))
    
    return [i[0] for i in results]
     