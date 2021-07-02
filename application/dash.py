
# OEntrada violencia de genero

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
#import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

#Tabla ranking delitos VG
tabla = pd.read_csv("https://raw.githubusercontent.com/fdealbam/violenciadegenero/main/Variacionesytasaygrandtotal.csv")
tabla1 = tabla.sort_values(by='tasa_acumulada', ascending=False)

#Tipo de delito
tipodel1 = tabla1.iloc[0]["Tipo de delito"]
tipodel2 = tabla1.iloc[1]["Tipo de delito"]
tipodel3 = tabla1.iloc[2]["Tipo de delito"]
tipodel4 = tabla1.iloc[3]["Tipo de delito"]
tipodel5 = tabla1.iloc[4]["Tipo de delito"]
tipodel6 = tabla1.iloc[5]["Tipo de delito"]
tipodel7 = tabla1.iloc[6]["Tipo de delito"]
tipodel8 = tabla1.iloc[7]["Tipo de delito"]
tipodel9 = tabla1.iloc[8]["Tipo de delito"]
tipodel10 = tabla1.iloc[9]["Tipo de delito"]
tipodel11 = tabla1.iloc[10]["Tipo de delito"]
tipodel12 = tabla1.iloc[11]["Tipo de delito"]
tipodel13 = tabla1.iloc[12]["Tipo de delito"]
tipodel14 = tabla1.iloc[13]["Tipo de delito"]
tipodel15 = tabla1.iloc[14]["Tipo de delito"]
tipodel16 = tabla1.iloc[15]["Tipo de delito"]
tipodel17 = tabla1.iloc[16]["Tipo de delito"]
tipodel18 = tabla1.iloc[17]["Tipo de delito"]

#abs
totdel1 =  tabla1.iloc[0]["GRAND TOTAL"]
totdel2 =  tabla1.iloc[1]["GRAND TOTAL"]
totdel3 =  tabla1.iloc[2]["GRAND TOTAL"]
totdel4 =  tabla1.iloc[3]["GRAND TOTAL"]
totdel5 =  tabla1.iloc[4]["GRAND TOTAL"]
totdel6 =  tabla1.iloc[5]["GRAND TOTAL"]
totdel7 =  tabla1.iloc[6]["GRAND TOTAL"]
totdel8 =  tabla1.iloc[7]["GRAND TOTAL"]
totdel9 =  tabla1.iloc[8]["GRAND TOTAL"]
totdel10 = tabla1.iloc[9]["GRAND TOTAL"]
totdel11 = tabla1.iloc[10]["GRAND TOTAL"]
totdel12 = tabla1.iloc[11]["GRAND TOTAL"]
totdel13 = tabla1.iloc[12]["GRAND TOTAL"]
totdel14 = tabla1.iloc[13]["GRAND TOTAL"]
totdel15 = tabla1.iloc[14]["GRAND TOTAL"]
totdel16 = tabla1.iloc[15]["GRAND TOTAL"]
totdel17 = tabla1.iloc[16]["GRAND TOTAL"]
totdel18 = tabla1.iloc[17]["GRAND TOTAL"]

#tasa acumulada

tasatotdel1 =  tabla1.iloc[0]["tasa_acumulada"]
tasatotdel2 =  tabla1.iloc[1]["tasa_acumulada"]
tasatotdel3 =  tabla1.iloc[2]["tasa_acumulada"]
tasatotdel4 =  tabla1.iloc[3]["tasa_acumulada"]
tasatotdel5 =  tabla1.iloc[4]["tasa_acumulada"]
tasatotdel6 =  tabla1.iloc[5]["tasa_acumulada"]
tasatotdel7 =  tabla1.iloc[6]["tasa_acumulada"]
tasatotdel8 =  tabla1.iloc[7]["tasa_acumulada"]
tasatotdel9 =  tabla1.iloc[8]["tasa_acumulada"]
tasatotdel10 = tabla1.iloc[9]["tasa_acumulada"]
tasatotdel11 = tabla1.iloc[10]["tasa_acumulada"]
tasatotdel12 = tabla1.iloc[11]["tasa_acumulada"]
tasatotdel13 = tabla1.iloc[12]["tasa_acumulada"]
tasatotdel14 = tabla1.iloc[13]["tasa_acumulada"]
tasatotdel15 = tabla1.iloc[14]["tasa_acumulada"]
tasatotdel16 = tabla1.iloc[15]["tasa_acumulada"]
tasatotdel17 = tabla1.iloc[16]["tasa_acumulada"]
tasatotdel18 = tabla1.iloc[17]["tasa_acumulada"]



