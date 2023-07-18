import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

tanio_to = 4600

# Chrome
driver = webdriver.Chrome()

# Lista adresów URL do stron
urls = [
    "https://www.morele.net/laptop-lenovo-legion-5-15ach6h-82ju00jfpb-16-gb-ram-512-gb-ssd-pcie-windows-11-home-9848453/",
    "https://www.mediaexpert.pl/komputery-i-tablety/laptopy-i-ultrabooki/laptopy/laptop-lenovo-legion-5-15ach6h-15-6-ips-165hz-r5-5600h-16gb-ssd-1tb-geforce-rtx3060-windows-11-home",
    "https://www.x-kom.pl/p/717561-notebook-laptop-156-lenovo-legion-5-15-ryzen-5-16gb-1tb-win11-rtx3060-165hz.html"
]

# Pobranie ceny przedmiotu z każdej strony
prices = []
for url in urls:
    # Przejście do adresu URL
    driver.get(url)

    # Pobranie ceny przedmiotu z odpowiedniego selektora
    if url == "https://www.morele.net/laptop-lenovo-legion-5-15ach6h-82ju00jfpb-16-gb-ram-512-gb-ssd-pcie-windows-11-home-9848453/":
        price_element = driver.find_element(By.CSS_SELECTOR, "#product_price_brutto")
    elif url == "https://www.mediaexpert.pl/komputery-i-tablety/laptopy-i-ultrabooki/laptopy/laptop-lenovo-legion-5-15ach6h-15-6-ips-165hz-r5-5600h-16gb-ssd-1tb-geforce-rtx3060-windows-11-home":
        price_element = driver.find_element(By.CSS_SELECTOR, "#section_offer-available > div.price-box > div.prices-section > div > div > span.whole")
    elif url == "https://www.x-kom.pl/p/717561-notebook-laptop-156-lenovo-legion-5-15-ryzen-5-16gb-1tb-win11-rtx3060-165hz.html":
        time.sleep(2)
        #klika ciastka na 100%
        driver.find_element(By.CSS_SELECTOR, ".sc-1p1bjrl-9").click()
        time.sleep(2)
        price_element = driver.find_element(By.CSS_SELECTOR, ".sc-n4n86h-1")

    time.sleep(1)
    # Pobranie tekstu z elementu ceny
    price = price_element.text
    prices.append(price)

# Wyświetlenie pobranych cen
for i, url in enumerate(urls):
    print(f"Cena przedmiotu na stronie {url}: {prices[i]}")


for price_str in prices:
    # Ekstrakcja tylko cyfr
    digits = ''.join(filter(str.isdigit, price_str))

    if digits:
        # Pobranie pierwszych 4 cyfr
        price = int(digits[:4])

        # Porównanie ceny z wartością progową
        if price >= tanio_to:
            print(f"Cena {price_str} jest większa lub równa {tanio_to} zł.")
        else:
            print(f"Cena {price_str} jest mniejsza niż {tanio_to} zł, Jest bardzo tanio!!!.")
    else:
        print(f"Niewłaściwy format ceny: {price_str}")

driver.quit()
