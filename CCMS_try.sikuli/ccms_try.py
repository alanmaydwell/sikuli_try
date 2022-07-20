# for Python v2/v3 compatibility
from __future__ import print_function

browser_path = r"C:\Program Files\Internet Explorer\iexplore.exe"
initial_url = "https://ccmsebs.uat.legalservices.gov.uk"
username = "NB_CASEWORKER"
password = input("Password (will show):")

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

# Search for case
click("organization_field.png")
type("300001345114")
# Note could try keyboard shortcut as alternative to image
click("search_button.png")
# Expected result - note not flexible, need dedicated screenshot!
wait("result_1345114.png", 20)
print("Finished!")
