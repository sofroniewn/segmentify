"""
Perform interactive semantic segmentation
"""

import numpy as np
from napari import Viewer, gui_qt
from skimage import data
from segmentify.semantic import fit, predict
import napari
print(napari.__version__)

coins = data.coins()
labels = np.zeros(coins.shape, dtype=int)


with gui_qt():

    # create an empty viewer
    viewer = Viewer()

    viewer.add_image(coins, name='input', colormap='gray')

    # add empty labels
    viewer.add_labels(labels, name='output')
    viewer.add_labels(labels, name='train')
    viewer.layers['train'].opacity = 0.9

    @viewer.bind_key('s')
    def segment(viewer):
        image = viewer.layers['input'].data
        labels = viewer.layers['train'].data
        clf = fit(image, labels)
        segmentation = predict(clf, image)
        print(np.unique(segmentation))
        viewer.layers['output'].data = segmentation
