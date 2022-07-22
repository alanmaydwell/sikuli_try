# for Python v2/v3 compatibility
from __future__ import print_function
import subprocess
import time
# Custom function for reading text from image on screen
from my_lib import get_text_from_image


browser_path = r"C:\Program Files\Internet Explorer\iexplore.exe"
initial_url = "https://ccmsebs.uat.legalservices.gov.uk"
username = "NB_CASEWORKER"
password = input("Password (will show):")
case_ids = ["300001345114", "300001345115", "300001345116", "300001345117", "300001345118", "400001345118"]


def case_search(case_id):
    # Search for case - note was sometimes confused by "Organization" in Find field!
    # May be partly due to left over text from old search reducing similarity
    # Fixed by switching to more distinctive image. Also needs offset as text
    # entry now in its bottom-left corner.
    ## click("organization_field.png")
    # Different image to solve proble. Note target offset to get the text part
    click(Pattern("organization_filed_less_ambiguous.png").targetOffset(60,16))
    
    # Enter Organization reference    
    # Select any existing text to ensure it is replaced by new value
    type("a", Key.CTRL)
    type(Key.DELETE)
    type(case_id)
    # Note could try keyboard shortcut as alternative to image
    click("search_button.png")
    # Check for nothing returned (2nd arg is timeout time)
    # Return empty string. Beware default similarity setting - too wide!
    if exists(Pattern("search_found_nothing.png").similar(0.86), 2):
        click("dialogue_ok_button.png")
        return ""
            
    # Wait for search results screen
    wait("search_results_window_top.png", 20)
    
    # Also wait for some blue background to show a search result is actually present
    # Otherwise can be too quick and pick up no reference
    wait("search_result_blue_background.png")
    
    # Reading reference number returned by search
    # Using offsets to look below the Organization heading and a bit to the right
    # Also home made repeat and delay for sync
    for _ in range(10):
        found_id = get_text_from_image("organization_heading.png", width=100, xo=20, yo=20)
        if found_id != "":
            break
        else:
            time.sleep(0.5)
    return found_id


# Open browser
browser = subprocess.Popen([browser_path, initial_url])

# Login to EBS(can be slow to appear, extra wait time added)
wait("username_field.png", 30)
click("username_field.png")
type(username)
wait("password_field.png")
click("password_field.png")
type(password)
click("login_button.png")

# Wait for Home Page to open (more wait time as can be a bit slow)
wait("oracle_applications_title.png", 30)

# Select role and screen, which opens Oracle Forms
click("complex_merits_caseworker.png")
wait("cases_and_clients.png")
click("cases_and_clients.png")

# Wait for Oracle Forms Launch (allowing 60s)!
wait("universal_search_top.png", 60)

for case_id in case_ids:
    found_id = case_search(case_id)       
    print("Searched for:", case_id, " Found:", found_id)
    # Return to search screen
    if exists("return_to_search_button.png"):
        click("return_to_search_button.png")
    wait("universal_search_top.png", 60)

# End
browser.terminate()
print("Finished!")
