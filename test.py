import numpy as np
import h5py as h5

waves = np.ones(shape=(8152,))


with h5.File("testing/"+"10501676"+".h5") as f:
    print(f['intensity'].shape)
    wavelength = np.array(f['wavelength'][...])
    print(wavelength[5])
