import featuretools as ft
from dask import bag
from dask.diagnostics import ProgressBar
import pandas as pd
import utils
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import os


es = utils.load_entityset("partitioned_data/part_1/")
# print es
# print es.plot()

label_times = utils.make_labels(es=es,
                                product_name="Banana",
                                cutoff_time=pd.Timestamp('March 15, 2015'),
                                prediction_window=ft.Timedelta("4 weeks"),
                                training_window=ft.Timedelta("60 days"))
# print label_times.head(5)
print label_times["label"].value_counts()