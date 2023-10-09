#!/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.style.use('seaborn-v0_8-poster')

    sr = 2000
    ts = 1.0/sr
    t = np.arange(0, 1, ts)

    wave = lambda freq, ampl: ampl*np.sin(2*np.pi*freq*t)

    x = wave(1, 3)
    x += wave(4, 2)
    x += wave(7, 0.5)
    x += wave(9, 1)

    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.ylabel('Amplitude')
    plt.plot(t, x, 'r')

    X = np.fft.fft(x)
    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T

    plt.subplot(122)
    plt.stem(freq, np.abs(X), 'b', markerfmt=' ', basefmt='-b')
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)')
    plt.xlim(0,10)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