########################################################
#GRAFICA COLORES
#link:                           https://htmlcolorcodes.com/es/nombres-de-los-colores/
#nota: creo que tienen el orden invertido p ej. Orchid es violencia familiar
#Asignar color manual, orden: 
colors = ['black',  #Aborto
          'Violet',# Abuso sexual
          'SlateBlue', #Acoso sexual
          'Indigo', #Corrupcion de menores
          'DarkOrchid', #Feminicidio
          'PaleGoldenrod', #Hostigamiento sexual
          'black', 
          'Thistle', #imcumplimiento vf
          'Lavender', #vs la familia
          'DarkMagenta', #vs libertad personal
          'black'
          'black', 
          'MediumOrchid', #vs lavidaylibertadcorporral
          'black', #Trata de personas
          'black', #Trafico de menores
          'DarkViolet', #Violacion equiparada
          'MediumPurple', #Violacion simple
          "Plum", #VG en todas sus modalidades
          "Purple"#violenciafamiliar
         ]


treedel = px.treemap(tabla1, path=['Tipo de delito'],
                 values='GRAND TOTAL',#color_continuous_scale='RdBu',
                    )
#treedel = px.colors.diverging.swatches_continuous("Picnic")
#treedel.write_html("porcentZMtreegraph.html")
treedel.update_layout(paper_bgcolor= "lightgray",
                      #'rgba(0,0,0,0)',
                  plot_bgcolor= "lightgray",    
                       #'rgba(0,0,0,0)',
                  uniformtext_minsize=10,
                  uniformtext_mode='hide',
                  title_font_size = 10,
                  font_color="white",
                  title_font_family="Monserrat",
                  title_font_color="white",
                  margin = dict(autoexpand=False,
                              l=0, r=0, t=0, b=0),
                  showlegend=False,
                  #autosize=True,
                  width=450,
                  height=490    
                    ),
treedel.update_traces(marker=dict(colors=colors, line=dict(color='lightgray', width=.5)
                                        )
                              # marker=dict(#colors=colors)
)



#treedel.show()
##################################################################################
          
            
              
              
#card3 = dbc.Card(
#    dbc.CardBody(
#        [
#            
#            html.P([dbc.Button([
#                html.H3(
#                    dbc.CardImg(src= "https://github.com/fdealbam/violenciadegenero/blob/main/application/static/fight.svg?raw=true",
#                                href="https://violenciafamiliar.herokuapp.com/",
#                                style={"color": "black",
#                                       "height" :"25px",
#                                      "background-clor": "light"})),
#            "  Violencia Familiar"], 
#                    style={'textAlign': 'left',"color":"#FBC02D",
#                   "font-size": "30px",
#                           'margin-bottom':'-30px'
#                          })]),
#            
#     html.A([html.Img(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/fight.svg?raw=true",
#                        style={'height' : '170px',
#                    'width' : '120px',
#                    'float' : 'left' })],
#                  href="https://violenciafamiliar.herokuapp.com/", 
#                  ),
#        ]),
#    
#    
#    style={"width": "50rem", 
#          "border": "0",
#          "fill" : "orange"},
#)
#


################################################
# a p p 
################################################

#FONT_AWESOMEpro1 = "{% static 'fontawesome_pro/js/all.min.js' %}"
#FONT_AWESOMEpro = "{% static 'fontawesome_pro/css/all.min.css' %}"
#FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, 
                                                #FONT_AWESOMEpro1,
                                                #FONT_AWESOME, 
                                                #FONT_AWESOMEpro
                                               ], server=server)



