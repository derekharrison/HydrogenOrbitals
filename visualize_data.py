import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

grid_data_file = 'grid_data.txt'
nr, ntheta, nphi, max_pd, max_real = np.genfromtxt(grid_data_file, unpack=True)

nr = int(nr)
ntheta = int(ntheta)
nphi = int(nphi)

num_data_file = 'data.txt'
X, Z, Psi_sq = np.genfromtxt(num_data_file, unpack=True)

num_data_file = 'data_real.txt'
X_r, Z_r, Psi_r = np.genfromtxt(num_data_file, unpack=True)

num_data_file = 'data_im.txt'
X_im, Z_im, Psi_im = np.genfromtxt(num_data_file, unpack=True)

num_data_file = 'data_real_phi_2.txt'
X_r_phi_2, Y_r_phi_2, Psi_r_phi_2 = np.genfromtxt(num_data_file, unpack=True)

num_data_file = 'data_im_phi_2.txt'
X_r_phi_2_im, Y_r_phi_2_im, Psi_r_phi_2_im = np.genfromtxt(num_data_file, unpack=True)

X_2d = np.zeros((nr, nphi))
Z_2d = np.zeros((nr, nphi))
Psi_sq_2d = np.zeros((nr, nphi))

X_2d_m = np.zeros((nr, nphi))
Z_2d_m = np.zeros((nr, nphi))
Psi_sq_2d_m = np.zeros((nr, nphi))

X_r_2d = np.zeros((nr, nphi))
Z_r_2d = np.zeros((nr, nphi))
Psi_r_2d = np.zeros((nr, nphi))

X_r_2d_m = np.zeros((nr, nphi))
Z_r_2d_m = np.zeros((nr, nphi))
Psi_r_2d_m = np.zeros((nr, nphi))

X_im_2d = np.zeros((nr, nphi))
Z_im_2d = np.zeros((nr, nphi))
Psi_im_2d = np.zeros((nr, nphi))

X_im_2d_m = np.zeros((nr, nphi))
Z_im_2d_m = np.zeros((nr, nphi))
Psi_im_2d_m = np.zeros((nr, nphi))

X_r_phi_2_2d = np.zeros((nr, ntheta))
Y_r_phi_2_2d = np.zeros((nr, ntheta))
Psi_r_phi_2_2d = np.zeros((nr, ntheta))

X_r_phi_2_2d_im = np.zeros((nr, ntheta))
Y_r_phi_2_2d_im = np.zeros((nr, ntheta))
Psi_r_phi_2_2d_im = np.zeros((nr, ntheta))

num = 0
for i in range(0, nr):
    for j in range(0, nphi):
        X_2d[i][j] = X[num]
        Z_2d[i][j] = Z[num]
        Psi_sq_2d[i][j] = Psi_sq[num]

        X_r_2d[i][j] = X_r[num]
        Z_r_2d[i][j] = Z_r[num]
        Psi_r_2d[i][j] = Psi_r[num]        

        X_im_2d[i][j] = X_im[num]
        Z_im_2d[i][j] = Z_im[num]
        Psi_im_2d[i][j] = Psi_im[num] 
        
        num = num + 1 

for i in range(0, nr):
    for j in range(0, nphi):
        X_2d_m[i][j] = X[num]
        Z_2d_m[i][j] = Z[num]
        Psi_sq_2d_m[i][j] = Psi_sq[num]

        X_r_2d_m[i][j] = X_r[num]
        Z_r_2d_m[i][j] = Z_r[num]
        Psi_r_2d_m[i][j] = Psi_r[num]

        X_im_2d_m[i][j] = X_im[num]
        Z_im_2d_m[i][j] = Z_im[num]
        Psi_im_2d_m[i][j] = Psi_im[num]        
        
        num = num + 1

X_t = np.zeros((2*nr, nphi))
Z_t = np.zeros((2*nr, nphi))
Psi_p = np.zeros((2*nr, nphi))

X_r_t = np.zeros((2*nr, nphi))
Z_r_t = np.zeros((2*nr, nphi))
Psi_r_t = np.zeros((2*nr, nphi))

X_im_t = np.zeros((2*nr, nphi))
Z_im_t = np.zeros((2*nr, nphi))
Psi_im_t = np.zeros((2*nr, nphi))

for i in range(0, nr):
    for j in range(0, nphi):
        X_t[i][j] = X_2d[i][j]
        Z_t[i][j] = Z_2d[i][j]
        Psi_p[i][j] = Psi_sq_2d[i][j]

        X_r_t[i][j] = X_r_2d[i][j]
        Z_r_t[i][j] = Z_r_2d[i][j]
        Psi_r_t[i][j] = Psi_r_2d[i][j]

        X_im_t[i][j] = X_im_2d[i][j]
        Z_im_t[i][j] = Z_im_2d[i][j]
        Psi_im_t[i][j] = Psi_im_2d[i][j]

for i in range(0, nr):
    for j in range(0, nphi):
        X_t[i+nr][j] = X_2d_m[i][j]
        Z_t[i+nr][j] = Z_2d_m[i][j]
        Psi_p[i+nr][j] = Psi_sq_2d_m[i][j]

        X_r_t[i+nr][j] = X_r_2d_m[i][j]
        Z_r_t[i+nr][j] = Z_r_2d_m[i][j]
        Psi_r_t[i+nr][j] = Psi_r_2d_m[i][j]

        X_im_t[i+nr][j] = X_im_2d_m[i][j]
        Z_im_t[i+nr][j] = Z_im_2d_m[i][j]
        Psi_im_t[i+nr][j] = Psi_im_2d_m[i][j]        

num = 0
for i in range(0, nr):
    for j in range(0, ntheta):
        X_r_phi_2_2d[i][j] = X_r_phi_2[num]
        Y_r_phi_2_2d[i][j] = Y_r_phi_2[num]
        Psi_r_phi_2_2d[i][j] = Psi_r_phi_2[num]

        X_r_phi_2_2d_im[i][j] = X_r_phi_2_im[num]
        Y_r_phi_2_2d_im[i][j] = Y_r_phi_2_im[num]
        Psi_r_phi_2_2d_im[i][j] = Psi_r_phi_2_im[num]
        
        num = num + 1
        
        
cont = plt.contourf(X_t, Z_t, Psi_p, linspace(0, max_pd, 300), cmap = 'RdBu')
#cont = plt.contourf(X_r_t, Z_r_t, Psi_r_t, linspace(-max_real, max_real, 300), cmap = 'RdBu')
#cont = plt.contourf(X_im_t, Z_im_t, Psi_im_t, linspace(-max_real, max_real, 300), cmap = 'RdBu')
#cont = plt.contourf(X_r_phi_2_2d, Y_r_phi_2_2d, Psi_r_phi_2_2d, linspace(-max_real, max_real, 300), cmap = 'RdBu')
#cont = plt.contourf(X_r_phi_2_2d_im, Y_r_phi_2_2d_im, Psi_r_phi_2_2d_im, linspace(-max_real, max_real, 300), cmap = 'RdBu')

plt.colorbar()
plt.xlabel("X")
plt.ylabel("Z")

plt.show()
