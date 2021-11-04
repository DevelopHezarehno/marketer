import streamlit as st
import requests , json



endpoint=st.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])

st.header(f"Opean sea NFT API Explorer - {endpoint}")

st.sidebar.subheader("Filters")
collection = st.sidebar.text_input("Collection")
owner = st.sidebar.text_input("Owner")

if endpoint =='Assets':
  params ={
    
    'collection': collection
   
  }

  r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

response = r.json()

for asset in response["assets"]:
    st.image(asset['image_url'])


