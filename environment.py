from selenium import webdriver

def before_scenario(context, scenario):
    print(scenario)
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.cifraclub.com.br/")

def after_scenario(context, scenario):
    context.driver.quit()