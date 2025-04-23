import numpy as np
import matplotlib.pyplot as plt

# 生成滤波器系数示例
freq = np.fft.fftfreq(64)[:32]  # 取正频率部分
H_real = np.exp(-freq**2 * 100)  # 高斯型实部
H_imag = 0.1 * np.sin(2 * np.pi * 10 * freq)  # 正弦型虚部
H = H_real + 1j * H_imag

# 绘制滤波器系数
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
axs[0].plot(freq, np.abs(H), label='Magnitude')
axs[0].set_xlabel('Frequency (Hz)')
axs[0].set_ylabel('|H[k]|')
axs[0].set_title('Filter Magnitude Response')
axs[1].plot(freq, np.angle(H), label='Phase')
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('∠H[k] (rad)')
axs[1].set_title('Filter Phase Response')
plt.tight_layout()
plt.show()