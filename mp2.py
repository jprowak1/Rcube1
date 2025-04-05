import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
#from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
plt.show()
