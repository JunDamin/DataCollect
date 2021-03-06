import os
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
import plotly.colors as c
from plotly.offline import plot
import plotly.express as px
from config.settings import BASE_DIR

"""
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv"
)

fig = go.Figure(
    data=go.Choropleth(
        locations=df["CODE"],
        z=df["GDP (BILLIONS)"],
        text=df["COUNTRY"],
        colorscale=c.sequential.Blues,
        autocolorscale=False,
        reversescale=False,
        marker_line_color="darkgray",
        marker_line_width=0.5,
        colorbar_ticksuffix="명",
        colorbar_title="GDP<br>Billions US$",
    )
)

fig.update_layout(
    title_text="인원현황",
    geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"),
    annotations=[
        dict(
            x=0.55,
            y=0.1,
            xref="paper",
            yref="paper",
            text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
            showarrow=False,
        )
    ],
)

fig.show()
"""


def plot_personnel(df):

    fig = go.Figure(
        data=go.Choropleth(
            locations=df["location_code"],
            z=df["total"],
            text=df["country"],
            colorscale=c.sequential.Blues,
            autocolorscale=False,
            reversescale=False,
            marker_line_color="darkgray",
            marker_line_width=0.5,
            colorbar_ticksuffix="명",
            colorbar_title="인원",
        )
    )

    fig.update_layout(
        autosize=True,
        width=1200,
        height=800,
        title_text="인원현황",
        geo=dict(
            showframe=False, showcoastlines=False, projection_type="equirectangular"
        ),
        annotations=[
            dict(
                x=0.55,
                y=0.1,
                xref="paper",
                yref="paper",
                text="Source: 취합기준 " + str(datetime.now())[:-7],
                showarrow=False,
            )
        ],
    )
    path = os.path.join(BASE_DIR, "templates/mixins/personnel_graph.html")
    with open(path, "w") as p:
        p.write(plot(fig, output_type="div"))
        print("generate")

    return "generated"


def plot_prediction(df):

    fig = px.choropleth(
        df,
        color="total_score",
        locations="location_code",
        hover_name="location_situation",
        color_continuous_scale=[
            [0, "rgb(112, 219, 112)",],
            [0.5, "rgb(255, 209, 26)",],
            [1, "rgb(128, 0, 64)",],
        ],
    )

    fig.update_layout(
        autosize=True,
        width=1200,
        height=800,
        title_text="안전예보",
        geo=dict(
            showframe=False, showcoastlines=False, projection_type="equirectangular"
        ),
        annotations=[
            dict(
                x=0.55,
                y=0.1,
                xref="paper",
                yref="paper",
                text="Source: 취합기준 " + str(datetime.now())[:-7],
                showarrow=False,
            )
        ],
    )
    path = os.path.join(BASE_DIR, "templates/mixins/prediction_graph.html")
    with open(path, "w") as p:
        p.write(plot(fig, output_type="div"))
        print("generate")

    return "generated"
