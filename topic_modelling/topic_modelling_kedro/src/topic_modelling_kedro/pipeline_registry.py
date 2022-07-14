"""Project pipelines."""
from cProfile import run
from os import sched_param
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from topic_modelling_kedro.pipelines import scrap_articles
from topic_modelling_kedro.pipelines import run_model 

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    scrap = scrap_articles.create_pipeline()
    modelling = run_model.create_pipeline()

    return {"__default__": scrap+modelling,
            "get_articles":scrap,
            "run_model": modelling}
            
