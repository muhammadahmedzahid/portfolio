from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Global variable for script status
script_status = None


def main():
    global script_status
    options = Options()
    # options.add_argument('--headless')
    options.add_argument("--start-maximized")

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # URL of the webpage to scrape
    url = "https://google.com"

    # Open the webpage
    driver.get(url)

    # Get the page title
    page_title = driver.title
    print(f"Page title: {page_title}")

    # Get the page source
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Save the page source to a local file
    with open("scraped_page.html", "w", encoding="utf-8") as file:
        file.write(page_source)

    print("Page scraped and saved as scraped_page.html")
    script_status = "Completed"


if __name__ == "__main__":
    main()
