import pandas as pd
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_widget

f = './data/Tmx.csv'
tmx = pd.read_csv(f, index_col=0, parse_dates=True)
columnas = list(tmx.columns)

ui.page_opts(title="Web App")