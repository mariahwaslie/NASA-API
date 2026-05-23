# 🚀 NASA Space Image & News Search App

A Streamlit web application that displays NASA's Astronomy Picture of the Day (APOD) and allows users to search for NASA-related news articles directly from the sidebar.

This project combines:

- NASA's APOD API
- Web scraping with BeautifulSoup
- Interactive Streamlit UI components
- Dynamic image and news rendering

---

# 🌐 Live Demo

## Deployed Streamlit App

https://nasa-apigit-nwvrd5guepmhpbtsmujsbm.streamlit.app/

---

# Features

- View NASA's Astronomy Picture of the Day
- Select images by historical date
- Display image titles and explanations
- Search NASA-related news articles
- Display article thumbnails and summaries
- Interactive sidebar search experience
- Real-time API data retrieval

---

# Technologies Used

- Python 3
- Streamlit
- Requests
- BeautifulSoup4
- NASA APOD API
- HTML Parsing / Web Scraping

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nasa-space-app.git
cd nasa-space-app
```

---

## 2. Create a Virtual Environment

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
NASA_API_KEY=YOUR_API_KEY_HERE
```

You can get a free API key from:

https://api.nasa.gov/

---

# Running the Application

Run the Streamlit app locally with:

```bash
streamlit run app.py
```

---

# Project Structure

```bash
project/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# How It Works

## NASA Astronomy Picture of the Day

The application connects to NASA's APOD API and retrieves:

- High-resolution image
- Image title
- Detailed explanation
- Historical image data by date

The content is rendered dynamically using Streamlit components.

---

## NASA News Search

Users can search NASA-related topics directly from the sidebar.

The application:

1. Sends a request to NASA-related pages
2. Scrapes article content using BeautifulSoup
3. Displays:
   - Article title
   - Thumbnail image
   - Summary
   - Article link

---

# Example Searches

Try searching topics like:

- Mars
- Black holes
- Artemis mission
- Hubble Telescope
- SpaceX
- James Webb Telescope

---

# Future Improvements

- Add clickable article navigation
- Improve search result formatting
- Add response caching
- Add loading animations
- Improve responsive/mobile design
- Add dark mode support
- Add NASA video/media support
- Add article bookmarking functionality

---

# Known Issues

- Some NASA pages may change structure and affect scraping
- Search results depend on external website formatting
- NASA API rate limits may occasionally apply

---

# Concepts Demonstrated

This project demonstrates:

- REST API integration
- Web scraping
- Streamlit application development
- Environment variable management
- JSON parsing
- HTTP requests
- Interactive UI design
- Dynamic content rendering

---

# Requirements

```txt
streamlit
requests
beautifulsoup4
python-dotenv
```

---

# Author

Created as a Python + Streamlit project exploring:

- APIs
- Space data visualization
- Web scraping
- Interactive web applications
- Python development workflows
