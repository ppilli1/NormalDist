import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("mobile.csv")
avg_rating = df["Avg Rating"].tolist()
fig = ff.create_distplot([avg_rating], ["Probability"], show_hist = False)
fig.show()