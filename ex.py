from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import time

driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
time.sleep(1000)

