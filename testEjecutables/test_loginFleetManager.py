import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Interfaces.LoginFleetManager import LoginFleetManager

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()  # Inicializa el controlador
    yield driver
    driver.quit()  # Cierra el navegador después de las prueba

def test_loginFleetManagerHappyPast (setup_driver):
    
    driver = setup_driver
    driver.get("https://fleet-manager-nextjssprint3-93u6nz9bs-makzzs-projects.vercel.app/login")

    login_page = LoginFleetManager(driver)

    #Realizo acciones en la pagina de login

    login_page.enter_username("jgimenez")
    time.sleep(10)
    login_page.enter_password("123")
    time.sleep(10)
    login_page.click_login()
    time.sleep(10)

    #Validaciones si inicia sesion va a ir a la pantalla del dashboard
    assert driver.current_url == "https://fleet-manager-nextjssprint3-93u6nz9bs-makzzs-projects.vercel.app/dashboard"

def test_loginFleetManaferFailed(setup_driver):
    driver = setup_driver
    driver.get("https://fleet-manager-nextjssprint3-93u6nz9bs-makzzs-projects.vercel.app/login")

    login_page = LoginFleetManager(driver)

    login_page.enter_username("pcamila")
    time.sleep(10)
    login_page.enter_password("123")
    time.sleep(10)
    login_page.click_login()
    time.sleep(10)

    error_message = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/form/p[1]")

    assert "Usuario o contraseña incorrectos" in error_message.text

def test_loginFleetManager_vacio(setup_driver):
     driver = setup_driver
     driver.get("https://fleet-manager-nextjssprint3-93u6nz9bs-makzzs-projects.vercel.app/login")

     login_page = LoginFleetManager(driver)

     login_page.enter_username("")
     time.sleep(10)
     login_page.enter_password("")
     time.sleep(10)
     login_page.click_login()
     time.sleep(10)

     assert driver.current_url == "https://fleet-manager-nextjssprint3-93u6nz9bs-makzzs-projects.vercel.app/login"  # URL de la página de login



    
