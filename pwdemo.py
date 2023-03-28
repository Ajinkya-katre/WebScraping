from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False, slow_mo = 50)
    page = browser.new_page()
    page.goto('https://tapfarm-9ecda.web.app/contact')
    page.fill('input#your-name','Ajinkya Katre')
    page.fill('input#your-surname','katreajinkya@gmail.com')
    page.fill('input#your-email','katreajinkya@gmail.com')
    page.fill('input#your-subject','Enquiry Regarding Grapes Farming')
    page.fill('textarea#your-message','Hi, Enquiry Regarding Grapes Farming')
    page.click('button[type = submit]')
    html = page.inner_html('.contact-info')
    soup = BeautifulSoup(html,'html.parser')
    print(soup.find_all('h4'))



