import numpy as np

S = np.array([[4410000*4410000, 4410000, 1],
            [4830000*4830000,4830000,1],
            [5250000*5250000,5250000,1]])

P = np.array([[1165978],
            [1329190],
            [1501474]])

notZero = 1e-15 
S = np.array(S,dtype=float) 


SP = np.concatenate((S,P),axis=1)
augmented_matrix = np.copy(SP)


size = np.shape(SP)
n = size[0]
m = size[1]


for i in range(0,n-1):

    col = abs(SP[i:,i])
    max = np.argmax(col)

    if (max !=0):
        temp = np.copy(SP[i,:])
        SP[i,:] = SP[max+i,:]
        SP[max+i,:] = temp
        
partial_Pivot_Rows = np.copy(SP)


for i in range(0,n-1):
    pivot = SP[i,i]
    foward = i + 1
    for k in range(foward,n,1):
        factor = SP[k,i]/pivot
        SP[k,:] = SP[k,:] - SP[i,:]*factor
backward_elimination = np.copy(SP)

last_row = n-1
last_col = m-1
for i in range(last_row,-1,-1):
    pivot = SP[i,i]
    backwards = i-1 
    for k in range(backwards,-1,-1):
        factor = SP[k,i]/pivot
        SP[k,:] = SP[k,:] - SP[i,:]*factor
    SP[i,:] = SP[i,:]/SP[i,i]
X = np.copy(SP[:,last_col])
X = np.transpose([X])


print('Matriz aumentada:')
print(augmented_matrix)
print('Pivoteo parcial por filas')
print(partial_Pivot_Rows)
print('eliminacion hacia adelante')
print(backward_elimination)
print('eliminación hacia atrás')
print(SP)
print('solución de X: ')
print(X)

value=5000000
total_value=value*value*X[0]+value*X[1]+X[2]
print('El valor total es ')
print (total_value)