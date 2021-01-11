#created By Upendra Goutam @k4coding
import streamlit as st
from pytube import YouTube
import os
import base64


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
      yt.streams.filter().get_by_resolution("720p").download("","yt.mp4")#.download('D:/') # download with resolution and path 
      href1= get_binary_file_downloader_html("yt.mp4",'Video', unsafe_allow_html=True)
      st.write(href1)
      st.info('file downloaded in D: drive')
      st.balloons()
    except Exception as e:  
        print( e )  

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'wb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href