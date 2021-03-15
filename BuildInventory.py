from bs4 import BeautifulSoup
import requests
import json
import datetime

f = open('food.html', 'r')
#count = 0
#for line in f:
#  print(line)
#  count += 1
#print(count)

def GetFromWiki(soupinfo):
  #f = open('Food/hot_wing.html', 'r')

  soup = BeautifulSoup(soupinfo, 'html.parser')
  new_soup = soup.find("blockquote")

  food_info = []
  type_index = -1;
  size_index = -1;
  level_index = -1;
  price_index = -1;

  for item in new_soup.stripped_strings:
    food_info.append(str(item))

  try:
    type_index = food_info.index("Type:")
  except:
    type_index = -1

  try:
    size_index = food_info.index("Size:")
  except:
    size_index = -1;

  try:
    level_index = food_info.index("Level required:")
  except:
    level_index = -1

  try:
    price_index = food_info.index("Selling Price:")
  except:
    price_index = -1

  #Food Type
  if type_index > 0 and size_index > type_index:
    print(food_info[type_index:size_index])

  #Size
  if size_index > 0 and level_index > size_index:
    print(food_info[size_index:level_index])
  elif size_index > 0 and price_index > size_index:
    print(food_info[size_index:price_index])

  #Level Required
  if level_index > 0 and price_index > level_index:
    print(food_info[level_index:price_index])

  if price_index > 0:
    print(food_info[price_index:])
#END OF FUNTION

soup = BeautifulSoup(f, "html.parser")
#print(soup.prettify())
food_items = soup.find_all("b", class_="ircm")
#print(food_items)
#print(str(food_items))
#print(len(food_items))

food_names = [] 

#remove the tag info 
for item in food_items:
  #print(str(item))
  curr = str(item)
  start = curr.find(">")
  end = curr.find("</")
  start += 1
  #print(curr[start:end])
  food_names.append(curr[start: end])

#print(food_names) 
for item in food_names:
  curr_item = item.replace(" ", "_")
  r = requests.get('https://kol.coldfront.net/thekolwiki/index.php/'+ curr_item)
  #print(r.text)
  #print(curr_item)
  soup = BeautifulSoup(r.text, "html.parser")
  #info = soup.find(id="mw-content-text")
  info = soup.select("#mw-content-text > table")
  #print(info)
  print(item)
  try:
    GetFromWiki(str(info))
  except:
    print("NOTHING FOUND IN WIKI FOR:", item)
  print("\n\n")
#  filename = "Food/" + curr_item + ".html"
#  w = open(filename, 'w')
#  w.write(str(info))
#  w.close()
  print("created file for:", item)
