#created By Upendra Goutam @k4coding
import streamlit as st
import pandas as pd
from pytube import YouTube

url=st.text_input("enter youtube url here") #input text box for url
if st.button("Load"): #runs when button click
   yt=YouTube(url) # youtube instance 
   highres=yt.streams.get_highest_resolution().resolution #finding highest resolution
   st.write("resolution:" + highres) # displaying highest resolution
   
if st.button("download"):
    print(url)
    yt=YouTube(url)  
    try:  
        # downloading the video  
        
      yt.streams.filter().get_by_resolution("720p").download("D:/") # download with resolution and path

      st.info('file downloaded in D drive')
      st.balloons()
    except Exception as e:  
        print( e )  
print('Task Completed!')  