# topic_modelling_kedro

## Overview

Kedro project generated using `Kedro 0.18.1`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run                       collects articles and splits them into topics
kedro run -p get_articles       collects articles and saves them as cvs in data/01_raw folder
kedro run -p run_model          performs topic modelling on gathered articles and saves output to data/07_model_output folder
```

## How to visualize pipeline

run:

`kedro viz`
