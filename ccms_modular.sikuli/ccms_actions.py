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


def go_to_search_screen():
    navigate = SearchSik(new_paths=["search_images", "generic_images"])
    # See if already on search screen
    if navigate.exists("universal_search_top.png"):
        # See if "return to search" button present, if so needs to be pressed
        # so go from search result to search request
        if navigate.exists("return_to_search_button.png"):
            navigate.click("return_to_search_button.png")
    else:
        navigate.click("torch.png")
    # Wait for search screen. (organization_filed (sic) is better than universal_search_top
    # as we universal_search_top is same for both search request and results)
    navigate.wait("organization_filed_less_ambiguous.png", 10)
    navigate.remove_added_paths()


def case_search(case_id, click_ok=False):
    search = SearchSik(new_paths=["search_images"])
    found_id = search.case_search(case_id)
    if click_ok:
        search.click_ok()
        # Wait for "eBusiness Center" page. Need image not affected by
        # data values or the intermittent "Choose Role and Group" message
        search.wait("confirm_new_screeen_after_search_ok")
    search.remove_added_paths()
    return found_id
