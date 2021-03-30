pip freeze > requirements.txtpip freeze > requirements.txt# In[1]:


import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from plotly.subplots import make_subplots


# In[2]:



USERNAME_PASSWORD_PAIRS = [['username','password'],['chipsboard','potato123']]


# In[3]:


df = pd.read_excel (r'BATCH1234.xls')
df.to_csv (r'BATCH1234.csv', index = None, header=True)


# In[4]:


df.columns=['Time','da','dd','LAAVG','PRD','Glucose','Yield','LA','NA','Time2','Glucose2','LA2', 'NA2','Time3','Glucose3','areaa','aread','conca','concd','lact3','Time4','Glucose4','areaa4','aread4','conca4','concd4','lact4']


# In[5]:


df2 = pd.read_excel (r'fedbatch.xls')
df2.to_csv (r'fedbatch.csv', index = None, header=True)

df3 = pd.read_excel (r'mrs.xls')
df3.to_csv (r'mrs.csv', index = 0, header=True)


# In[6]:


# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])


# Add traces
fig.add_trace(
    go.Scatter(     x = df['Time'],
                    y = df['Glucose'],
                    name='Glucose Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='Salmon',
                                size=10,
                                line=dict(
                                          color='DarkRed',
                                          width=2
                                )
        )
                ), 
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(     x = df['Time'],
                    y = df['LAAVG'],
                    name='Lactic Acid Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='yellow',
                                size=10,
                                line=dict(
                                          color='DarkOrange',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(     x = df['Time'],
                    y = df['da'],
                    name='Concentration 1A',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='lime',
                                size=10,
                                line=dict(
                                          color='DarkGreen',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(     x = df['Time'],
                    y = df['dd'],
                    name='Concentration 1D',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'color':'Fuchsia',
                        'size': 10,
                        'line': {'color':'purple','width': 2}
                        }
                ), 
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(     x = df['Time'],
                    y = df['PRD'],
                    name='Productivity',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'color':'cyan',
                        'size': 10,
                        'line': {'color':'black','width': 2}
                        }
                ), 
    
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Batch Fermentation (Pea Flour)",
    height = 500,
    plot_bgcolor='rgb(229,255,255)'
)

# Set x-axis title
fig.update_xaxes(title_text="Time")

# Set y-axes titles
fig.update_yaxes(title_text="Concentration", secondary_y=False)
fig.update_yaxes(title_text="Productivity", secondary_y=True)

fig.show()


# In[7]:


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": False}]])


# Add traces
fig2.add_trace(
    go.Scatter(     x = df['Time2'],
                    y = df['Glucose2'],
                    name='Glucose Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='Salmon',
                                size=10,
                                line=dict(
                                          color='DarkRed',
                                          width=2
                                )
        )
                ), 
    secondary_y=False,
)

