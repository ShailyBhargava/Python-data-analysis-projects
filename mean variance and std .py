import numpy as np
def calculate(input):
    if len(input) != 9:
        raise ValueError("list must contain nine numbers.")
    a =np.array(input).reshape(3,3)
   # print (a)
    #print(a.mean(0),a.mean(1),a.mean())

    cal =dict()
    cal['mean'] =[a.mean(0).tolist(),a.mean(1).tolist(),a.mean().tolist()]
    cal['standard deviation'] =[a.std(0).tolist(),a.std(1).tolist(),a.std().tolist()]
    cal['max'] =a.max(0).tolist(),a.max(1).tolist(),a.max().tolist()
    cal['min'] =a.min(0).tolist(),a.min(1).tolist(),a.min().tolist()
    cal['variance'] =a.var(0).tolist(),a.var(1).tolist(),a.var().tolist()
    cal['sum'] =a.sum(0).tolist(),a.sum(1).tolist(),a.sum().tolist()
    return cal
print(calculate([0,1,2,3,4,5,6,7,8]))

