# Trying out Sikuli/Sikulix
# Note Sikuli types text using its type command, so standard Python type fuction 
# not avaiable (Sikuli also has write that seems to do the same)

# Try to speed up the slow typing speed. Doesn't help!
Settings.TypeDelay = 0

# Open browser
##browser_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
##url_bar = "chrome_url_bar.png"

browser_path = r"C:\Program Files\Internet Explorer\iexplore.exe"
url_bar = "ie_url_bar.png"
openApp(browser_path)

# Enter URL in browser
wait(url_bar)
click(url_bar)
# To make sure any existing text is cleared by selecting it
type("a", Key.CTRL)
# Trying write in place of type but both are slow!
write("https://cwa.tst.legalservices.gov.uk/OA_HTML/AppsLocalLogin.jsp")
type(Key.ENTER)

# Oracle EBS direct login screen
wait("ebs_logo.png")

# Login
click(Pattern("username_field.png").similar(0.60))
type("GET-SERVICE1")
password = input("Password?")
click(Pattern("password_field.png").similar(0.59))
type(password)
click("login_button.png")
wait("navigator_heading.png")

# Select role
wait("provider_support.png")
click("provider_support.png")
wait("firm_inquiry.png")
click("firm_inquiry.png")

# Wait for horrible forms
wait("find_suppliers_form.png")

# Search for supplier
click("firm_name_field.png")
type("FISHER MEREDITH")
click("find_button.png")

