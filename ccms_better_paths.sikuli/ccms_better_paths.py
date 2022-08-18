# for Python v2/v3 compatibility
from __future__ import print_function

import os
import subprocess
# Custom things
from my_lib import get_text_from_image, wait_with_pauses, BaseSik, SearchSik


def get_file_data(path):
    with open(data_file, "r") as infile:
        case_ids = infile.readlines()
    case_ids = [c.strip() for c in case_ids if c]
    return case_ids


browser_path = r"C:\Program Files\Internet Explorer\iexplore.exe"
initial_url = "https://ccmsebs.uat.legalservices.gov.uk"
username = "NB_CASEWORKER"
# hidden flag isn't available in standard Python!
password = input("Password:", hidden=True)

# Read case IDs from file
test_directory = getBundlePath()
data_file = os.path.join(test_directory, "case_ids.txt")
case_ids = get_file_data(data_file)

# Open browser
browser = subprocess.Popen([browser_path, initial_url])

# Login to EBS
login = BaseSik(new_paths=["login_images"])
login.list_image_files()
login.waitclicktype("username_field.png", 30, username)
login.waitclicktype("password_field.png", 10, password)
login.click("login_button.png")
login.wait("oracle_applications_title.png", 30)
# Optional - clear the added paths. May reduce image caching.
login.remove_added_paths()

# Select role and screen, which opens Oracle Forms
dashboard = BaseSik(new_paths=["dashboard_images"])
dashboard.list_image_files()
dashboard.click("complex_merits_caseworker.png")
dashboard.wait("cases_and_clients.png", 10)
dashboard.click("cases_and_clients.png")
dashboard.remove_added_paths()

# Searches in EBS
search = SearchSik(new_paths=["search_images"])
search.list_image_files()
# Special wait for forms launch - less CPU load!
wait_with_pauses("universal_search_top.png", 1, 90)
# Search each ID
for case_id in case_ids:
    found_id = search.case_search(case_id)       
    print("Searched for:", case_id, " Found:", found_id)
    # Return to search screen - not needed after failed search
    if exists("return_to_search_button.png"):
        click("return_to_search_button.png")
    search.wait("universal_search_top.png", 60)
search.remove_added_paths()

# End
browser.terminate()
print("Finished!")
