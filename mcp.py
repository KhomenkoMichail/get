import mcp3021_driver as mcp
import adc_plot as plot
import time

max_vol = 5.15

mcp = mcp.MCP3021(max_vol)

vols = []

ts = []

duration = 5.0

if __name__ == "__main__":
    try:
        t = time.time()
        while time.time() - t <= duration:
            vols.append(mcp.get_vol())
            ts.append(time.time() - t)
        plot.plot_vol_vs_time(ts, vols, max_vol)
        plot.plot_hist(ts)
    finally:
        mcp.deinit()
