import streamlit as st
import serpapi
import pandas as pd
import matplotlib.pyplot as plt
from serpapi import GoogleSearch

#header
c1,c2 = st.columns(2)
c1.image("E-pharmacy logo.png", width= 250)
c2.header("E-Pharmacy price compairsion system")

#-----------------------------------------------------------------------------------------
def compare(med_name):
    params = {
        "engine": "google_shopping",
        "q":med_name,
        "api_key": "09f56ef98187254e9ea20f09d0f120c6d9bc9bbbb401615a00c6b7b29e64f4be",
        "gl":"in"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["shopping_results"]
    return(shopping_results)

#----------------------------------------------------------------------------------------
st.sidebar.title("Enter Name of Medicine:")
med_name=st.sidebar.text_input("Enter Name here 👇:")
number=st.sidebar.text_input("Enter Number of options here 👇:")

med_company=[]
med_price=[]

if med_name is not None:
    if st.sidebar.button("Price compair"):
        shopping_results=compare(med_name)
        lowest_price = float((shopping_results[0].get('price'))[1:])
        print(lowest_price)
        lowest_price_index = 0

        st.sidebar.image(shopping_results[0].get('thumbnail'))


        for i in range(int(number)):
            current_price =  float((shopping_results[i].get('price'))[1:])
            med_company.append(shopping_results[i].get("source"))
            med_price.append (float((shopping_results[i].get('price'))[1:]))
            #---------------------------------------------------------------------------
            st.title(f"Option {i+1}")
            c1,c2 = st.columns(2)
            c1.write("company:")
            c2.write(shopping_results[i].get("source"))

            c1.write("Title:")
            c2.write(shopping_results[i].get("title"))

            c1.write("Price:")
            c2.write(shopping_results[i].get("price"))

            url=shopping_results[i].get("product_link")
            c1.write("Buy link:")
            c2.write(f"[Link]({url})")
            if (current_price < lowest_price):
                lowest_price = current_price
                lowest_price_index = i

        #For best price

        st.title("Best option:")
        c1, c2 = st.columns(2)
        c1.write("company:")
        c2.write(shopping_results[lowest_price_index ].get("source"))

        c1.write("Title:")
        c2.write(shopping_results[lowest_price_index ].get("title"))

        c1.write("Price:")
        c2.write(shopping_results[lowest_price_index ].get("price"))

        url = shopping_results[lowest_price_index ].get("product_link")
        c1.write("Buy link:")
        c2.write(f"[Link]({url})")

        #Graph comparision
        df=pd.DataFrame(med_price,med_company)
        st.title("chart comparison")
        st.bar_chart(df)

        fig,ax=plt.subplots()
        ax.pie(med_price,labels=med_company,shadow=True)
        ax.axis("equal")
        st.pyplot(fig)




