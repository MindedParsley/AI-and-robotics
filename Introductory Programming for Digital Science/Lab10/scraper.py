import os
from guizero import App, Text, Box, Picture, ListBox
from bs4 import BeautifulSoup as bs

#get filee paths
Base_DIR = os.path.dirname(os.path.abspath(__file__))
htmlFile = os.path.join(Base_DIR,"BattleStar.html")
logo = os.path.join(Base_DIR,"logo.png")

# load html and decode
with open(htmlFile, "r", encoding="utf-8") as file:
    html = file.read()

parsed = bs(html, "html.parser")

table = parsed.find("table")

#spittign the usefull data from the table
rows_data = []
for row in table.find_all("tr"):
    # Grab both header (th) and data (td) cells
    cells = row.find_all(["td", "th"])
    # Clean whitespace from each cell
    row_text = [cell.get_text(strip=True) for cell in cells]
    rows_data.append(row_text)

rows_data.pop(0)
episodes = []
summaries = []

for i in range(len(rows_data)):
    episodes.append(rows_data[i][0])
    summaries.append(rows_data[i][2])

#change summary text
def printSummary(epsiode):
    index = episodes.index(epsiode)
    summary = summaries[index]

    text.clear()
    text.append(summary)


#build the app
app = App(title="3x3 Button Grid", width=500, height=400, bg= "#303030")

imagebox = Box(app,width="fill",height=150,border=3)
listbox = Box(app,width=100,height="fill",align="left",border=0)
summaryBox = Box(app,width="fill",height="fill",border=0)

logo = Picture(imagebox, image=logo)

list = ListBox(listbox,episodes, height="fill",width="fill",command=printSummary)
list.text_size = 10
list.text_color = "#ffffff"

text = Text(summaryBox,text="please select an episode to view the summary",color="#ffffff")
text.tk.config(wraplength=230, justify="left")

app.display()
