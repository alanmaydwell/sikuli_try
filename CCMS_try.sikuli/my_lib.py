# Main Sikuli file doesn't need to import Sikuli but modules do, like below?
from sikuli.Sikuli import *
## from sikuli import *

def get_text_from_found_image(found_image, width=0, height=0, xo=0, yo=0):
    """
    Examine already found image (or region based on its position) 
    and return text found within it using OCR 
    
    params: 
        found_image - image that's already been located (Sikuli Region object?)
        width (optional) - width to examine (pixels). Auto set to image width if <1
        height (optional) - height to examine (pixels). Auto set to image height if <1
        xo (optional) - x-offset (pixels), from top-left corner
        yo (optional) - y-offset (pixels), from top-left corner
    Returns:
        text found
    """    
    # Default to image's actual width, height if <1 values received
    if width < 1:
        width = found_image.getW()
    if height < 1:
        height = found_image.getH()
    region_to_examine = Region(found_image.getX() + xo, found_image.getY() + yo, width, height)
    return region_to_examine.text()

    
def get_text_from_image(image, width=0, height=0, xo=0, yo=0):
    """Look for image on screen and return text found within it
    , or in related location, using OCR"""
    found = find(image)
    text = get_text_from_found_image(found, width, height, xo, yo)
    return text
