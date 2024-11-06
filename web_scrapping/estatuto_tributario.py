import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario.html"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Extract the articles
    articles = soup.find_all('div', class_='articulo')  # Adjust the class name if needed
    complete_text = ""
    
    # Step 4: Save all articles to a complete text file
    with open('complete_text.txt', 'w', encoding='utf-8') as complete_file:
        for idx, article in enumerate(articles, start=1):
            article_text = article.get_text(separator='\n', strip=True)
            complete_text += f"Articulo {idx}:\n{article_text}\n\n"
            
            # Step 5: Save each article in a separate text file
            with open(f'articulo_{idx}.txt', 'w', encoding='utf-8') as article_file:
                article_file.write(article_text)
        
        # Write the complete text to the complete file
        complete_file.write(complete_text)
    
    print("Articles extracted and saved successfully.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
