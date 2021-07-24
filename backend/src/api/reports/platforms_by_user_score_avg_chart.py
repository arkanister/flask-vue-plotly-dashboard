import plotly.graph_objects as go
from flask import request

from api.reports.data import get_data
from commons import parser
from commons.resources import PlotlyChartResource


class PlatformsByUserScoreAVGChartResource(PlotlyChartResource):

    def get(self):
        # load data
        df = get_data()

        # filters
        top = parser.parse(request.args.get('top'), cast=int, default=10)
        total = len(df['platforms'].unique())

        # calc the mean grouped by platforms.
        df = df[['platforms', 'userscore']] \
            .groupby(['platforms'], as_index=False) \
            .mean()[:top] \
            .sort_values('userscore', ascending=True, ignore_index=True)

        # build the figure.
        fig = go.Figure() \
            .add_trace(go.Bar(
                x=df['userscore'],
                y=df['platforms'],
                text=df['userscore'],
                orientation='h',
                hovertemplate='%{y}: %{x:.2f}<extra></extra>',
                marker=dict(color='#000')
            ))

        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f7f7f7')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f7f7f7')
        fig.update_layout(
            xaxis_title='Avg. Userscore',
            yaxis_title='Platform',
            bargap=0.3,
            plot_bgcolor='#FFFFFF',
            margin=dict(t=40, r=20, b=20, l=50)
        )

        return {
            'properties': {
                'top': top,
                'total': total,
            },
            'chart': fig.to_dict()
        }
