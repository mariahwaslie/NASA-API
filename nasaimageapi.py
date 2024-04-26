import requests
import streamlit as st
from bs4 import BeautifulSoup

date = st.date_input('put a date here')



def nasa_image():
    URL = f"https://api.nasa.gov/planetary/apod?api_key={API}&date={date}"
    r = requests.get(URL)
    data = r.json()
    st.title("Nasa Space Image of the Day")
    st.subheader(data['title'])

    text = data["hdurl"]
    st.image(text)
    st.caption(f'{data["explanation"]}')


st.sidebar.header("Search NASA News")


def search():
    space_search = st.sidebar.chat_input('Ask About Space')
    if space_search:
        st.sidebar.write("Search results for: " + space_search.capitalize())
        s = space_search.split(' ')
        words_to_search = ""
        for word in s:
            if len(s) > 1 and s[-1] != word:
                words_to_search += word + "+"
            else:
                words_to_search += word
        #searches the nasa news
        search_url = f'https://www.nasa.gov/?search={words_to_search}'
        r = requests.get(search_url)
        soup = BeautifulSoup(r.content, "html.parser")

        res = soup.find_all("div", class_="hds-search-result-content")
        images = soup.find_all("div", class_="hds-search-result-thumbnail")

        for i, image in zip(res, images):
            words_to_search = ""
            click = st.sidebar.write(i.find('h4',class_="hds-search-result-heading color-carbon-black heading-18 line-height-md").getText(),)
            link = i.find('em').getText()
            if click:
                 link_page = requests.get(url=link)
                 soup_page = BeautifulSoup(link_page.content, "html.parser")
            #     a = soup_page.prettify()
            #     st.sidebar.write('working')
            #     break
            # else:
            #     pass

            st.sidebar.image(image.find('img').get('src'), width=70)
            st.sidebar.write(link)
            st.sidebar.write(i.find('p', class_='hds-search-result-excerpt color-carbon-black margin-0').getText())

            # get the contents on the link on the same page



nasa_image()
search()
