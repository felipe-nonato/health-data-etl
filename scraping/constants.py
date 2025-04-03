from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Exportando path de download
download_path = "/home/lipe/Codes/teste/scraping/downloads"


chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_path,  # Define a pasta de downloads
    "download.prompt_for_download": False,        # Baixa sem perguntar
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,   # Impede que o Chrome abra PDFs
    "profile.default_content_settings.popups": 0
})

# Exportando driver
driver = webdriver.Chrome(options=chrome_options)