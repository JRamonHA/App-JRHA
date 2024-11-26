import pandas as pd
import plotly.express as px
from shiny import App, ui
from shinywidgets import render_widget, output_widget

f = './data/Tmx.csv'
tmx = pd.read_csv(f, index_col=0, parse_dates=True)

columnas = ['To', 'Ib', 'Ig']

app_ui = ui.page_sidebar(
    ui.sidebar(ui.input_select("var", "Selecciona una variable", choices=columnas)),
    ui.navset_tab(
        ui.nav_panel("Temperatura", ui.card(output_widget("temp_plot"), full_screen=True)),
        ui.nav_panel("Radiación", ui.card(output_widget("radiacion_plot"), full_screen=True))
    )
)


def server(input, output, session):
    @render_widget
    def temp_plot():
        df = tmx.resample('ME').mean()
        fig = px.line(
            df,
            x=df.index,
            y='To'
        )
        fig.update_layout(
            title='Temperatura',
            yaxis_title='(°C)',
            xaxis_title='Tiempo'
        )
        return fig

    @render_widget
    def radiacion_plot():
        df = tmx.resample('ME').mean()
        fig = px.line(
            df,
            x=df.index,
            y=['Ib', 'Ig']
        )
        fig.update_layout(
            title='Radiación',
            yaxis_title='(W/m2)',
            xaxis_title='Tiempo'
        )
        return fig

app = App(app_ui, server)