import scipy.signal as signal
import numpy as np
import pylab as pl

fs = 100
fc1 = 9
fc2 = 10
fc3 = 11
fc4 = 12

length = 41

b = signal.remez(length, (0,fc1/fs,fc2/fs,0.5), (1,0) ,(1,100))
w, h = signal.freqz(b, 1)
pl.plot(fs*w/2/np.pi, 20*np.log10(np.abs(h)), label=str(length))
pl.legend()
pl.show()


# def h_ideal(n, fc):
#     return 2*fc*np.sinc(2*fc*np.arange(-n, n, 1.0))

# b = h_ideal(30, 0.25) # 以fs正规化的频率
# b2 = signal.firwin(len(b), 0.5) # 以fs/2正规化的频率

# w, h = signal.freqz(b)
# w2, h2 = signal.freqz(b2)

# pl.figure(figsize=(8,6))
# pl.subplot(211)
# pl.plot(w/2/np.pi, 20*np.log10(np.abs(h)), label=u"h_ideal")
# pl.plot(w2/2/np.pi, 20*np.log10(np.abs(h2)), label=u"firwin")
# pl.xlabel(u"正规化频率 周期/取样")
# pl.ylabel(u"幅值(dB)")
# pl.legend()
# pl.subplot(212)
# pl.plot(b, label=u"h_ideal")
# pl.plot(b2, label=u"firwin")
# pl.legend()
# pl.show()