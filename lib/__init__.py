
from .bisenetv1 import BiSeNetV1
from .bisenetv2 import BiSeNetV2
import lib.cityscapes_cv2
import lib.duckietown_cv2


data_factory = {
    'cityscapes': cityscapes_cv2,
    'duckietown': duckietown_cv2,
}
