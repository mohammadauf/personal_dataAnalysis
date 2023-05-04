from bs4 import BeautifulSoup

# load the HTML file
data = open("data.html", 'r', encoding='utf-8')
# parse the HTML file using BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

# find the div container with a specific class and remove it
divs_to_remove = soup.find_all('div', {'class': 'mdl-typography--text-right'})
for div in divs_to_remove:
    div.extract()

# save the modified HTML back to the file
with open('data.html', 'w',encoding='utf-8') as file:
    file.write(str(soup))
print("Done..")