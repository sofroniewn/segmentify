import os
import napari
import numpy as np


# parse input file
example_image = os.path.join(os.path.abspath(os.path.dirname(__file__)), "hpa.png")
example_labels = os.path.join(os.path.abspath(os.path.dirname(__file__)), "hpa_labels.tif")

with napari.gui_qt():
    viewer = napari.Viewer()

    # load data
    viewer.open(example_image)
    viewer.open(example_labels, layer_type='labels')
