# anomaly detection module
import numpy as np

def detect_anomaly(img):

    mean = np.mean(img)

    if mean < 0.3:

        return "Possible Bone Loss"

    elif mean > 0.7:

        return "Possible Implant"

    else:

        return "Normal"
