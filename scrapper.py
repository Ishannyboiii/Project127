from bs4 import BeautifulSoup as bs
import pandas as pd
import requests 


# Wikipedia Exoplanet URL
stars_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(stars_url)

soup = bs(page.text,'html.parser')
star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)), columns = ["Star_name","Distance","Mass","Radius","Luminosity"])
df2.to_csv("stars.csv")

# # Define Exoplanet Data Scrapping Method
# def scrape():

#     for i in range(0,10):
#         print(f'Scrapping page {i+1} ...' )
        
#         # BeautifulSoup Object     
#         soup = BeautifulSoup(browser.page_source, "html.parser")

#         # Loop to find element using XPATH
#         for tr_tag in soup.find_all("tr", attrs={"class", "headerSort"}):

#             th_tags = tr_tag.find_all("li")
           
#             temp_list = []

#             for index, th_tag in enumerate(th_tags):

#                 if index == 0:                   
#                     temp_list.append(th_tag.find_all("a")[0].contents[0])
#                 else:
#                     try:
#                         temp_list.append(th_tag.contents[0])
#                     except:
#                         temp_list.append("")

#             star_data.append(temp_list)

#         # Find all elements on the page and click to move to the next page
#         browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

# # Calling Method    
# scrape()

# # Define Header
# headers = ["name", "distance", "mass", "radius"]

# # Define pandas DataFrame   
# planet_df_1 = pd.DataFrame(star_data, columns=headers)

# # Convert to CSV
# planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
