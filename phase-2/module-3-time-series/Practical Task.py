# %%
import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import Naive, WindowAverage, SeasonalNaive, AutoARIMA
from utilsforecast.evaluation import evaluate
from utilsforecast.losses import mae, rmse, mape
from utilsforecast.plotting import plot_series
from statsmodels.tsa.seasonal import seasonal_decompose

# %%
df = pd.read_csv("daily_water_consumption.csv", parse_dates=["Date"])
df.head()

# %%
series = df.rename(columns={
    "Zone": "unique_id",
    "Date": "ds",
    "Residential_Usage": "y",
})[["unique_id", "ds", "y"]]
series = series.sort_values(["unique_id", "ds"]).reset_index(drop=True)
series

# %%
parts = []
for zone, g in series.groupby("unique_id"):
    g = g.set_index("ds").asfreq("D")
    print("missing in", zone, ":", int(g["y"].isna().sum()))
    g["unique_id"] = zone
    parts.append(g.reset_index())
series = pd.concat(parts)[["unique_id", "ds", "y"]].reset_index(drop=True)

# %%
plot_series(series, max_insample_length=30)

# %%
zone_a = series[series["unique_id"] == "ZONE_A"].set_index("ds")["y"]
try:
    decomposition = seasonal_decompose(zone_a, model="additive", period=7)
    decomposition.plot()
except ValueError as e:
    print("decomposition needs at least 14 days:", e)

# %%
horizon = 3

test = series.groupby("unique_id").tail(horizon)
train = series.drop(test.index).reset_index(drop=True)

# %%
models = [
    Naive(),
    WindowAverage(window_size=3),
    SeasonalNaive(season_length=7),
    AutoARIMA(season_length=7),
]
sf = StatsForecast(models=models, freq="D")
sf.fit(train)
preds = sf.predict(h=horizon)
preds

# %%
eval_df = pd.merge(test, preds, how="left", on=["ds", "unique_id"])
evaluation = evaluate(eval_df, metrics=[mae, rmse, mape])
evaluation

# %%
best_per_zone = (
    evaluation[evaluation["metric"] == "mae"]
    .drop(columns="metric")
    .set_index("unique_id")
    .idxmin(axis=1)
)
best_per_zone

# %%
sf_ci = StatsForecast(models=[AutoARIMA(season_length=7)], freq="D")
sf_ci.fit(train)
preds_pi = sf_ci.predict(h=horizon, level=[80])
preds_pi

# %%
plot_series(train, preds_pi, level=[80])

# %%
sf_full = StatsForecast(models=models, freq="D")
sf_full.fit(series)
future = sf_full.predict(h=horizon)
future
