import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


def visualize(path: str):
    raw = wave.open(path)

    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype='int16')
    f_rate = raw.getframerate()

    time = np.linespace(0, len(signal)/f_rate, num=len(signal))

    plt.figure(1)

    plt.title('Sound Wave')

    plt.xlabel('Time')

    plt.plot(time, signal)

    plt.show()


if __name__ == '__main__':
    path = sys.argv[1]
    visualize(path)
    # I dont know why this is not Starting.........
