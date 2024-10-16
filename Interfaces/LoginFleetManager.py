from selenium.webdriver.common.by import By


class LoginFleetManager:

    def __init__ (self, driver): #constructor de la clase 
        self.driver= driver

        #Estas líneas definen cómo se van a localizar los elementos en la página
        self.username_input = (By.ID, ":R3akvesq:")
        self.password_input = (By.ID, ":R5akvesq:")
        self.login_button = (By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/form/button")

    

    def enter_username(self, username): #metodo para ingresar nombre de usuario 
        self.driver.find_element(*self.username_input).send_keys(username)

    
    def enter_password(self, password): # metodo para ingresar contraseña
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self): # metodo para hcer clic en boton inicio de sesion
        self.driver.find_element(*self.login_button).click()

#Se define como ingresar usuario, contraseña y hacer clic en el botón de login 