fig2.add_trace(
    go.Scatter(     x = df['Time2'],
                    y = df['LA2'],
                    name='Lactic Acid Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='yellow',
                                size=10,
                                line=dict(
                                          color='DarkOrange',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

# Add figure title
fig2.update_layout(
    title_text="Batch Fermentation 2 (Pea Flour)",
    height = 500,
    plot_bgcolor='rgb(229,255,255)'
)

# Set x-axis title
fig2.update_xaxes(title_text="Time")

# Set y-axes titles
fig2.update_yaxes(title_text="Concentration", secondary_y=False)

fig2.show()


# In[8]:


# Create figure 2 (batch3) with secondary y-axis
fig3 = make_subplots(specs=[[{"secondary_y": True}]])


# Add traces
fig3.add_trace(
    go.Scatter(     x = df['Time3'],
                    y = df['Glucose3'],
                    name='Glucose Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='Salmon',
                                size=10,
                                line=dict(
                                          color='DarkRed',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

fig3.add_trace(
    go.Scatter(     x = df['Time3'],
                    y = df['lact3'],
                    name='Lactic Acid Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='yellow',
                                size=10,
                                line=dict(
                                          color='Orange',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

fig3.add_trace(
    go.Scatter(     x = df['Time3'],
                    y = df['conca'],
                    name='Concentration 1A',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='lime',
                                size=10,
                                line=dict(
                                          color='DarkGreen',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

fig3.add_trace(
    go.Scatter(     x = df['Time3'],
                    y = df['concd'],
                    name='Concentration 1D',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'color':'Fuchsia',
                        'size': 10,
                        'line': {'width': 2}
                        }
                ), 
    secondary_y=False,
)

fig3.add_trace(
    go.Scatter(     x = df['Time3'],
                    y = df['areaa'],
                    name='Area 1A',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'color':'DeepSkyBlue',
                        'size': 10,
                        'line': {'color':'DarkBlue','width': 2}
                        }
                ), 
    
    secondary_y=True,
)

fig3.add_trace(
    go.Scatter(     x = df['Time3'],
                    y = df['aread'],
                    name='Area 1D',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'color':'cyan',
                        'size': 10,
                        'line': {'color':'black','width': 2}
                        }
                ), 
    secondary_y=True,
)


# Add figure title
fig3.update_layout(
    title_text="Batch Fermentation 3 (Potato Chips)",
    height = 500,
    plot_bgcolor='rgb(229,255,255)'
)

# Set x-axis title
fig3.update_xaxes(title_text="Time")

# Set y-axes titles
fig3.update_yaxes(title_text="Concentration", secondary_y=False)
fig3.update_yaxes(title_text="Area", secondary_y=True)

fig3.show()


# In[9]:


# Create figure 2 (batch3) with secondary y-axis
fig4 = make_subplots(specs=[[{"secondary_y": True}]])


# Add traces
fig4.add_trace(
    go.Scatter(     x = df['Time4'],
                    y = df['Glucose4'],
                    name='Glucose Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='Salmon',
                                size=10,
                                line=dict(
                                          color='DarkRed',
                                          width=2
                                )
        )
                ), 
    secondary_y=False,
)

fig4.add_trace(
    go.Scatter(     x = df['Time4'],
                    y = df['lact4'],
                    name='Lactic Acid Concentration',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker=dict(
                                color='yellow',
                                size=10,
                                line=dict(
                                          color='Orange',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

fig4.add_trace(
    go.Scatter(     x = df['Time4'],
                    y = df['conca4'],
                    name='Concentration 1A',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = dict(color='lime',
                                size=10,
                                line=dict(
                                          color='DarkGreen',
                                          width=2
            )
        )
                ), 
    secondary_y=False,
)

fig4.add_trace(
    go.Scatter(     x = df['Time4'],
                    y = df['concd4'],
                    name='Concentration 1D',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'color':'Fuchsia',
                        'size': 10,
                        'line': {'width': 2}
                        }
                ), 
    secondary_y=False,
)

fig4.add_trace(
    go.Scatter(     x = df['Time4'],
                    y = df['areaa4'],
                    name='Area 1A',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'color':'DeepSkyBlue',
                        'size': 10,
                        'line': {'color':'DarkBlue','width': 2}
                        }
                ), 
    secondary_y=True,
)

fig4.add_trace(
    go.Scatter(     x = df['Time4'],
                    y = df['aread4'],
                    name='Area 1D',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'color':'cyan',
                        'size': 10,
                        'line': {'color':'black','width': 2}
                        }
                ), 
    
    secondary_y=True,
)

# Add figure title
fig4.update_layout(
    title_text="Batch Fermentation 4 (Potato Chips)",
    height = 500,
    plot_bgcolor='rgb(229,255,255)'
)

# Set x-axis title
fig4.update_xaxes(title_text="Time")

# Set y-axes titles
fig4.update_yaxes(title_text="Concentration", secondary_y=False)
fig4.update_yaxes(title_text="Area", secondary_y=True)

fig4.show()


# In[10]:


# Create figure 2 (batch3) with secondary y-axis
fig5 = make_subplots(specs=[[{"secondary_y": True}]])


# Add traces
fig5.add_trace(
    go.Scatter(
                    x = df2['Time'],
                    y = df2['Acid'],
                    name='Lactic Acid',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {
                        'size': 10,
                        'color': 'Yellow',
                        'line': {'color':'DarkOrange','width': 2}
                        }
                ))

fig5.add_trace(
    go.Scatter(x = df2['Time'],
                    y = df2['Glucose'],
                    name = 'Glucose',
                    hoverinfo = 'x+y',
                    dy = 1,
                    mode = 'markers',
                    marker = {'symbol': 'pentagon',
                        'size': 10,
                        'color': 'Salmon',
                        'line': {'color':'DarkRed','width': 2}
                        }
                ))

# Add figure title
fig5.update_layout(
    title ={'text': 'Fed-Batch Fermentation',
        'y':0.9,
        'x':0.43,
        'xanchor': 'center',
        'yanchor': 'top'},
    height = 500,
    plot_bgcolor='rgb(229,255,255)'
)

# Set x-axis title
fig5.update_xaxes(title_text="Time/h")

# Set y-axes titles
fig5.update_yaxes(title_text="Concentration/g", secondary_y=False)


fig5.show()


# In[11]:


# Create figure 2 (batch3) with secondary y-axis
fig6 = make_subplots(specs=[[{"secondary_y": True}]])


# Add traces
fig6.add_trace(
    go.Scatter(
            x=df3['Time'],
            y=df3['PF'],
            mode='markers',
            opacity=0.8,
            marker=dict(
            color='Gold',
            size=12,
            line=dict(
                color='Salmon',
                width=2
            )
        ),
            name='Pea Flour'
        ))

fig6.add_trace(
    go.Scatter(
            x=df3['Time'],
            y=df3['PFMRS'],
            mode='markers',
            opacity=0.8,
            marker=dict(
            color='GreenYellow',
            size=12,
            line=dict(
                color='Green',
                width=2
            )
        ),
            name='Pea Flour + MRS' 
        ))

fig6.add_trace(
    go.Scatter(
            x=df3['Time'],
            y=df3['MRS'],
            mode='markers',
            opacity=0.8,
            marker=dict(
            color='LightSkyBlue',
            size=12,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
            name='MRS'
        ))

# Add figure title
fig6.update_layout(
    title ={'text': 'L. Rhamnosus Growth Curve',
        'y':0.9,
        'x':0.43,
        'xanchor': 'center',
        'yanchor': 'top'},
    height = 500,
    plot_bgcolor='rgb(229,255,255)'
)

# Set x-axis title
fig6.update_xaxes(title_text="Time/h")

# Set y-axes titles
fig6.update_yaxes(title_text="OD", secondary_y=False)


fig6.show()


# In[ ]:


app = dash.Dash()
server = app.server

auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)

app.layout = html.Div([
    html.H1('Chip[S] Board Upstream', style={
            'textAlign': 'center'}),
    
    html.Div([
    dcc.Graph(
        id='batch1-plot',
        figure=fig)], style={'width':'70%', 'float':'left'}),
    
    html.Div([
    dcc.Graph(
        id='batch2-plot',
        figure=fig2
    )],
        style={'width':'70%', 'float':'right'}),
    
     html.Div([
    dcc.Graph(
        id='batch3-plot',
        figure=fig3)], style={'width':'70%', 'float':'left'}),
    
    html.Div([
    dcc.Graph(
        id='batch4-plot',
        figure=fig4
    )],
        style={'width':'70%', 'float':'right'}),
    
    html.Div([
    dcc.Graph(
        id='fedbatch-plot',
        figure=fig5)], style={'width':'49%', 'float':'left','border':'2px black solid'}),
    
    html.Div([
    dcc.Graph(
        id='mrs-plot',
        figure=fig6)], style={'width':'49%', 'float':'right','border':'2px black solid'})
    
    
])

if __name__ == '__main__':
    app.run_server()


# In[ ]:




