import streamlit as st
import requests

def download_font_file(url):
    headers = {
        'Dnt': '1',
        'Origin': 'https://app.fontvisual.com',
        'Referer': 'https://app.fontvisual.com/',
        'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        return None

st.title('Font Downloader')

url = st.text_input('Enter the URL of the font file')
if st.button('Download'):
    if url:
        font_file = download_font_file(url)
        if font_file:
            st.markdown(f"### Download Here: [Download {url.split('/')[-1]}](data:application/font-woff;base64,{font_file.decode('utf-8')})")
        else:
            st.markdown('Failed to download the font file. Please check the URL and try again.')
