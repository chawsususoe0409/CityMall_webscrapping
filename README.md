# CityMall_webscrapping
Finalcaptstoneprojectv1.1
# City Mall Myanmar Product Data Extraction System

## Project Overview

This project is a Python-based web scraping system developed to automate the collection of product information from the City Mall Myanmar e-commerce website.

The system extracts product details from the **Computer Components & Accessories** category and exports the collected data into Microsoft Excel format for further analysis and reporting.

The project was developed as a capstone project to demonstrate practical skills in:

- Web Scraping
- Data Collection
- Data Processing
- Python Programming
- Excel Data Export
- Error Handling
- HTML Parsing

---

## Business Problem

E-commerce websites contain large amounts of product information that can be useful for:

- Market research
- Competitor analysis
- Price comparison
- Product monitoring
- Business intelligence

Manually collecting this information is time-consuming and inefficient.

This project automates the data collection process and stores the results in a structured Excel file.

---

## Project Objectives

### Primary Objective

Develop an automated solution to collect product information from City Mall Myanmar.

### Specific Objectives

- Extract product names.
- Extract product prices.
- Extract seller information.
- Extract product URLs.
- Process multiple category pages automatically.
- Export data into Excel format.
- Handle missing values gracefully.

---

## Target Website

**Website:** City Mall Myanmar

**Category:**
Computer Components & Accessories

Example URL:

```text
https://www.citymall.com.mm/citymall/en/Categories/Home-%26-Living-Lifestyle/Electronics/Computer-Components-%26-Accessories/c/id05011003
```

---

## System Architecture

```text
City Mall Website
        │
        ▼
HTTP Request (Requests)
        │
        ▼
HTML Response
        │
        ▼
BeautifulSoup Parser
        │
        ▼
Data Extraction
        │
        ▼
Data Validation
        │
        ▼
Pandas DataFrame
        │
        ▼
Excel Export
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main Programming Language |
| Requests | Web Request Handling |
| BeautifulSoup4 | HTML Parsing |
| Pandas | Data Processing |
| tqdm | Progress Bar Display |
| urllib | URL Decoding |
| datetime | Timestamp Generation |
| openpyxl | Excel File Export |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/citymall-product-scraper.git
```

### Navigate to Project Folder

```bash
cd Finalproject
```

### Install Dependencies

```bash
pip install requests beautifulsoup4 pandas tqdm openpyxl
```

---

## Project Structure

```text
citymall-product-scraper/
│
├── finalcapstonev1_1.py
├── README.md
│
├── Output Files
│   ├── CMProduct_Computeraccessories_update.xlsx
│   └── CMtimelyproduct_YYYY-MM-DD_HH-MM-SS.xlsx
│
└── Screenshots
    ├── execution.png
    └── output.xlsx
```

---

## Functional Modules

### 1. Web Page Retrieval Module

Responsible for:

- Sending HTTP requests
- Receiving HTML responses
- Creating BeautifulSoup objects

Output:

```text
BeautifulSoup Object
```

---

### 2. Page URL Generation Module

Creates category page URLs automatically.

Example:

```text
Page 0
Page 1
Page 2
Page 3
...
```

Current implementation uses a predefined page count.

---

### 3. Product Information Extraction Module

Extracts:

#### Product Name

Example:

```text
Wireless Mouse
```

#### Product Price

Example:

```text
35000 Ks
```

#### Seller

Example:

```text
ABC Electronics
```

#### Product URL

Example:

```text
https://www.citymall.com.mm/...
```

---

### 4. Data Export Module

Creates a Pandas DataFrame and exports the result into Excel.

Generated Files:

```text
CMProduct_Computeraccessories_update.xlsx
```

and

```text
CMtimelyproduct_2026-10-07_10-30-00.xlsx
```

---

## Data Flow Diagram

```text
Website
   │
   ▼
Page Collection
   │
   ▼
Product Extraction
   │
   ▼
Data Storage (Lists)
   │
   ▼
Pandas DataFrame
   │
   ▼
Excel Output
```

---

## Sample Output

| Product Name | Price | Seller | Product URL |
|-------------|--------|---------|-------------|
| Gaming Mouse | 35000 | Seller A | URL |
| USB Hub | 25000 | Seller B | URL |
| Keyboard | 55000 | Seller C | URL |

---

## Error Handling

The system includes exception handling for:

### Missing Price

Returns:

```text
Price may not Specified
```

### Missing Seller

Returns:

```text
Seller not display
```

### Export Errors

Displays error messages if Excel export fails.

---

## Project Strengths

- Easy to understand.
- Modular function design.
- Handles missing data.
- Exports directly to Excel.
- Uses progress tracking.
- Suitable for beginners learning web scraping.
- Reusable architecture for other e-commerce websites.

---

## Current Limitations

### Fixed Page Count

The current version uses a manually defined page count.

If the website adds more pages, the script must be updated manually.

### Website Dependency

Changes to the website HTML structure may require updates to the scraping logic.

### No Retry Mechanism

Failed requests are not automatically retried.

---

## Future Enhancements

### Version 2.0

Planned improvements:

- Automatic page number detection
- Loop pages and extract data from all pages
- Retry mechanism for failed requests
- Logging system
- CSV export
- Database storage
- Duplicate record removal
- Product stock status extraction
- Product category extraction
- Scheduled execution
- Dashboard reporting

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- Python Programming
- Web Scraping Techniques
- HTML Structure Analysis
- Data Cleaning
- Data Processing
- Excel Automation
- Error Handling
- Modular Programming
- Software Development Lifecycle

---

## Conclusion

This project successfully demonstrates the development of an automated web scraping solution for collecting product information from an e-commerce platform.

The solution reduces manual effort, improves efficiency, and provides structured data for analysis and decision-making. It also serves as a foundation for future enhancements involving data analytics, reporting dashboards, and automated market monitoring systems.

---

## Author

**Chaw Su Su Soe**

IT Professional | Odoo System Administrator | Software Support Specialist

Capstone Project – Python Web Scraping & Data Extraction
