from numpy import *

N = 64 
L = 1
dx = L/N

phi = zeros(N+1)
new = zeros(N+1)
tmp = array([sin(pi*i*dx)/2 + sin(16*pi*i*dx)/2 for i in range(1,N)])
r0 = zeros(N+1)
r10 = zeros(N+1)
r100 = zeros(N+1)
r0[1:N] = tmp
resi = [0]
resi[0] = max(abs(tmp))

new = zeros(N+1)
for t in range(0,10000):
    for j in range(1,N):
        new[j] = (phi[j+1]+new[j-1]-dx**2*tmp[j-1])/2
    new[0] = new[N] = 0
    r = tmp-(new[0:N-1]-2*new[1:N]+new[2:N+1])/dx**2
    resi.append(max(abs(r)))
    phi = new
    if t == 10:
        r10[1:N] = r
    elif t == 100:
        r100[1:N] = r
    if(max(abs(r)) < 0.001):
        print("converge at {} iterations".format(t))
        break

import matplotlib.pyplot as plt

plt.figure()
plt.plot(range(len(resi)),resi,'+-')
plt.xlabel('Number of Iterations')
plt.ylabel('max(|r_j|)')
plt.title('Convergence Curve')

plt.figure()
x = linspace(0,1,N+1)
plt.plot(x,r0,'-',x,r10,'+-',x,r100,'x-')
plt.legend(['0 iterations','10 iterations','100 iterations'])
plt.xlabel('x_j')
plt.ylabel('r_j')
plt.title('r_j against x_j')
plt.show()