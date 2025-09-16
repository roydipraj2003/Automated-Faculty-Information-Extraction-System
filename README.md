# Automated-Faculty-Information-Extraction-System
This project automates the process of extracting faculty details from college websites and organizes the information into a clean, searchable format. Using web scraping techniques, the system collects key details such as Name, Designation, Email, Research Interests, and Department. The extracted data is stored in a structured format and made accessible through an interactive dashboard.

**Objectives**
•	Scrape faculty names, titles, descriptions, emails, phone numbers, research areas from college webpages.
•	Save extracted data into structured Excel files.
•	Build a user-friendly Streamlit app for live scraping or Excel upload.
•	Provide data display and download features in the dashboard.

**Tools and Technologies**
•	Python for scripting.
•	BeautifulSoup and requests for web scraping.
•	Pandas for data handling and Excel export.
•	Streamlit for creating the interactive web app.

**Implementation Details**
•	Analyzed webpage HTML to identify tags and classes used for faculty info.
•	Developed scraping logic targeting specific HTML classes to reliably extract required fields.
•	Addressed challenges in extracting nested email tags and attribute fields.
•	Designed Streamlit app to take user inputs (college name, URL, or Excel upload).
•	Enabled data display in tables and Excel file download from the dashboard.

**Challenges**
•	Email extraction was complicated by nested HTML structures, requiring refined parsing strategy.
•	Handling dynamic content loading could be improved with browser automation (future work).
•	Ensuring flexible input modes necessitated integrating file upload and live scraping together.

**Results**
•	Successfully extracted faculty data into clean Excel files with complete fields.
•	Streamlit app provides seamless user experience to scrape or upload data and download results.
•	Facilitates rapid faculty data collection and visualization without manual copy-paste.

**Future Enhancements**
•	Implement JavaScript rendering support via Selenium or Puppeteer to handle dynamic pages.
•	Add pagination support to scrape multiple pages automatically.
•	Enhance UI with filters, search, and export options for better data exploration.
•	Deploy the Streamlit app on cloud platforms for web access.
•	Deploy the Streamlit app on cloud platforms for web access.
