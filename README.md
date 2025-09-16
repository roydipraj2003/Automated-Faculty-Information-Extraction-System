# Automated-Faculty-Information-Extraction-System
This project automates the process of extracting faculty details from college websites and organizes the information into a clean, searchable format. Using web scraping techniques, the system collects key details such as Name, Designation, Email, Research Interests, and Department. The extracted data is stored in a structured format and made accessible through an interactive dashboard.

# Automated Faculty Directory with Interactive Dashboard

This project automates the extraction of faculty details from college websites and provides a user-friendly **Streamlit dashboard** for data exploration and download. It helps students, researchers, and institutions save time by eliminating manual copy-paste from faculty web pages.  

---

##  Objectives
- Scrape faculty **names, titles, descriptions, emails, phone numbers, research areas** from college webpages.  
- Save extracted data into structured **Excel files**.  
- Build a **Streamlit app** for live scraping or Excel upload.  
- Provide data **display and download features** in the dashboard.  

---

##  Tools and Technologies
- **Python** – scripting and automation  
- **BeautifulSoup, Requests** – web scraping  
- **Pandas** – data handling & Excel export  
- **Streamlit** – interactive web app  

---

##  Implementation Details
- Analyzed webpage HTML to identify relevant **tags and classes** used for faculty info.  
- Developed scraping logic targeting specific HTML classes to reliably extract required fields.  
- Addressed challenges in extracting **nested email tags and attribute fields**.  
- Designed a **Streamlit app** to take user inputs (college name, URL, or Excel upload).  
- Enabled data display in tables and **Excel file download** from the dashboard.  

---

##  Challenges
- Email extraction was complicated by **nested HTML structures**, requiring refined parsing.  
- Handling **dynamic content loading** (future enhancement with Selenium/Puppeteer).  
- Ensuring flexible input modes (file upload + live scraping) required robust integration.  

---

## Results
- Successfully extracted faculty data into **clean Excel files** with complete fields.  
- Built an **interactive Streamlit dashboard** for scraping, uploading, and downloading results.  
- Facilitates **rapid faculty data collection and visualization** without manual effort.  

---

##  Future Enhancements
- Add **JavaScript rendering support** (Selenium or Puppeteer) for dynamic sites.  
- Implement **pagination support** to scrape multiple pages.  
- Enhance UI with **filters, search, and export options** for better exploration.  
- Deploy the Streamlit app on **cloud platforms** (Streamlit Cloud, Heroku, AWS).  