app.layout = html.Div([
    #Logo
     dbc.Row([dbc.Col(
         dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/ce2cda9ccf7732861b8494b36562ebe9c8c642a6/application/static/logo%20cesopycamara.jpeg?raw=true"),
                        width=5, md={'size': 2,  "offset": 6, }),
         dbc.Col(html.H6(" Centro de Estudios Sociales y de Opinión Pública," 
                           " Cámara de Diputados"
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0, "font-family": "Sitka",}),
               ], justify="start",),
     html.Br(),
   html.Br(),
     html.Br(),
   html.Br(),

    #########################################################   Título
    dbc.Row(
           [
               dbc.Col([html.P("Violencia de género en México" ,
                      style={'textAlign': 'center',
                             "font-size": "65px",
                             "font-family": "Arial",
                           "color": "black", 
                          "text-shadow": "10px 20px 30px black",}),
                   html.P("Incidencia de 12 delitos seleccionados, en el período de 2015 al 2021" ,
                      style={'textAlign': 'center',
                             "font-size": "20px",
                             "font-family": "Arial",
                           "color": "black"}),
   html.Br(),
   html.Br(),
                   html.P("En este dashboard presentamos 12 delitos que reflejan la "
                          "gravedad que tiene la violencia de "
                          "género en el páís, analizados del año 2015 "
                          "hasta los datos más recientes, mayo de 2021. "
                          "Con el objeto de proporcionar a las diputadas y diputados información "
                          "basada en la evidencia, aquí presentamos análisis de cifras de un fenómeno con "
                          "alcance nacional. Estas cifras evocan la "
                          "necesidad insoslayable de profundizar las políticas "
                          "de equidad de género, de acciones sustantivas de equidad; acciones que nos hagan más "
                          "conscientes, más vigilantes respecto a sus multiples manifestiaciones; se requieren "
                          "también crear conciencia colectiva e intervención institucional para que nuestras "
                          "politicas y acciones sean "
                          "inclusivas e incluyentes, respetuosas del otro, sin importar condicíón o género "
                          "Los 12 delitos que se analizan son : "
                          "LISTAR LOS DELITOS." 
                          "Este trabajo tiene una actualización mensual automática, para disponer de cifras más "
                          " recientes.",
                          style={'textAlign': 'justify',
                             "font-size": "16px",
                             "font-family": "Arial",
                           "color": "ligthgray",
                            "margin-left": "100px",
                            "margin-right": "100px",}),
                          #"text-shadow": "10px 20px 30px black",
         
                            ]),
                       
                       
                       #width={'size': 20, "offset":1 },
                      #),
           
           ],justify="start",),
    
   html.Br(),
   html.Br(),
   html.Br(),
   dbc.Row(
           [
               dbc.Col(html.P(["Ranking de los delitos de género más frecuentes" ],
                      style={"color": "purple", 
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
 
    html.Br(),
 
    
    
    #################################################################PRIMERA COLUMNA
    dbc.Button(([html.P("Tipo de delito", style={
                               "color": "black", 
                               "font-size": "12px",
                               "font-weight": "bold",         
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }), 
                 html.P(tipodel1,#f"{int(num_zm):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "10px",
                               "font-weight": "bold",                                     
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel2,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel3,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel4,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel5,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel6,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),

#delito 7                 
                 html.P(tipodel7,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel8,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel9,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel10,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel11,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel12,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),

#delito 13                 
                 html.P(tipodel13,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel14,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel15,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
      html.P(tipodel16,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel17,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel18,#f"{int(num_zm):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                   
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '100px',
                 #"height":"140px" 
                 } ,disabled=True),

    
    
    
    
    #################################################################SEGUNDA COLUMNA
    dbc.Button(([html.P("Totales", style={
                               "color": "black", 
                               "font-size": "12px",
                               "font-weight": "bold", 
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }), 
                 html.P(f"{int(totdel1):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "11px",
                               "font-weight": "bold", 
                               "font-family": "Montserrat",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel2):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel3):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel4):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel5):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel6):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),

                 html.P(f"{int(totdel7):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel8):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel9):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel10):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel11):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel12):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 
                 html.P(f"{int(totdel13):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel14):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel15):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                    html.P(f"{int(totdel16):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel17):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel18):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '5px',
                 } ,disabled=True),

    
    
    
    
    
    #################################################################TERCERA COLUMNA
    dbc.Button(([html.P("Tasa*", style={
                               "color": "black", 
                               "font-size": "12px",
                               "font-weight": "bold", 
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }), 
                 html.P(f"{int(tasatotdel1):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "11px",
                               "font-weight": "bold", 
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel2):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel3):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel4):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel5):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel6):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),

                 html.P(f"{int(tasatotdel7):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel8):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel9):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel10):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel11):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel12):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel13):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel14):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel15):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                     html.P(f"{int(tasatotdel16):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "11px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel17):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel18):,}",  
                        style={
                               "color": "dark", 
                               "font-size": "10px",
                               "font-family": "Montserrat",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 

                 
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '5px',
                  'margin-right': '100px',
                 
                 "width":"100px" 
                 } ,disabled=True),

    
       dbc.Button(([dcc.Graph(figure=treedel), 
    
    
              
       ]),style={ "backgroundColor": "lightgray",
                  #"box-shadow": "10px 20px 30px gray",
                  #'margin-top': '20px',
                  'margin-left': '870px',
                 "width":"520px",
     "margin-top":"-520px"
                 } ,disabled=True),
    
    
    

    
    
    
    
    
   

    html.Br(),
    html.Br(),

    #subtitulo
      dbc.Row(
           [
               dbc.Col(html.P(["*Tasa: número de delitos por cada 100 mil habitantes." ],
                      style={"color": "gray", 
                               #"text-align": "right",
                               "margin-left": "100px",
                               "font-size": "12px",
                               "font-family": "Arial",        
                               #"text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                      )]),
 

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
  dbc.Row(
           [
               dbc.Col(html.P(["Acceso a los dashboards analíticos de cada delito" ],
                      style={"color": "black", 
                               #"font-weight": 'bold',
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
 
 

 
    
#dbc.Row( [
#    
#    dbc.Col(
        dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink("Violencia Familiar", 
                        href="https://violenciafamiliar.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                               #"margin-left": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
            
        html.A([
        html.Img(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/fight.svg?raw=true",
                        style={'height' : '170px',
                    'width' : '120px',
                    'float' : 'center' ,
                    #"margin-left":"100px"
                              })],
                  href="https://violenciafamiliar.herokuapp.com/", 
                  ),
                    # html.Br(),
  #   dbc.Col(
               
                     #),
           # ]),
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '105px',
                                "width":"180px", 
                                "height":"250px"
                 } ,disabled=True),
               
  
    
    #Estilo de fondo
    html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
],style={
            'margin-top': '0px',
            'margin-left': '10px',
            'width': '1400px',
           # 'height': '1413px',
      'backgroundColor': 'lightgray'
         });



if __name__ == '__main__':
    app.run_server()
