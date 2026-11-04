# %%
import pandas as pd

# %%
df = pd.read_csv("daily_water_consumption.csv", parse_dates=["Date"])
df.head()

# %%
series = df.rename(columns={
    "Zone": "unique_id",
    "Date": "ds",
    "Residential_Usage": "y",
})[["unique_id", "ds", "y"]]

# %%
from utilsforecast.plotting import plot_series

# %%
plot_series(series, max_insample_length=30)

# %%
from statsforecast import StatsForecast
from statsforecast.models import Naive, HistoricAverage, WindowAverage, SeasonalNaive

# %%
horizon = 3
models = [Naive(), HistoricAverage(), WindowAverage(window_size=3), SeasonalNaive(season_length=7)]
sf = StatsForecast(models=models, freq="D")
sf.fit(series)
preds = sf.predict(h=horizon)
preds

# %%
test = series.groupby("unique_id").tail(horizon)
train = series.drop(test.index).reset_index(drop=True)
sf.fit(train)
preds = sf.predict(h=horizon)
preds

# %%
from utilsforecast.evaluation import evaluate
from utilsforecast.losses import mae

eval_df = pd.merge(test, preds, how="left", on=["ds", "unique_id"])
evaluation = evaluate(eval_df, metrics=[mae])
evaluation

# %%
from statsforecast.models import AutoARIMA
models = [SeasonalNaive(season_length=7), AutoARIMA(season_length=7)]
sf = StatsForecast(models=models, freq="D")
sf.fit(train)
preds = sf.predict(h=horizon)
preds

# %%
cv_df = sf.cross_validation(
    df=series,
    h=1,
    n_windows=3,
    step_size=1,
)
cv_df

# %%
cv_eval = evaluate(cv_df.drop(columns="cutoff"), metrics=[mae])
cv_eval
# %%
future_exog_df = test.drop(columns="y")
# %%
from functools import partial
from utilsforecast.feature_engineering import fourier, time_features, pipeline

features = [
    partial(fourier, season_length=7, k=2),
    partial(time_features, features=["day", "week", "month"]),
]
