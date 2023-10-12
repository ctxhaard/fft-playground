#!/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt

def main():
    plt.style.use('seaborn-v0_8-poster')

    sr = 2000
    ts = 1/sr
    t = np.arange(0, 10, ts)

    wave = lambda freq, ampl, phase = 0: ampl*np.sin(phase + 2*np.pi*freq*t)

    x = wave(10, 3)
    x += wave(40, 2, np.pi/4)
    x += wave(70, 0.5, np.pi/3)
    x += wave(90, 1, np.pi/2)
    x += wave(100, 1)

    x = x * np.hanning( x.size )

    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.ylabel('Amplitude')
    plt.plot(t, x, 'r')

    

    X = np.fft.fft(x) # the FFT
    N = len(X) # the bins number
    n = np.arange(N) # the bin indexes
    T = N/sr # the sampling period
    
    freq = n/T # the sampling frequencies

    plt.subplot(132)
    plt.stem(freq, np.abs(X), 'b', markerfmt=' ', basefmt='-b')
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)')
    plt.xlim(0, 200)

    plt.subplot(133)
    plt.stem(freq, np.angle(X), 'b', markerfmt=' ', basefmt='-b')
    plt.xlabel('Freq (Hz)')
    plt.ylabel('Phase')
    plt.xlim(0, 100)


    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
