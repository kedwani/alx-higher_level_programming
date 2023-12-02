import requests
from bs4 import BeautifulSoup
import spacy

# Fetch the webpage content
url = "your_webpage_url"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract text from HTML
paragraphs = soup.find_all('p')
text_content = ' '.join([p.text for p in paragraphs])

# Summarize using spaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp(text_content)
summary = ' '.join(sent.text for sent in doc.sents[:3])  # Adjust the number of sentences as needed

print(summary)
