# prediction pipeline
import cv2
from utils.preprocessing import preprocess_image
from utils.tooth_detection import detect_teeth
from utils.numbering import assign_fdi_numbers

def run_inference(image_path):

    img = cv2.imread(image_path,0)

    mask = img

    teeth = detect_teeth(mask)

    numbers = assign_fdi_numbers(teeth)

    return teeth,numbers
