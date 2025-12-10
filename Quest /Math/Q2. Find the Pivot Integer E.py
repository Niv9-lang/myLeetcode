
import numpy as np
def pivotInteger(n: int) -> int:
    if np.sqrt((n**2+n)/2)-int(np.sqrt((n**2+n)/2))==0:
        return int(np.sqrt((n**2+n)/2))
    return -1
    
print(pivotInteger(8))

"""
La formule utilisée découle de pure math
"""
