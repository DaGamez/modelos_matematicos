import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario.html"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Extract all visible text
    complete_text = soup.get_text(separator='\n', strip=True)

    # Step 4: Save the complete text to a file
    with open('complete_text2.txt', 'w', encoding='utf-8') as file:
        file.write(complete_text)
    
    print("Complete text extracted and saved successfully.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
