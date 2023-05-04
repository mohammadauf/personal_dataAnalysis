from bs4 import BeautifulSoup
import pandas as pd


# read file
data = open("data.html", 'r', encoding='utf-8')
soup = BeautifulSoup(data, 'html.parser')

# get all anchor tag
containers = soup.find_all('div', {'class': 'mdl-typography--body-1'})
all_links = []
for container in containers:
    try:
        second_anchors = container.find_all('a')[0]
        all_links.append(second_anchors.get('href'))
    except IndexError:
        all_links.append("")



# scrap the video title..
text=[]
for container in containers:
    try:
        second_anchors = container.find_all('a')[0]
        text.append(second_anchors.get_text().replace("\n          ",""))
    except IndexError:
        text.append("")


# scrap the youtube channel name..
channel_name = []

for container in containers:
    try:
        second_anchors = container.find_all('a')[1]
        channel_name.append(second_anchors.get_text().replace("\n          ",""))
    except IndexError:
        channel_name.append("")


date_and_time=[]
for container in containers:
    try:
        br_tag=container.find('br')
        text_after_br = br_tag.next_sibling.next_sibling.next_sibling
        date_and_time.append(text_after_br)
    except AttributeError:
        text_after_br = br_tag.next_sibling.next_sibling
        date_and_time.append(text_after_br)


# export into csv file...
df = pd.DataFrame({"title": text, "channel_name":channel_name,"links": all_links,"date_&_time":date_and_time})

df.to_csv("out.csv")

print("export sucessfull...")
data.close()


