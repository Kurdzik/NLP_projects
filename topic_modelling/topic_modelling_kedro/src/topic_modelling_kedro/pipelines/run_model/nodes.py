"""
This is a boilerplate pipeline 'run_model'
generated using Kedro 0.18.1
"""


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

def split_into_topics(articles,parameters):

    articles = articles.dropna()
    
    tfidf = TfidfVectorizer(max_df=0.95, min_df=5, stop_words='english')
    dtm = tfidf.fit_transform(articles['Content'])

    nmf = NMF(n_components=parameters['n_topics'], random_state=42)
    nmf.fit(dtm)

    for i, topic in enumerate(nmf.components_):
        print(f'Topic {i+1} most frequent words:')
        print([tfidf.get_feature_names_out()[x] for x in topic.argsort()[-5:]])


    topic_results = nmf.transform(dtm)
    topic_results = topic_results.argmax(axis=1)
    articles['Topic'] = topic_results

    return articles