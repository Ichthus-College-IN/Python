import numpy as np
np.random.seed(6942059)

f_in = open("raw.txt")
raw = f_in.readlines()          # individual lines
raw = "".join(raw)              # one string of all lines
raw = [int(x) for x in raw if x != '\n']     # int array of all chars
raw = np.array(raw, dtype=int)             # int ndarray
raw = raw.reshape((int(np.sqrt(len(raw))), int(np.sqrt(len(raw)))))
#np.savetxt("bonus_getallen_raw.txt", raw, fmt = '%d')
dist = np.random.rand(raw.shape[0], raw.shape[1]) # distortion [ 0.00, 1.00)
dist -= 0.5                     # distortion [-0.50, 0.50)
dist *= 0.9                     # distortion [-0.45, 0.45)

proc = raw + dist               # binary array + distortion
proc = np.round(proc, 2)        # round to two decimals
np.savetxt("bonus_getallen.txt", proc, delimiter = ',', fmt = '%.2f')