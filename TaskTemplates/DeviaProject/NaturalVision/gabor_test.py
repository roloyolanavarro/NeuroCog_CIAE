from skimage.filters import gabor
from skimage import data, io
from skimage.util import img_as_float


from matplotlib import pyplot as plt  # doctest: +SKIP

brick = img_as_float(data.load('test-crop.png'))
image = data.coins()
# detecting edges in a coin image
filt_real, filt_imag = gabor(brick, frequency=0.6, theta=100)
plt.figure()            # doctest: +SKIP
io.imshow(filt_real)    # doctest: +SKIP
io.show()               # doctest: +SKIP
# less sensitivity to finer details with the lower frequency kernel
filt_real, filt_imag = gabor(image, frequency=0.1)
plt.figure()            # doctest: +SKIP
io.imshow(filt_real)    # doctest: +SKIP
io.show()               # doctest: +SKIP