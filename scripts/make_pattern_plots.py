import pickle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

def get_r(x,y):
    '''Get r from x and y.'''
    return np.sqrt(np.power(x,2) + np.power(y,2))

def plot_pattern(pattern, hex_id):
    fig,ax = plt.subplots(1,1,figsize = (9,9))
    ax.set_title('Pattern interpolation\n(spline, k=3)')
    _x = np.arange(-100,100,0.1)
    _y = np.arange(-100,100,0.1)
    _xx,_yy = np.meshgrid(_x,_y, indexing='ij')
    _rr = get_r(_xx,_yy)
    _xx = _xx[_rr < 100]
    _yy = _yy[_rr < 100]
    _zz = pattern.ev(_xx,_yy)
    interpolated = ax.scatter(_xx, _yy, c=np.log10(_zz), marker = 's',
                              s = 5,vmin = -6.2)

    ax.add_patch(Circle((0,0),75, color = 'r',fill = False, linewidth = 1, 
                        ls ='--', label = 'TPC'))
    ax.set_aspect('equal')
    fig.colorbar(interpolated, ax = ax)
    ax.legend()
    
    plt.savefig('figures/patterns/hex_%d' %hex_id)
    
    return None

### MAIN ###
for hex_id in range(1):
    with open('patterns/hex_%d.pck'%hex_id, 'rb') as file:
        boop = pickle.load(file)
        
    plot_pattern(boop, hex_id)