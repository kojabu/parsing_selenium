# Selenium Image Scraper

This project is a web scraping tool built with Python and Selenium. It allows you to parse product images from a website by searching for barcodes and saving the images locally in organized folders. The project is especially useful for automating the collection of product images using barcodes.

## Features
- Reads a list of barcodes from a file.
- Searches for products on a specified website using the barcodes.
- Downloads product images and saves them into individual folders for each barcode.
- Logs barcodes for which images are not found.

## Requirements
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver compatible with your Chrome version

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kojabu/parsing_selenium.git
   cd parsing_selenium
   ```

2. **Create a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install all required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download ChromeDriver**
   - Ensure you have Google Chrome installed on your machine.
   - Download the version of ChromeDriver that matches your Chrome browser version from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
   - Add the downloaded `chromedriver` executable to your system's PATH or place it in the project directory.

## Usage

1. **Prepare a Barcode File**
   - Create a file named `barcodes.txt` in the project directory.
   - Add one barcode per line. Example:
     ```
     1234567890123
     9876543210987
     1122334455667
     ```

2. **Run the Script**
   Execute the script to start scraping:
   ```bash
   python main.py
   ```

3. **Output**
   - Images for each barcode will be saved in a separate folder named after the barcode.
   - If images are not found for a barcode, the barcode will be logged in a file named `not_found.txt`.

## File Structure
```
parsing_selenium/
├── main.py              # Main script for scraping
├── requirements.txt     # List of dependencies
├── barcodes.txt         # Input file with barcodes
├── not_found.txt        # Log file for barcodes with no images
├── <barcode_folders>/   # Folders containing downloaded images
```

## Notes
- The script uses Selenium in headless mode to avoid opening a browser GUI during scraping.
- Ensure that the target website's structure has not changed, as it may affect the script's ability to locate elements.
- Use the script responsibly and follow the website's terms of service.




