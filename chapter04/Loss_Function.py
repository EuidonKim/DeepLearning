import numpy as np

def SSE(y,t):
    return 0.5*np.sum((y-t)**2)

def CEE(y,t):
    return -np.sum(t*np.log(y+1e-7))    ##1e-7은 log function이 -inf으로 발산하지 않게 막아주는 값