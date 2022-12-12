import pandas as pd
import feedparser as fp
import streamlit as st
import yaml

st.title('Cleanfeed')

with open("sources.yml", "r") as stream:
        publ = yaml.safe_load(stream)

def read_rss(tag, url):
    feed = fp.parse(url)
    df = pd.DataFrame([entry for entry in feed.entries])
    df["tag"] = tag
    cols = ['title', 'published', 'tag']
    return df[cols]

merged = pd.concat([read_rss(key, val['url']) for key, val in publ.items()], axis=0)

st.dataframe(merged)





#st.write(read_rss('https://www.svd.se/feed/articles.rss', 'SvD'))
