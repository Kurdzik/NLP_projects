"""
This is a boilerplate pipeline 'scrap_articles'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_fresh_bbc_news



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=get_fresh_bbc_news,
                          inputs=None,
                          outputs='articles',
                          name='scrapping_articles_node')])
