import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import plotly.express as px

import base64

df_bmo = pd.read_excel('data_mea_bmo2.xlsx')
df_bmo_c = df_bmo.replace(np.nan, 'empty')
df_bmo_l = df_bmo[df_bmo.type_validation != 'False ']

app = dash.Dash(
    external_stylesheets=[dbc.themes.CYBORG],
    name = 'Mining Eyes Analytics'
)

app.title = 'Mining Eyes Analytics'

# Jumbotron
jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Evaluasi Post Event Mining Eyes Analytics", className="display-3"),
            html.P(
                "Interactive Dashboard Mining Eyes Analytics",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Use this dashboard and get the insight!"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)

# image
path_img = 'tes.png'
encode = base64.b64encode(open(path_img, 'rb').read()).decode('ascii')


# viz card
person_cases = [
    dbc.CardHeader('Temuan Person'),
    dbc.CardBody([
        html.H1(df_bmo[(df_bmo['type_validation']=='True ') & (df_bmo['type_object']=='Person') ].count()["violate_count"])
    ]),
]
hd_d_cases = [
    dbc.CardHeader('Temuan HD Hadap Depan'),
    dbc.CardBody([
        html.H1(df_bmo[(df_bmo['type_validation']=='True ') & (df_bmo['type_object']=='HD-D') ].count()["violate_count"])
    ]),
]
hd_b_cases = [
    dbc.CardHeader('Temuan HD Hadap Belakang'),
    dbc.CardBody([
        html.H1(df_bmo[(df_bmo['type_validation']=='True ') & (df_bmo['type_object']=='HD-B') ].count()["violate_count"])
    ]),
]
hd_ka_cases = [
    dbc.CardHeader('Temuan HD Hadap Kanan'),
    dbc.CardBody([
        html.H1(df_bmo[(df_bmo['type_validation']=='True ') & (df_bmo['type_object']=='HD-KA') ].count()["violate_count"])
    ]),
]
hd_ki_cases = [
    dbc.CardHeader('Temuan HD Hadap Kiri'),
    dbc.CardBody([
        html.H1(df_bmo[(df_bmo['type_validation']=='True ') & (df_bmo['type_object']=='HD-KI') ].count()["violate_count"])
    ]),
]
lv_cases = [
    dbc.CardHeader('Temuan LV'),
    dbc.CardBody([
        html.H1(df_bmo[(df_bmo['type_validation']=='True ') & (df_bmo['type_object']=='LV') ].count()["violate_count"])
    ]),
]



# tabs True bar_tf_true
validasi = df_bmo[df_bmo['type_validation']=='True ']
val = pd.crosstab(index=[validasi['type_object'],validasi['type_validation']],
            columns='Total',
            values=validasi['violate_count'],
            aggfunc='sum').sort_values(by=['Total'], ascending = False)

val.reset_index(inplace=True)

fig_bar_tf_true = px.bar(val, x="type_object", y='Total', text_auto='.2s', 
                    labels={
                        "type_object": "Type Object",
                    },
                    title="Temuan Berdasarkan Object")


# tabs True bar_tf_False          
validasi = df_bmo[df_bmo['type_validation']=='False ']
val = pd.crosstab(index=[validasi['type_object'],validasi['type_validation']],
            columns='Total',
            values=validasi['violate_count'],
            aggfunc='sum').sort_values(by=['Total'], ascending = False)

val.reset_index(inplace=True)

fig_bar_tf_false = px.bar(val, x="type_object", y='Total', text_auto='.2s', 
                    labels={
                        "type_object": "Type Object",
                    },
                    title="Temuan Berdasarkan Object")


# tabs True bar_c_true
val_c = df_bmo_c[df_bmo_c['type_validation']=='True ']

tes3 = pd.crosstab(index=[val_c['comment'],val_c['type_object'], val_c['type_validation']],
        columns='Total',
        values=val_c['comment'],
        aggfunc='count')

tes3.reset_index(inplace=True)

tesx = tes3[tes3.comment != 'empty']
tesx.sort_values(by='Total', ascending=False)

fig_bar_c_true = px.bar(tesx, x="comment", y="Total", color='type_object', text_auto='.2s', 
                    labels={
                        "type_object": "Type Object",
                    },
                    title="Top Comment")

# tabs True bar_c_False          
val_c = df_bmo_c[df_bmo_c['type_validation']=='False ']

tes3 = pd.crosstab(index=[val_c['comment'],val_c['type_object'], val_c['type_validation']],
        columns='Total',
        values=val_c['comment'],
        aggfunc='count')

tes3.reset_index(inplace=True)

tesx = tes3[tes3.comment != 'empty']
tesx.sort_values(by='Total', ascending=False)

fig_bar_c_false = px.bar(tesx, x="comment", y="Total", color='type_object', text_auto='.2s', 
                    labels={
                        "comment": "Comment",
                    },
                    title="Top Comment")


# tabs True bar_s_true
val_s = df_bmo[df_bmo['type_validation']=='True ']

tes4 = pd.crosstab(index=[val_s['user_id'],val_s['type_object'], val_s['type_validation']],
        columns='Total',
        values=val_s['user_id'],
        aggfunc='count').sort_values(by='Total', ascending=False )

tes4.reset_index(inplace = True)

fig_bar_s_true = px.bar(tes4, x="user_id", y='Total', color="type_object", text_auto='.2s', 
                    labels={
                        "user_id": "User",
                    },
                    title="Top User")


# tabs False bar_s_true
val_s = df_bmo[df_bmo['type_validation']=='False ']

tes4 = pd.crosstab(index=[val_s['user_id'],val_s['type_object'], val_s['type_validation']],
        columns='Total',
        values=val_s['user_id'],
        aggfunc='count').sort_values(by='Total', ascending=False)

tes4.reset_index(inplace = True)

fig_bar_s_false = px.bar(tes4, x="user_id", y='Total', color="type_object", text_auto='.2s', 
                    labels={
                        "user_id": "User",
                    },
                    title="Top User")

app.layout = html.Div([
    jumbotron,
    html.Br(),
    
    # row 1
    dbc.Row([
        
    dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    # html.Br(),
                    html.H5('Post Event 11 Desember', className="card-title", style={'textAlign': 'center'}),
                    # html.Br(),
                ]),
            )
        ]),
    dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    # html.Br(),
                    html.H5('Trend True Deviasi', className="card-title", style={'textAlign': 'center'}),
                    # html.Br(),
                ]),
            ]),
        ]),
    ]),
    html.Br(),

    # row 2
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.Div(html.Img(src='data:image/png;base64,{}'.format(encode))),
                    html.Br(),
                    html.H6('Mining Eyes Analytics', className="card-title"),
                    html.P(
                        '''Mining Eyes Analytics bertujuan untuk membantu pengawas dalam melakukan pengawasan langsung berjarak dengan cara mendeteksi temuan (pelanggaran) secara otomatis menggunakan Artificial Intelligence ''',
                        className="card-text",),
                ])
            )
        ]),
        dbc.Col([
            dbc.Card([
               dbc.Col([
                 html.Br(),
                # dbc.CardHeader([title_line], style={'textAlign': 'center'}),
                dbc.Container([
                    dcc.Dropdown(id='choose_val',
                            options = df_bmo['type_object'].unique(),
                            value = 'Person',
                            ),
                    dcc.Graph(id='trend')]),
                html.Br(),
               ])
            ])
        ]),
        
    ]),
    html.Br(),

    # row 3
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.Card(person_cases)
            )
        ]),
        dbc.Col([
            dbc.Card(
                dbc.Card(hd_d_cases)
            )
        ]),
        dbc.Col([
            dbc.Card(
                dbc.Card(hd_b_cases)
            )
        ]),
        dbc.Col([
            dbc.Card(
                dbc.Card(hd_ka_cases)
            )
        ]),
        dbc.Col([
            dbc.Card(
                dbc.Card(hd_ki_cases)
            )
        ]),
        dbc.Col([
            dbc.Card(
                dbc.Card(lv_cases)
            )
        ]),
        
    ]),
    html.Br(),
    html.Hr(className="my-2"),
    html.Br(),
    # Row 4
    dbc.Row([
        dbc.Card(
                dbc.CardBody([
                    html.H5('Analysis Based On True And False Validations', className="card-title", style={'textAlign': 'center'}),
                ]),

            )
    ]),

    html.Br(),
    # row 5
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.Container([
                    dbc.Tabs([
                        dbc.Tab(
                            dcc.Graph(figure = fig_bar_tf_false),
                            label='False Deviation'
                        ),
                        dbc.Tab(
                            dcc.Graph(figure = fig_bar_tf_true),
                            label='True Deviation'
                        ),
                    ]),
                ]),
                html.Br(),
            ]),
        ]),
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.Container([
                    dcc.Dropdown(id='choose_object',
                            options = df_bmo['type_object'].unique(),
                            value = 'Person',
                            ),
                    dcc.Graph(id='pie_tf')]),
                html.Br(),
            ]),
        ]),
    ]),

    html.Br(),
    html.Hr(className="my-2"),
    html.Br(),
    # row 6
    dbc.Row([
        dbc.Card(
                dbc.CardBody([
                    html.H5('Analysis Based On Comment or Supervisory', className="card-title", style={'textAlign': 'center'}),
                ]),

            )
    ]),

    html.Br(),
    # row 7
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.Container([
                    dbc.Tabs([
                        dbc.Tab(
                            dcc.Graph(figure = fig_bar_c_false), 
                            label = 'False Deviation'
                        ),
                        dbc.Tab(
                            dcc.Graph(figure = fig_bar_c_true), 
                            label = 'True Deviation'
                        ),
                    ]),
                ]),
                html.Br(),
            ]),
        ]),
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.Container([
                    dbc.Tabs([
                        dbc.Tab(
                            dcc.Graph(figure = fig_bar_s_false),
                            label="False Deviations"
                        ),
                        dbc.Tab(
                            dcc.Graph(figure = fig_bar_s_true),
                            label="False Deviations"
                        ),
                    ])
                ]),
                html.Br(),
            ]),
        ]),
    ]),

    html.Br(),
    html.Hr(className="my-2"),
    html.Br(),

])


