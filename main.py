##Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from math import pi
import statistics
import string
import altair as alt

#Title of the dashboard
st.title("Tracer Study")


#Define the file path 
path1 = "C:/Users/MSI/Downloads/Magang 2.0/Data Mentah Sortir_Analisis Tren_v2.xlsx"
path2 = "C:/Users/MSI/Downloads/Magang 2.0/Data responden 2018-2022.xlsx"
path3 = "C:/Users/MSI/Downloads/Magang 2.0/Data Mentah Kuesioner User Survey_Analisis Tren_v3.xlsx"

#show the text input for the Program Studi
jurusan = st.text_input('Masukkan jurusan (Huruf Awal Kapital)')


#DATA MENTAH SORTIR ANALISIS TREN
#import specific sheets and store it into dataframe
# List to store the filtered dataframes
# List to store the filtered dataframes
filtered_dataframes = []

# Loop through each year
for year in range(2018, 2023):
    sheet_name = str(year)
    
    try:
        # Read the Excel sheet for the current year
        df = pd.read_excel(path1, sheet_name=sheet_name, header=0)
        
        # Check the column name based on the year
        if year >= 2018 and year <= 2020:
            column_name = '4. Program Studi'
        else:
            column_name = 'Program Studi'
        
        # Filter the dataframe based on the program study
        conditional = [x+1 for x in df[df[column_name] != jurusan].index]
        df_filtered = pd.read_excel(path1, sheet_name=sheet_name, header=0, skiprows=conditional)
        
        # Add the filtered dataframe to the list
        filtered_dataframes.append(df_filtered)
        
    except FileNotFoundError:
        # Handle the case when the sheet is not found
        print("Sheet not found:", sheet_name)

ITB_2011 = filtered_dataframes[0]
ITB_2012 = filtered_dataframes[1]
ITB_2013 = filtered_dataframes[2]
ITB_2014 = filtered_dataframes[3]
ITB_2015 = filtered_dataframes[4]
      

# Dataframe Responden
filtered_dataframes_responden = []

# Loop through each year
for year in range(2018, 2023):
    if year >= 2018 and year <=2020:
        sheet_name = f'sarjana_{year}_ ang.{year-7}'
    else:    
        sheet_name = f'sarjana_{year}_ang.{year-7}'
    
    try:
        # Read the Excel sheet for the current year
        df = pd.read_excel(path2, sheet_name=sheet_name, header=0)
        
        # Check the column name based on the year
        column_name = 'PRODI'
        
        # Filter the dataframe based on the program study
        conditional = [x+1 for x in df[df[column_name] != jurusan].index]
        df_filtered = pd.read_excel(path2, sheet_name=sheet_name, header=0, skiprows=conditional)
        
        # Add the filtered dataframe to the list
        filtered_dataframes_responden.append(df_filtered)
        
    except FileNotFoundError:
        # Handle the case when the sheet is not found
        print("Sheet not found:", sheet_name)


responden2018=filtered_dataframes_responden[0]
responden2019=filtered_dataframes_responden[1]
responden2020=filtered_dataframes_responden[2]
responden2021=filtered_dataframes_responden[3]
responden2022=filtered_dataframes_responden[4]

## USER SURVEI
# List to store the filtered dataframes
filtered_dataframes_kuisioner = []
# Loop through each year
for year in range(2018, 2023):
    sheet_name = f'User Survey {year}'  # Generate the sheet name dynamically
    
    try:
        # Read the Excel sheet for the current year
        df = pd.read_excel(path3, sheet_name=sheet_name, header=0)
        
        # Drop the blank column in the first row
        df = df.dropna(axis=1, how='all')
        
        # Check the column name based on the year
        column_name = 'Prodi' if year == 2018 else 'Program Studi'
        
        # Filter the dataframe based on the program study
        conditional = [x+1 for x in df[df[column_name] != jurusan].index]
        df_filtered = pd.read_excel(path3, sheet_name=sheet_name, header=0, skiprows=conditional)
        
        # Add the filtered dataframe to the list
        filtered_dataframes_kuisioner.append(df_filtered)
        
    except FileNotFoundError:
        # Handle the case when the sheet is not found
        print("Sheet not found:", sheet_name)

