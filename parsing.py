import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Func for creating folder
def create_folder(barcode):
    folder_path = os.path.join(os.getcwd(), barcode)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

# Func for saving images
def save_image(url, folder_path, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Images was downloaded: {file_path}")
    except Exception as e:
        print(f"Error during downloading {url}: {e}")

# Main process of parsing with Selenium
def scrape_images(barcodes_file):
    not_found_barcodes = []

    # Settings for Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск без GUI
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    # Reading barcodes from file
    with open(barcodes_file, 'r') as file:
        barcodes = file.read().splitlines()

    for barcode in barcodes:
        print(f"Barcode processing: {barcode}")
        search_url = f"https://minim.kz/poisk?filter_name={barcode}"  # URL for seeacrh pages
        try:
            driver.get(search_url)

            # Waiting for element with link to product
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "c-product-item__link")))

            # Taking a products link
            product_link = driver.find_element(By.CLASS_NAME, "c-product-item__link")
            product_url = product_link.get_attribute("href").lstrip('/')  # 
            print(f"Switching with the link to product : {product_url}")

            # Switching to products page
            driver.get(product_url)

            # Waiting for products images on the page
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "c-product-info__image-img")))

            # Taking image
            images = driver.find_elements(By.CLASS_NAME, "c-product-info__image-img")
            if not images:
                print(f"Images was not found for barcode{barcode}")
                not_found_barcodes.append(barcode)
                continue

            # Creating a folder for current barcode
            folder_path = create_folder(barcode)

            # Downloading iamges
            for idx, img in enumerate(images):
                img_url = img.get_attribute("srcset").split(', ')[-1].split(' ')[0]  # Берём самое крупное изображение
                if img_url:
                    save_image(img_url, folder_path, f"{barcode}-{idx + 1}.jpg")

        except Exception as e:
            print(f"Error during barcode processing {barcode}: {e}")
            not_found_barcodes.append(barcode)

    # Quit web-browser
    driver.quit()

    # Saving not-found barcodes into txt file
    with open('not_found.txt', 'w') as file:
        file.write("\n".join(not_found_barcodes))
    print("Parsing ended. The list of not found barcodes is saved in not_found.txt.")

# Running
if __name__ == "__main__":
    barcodes_file = 'barcodes.txt'  # Name of file with barcodes
    scrape_images(barcodes_file)
