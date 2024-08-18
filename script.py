from exceptions import exceptions_set

from playwright.sync_api import sync_playwright
import pywhatkit
import time
import random

# =====================================
#        Script Author: Somesh Kumar
#        Website: https://kumarsomesh.in
# =====================================
#        Version: 1.0
# =====================================

# ----------------------------------- IMPORTANT STUFF -----------------------------------------
#
# THIS SCRIPT REQUIRES the "playwright" and "pywhatkit" packages.
# Ensure you have installed the necessary packages using pip:
# pip install playwright pywhatkit && playwright install
#
# Playwright documentation: https://playwright.dev/python/docs/intro
# Pywhatkit documentation: https://pypi.org/project/pywhatkit/
# ---------------------------------------------------------------------------------------------

# =================================== CONFIGURATION ==========================================
# Define constants for the scraper
URL = "https://www.timesnownews.com/education/ugc-net-admit-card-2024-live-nta-ugc-net-june-admit-card-link-soon-on-ugcnet-nta-ac-in-exam-from-aug-21-liveblog-112582826"
LOAD_TIMEOUT = 60000  # Timeout for page load in milliseconds
HEADLESS = False  # Set to True to run browser in headless mode
CLASSNAME = "._3tRg"  # CSS class name to locate elements on the page
WHATSAPP_NUMBER = "+919142428071"  # Recipient WhatsApp number
MESSAGE_PREFIX = "Automated Message: "  # Prefix for the message to be sent

RELOAD_AFTER = 120  # Time in seconds to wait before reloading the page
RELOAD_RANDOMNESS = 60  # Additional randomness in the reload time
# ============================================================================================


class WebScraper:
    """A class to handle web scraping and sending messages."""

    def __init__(self, playwright):
        """
        Initialize the WebScraper with Playwright instance.

        Args:
            playwright: The Playwright instance used to launch the browser.
        """
        self.playwright = playwright
        self.browser = None
        self.page = None

    def start_browser(self):
        """Launch the browser and navigate to the URL."""
        self.browser = self.playwright.chromium.launch(headless=HEADLESS)
        self.page = self.browser.new_page()
        self.page.goto(URL, wait_until="domcontentloaded", timeout=LOAD_TIMEOUT)

    def close_browser(self):
        """Close the browser if it is open."""
        if self.browser:
            self.browser.close()

    def scrape_and_send(self):
        """Scrape the content from the page and send messages."""
        elements = self.page.query_selector_all(CLASSNAME)
        for element in elements:
            content = element.text_content()
            if content and content not in exceptions_set:
                exceptions_set.add(content)
                print(content)
                pywhatkit.sendwhatmsg_instantly(
                    phone_no=WHATSAPP_NUMBER,
                    message=f"{MESSAGE_PREFIX}\n{content}",
                    tab_close=True,
                )

    def reload_page(self):
        """Reload the page and print a message."""
        self.page.reload(timeout=LOAD_TIMEOUT)
        print("Page reloaded")

    def run(self):
        """Main method to run the scraping process."""
        try:
            self.start_browser()
            while True:
                self.scrape_and_send()
                time.sleep(
                    random.randint(RELOAD_AFTER, RELOAD_AFTER + RELOAD_RANDOMNESS)
                )
                self.reload_page()
        finally:
            self.close_browser()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        scraper = WebScraper(playwright)
        scraper.run()
