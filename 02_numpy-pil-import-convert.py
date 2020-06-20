# convert colour image into grayscale using manual numpy matrix conversion
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

dummy = np.zeros((10, 10))

# write your python program here












# Set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)
# Plot colour image image
plt.subplot(121)
plt.axis('on')
plt.title('Original', fontsize=10)
#replace the correct variable dummy for your plot
plt.imshow(dummy)
# Plot gray image
plt.subplot(122)
plt.axis('on')
plt.title('Gray', fontsize=10)
#replace the correct variable dummy for your plot
plt.imshow(dummy, cmap = plt.get_cmap(name = 'gray'), vmin=0, vmax=255)
# Show the plot
plt.show()
