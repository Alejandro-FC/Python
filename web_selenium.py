import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#Para inicializar el web scrapping con Selenium:

#Data para un mundial:

#path = '/home/alejandro/Programs/Cromedriver/chromedriver_linux64/chromedriver'
#service = Service(executable_path=path)
#driver = webdriver.Chrome(service=service)
#web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'

#driver.get(web)


#matches = driver.find_elements(by='xpath', value= '//th[@class="fhome"]/..')


#home = []
#score = []
#away=[] 

#for match in matches:
    #home.append(match.find_element(by='xpath', value = './th[1]').text)
    #score.append(match.find_element(by='xpath', value = './th[2]').text)
    #away.append(match.find_element(by='xpath', value = './th[3]').text)

    
#dict_football = {'home': home, 'score':score, 'away': away}
#df_football = pd.DataFrame(dict_football)
#df_football['year'] = '1982'
#time.sleep(2)


#df_football.to_csv('test_1982.csv')


#driver.quit()



#input() #Para que no se cierre al ejecutar el programa


#DATA para todos los mundiales:

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

path = '/home/alejandro/Programs/Cromedriver/chromedriver_linux64/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

def obtener_data(year):

    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    driver.get(web)


    matches = driver.find_elements(by='xpath', value= '//th[@class="fhome"]/..')


    home = []
    score = []
    away=[] 

    for match in matches:
        home.append(match.find_element(by='xpath', value = './th[1]').text)
        score.append(match.find_element(by='xpath', value = './th[2]').text)
        away.append(match.find_element(by='xpath', value = './th[3]').text)

    
    dict_football = {'home': home, 'score':score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)
    return df_football

fifa = [obtener_data(year) for year in years]


driver.quit()

df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_data.csv', index=False)




