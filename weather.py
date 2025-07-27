import streamlit as st
import feedparser
import tempfile
from gtts import gTTS
from datetime import datetime
from bs4 import BeautifulSoup

# ---------------------------
# App Configuration
# ---------------------------
st.set_page_config(page_title="🌦️ Weather Broadcaster", layout="centered")
st.title("🌦️ Weather Broadcaster with Voice")
st.caption("Click the refresh button below to update manually.")

# ---------------------------
# Manual Refresh Button
# ---------------------------
st.session_state.setdefault("refresh_trigger", 0)
if st.button("🔄 Refresh Now"):
    st.session_state.refresh_trigger += 1

# ---------------------------
# Location Selection
# ---------------------------
LOCATION_FEEDS = {
    "New York (JFK)": "https://forecast.weather.gov/xml/current_obs/KJFK.rss",
    "Los Angeles (LAX)": "https://forecast.weather.gov/xml/current_obs/KLAX.rss",
    "Chicago (ORD)": "https://forecast.weather.gov/xml/current_obs/KORD.rss",
    "Miami (MIA)": "https://forecast.weather.gov/xml/current_obs/KMIA.rss",
    "Dallas (DFW)": "https://forecast.weather.gov/xml/current_obs/KDFW.rss",
    "Seattle (SEA)": "https://forecast.weather.gov/xml/current_obs/KSEA.rss",
    "San Francisco (SFO)": "https://forecast.weather.gov/xml/current_obs/KSFO.rss",
    "Denver (DEN)": "https://forecast.weather.gov/xml/current_obs/KDEN.rss",
    "Atlanta (ATL)": "https://forecast.weather.gov/xml/current_obs/KATL.rss",
    "Boston (BOS)": "https://forecast.weather.gov/xml/current_obs/KBOS.rss",
    "Stockton (KSCK)": "https://forecast.weather.gov/xml/current_obs/KSCK.rss"
}

location = st.selectbox("Select a location:", list(LOCATION_FEEDS.keys()))
rss_url = LOCATION_FEEDS[location]

# ---------------------------
# Fetch and Clean Weather Data
# ---------------------------
feed = feedparser.parse(rss_url)
if not feed or not feed.entries or "summary" not in feed.entries[0]:
    st.error("⚠️ Unable to retrieve weather information. Please check the feed or try again later.")
    st.stop()

raw_summary = feed.entries[0].summary
soup = BeautifulSoup(raw_summary, "html.parser")
clean_summary = soup.get_text(separator="\n").strip()

last_updated = feed.entries[0].get("updated", datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))

# ---------------------------
# Display Weather Info
# ---------------------------
st.subheader(f"Weather in {location}")
st.write(clean_summary)
st.caption(f"Last updated: {last_updated}")

# ---------------------------
# Generate TTS Audio
# ---------------------------
@st.cache_data(show_spinner=False)
def generate_tts_audio(text: str) -> str:
    tts = gTTS(text)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    return tmp_file.name

try:
    audio_path = generate_tts_audio(clean_summary)
    st.subheader("🔊 Voice Forecast")
    with open(audio_path, "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
except Exception as e:
    st.error(f"Text-to-Speech generation failed: {e}")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit, gTTS, BeautifulSoup, and NOAA Weather Feeds.")
