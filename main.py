import streamlit as st
from scholarly import scholarly

def search_scholar(topic, num_papers=10):
    search_query = scholarly.search_pubs(topic)
    papers = []
    for i, paper in enumerate(search_query):
        if i >= num_papers:
            break
        paper_dict = paper
        papers.append({
            'title': paper_dict.get('bib', {}).get('title', 'No title available'),
            'author': paper_dict.get('bib', {}).get('author', 'No authors available'),
            'pub_year': paper_dict.get('bib', {}).get('pub_year', 'N/A'),
            'abstract': paper_dict.get('bib', {}).get('abstract', 'No abstract available'),
            'url': paper_dict.get('pub_url', 'No URL available')  # Use 'pub_url' for the URL
        })
    return papers

st.title("Google Scholar Research Paper Scraper")

topic = st.text_input("Enter a topic")

if st.button("Search Papers"):
    if topic:
        st.write(f"Searching papers on: {topic}")
        papers = search_scholar(topic, num_papers=20)
        if papers:
            for paper in papers:
                st.subheader(paper['title'])
                st.write(f"**Authors:** {paper['author']}")
                st.write(f"**Published Year:** {paper['pub_year']}")
                st.write(f"**Abstract:** {paper['abstract']}")
                if paper['url'] != 'No URL available':
                    st.markdown(f"[Click to go to the paper]({paper['url']})")
                st.write("---")
        else:
            st.write("No papers found on this topic.")