kuisioner2018 = filtered_dataframes_kuisioner[0]
kuisioner2019 = filtered_dataframes_kuisioner[1]
kuisioner2020 = filtered_dataframes_kuisioner[2]
kuisioner2021 = filtered_dataframes_kuisioner[3]
kuisioner2022 = filtered_dataframes_kuisioner[4]



## Visualization
#Bar Chart Data Responden
def summing(a):
    x = len(a)
    b = 0
    for i in range(x):
        b += a[i]
    return b

# Extract only % column from DataFrame with default value of None
if not responden2018.empty:
    resp2018 = responden2018['%'].values[0] * 100
else:
    resp2018 = 0

if not responden2019.empty:
    resp2019 = responden2019['%'].values[0] * 100
else:
    resp2019 = 0
if not responden2020.empty:
    resp2020 = responden2020['%'].values[0] * 100
else:
    resp2020 = 0
if not responden2021.empty:
    resp2021 = responden2021['%'].values[0] * 100
else:
    resp2021 = 0
if not responden2022.empty:
    resp2022 = responden2022['%'].values[0] * 100
else:
    resp2022 = 0

responden = [resp2018, resp2019, resp2020, resp2021, resp2022]
# responden = np.concatenate([resp2018, resp2019, rep2020, resp2021, resp2022])

#initiate year
year = ['2018','2019','2020','2021','2022']


# Buat DataFrame baru dengan semua tahun
data = pd.DataFrame({'Tahun': ['2018', '2019', '2020', '2021', '2022']})
#set color for graph
colorresp = ['#4F81BD','#F79646','#95B554','#7E629F','#CC3300']

source = pd.DataFrame({
    'Responden(%)':responden,
    'Tahun':['2018','2019','2020','2021','2022']
})

bar_chart = alt.Chart(source).mark_bar().encode(
        y='Responden(%):Q',
        x='Tahun:O',
        color=alt.Color("Tahun", scale=alt.Scale(domain=year, range=colorresp)
    ))
 
bares = st.altair_chart(bar_chart, use_container_width=True)


# #Job status
# def countps(a,b,c):
# #this function is for count how much the exact string occurs in the data
#     a = (b == c)
#     a = a.sum()
#     return a
# def counterps(a,b):
# #this function calls previous function with automated condition/string so it
# #might be easier and look more clean in the main script
#     kw1 = 'bekerja'
#     kw2 = 'bekerja dan wiraswasta' 
#     kw3 = 'wirausaha'
#     kw4 = 'melanjutkan studi'
#     kw5 = 'tidak bekerja'
#     if (b==1):
#         e=kw1
#     elif(b==2):
#         e=kw2
#     elif(b==3):
#         e=kw3
#     elif(b==4):
#         e=kw4
#     elif(b==5):
#         e=kw5
#     c = []
#     d = countps(c, a, e)
#     return d
# def categ(i):
#     a = [js18[i],js19[i],js20[i],js21[i],js22[i]]
#     return a
# def findpercentage(a,b,c):
#     e = a+b+c
#     a = (a/e)*100
#     a = round(a)
#     b = (b/e)*100
#     b = round(b)
#     c = (c/e)*100
#     c = round(c)
#     d = [a,b,c]
#     return d
# def summing(a):
#     x = len(a)
#     b = 0
#     for i in range(x):
#         b += a[i]
#     return b

# #extracting the "pekerjaan utama saat ini" column for each year
# jb18 = ITB_2011.iloc[:,75]
# jb19 = ITB_2012.iloc[:,76]
# jb20 = ITB_2013.iloc[:,76]
# jb21 = ITB_2014.iloc[:,77]
# jb22 = ITB_2015.iloc[:,77]

# #make the format uniform for all sheets
# jb21 = jb21.str.lower()
# jb22 = jb22.str.lower()
# #count the sum for each categories by calling the function counterps
# # kw1 = 'bekerja' kw2 = 'bekerja dan wiraswasta' kw3 = 'wirausaha'
# # kw4 = 'melanjutkan studi'kw5 = 'tidak bekerja'
# # bekerja
# emp18 = counterps(jb18,1)
# emp19 = counterps(jb19,1)
# emp20 = counterps(jb20,1)
# emp21 = counterps(jb21,1)
# emp22 = counterps(jb22,1)

