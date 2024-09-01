## AI Research Paper Scraper

This project is a simple web application built with Streamlit that allows users to input a research topic and fetch the top 20 related research papers from Google Scholar. The project uses the `scholarly` library to interact with Google Scholar without needing a web driver.

https://research-paper-web-scapper-jaq3ldby7mtddytuakswep.streamlit.app


## Features

- **Topic Search:** Input a research topic and retrieve the top 20 related research papers.
- **Streamlit Interface:** Simple and interactive web interface.
- **Google Scholar Integration:** Fetches paper details such as title, authors, and publication year.



## Installation

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/DD-og/research-paper-web-scapper.git>
   cd <research-paper-web-scapper>
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv ai
   source ai/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
