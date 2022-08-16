import time
import os
# Main Sikuli file doesn't need to import Sikuli but modules do as below
from sikuli.Sikuli import *


class BaseSik(object):
    """
    Generic Sikulix
    image_dir - sub directory that holds the images to be used. Needs to be sub
    direcotry of the Sikuli script dir. Also defaults to Sikuli script dir.
    """
    def __init__(self, image_dir=None):
        if not image_dir:
            # getBundlePath() is provided by SikuliX and returns the script's own dir
            self.image_path = getBundlePath()
        else:
            self.image_path = os.path.join(getBundlePath(), image_dir)
        self.images = self.find_images()
        
    def find_images(self):
        """Create dictionary with filenames as keys and full path as values"""
        files =  {f: os.path.join(self.image_path, f)
                  for f in os.listdir(self.image_path)
                  if f.endswith(".png")}
        return files
    
    def wait(self, image, delay=5):
        wait(self.images[image], delay)
    
    def click(self, image):
        click(self.images[image])
        
    def waitclick(self, image, delay):
        self.wait(image, delay)
        self.click(image)
        
    def waitclicktype(self, image, delay, text):
        self.waitclick(image, delay)
        type(text)
        
    def list_images(self):
        # iteritems method is Python 2 (items in Python 3)
        for k, v in self.images.iteritems():
            print k, v


class SearchSik(BaseSik):
    """Case Search in EBS"""
    def case_search(self, case_id):
        # Enter Organization reference
        wait(self.images["organization_filed_less_ambiguous.png"], 5)
        click(Pattern(self.images["organization_filed_less_ambiguous.png"]).targetOffset(60,16))
        # Select any existing text to ensure it is replaced by new value
        type("a", Key.CTRL)
        type(Key.DELETE)
        type(case_id)
        # Note could try keyboard shortcut as alternative to image
        click(self.images["search_button.png"])
            
        # Check for nothing returned (last arg below is timeout time)
        # Return empty string. Beware default similarity setting - too wide!
        if exists(Pattern(self.images["search_found_nothing.png"]).similar(0.86), 2):
            click(self.images["dialogue_ok_button.png"])
            return ""
        
        # Wait for search results screen
        wait(self.images["search_results_window_top.png"], 20)
        
        # Reading reference number returned by search
        # Using offsets to look below the Organization heading and a bit to the right
        # Also home made repeat and delay for sync
        for _ in range(10):
            found_id = get_text_from_image(self.images["organization_heading.png"], width=100, xo=20, yo=20)
            if found_id != "":
                break
            else:
                time.sleep(0.5)
        return found_id


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


def wait_with_pauses(image, pause=1, iterations=10):
    """
    Wait for image to be displayed with wait based on a pause
    interval and number of iterations. Each pause will pause
    the screen scanning, so should reduce CPU load.
    
    Returns True/False depending on whether image found
    """
    found = False
    for _ in range (iterations):
        if exists(image):
            found = True
            break
        else:
            time.sleep(pause)
    return found
