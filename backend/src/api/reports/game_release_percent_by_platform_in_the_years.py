import datetime

import plotly.graph_objects as go
from flask import request

from api.reports.data import get_data
from commons import parser
from commons.resources import PlotlyChartResource


class GameReleasePercentByPlatformInTheYearsChartResource(PlotlyChartResource):

    def get(self):
        # load data
        df = get_data()

        all_genres = list(df['genre'].unique())

        # filters
        current_year = datetime.datetime.now().year
        start_year = parser.parse(request.args.get('start_year'), cast=int, default=current_year - 5)
        end_year = parser.parse(request.args.get('end_year'), cast=int, default=current_year)
        genres = parser.parse(request.args.get('genres'), cast=parser.csv(), default=[]) or all_genres[:5]
        years = list(df['year'].unique())

        # filter by year
        df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]

        df = df[['genre', 'year']] \
            .groupby(['genre', 'year'], as_index=False) \
            .size()

        # calc release percent size
        df['p'] = df.apply(lambda x: x[2] / df[(df['year'] == x[1])]['size'].sum(), axis=1)

        # filter genres
        df = df[(df['genre'].isin(genres))]

        # build the chart
        traces = [go.Scatter(
            name=genre,
            x=data['year'],
            y=data['p'],
            mode='markers+lines'
        ) for genre, data in map(lambda x: (x, df[(df['genre'] == x)]), genres)]

        fig = go.Figure(data=traces)

        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f7f7f7')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f7f7f7')
        fig.update_layout(
            xaxis_title='Year',
            yaxis_title='% of Realeases',
            yaxis_tickformat='1%',
            plot_bgcolor='#FFFFFF'
        )

        return {
            'properties': {
                'start_year': start_year,
                'end_year': end_year,
                'years': years,
                'selected_genres': genres,
                'genres': all_genres
            },
            'chart': fig.to_dict()
        }
