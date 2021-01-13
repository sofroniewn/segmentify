from napari_plugin_engine import napari_hook_implementation
from .segmentify import segmentation


@napari_hook_implementation
def napari_experimental_provide_function_widget():
    return (segmentation, {'call_button': "execute"})