# # bekerja dan wiraswasta
# bw18 = counterps(jb18,2)
# bw19 = counterps(jb19,2)
# bw20 = counterps(jb20,2)
# bw21 = counterps(jb21,2)
# bw22 = counterps(jb22,2)

# # wirausaha
# wr18 = counterps(jb18,3)
# wr19 = counterps(jb19,3)
# wr20 = counterps(jb20,3)
# wr21 = counterps(jb21,3)
# wr22 = counterps(jb22,3)

# # melanjutkan studi
# ms18 = counterps(jb18,4)
# ms19 = counterps(jb19,4)
# ms20 = counterps(jb20,4)
# ms21 = counterps(jb21,4)
# ms22 = counterps(jb22,4)

# # tidak bekerja
# tb18 = counterps(jb18,5)
# tb19 = counterps(jb19,5)
# tb20 = counterps(jb20,5)
# tb21 = counterps(jb21,5)
# tb22 = counterps(jb22,5)

# #calculate percentage for each categories for each years and store it into matrix
# js18 = [emp18,bw18,wr18,ms18,tb18]
# js19 = [emp19,bw19,wr19,ms19,tb19]
# js20 = [emp20,bw20,wr20,ms20,tb20]
# js21 = [emp21,bw21,wr21,ms21,tb21]
# js22 = [emp22,bw22,wr22,ms22,tb22]

# # def categ(i):
# #     a = [js18[i],js19[i],js20[i],js21[i],js22[i]]
# #     return a
# #this var still contain amount(N) not percentage
# emp_tot = categ(0)
# bw_tot = categ(1)
# wr_tot = categ(2)
# ms_tot = categ(3)
# tb_tot = categ(4)
# # display(tb_tot)

# def percent(a,b):
#     x = []
#     for i in range(len(a)):
#         pct = (a[i]/b) * 100
#         x.append(round(pct))
#     return x
# def categ(i):
#     a = [per18[i],per18[i],per20[i],per21[i],per22[i]]
#     return a

# js18 = [emp18,bw18,wr18,ms18,tb18]
# js19 = [emp19,bw19,wr19,ms19,tb19]
# js20 = [emp20,bw20,wr20,ms20,tb20]
# js21 = [emp21,bw21,wr21,ms21,tb21]
# js22 = [emp22,bw22,wr22,ms22,tb22]

# #calculate percentage for each year
# sum18 = summing(js18)
# per18 = percent(js18,sum18)
# sum19 = summing(js19)
# per19 = percent(js19,sum19)
# sum20 = summing(js20)
# per20 = percent(js20,sum20)
# sum21 = summing(js21)
# per21 = percent(js21,sum21)
# sum22 = summing(js22)
# per22 = percent(js22,sum22)

# #visualization
# #set the bar graph length and amount of bar
# x = np.arange(len(js18))
# width = 0.15

# category = ['Bekerja', 'Bekerja dan\nWiraswasta', 'Wirausaha',
#                'Melanjutkan Studi', 'Tidak Bekerja']
# colorresp = ['steelblue','orange','yellowgreen','mediumpurple','indianred']

# plot data in grouped manner of bar type

# graph = st.selectbox(
#     'Choose Data Visualization',
#     ('Data Responden Bar Graph',
#      'Status Pekerjaan Bar Graph',
#      'Radar Graph Kompetensi')
# )

# if graph =='Data Responden Bar Graph':

##Waktu Tunggu

# display(ITB_2011)
# sl18 = ITB_2011.iloc[1:,77]
# sl19 = ITB_2012.iloc[1:,78]
# sl20 = ITB_2013.iloc[1:,78]
# sl21 = ITB_2014.iloc[1:,79]
# sl22 = ITB_2015.iloc[1:,79]

# co18 = sl18.describe().T
# co19 = sl19.describe().T
# co20 = sl20.describe().T
# co21 = sl21.describe().T
# co22 = sl22.describe().T

# # st.write(co18)
# sl = pd.concat([co18,co19,co20,co21,co22], axis=1)

# st.write(sl)

