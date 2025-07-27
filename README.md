# 🌦️ Weather Broadcaster with Voice [DEMO](https://weatherbroadcast.streamlit.app/)

This is a Streamlit-based web app that reads real-time weather updates from NOAA RSS feeds and speaks them aloud using text-to-speech (TTS).

## 🚀 Features

- 🔊 Converts current weather conditions to voice using `gTTS`
- 📍 Select from 11 U.S. cities (including Stockton, NY, LA, etc.)
- 🌐 Pulls weather via NOAA's `forecast.weather.gov` RSS feeds
- 🎛️ Clean user interface built with Streamlit
- 🧼 Auto-cleans HTML content from feeds for clarity

## 📦 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run app.py
```

> Replace `app.py` with your actual filename if different.

## 🔧 Technologies Used

- [Streamlit](https://streamlit.io/) for the interactive UI
- [gTTS](https://pypi.org/project/gTTS/) for text-to-speech
- [feedparser](https://pypi.org/project/feedparser/) to read RSS
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to clean HTML

## 🌐 Supported Cities

- New York (JFK)
- Los Angeles (LAX)
- Chicago (ORD)
- Miami (MIA)
- Dallas (DFW)
- Seattle (SEA)
- San Francisco (SFO)
- Denver (DEN)
- Atlanta (ATL)
- Boston (BOS)
- Stockton (KSCK)

## 📝 License
MIT License. Feel free to use and modify.
