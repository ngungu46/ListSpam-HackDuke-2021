def parseLinkedin(LinkedInHomelink):
    import requests
    from bs4 import BeautifulSoup

    client = requests.Session()

    HOMEPAGE_URL = 'https://www.linkedin.com'
    LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
    USER_LOOKUP_URL = LinkedInHomelink

    #get url, soup object and csrf token value
    html = client.get(HOMEPAGE_URL).content
    soup = BeautifulSoup(html, "html.parser")
    csrf = soup.find('input', dict(name='loginCsrfParam'))['value']

    #create login parameters
    login_information = {
        'session_key':'tianshu.wang@duke.edu',
        'session_password':'?????????',  #We'd use an anayomous linkedin profile
        'loginCsrfParam': csrf,
    }

    try:
        client.post(LOGIN_URL, data=login_information)
        print("Login Successful")
    except:
        print("Failed to Login")


    #open the user html with soup object
    USER_LOOKUP_URL = "https://www.linkedin.com/in/islina-shan"
    html = client.get(USER_LOOKUP_URL).content
    soup = BeautifulSoup(html , "html.parser")

    # print(soup.prettify())
    # print(str(soup.prettify()))
    output = str(soup.prettify())
    # indexToTrim = output.rfind("defaultLocalizedNameWithoutCountryName")
    # output = output[indexToTrim:]
    # indexToTrim = output.find("</code>")
    # output = output[:indexToTrim]
    with open("user_info.html", "w", encoding="utf-8") as file:
        file.write(output)


parseLinkedin('https://www.linkedin.com/in/tianshu-terry-wang-820456117')