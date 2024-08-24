# **Web Scraping Project**

## **Project Overview**
This project involves web scraping book information from a website and storing the data in multiple formats: Excel (xlsx), CSV, and a MySQL database. The information scraped includes the **name**, **star rating**, **price** and **availability** of each book.

## **Technologies Used**
- **Python**: For scripting and web scraping.
- **BeautifulSoup**: For parsing HTML and extracting data.
- **Pandas**: For handling and manipulating data.
- **MySQL**: For storing data in a relational database.
- **OpenPyXL**: For writing data to Excel files.
- **CSV**: For writing data to CSV files.

## **Project Structure**
- **code.py**: The main script for scraping the data and saving it to different formats.
- **my.properties**: Configuration file for database connection details.
- **README.md**: Documentation of the project.


## **Data Storage Formats**

### **1. Excel (XLSX)**
- The scraped data is saved in an Excel file named `books.xlsx`.
- Each row contains the **name**, **star rating**, and **price** of a book.

### **2. CSV**
- The scraped data is also saved in a CSV file named `books.csv`.
- Each row contains the **name**, **star rating**, and **price** of a book.

### **3. MySQL Database**
- The scraped data is stored in a MySQL table named `books`.
- The table schema includes columns for **name**, **star rating**, and **price**.

## **How It Works**
1. **Scraping**: The script uses BeautifulSoup to parse the HTML of the target website and extract the required data.
2. **Data Processing**: Pandas is used to structure the data into a DataFrame.
3. **Data Storage**:
    - **Excel and CSV**: The DataFrame is written to `books.xlsx` and `books.csv` using Pandas.
    - **MySQL**: The DataFrame is inserted into the MySQL `books` table.

## **Dependencies**
- **beautifulsoup4**
- **pandas**
- **mysql-connector-python**
- **openpyxl**

## **Contributing**
If you would like to contribute to this project, please fork the repository and submit a pull request. For any issues, please open an issue on GitHub
