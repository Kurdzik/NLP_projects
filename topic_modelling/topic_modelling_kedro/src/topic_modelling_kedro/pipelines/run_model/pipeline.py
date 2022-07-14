"""
This is a boilerplate pipeline 'run_model'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_into_topics

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=split_into_topics,
                          inputs=['articles','params:NMF_options'],
                          outputs='preprocessed_articles',
                          name='modelling_node')])
