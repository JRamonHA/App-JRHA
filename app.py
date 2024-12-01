import io
import pandas as pd
import plotly.express as px
from shiny import App, Inputs, reactive, render, ui
from shinywidgets import render_widget, output_widget
import faicons
import funciones as func


f = func.cargar_anio("2010")
esol = pd.read_parquet(f)
nombres = list(esol.columns)
years = func.years


app_ui = ui.page_navbar(
    ui.nav_spacer(),
    ui.nav_panel(
        "Visualizador",
        ui.navset_card_underline(
            ui.nav_panel("Anual", output_widget("plot_anual")),
            ui.nav_panel("Mensual", output_widget("plot_mensual")),
            title="Meteorología",
        ),
    ),
    ui.nav_panel(
        "Datos",
        ui.card(
            ui.card_header(
                ui.span(ui.output_text("file_title"),
                        class_="me-auto"),
                ui.download_link("download_data", "Descargar archivo", icon=faicons.icon_svg("download"),
                                 class_="btn btn-primary btn-sm"),
                class_="d-flex justify-content-between align-items-center"
            ),
            ui.output_data_frame("data"),
        ),
    ),
    sidebar=ui.sidebar(
        ui.input_select("year", "Año", choices=list(years), selected="2010"),
        ui.input_date_range("daterange", "Rango de fechas", start="2010-01-01", end="2010-12-31"),
        ui.input_select("variable", "Variable", choices=nombres),
    ),
    id="tabs",
    title="Explorador ESOLMET",
    fillable=True,
)


def server(input: Inputs):
    @reactive.Effect
    @reactive.event(input.year)
    def actualizar_rango_fechas():
        year_selected = int(input.year())
        start_date = f"{year_selected}-01-01"
        end_date = f"{year_selected}-12-31"
        ui.update_date_range("daterange", start=start_date, end=end_date)

    @reactive.calc()
    def cargar_esol() -> pd.DataFrame:
        year_selected = input.year()
        f = func.cargar_anio(year_selected)
        esol = pd.read_parquet(f)
        return esol

    @reactive.calc()
    def filtrar_por_fecha() -> pd.DataFrame:
        esol = cargar_esol()
        start_date, end_date = input.daterange()
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        return esol.loc[(esol.index >= start_date) & (esol.index <= end_date)]

    @render_widget
    def plot_anual():
        df = filtrar_por_fecha().reset_index()
        var = input.variable()

        df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
        df.set_index('TIMESTAMP', inplace=True)

        fig = px.line(
            df,
            x=df.index,
            y=var,
            title=f"{var} - {input.year()}",
            labels={'TIMESTAMP': 'Fecha', var: var},
        )

        maximos = df[var].resample('D').max()
        maximos_idx = maximos.index
        maximos_valor = maximos.values

        fig.add_scatter(
            x=maximos_idx,
            y=maximos_valor,
            mode='markers',
            name="Máximos diarios",
            marker=dict(color='red', size=6)
        )

        return fig

    @render_widget
    def plot_mensual():
        df = filtrar_por_fecha().resample('ME').agg({input.variable(): ['mean', 'std']}).reset_index()
        df.columns = ['TIMESTAMP', 'mean', 'std']

        fig = px.line(
            df,
            x='TIMESTAMP',
            y='mean',
            title=f"{input.variable()} - {input.year()}",
            labels={'TIMESTAMP': 'Fecha', 'mean': f"{input.variable()}"}
        )

        if input.variable() not in ['Ib', 'Ig']:
            fig.add_scatter(
                x=df['TIMESTAMP'],
                y=df['std'],
                mode='lines',
                name="Desviación estándar",
                line=dict(dash='dot', color='red')
            )
        return fig

    @render.data_frame
    def data():
        df = filtrar_por_fecha().reset_index().rename(columns={"TIMESTAMP": "Fecha"})
        return df

    @render.text
    def file_title():
        return f"ESOLMET_{input.year()}.csv"

    @render.download(filename=lambda: f"ESOLMET_{input.year()}.csv")
    def download_data():
        df = filtrar_por_fecha().reset_index()
        df = df.rename(columns={"TIMESTAMP": "Fecha"})
        with io.StringIO() as buf:
            df.to_csv(buf, index=False)
            yield buf.getvalue().encode()

app = App(app_ui, server)