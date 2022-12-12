import pandas as pd
import feedparser as fp
import streamlit as st
import yaml

st.title('Cleanfeed')

with open("sources.yml", "r") as stream:
        publ = yaml.safe_load(stream)

def read_rss(url, tag):
    feed = fp.parse(url)
    entries = [entry for entry in feed.entries]
    df = pd.DataFrame(entries)
    df["tag"] = tag
    cols = ['title', 'published', 'tag']
    return df[cols]

tmp = []

for key, item in publ.items():

    tmp.append(read_rss(item['url'], key))

merged = pd.concat(tmp, axis=0).sort_values(by='published', ascending=False)

st.dataframe(merged)





#st.write(read_rss('https://www.svd.se/feed/articles.rss', 'SvD'))
