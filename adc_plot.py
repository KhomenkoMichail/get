import matplotlib.pyplot as plot


def plot_vol_vs_time(time, vol, max_vol):
    plot.figure(figsize = (10, 6))
    plot.plot(time, vol)
    plot.xlabel("Time, s")
    plot.ylabel("Voltage, V")
    plot.grid()
    plot.show()


def plot_hist(time):
    hs = []
    for i in range(1, len(time)):
        hs.append(time[i] - time [i - 1])
    plot.figure(figsize = (10, 6))
    plot.hist(hs)
    plot.xlabel("Time, s")
    plot.ylabel("Amnt")
    plot.grid()
    plot.show()
