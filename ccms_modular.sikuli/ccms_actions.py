import subprocess

from my_lib import BaseSik, SearchSik


def ccms_login(username, password, url, browser_path=r"C:\Program Files\Internet Explorer\iexplore.exe"):
    """Open browser and login to CCMS"""
    browser = subprocess.Popen([browser_path, url])
    login = BaseSik(new_paths=["login_images"])
    ## login.list_image_files()
    login.waitclicktype("username_field.png", 30, username)
    login.waitclicktype("password_field.png", 10, password)
    login.click("login_button.png")
    login.wait("oracle_applications_title.png", 30)
    # Optional - clear the added paths. May reduce image caching.
    login.remove_added_paths()
    return browser


def ccms_dashboard_set_role_and_access_search():
    dashboard = BaseSik(new_paths=["dashboard_images"])
    ## dashboard.list_image_files()
    dashboard.click("complex_merits_caseworker.png")
    dashboard.wait("cases_and_clients.png", 10)
    dashboard.click("cases_and_clients.png")
    # Oracle forms launch here.
    # Using wait_with_pauses to help with CPU load as actualy pausesscanning.
    dashboard.wait_with_pauses("universal_search_top.png", 1, 90)
    dashboard.remove_added_paths()


def case_search(case_id):
    search = SearchSik(new_paths=["search_images"])
    found_id = search.case_search(case_id)
    search.remove_added_paths()
    return found_id
