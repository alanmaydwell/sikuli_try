# for Python v2/v3 compatibility
from __future__ import print_function

# Magic for Sikuli to work with ordinary Jython
# https://answers.launchpad.net/sikuli/+question/676645
# (1) Need to have os-appropriate sikulixapi JAR file in CLASSPATH (e.g sikulixapi-2.0.5-win.jar)
# (2) The main Jython script needs the two lines below (in addition to any imports used by Sikuli IDE)
import org.sikuli.script.SikulixForJython
from sikuli import *
# Additional fix for ordinary Jython
# Unlike Sikuli IDE, BundlePath is not set automatically. Need to set it here
# manaully otherwise Image handling fails
import os
cwd = os.getcwd()
setBundlePath(cwd)

# Custom things
from ccms_actions import *

# SikuliX only - "hidden" flag isn't available in standard Python!
password = input("Password:", hidden=True)

browser = ccms_login("NB_CASEWORKER", password, "https://ccmsebs.uat.legalservices.gov.uk")
ccms_dashboard_set_role_and_access_search()
found_id = case_search("300001345114", click_ok=True)
print("found", found_id)
ebusiness_center()
access_submission_details()
#go_to_search_screen()

#browser.terminate()
print("Finished!")