@app.callback(
    Output(component_id='trend', component_property='figure'),
    Input(component_id='choose_val',component_property='value')
)

def update_plot0(object_val):
    validasi = df_bmo_l[df_bmo_l['type_object']==object_val]

    val = pd.crosstab(index=[validasi['time_create_at'],validasi['type_validation']],
                columns='Total',
                values=validasi['violate_count'],
                aggfunc='sum')
    val.reset_index(inplace=True)

    fig_line = px.line(val, x="time_create_at", y='Total', color="type_validation", 
    labels={
            "time_create_at": "Time Create",
            "type_validation": "Type validation",
        },
    title="Trend Temuan")

    # masukan semua nilai untuk setiap object
    fig_line.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['06:09:16', '07:36:04','09:07:44' ,'11:12:24', '13:37:28', '16:15:20', '17:57:48'],
        ticktext = ['06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00', '18:00:00']
        )
    )
    return fig_line

@app.callback(
    Output(component_id='pie_tf', component_property='figure'),
    Input(component_id='choose_object',component_property='value')
)

def update_plot2(object_val):
    validasi = df_bmo[df_bmo['type_object']==object_val]

    val = pd.crosstab(index=[validasi['type_object'],validasi['type_validation']],
                columns='bebas',
                values=validasi['violate_count'],
                aggfunc='sum').sort_values(by=['bebas'], ascending = False )
                
    val.reset_index(inplace=True)

    fig_pie_tf = px.pie(
        val,
        values='bebas',
        names='type_validation',
        # color_discrete_sequence=['darkgreen','red'],
        # template='ggplot2',
        hole=0.3,
        title = 'Persentase Berdasarkan Validasi'
)
    return fig_pie_tf

if __name__ == "__main__":
    app.run_server()
