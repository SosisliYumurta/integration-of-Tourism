import sys
import pandas as pd
import requests
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/andrzejmp/some_codes/main/python/tourism/data.csv')
def barForTK():
    year = df["YEAR"]
    tk = df[" TK"]

    import matplotlib.pyplot as plt

    plt.bar(year,tk,color="red")
    plt.title('Tourism Income of Turkey')
    plt.xlabel('Years')
    plt.ylabel('Income')
    
    plt.show()


def tourismForPoland():
    year = df["YEAR"]
    country = df[" PL"]

    plt.bar(year,country, color="pink")
    plt.title("Tourism Income of Poland")
    plt.xlabel("Years")
    plt.ylabel("Income")
    plt.show()   

def spainData():
    df = pd.read_csv('https://raw.githubusercontent.com/andrzejmp/some_codes/main/python/tourism/data.csv')

    years = df["YEAR"]
    country = df[" SP"]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.bar(years, country, color="yellow")
    ax.set_title("Data on tourism in Spain by year", fontsize=24)
    ax.set_xlabel('Years', fontsize=16)
    ax.set_ylabel("Number of people", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show() 

def allcountries():
  df = pd.read_csv('https://raw.githubusercontent.com/andrzejmp/some_codes/main/python/tourism/data.csv')
  
  year = df["YEAR"]
  spain = df[" SP"]
  turkey = df[" TK"]
  poland = df[" PL"]
  
  plt.style.use('seaborn')
  fig, ax = plt.subplots()
  ax.plot(year, spain, c='yellow')
  ax.plot(year, turkey, c='red')
  ax.plot(year, poland, c='pink')
  
  
  ax.set_title("Tourism in last decade, 2010-2020", fontsize=24)
  ax.set_xlabel('Income', fontsize=16) 
  ax.set_ylabel("Years", fontsize=16)
  ax.tick_params(axis='both', which='major', labelsize=16)
  
  plt.show()        

if len(sys.argv) == 1:
    print("please input t, p, s, a")
else:
    if sys.argv[1] == 't':
        barForTK() 
    elif sys.argv[1] == 'p':
        tourismForPoland()   
    elif sys.argv[1] == 's':
        spainData()  
    elif sys.argv[1] == "a":
        allcountries() 
    else:
        print("please input t, p, s, a")             




#tourismForPoland(df)




