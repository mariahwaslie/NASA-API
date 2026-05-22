# NASA Space Image & News Search App

A Streamlit web application that displays NASA's Astronomy Picture of the Day (APOD) and allows users to search for NASA-related news articles directly from the sidebar.

This project uses the NASA API along with web scraping techniques to create an interactive space-themed application.

---

## Features

- View NASA's Astronomy Picture of the Day
- Select images by date
- Display image title and explanation
- Search NASA news articles
- Display article thumbnails and summaries
- Interactive Streamlit sidebar search

---

## Technologies Used

- Python 3
- Streamlit
- Requests
- BeautifulSoup4
- NASA APOD API

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/nasa-space-app.git
cd nasa-space-app
```

---

### 2. Install dependencies

```bash
pip install streamlit requests beautifulsoup4
```

---

### 3. Add your NASA API key

Create a variable called `API` in your Python file:

```python
API = "YOUR_NASA_API_KEY"
```

You can get a free API key from:

https://api.nasa.gov/

---

## Running the Application

Run the Streamlit app with:

```bash
streamlit run app.py
```

---

## Project Structure

```bash
project/
├── app.py
├── README.md
└── requirements.txt
```

---

## How It Works

### NASA Image of the Day

The app connects to the NASA APOD API using a selected date and retrieves:

- Image
- Title
- Explanation

The image is displayed using Streamlit.

---

### NASA News Search

The sidebar includes a search bar where users can search NASA-related topics.

The application:

1. Sends a request to NASA's website
2. Scrapes search results using BeautifulSoup
3. Displays:
   - Article title
   - Thumbnail image
   - Summary
   - Link to the article

---

## Example Features

### Astronomy Picture of the Day

- Displays high-resolution NASA images
- Supports historical dates

### NASA News Search

Search examples:

- Mars
- Black holes
- Artemis mission
- SpaceX
- Hubble Telescope

---

## Example Screenshot

```bash
NASA Space Image of the Day

[Image Displayed Here]

Title: Galaxy Cluster

Explanation:
A detailed explanation of the selected NASA image...

Sidebar:
- Search NASA News
- Mars Articles
- Space Exploration News
```

---

## Future Improvements

- Add clickable article navigation
- Improve search result formatting
- Add caching for faster performance
- Add loading animations
- Deploy using Streamlit Cloud
- Add dark mode styling
- Add video support for NASA APOD media

---

## Known Issues

- Some NASA article pages may not load correctly
- Search results depend on NASA website structure
- API key must be manually added

---

## Concepts Demonstrated

This project demonstrates:

- API integration
- Web scraping
- Streamlit application development
- JSON handling
- Interactive UI development
- HTTP requests
- HTML parsing with BeautifulSoup

---

## Requirements

```txt
streamlit
requests
beautifulsoup4
```

---

## Author

Created as a Python and Streamlit project exploring:
- APIs
- Space data visualization
- Web scraping
- Interactive web applications
