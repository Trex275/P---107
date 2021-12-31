import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

fig = px.scatter(
    x= ["student_id"],
    y=["level"],
    orientation = 'h'
)
fig.show()