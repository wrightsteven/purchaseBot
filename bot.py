import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

a = "https://us.puma.com/en/us/account/login"
b = "https://us.puma.com/en/us/pd/rs-dreamer-concrete-jungle-basketball-shoes/194598.html?dwvar_194598_color=01"
user = ""
password = ""
path = "/users/steven/geckodriver.exe"

class Bot():
    def __init__(self, email, psswd):
        self.email = user
        self.psswd = password
        self.driver = webdriver.Firefox(path)

    def login(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(1)

        user_elem = driver.find_element_by_xpath('<input type="email" id="login-form-email" required="" aria-required="true" aria-describedby="form-email-error" class="form-control floatl__input hf-validated hf-invalid" name="loginEmail" placeholder="Email*" value="" pattern="^[\w.%+-]+@[\w.-]+\.[\w]{2,6}$" autocomplete="email" aria-invalid="true" aria-errormessage="hf_0s9utkwkmrr"> = $0')
        user_elem.clear()
        user_elem.sendkeys(self.email)
        time.sleep(1)

        password_elem = driver.find_element_by_xpath('<input type="password" id="login-form-password" required="" aria-required="true" aria-describedby="form-password-error" class="form-control floatl__input hf-validated hf-invalid" name="loginPassword" placeholder="Password*" autocomplete="password" minlength="8" maxlength="255" aria-invalid="true" aria-errormessage="hf_1f3hvcybke1b">')
        password_elem.clear()
        password_elem.send_keys(self.psswd)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def check(self, start, target):
        self.login(start)

        driver = self.driver
        driver.get(target)


        if available:
            buy(prod)
        else:
            print("not available")
            driver.quit()

    def buy(self, product):
        driver = self.driver
        driver.get("url for product")
        time.sleep(1)

        size = driver.find_element_by_xpath("data-js-product-swatches-swatch="">13")
        size.click()
        time.sleep(1)
        addToCart = driver.find_element_by_xpath("data-js-product-add-to-cart-btn")
        addToCart.click()
        time.sleep(1)
        cart = driver.find_element_by_xpath("<a class="p-header-actions-link p-header-actions-icon p-header-actions-icon--cart js-cmp-mini-cart-open" href="#cart" title="View Cart">
<svg class="icon">
<use xlink:href="#cart"></use>
</svg>
<span class="p-header-actions-count js-cmp-mini-cart-quantity-total p-header-actions-count--active">1</span>
</a>")
        cart.click()
        time.sleep(1)
        checkout = driver.find_element_by_xpath("<a href="https://us.puma.com/en/us/checkout/start" class="btn btn-primary btn-block checkout-btn" role="button" aria-pressed="true">
Checkout
</a>")
        checkout.click()
        time.sleep(1)

        total = driver.find_element_by_xpath()
        if total>200:
            print("error - price out of range")
            driver.quit()

        print("complete")
        driver.quit()

k = Bot(user, password)
k.check(a,b)