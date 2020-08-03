from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Llibre: # book

    def __init__(self, contra, pag, driver, user, mater):

        self.contra = contra #password
        self.pag = pag #page
        self.driver = driver
        self.user = user
        self.mater = mater # subject

    def main_(self):

        driver = self.driver
        driver.get("https://www.ecasals.net/es/index.php?ps=0b2b5bd55f4e2f414330b94ed744a2a15cfb26a9aa31f9a6a823a6a86c6"
                   "3e0d87934") # open the book
        user_elem = driver.find_element_by_xpath("//input[@type='text']")
        user_elem.clear() # delete everything
        user_elem.send_keys(self.user)
        contra_elem = driver.find_element_by_xpath("//input[@type='password']")
        contra_elem.clear() # write the user
        contra_elem.send_keys(self.contra)
        login_elem = driver.find_element_by_xpath("//button[@type='submit']")
        login_elem.click()  # write the password
        time.sleep(2)
        if self.mater.lower() == "cat":
            Llibre.cat(self)    # go to catalan book
        elif self.mater.lower() == "cas":
            Llibre.cas(self)    # go to spanish book
        else:
            print("Hi ha hagut un error, no has escrit bé l'assignatura. Et ficaré al llibre de català")
            Llibre.cat(self)    # open the catalan by default because there has been an error

    def cat(self):

        driver = self.driver
        bookcat_elem = driver.find_element_by_xpath('//a[@href="https://www.ecasals.net/es/index.php?ps=0b2b5bd55f'
                                                    '294ca2464b382f4a3fa746c359a7ab4af75fa22d413e2fa12c20405942c340'
                                                    '20ae3ed254585b51c05550696ce46a7ba0"]')
        bookcat_elem.click() # click the book
        time.sleep(2)
        unitat_elem = driver.find_element_by_xpath('//img[@src="uploads/resources/s249/1275454/miniatura_unitat.jpg"]')
        unitat_elem.click() # click a unit
        time.sleep(3)
        pagclick_elem = driver.find_element_by_class_name('pagination-wrapper')
        pagclick_elem.click()   # select to change the page
        pag_elem = driver.find_element_by_xpath('//input[@type="text"]')
        pag_elem.click()
        pag_elem.clear()
        pag_elem.send_keys(self.pag)    # write the page
        pag_elem.send_keys(Keys.RETURN)

    def cas(self): # same as the last method
        driver = self.driver
        bookcas_elem = driver.find_element_by_xpath('//a[@href="https://www.ecasals.net/es/index.php?p'
                                                    's=0b2b5bd55f2''94ca2464b382f4a3fa746c359a7ab4af75fa'
                                                    '22d413eaf23d25''c5b415c4''5c4''40''6272917c602c"]')
        bookcas_elem.click()
        time.sleep(2)
        unitatcas_elem = driver.find_element_by_xpath('//img[@src="uploads/resources/s247/12676'
                                                      '21/miniatura_unitat.jpg"]')
        unitatcas_elem.click()
        time.sleep(3)
        pagclickcas_elem = driver.find_element_by_class_name('pagination-wrapper')
        pagclickcas_elem.click()
        pagcas_elem = driver.find_element_by_xpath('//input[@type="text"]')
        pagcas_elem.click()
        pagcas_elem.clear()
        pagcas_elem.send_keys(self.pag)
        pagcas_elem.send_keys(Keys.RETURN)


with open("contraecasals.txt") as f: # open file with user and pass and create a list with it
    content = f.readlines()
content = [x.strip() for x in content]

y = str(input("Quina assignatura vols? (cat/cas) "))    # ask for the subject

try:
    x = int(input("A quina pàgina vols anar del llibre de català? ")) # ask for the page

except:

    x = 20
    print("No es vàlid, aniràs a la pagina 20") # set page 20 as default if there's a mistake

a = Llibre(content[0], x, webdriver.Chrome(), content[1], y)
a.main_()

