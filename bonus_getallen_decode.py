import numpy as np

np.set_printoptions(threshold = np.inf, linewidth = np.inf)

raw = np.genfromtxt("bonus_getallen.txt", delimiter = ',')
proc = np.round(raw, 0)
proc = proc.astype(int)

proc = str(proc).replace('[', '').replace(']', '')
f_out = open("final.txt", "w")
f_out.write(proc)
f_out.close()