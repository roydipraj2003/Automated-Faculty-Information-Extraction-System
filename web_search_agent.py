import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_faculty(url, college_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    name_divs = soup.find_all("div", class_="wph_element wmts_name wmts_element")

    faculty_data = []

    for name_div in name_divs:
        name = name_div.text.strip()
        parent = name_div.find_parent()
        if not parent:
            continue

        title_tag = parent.find("h3", class_="wph_element wmts_job_title wmts_element")
        title = title_tag.text.strip() if title_tag else None

        desc_tag = parent.find("div", class_="wph_element wmts_description wmts_element")
        description = desc_tag.text.strip() if desc_tag else None

        attr_container = parent.find("div", class_="wph_element wmts_attributes wmts_element")

        email = None
        research = None
        phone = None

        if attr_container:
            email_tag = attr_container.find("a", href=lambda href: href and href.startswith("mailto:"))
            if email_tag:
                email = email_tag.text.strip()

            attr_items = attr_container.find_all("div", class_="wph_element wmts_element wmts_attribute")
            for item in attr_items:
                label_span = item.find("span", {"data-wph-type": "label"})
                value_span = item.find("span", {"data-wph-type": "value"})
                label = label_span.text.strip().lower() if label_span else ""
                value = value_span.text.strip() if value_span else ""

                if "research" in label:
                    research = value
                elif "phone" in label:
                    phone = value

        faculty_data.append({
            "Name": name,
            "Title": title,
            "Description": description,
            "Email": email,
            "Phone": phone,
            "Research Areas": research,
            "College": college_name
        })

    df = pd.DataFrame(faculty_data)
    file_name = f"{college_name.replace(' ', '_')}_faculty_data.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Scraped and saved {len(df)} records to {file_name}")

if __name__ == "__main__":
    college_name = input("Enter the college name: ").strip()
    url = input("Enter the full faculty page URL: ").strip()
    scrape_faculty(url, college_name)
