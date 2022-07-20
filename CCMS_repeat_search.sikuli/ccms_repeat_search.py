# for Python v2/v3 compatibility
from __future__ import print_function
import time
# Custom function for reading text from image on screen
from my_lib import get_text_from_image

browser_path = r"C:\Program Files\Internet Explorer\iexplore.exe"
initial_url = "https://ccmsebs.uat.legalservices.gov.uk"
username = "NB_CASEWORKER"
password = input("Password (will show):")
case_ids = ["300001345114", "300001345115", "300001345116",  "300001345117",  "300001345118"]


def case_search(case_id):
    # Search for case
    click("organization_field.png")
    # Select any existing text to ensure it is replaced by new value
    type("a", Key.CTRL)
    
    type(case_id)
    # Note could try keyboard shortcut as alternative to image
    click("search_button.png")
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
openApp(browser_path)
# Warning - user settings affect (1) cosmetic appearance (2) initial URL displayed
wait("ie_address.png")
click("ie_address.png")

# Open page - get to address bar by keyboard shortcut (avoids screenshot)
type("l", Key.CTRL)
type(initial_url)
type(Key.ENTER)

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
    click("return_to_search_button.png")
    wait("universal_search_top.png", 60)
    
print("Finished!")
