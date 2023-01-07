from numpy import *
N = 64
L = 1
h = L/N
phi = zeros(N+1)
f = array([sin(pi*i*h)/2 + sin(16*pi*i*h)/2 for i in range(0,N+1)])

def smoothing(phi,f,h)->array:
    N = len(phi)-1
    res = zeros(N+1)
    for j in range(1,N):
        phi[j+1]
        res[j] = (phi[j+1]+res[j-1]-h**2*f[j])/2
    return res

def restriction(r)->array:
    N = int((len(r)-1)/2)
    res = zeros(N+1)
    for j in range(2,N+1):
        res[j-1] = (r[2*j-3]+2*r[2*j-2]+r[2*j-1])/4
    return res

def prolongation(eps)->array:
    N = (len(eps)-1)*2
    res = zeros(N+1)
    for j in range(2,N+1,2):
        res[j-1] = (eps[int(j/2-1)]+eps[int(j/2)])/2
    for j in range(1,N+2,2):
        res[j-1] = eps[int((j+1)/2-1)]
    return res

def residual(phi,f,h)->array:
    N = len(phi)-1
    res = zeros(N+1)
    res[1:N] = f[1:N]-(phi[0:N-1]-2*phi[1:N]+phi[2:N+1])/h**2
    return res

def V_Cycle(phi,f,h):
    phi = smoothing(phi,f,h)
    r = residual(phi,f,h)
    rhs = restriction(r)
    eps = zeros(len(rhs))
    if len(eps)-1 == 2:
        eps = smoothing(eps,rhs,2*h)
    else:
        eps = V_Cycle(eps,rhs,2*h)
    phi = phi + prolongation(eps)
    phi = smoothing(phi,f,h)
    return phi

resi = []
for cnt in range(0,1001):
    phi = V_Cycle(phi,f,h)
    r = residual(phi,f,h)

    r_disp = max(abs(r))
    resi.append(r_disp)
    print("cnt: {}  r_disp: {}\n".format(cnt,r_disp))
    if max(abs(r)) < 0.001:
        print("converge at {} iterations".format(cnt*10))
        break

import matplotlib.pyplot as plt
plt.figure()
plt.plot(arange(len(resi))*10,resi,'+-')
plt.xlabel('Number of Iterations')
plt.ylabel('max(|r_j|)')
plt.title('Convergence Curve')
plt.show()