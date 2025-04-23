import numpy as np
import matplotlib.pyplot as plt
"""
展示频域零填充（Zero-Padding）和零交插（Zero-Interleaving）在时域的等效操作
"""
N = 64
t = np.linspace(0, 1, N)
x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

X = np.fft.fft(x)

# 零填充（频域延长时域）
L_pad = 128
X_pad = np.concatenate([X[:N//2], np.zeros(L_pad - N), X[N//2:]])
x_pad = np.fft.ifft(X_pad).real

# 零交插（频域提高时域分辨率）
L_inter = 128
X_inter = np.zeros(L_inter, dtype=complex)
X_inter[:N//2] = X[:N//2]                     
X_inter[-N//2:] = X[-N//2:]                   
x_inter = np.fft.ifft(X_inter).real           

fig, axs = plt.subplots(3, 1, figsize=(10, 6))
axs[0].plot(t, x, label='Original Signal')
axs[0].set_title('Original Signal (N=64)')
axs[1].plot(np.linspace(0, 1, L_pad), x_pad, label='Zero-Padding (L=128)')
axs[1].set_title('Time Extension via Zero-Padding')
axs[2].plot(np.linspace(0, 1, L_inter), x_inter, label='Zero-Interleaving (L=128)')
axs[2].set_title('Resolution Increase via Zero-Interleaving')
plt.tight_layout()
plt.show()