
# OEntrada violencia de genero

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
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



################################################################ inicia tratamiento


d_vg1 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/violenciadegenero/main/delitosvg2015_2021_a.csv?raw=true")
d_vg2 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/violenciadegenero/main/delitosvg2015_2021_b.csv?raw=true")

d_vg = pd.concat([d_vg1,d_vg2])

# REPLACE



#                                    ____________________________________________________________________________
#                                     >>>>>>>>>>>>>>>>>>>>>>>>>>> POR TIPO DE DELITO <<<<<<<<<<<<<<<<<<<<<<<<<<<<
d_vg.groupby(['Año','Tipo de delito'])['Enero', 
                 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre',
       'Noviembre', 'Diciembre'].sum().to_csv("00.csv",  header=True)
fem= pd.read_csv("00.csv")
############################################### separación de años

year15= fem[fem.Año == 2015]
year16= fem[fem.Año == 2016]
year17= fem[fem.Año == 2017]
year18= fem[fem.Año == 2018]
year19= fem[fem.Año == 2019]
year20= fem[fem.Año == 2020]
year21= fem[fem.Año == 2021]

############################################### Agregar suffix de años

y15 = year15.add_suffix('15')
y15.rename(columns ={'Año15': 'Año', 'Tipo de delito15': 'Tipo de delito', 'Unnamed: 015' : 'Unnamed: 0',
                            'Tipo de delito15': 'Tipo de delito'}, inplace = True)

y16 = year16.add_suffix('16')
y16.rename(columns ={'Año16': 'Año', 'Tipo de delito16': 'Tipo de delito', 'Unnamed: 016' : 'Unnamed: 0',
                            'Tipo de delito16': 'Tipo de delito'}, inplace = True)

y17 = year17.add_suffix('17')
y17.rename(columns ={'Año17': 'Año', 'Tipo de delito17': 'Tipo de delito', 'Unnamed: 017' : 'Unnamed: 0',
                            'Tipo de delito17': 'Tipo de delito'}, inplace = True)

y18= year18.add_suffix('18')
y18.rename(columns ={'Año18': 'Año', 'Tipo de delito18': 'Tipo de delito','Unnamed: 018' : 'Unnamed: 0',
                            'Tipo de delito18': 'Tipo de delito'}, inplace = True)

y19= year19.add_suffix('19')
y19.rename(columns ={'Año19': 'Año', 'Tipo de delito19': 'Tipo de delito', 'Unnamed: 019' : 'Unnamed: 0',
                            'Tipo de delito19': 'Tipo de delito'}, inplace = True)

y20= year20.add_suffix('20')
y20.rename(columns ={'Año20': 'Año', 'Tipo de delito20': 'Tipo de delito','Unnamed: 020' : 'Unnamed: 0',
                            'Tipo de delito20': 'Tipo de delito'}, inplace = True)

y21= year21.add_suffix('21')
y21.rename(columns ={'Año21': 'Año', 'Tipo de delito21': 'Tipo de delito','Unnamed: 021' : 'Unnamed: 0',
                            'Tipo de delito21': 'Tipo de delito'}, inplace = True)


############################################### Concat todos los años

fa = y15.merge(y16, on="Tipo de delito",  how="inner")
fb = fa.merge(y17, on="Tipo de delito",  how="inner")
fc = fb.merge(y18, on="Tipo de delito",  how="inner")
fd = fc.merge(y19, on="Tipo de delito",  how="inner")
fe = fd.merge(y20, on="Tipo de delito",  how="inner")
ff = fe.merge(y21, on="Tipo de delito",  how="inner")
                      
femi15_21 = ff[[
 'Tipo de delito','Enero15','Febrero15','Marzo15','Abril15','Mayo15','Junio15',
 'Julio15','Agosto15','Septiembre15','Octubre15','Noviembre15','Diciembre15',
 
 'Enero16','Febrero16','Marzo16','Abril16','Mayo16','Junio16','Julio16',
 'Agosto16','Septiembre16','Octubre16','Noviembre16','Diciembre16',

 'Enero17','Febrero17','Marzo17','Abril17','Mayo17','Junio17','Julio17',
 'Agosto17','Septiembre17','Octubre17','Noviembre17','Diciembre17',
    
 'Enero18','Febrero18','Marzo18','Abril18','Mayo18','Junio18','Julio18',
 'Agosto18','Septiembre18','Octubre18','Noviembre18','Diciembre18',
 
 'Enero19','Febrero19','Marzo19','Abril19','Mayo19','Junio19','Julio19',
 'Agosto19','Septiembre19','Octubre19','Noviembre19','Diciembre19',

 'Enero20','Febrero20','Marzo20','Abril20','Mayo20','Junio20','Julio20',
 'Agosto20','Septiembre20','Octubre20','Noviembre20','Diciembre20',

 'Enero21','Febrero21','Marzo21','Abril21','Mayo21','Junio21','Julio21',
 #'Agosto21','Septiembre21','Octubre21','Noviembre21','Diciembre21'
        ]]


##CRear columna de TOTAL ANUAL 
femi15_21['Total2015']= femi15_21[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               'Junio15', 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               'Noviembre15', 'Diciembre15',]].sum(axis=1)

#femi15_21['Total2015-21']= femi15_21[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               #'Junio15'#, 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               #'Noviembre15', 'Diciembre15',#
#                                     ]].sum(axis=1)

femi15_21['Total2016']= femi15_21[[ 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16',
                               'Junio16', 'Julio16', 'Agosto16', 'Septiembre16', 'Octubre16',
                               'Noviembre16', 'Diciembre16',]].sum(axis=1)
femi15_21['Total2017']= femi15_21[[ 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17',
                               'Junio17', 'Julio17', 'Agosto17', 'Septiembre17', 'Octubre17',
                               'Noviembre17', 'Diciembre17',]].sum(axis=1)
femi15_21['Total2018']= femi15_21[[ 'Enero18', 'Febrero18', 'Marzo18', 'Abril18', 'Mayo18',
                               'Junio18', 'Julio18', 'Agosto18', 'Septiembre18', 'Octubre18',
                               'Noviembre18', 'Diciembre18',]].sum(axis=1)
femi15_21['Total2019']= femi15_21[[ 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19',
                               'Junio19', 'Julio19', 'Agosto19', 'Septiembre19', 'Octubre19',
                               'Noviembre19', 'Diciembre19',]].sum(axis=1)
femi15_21['Total2020']= femi15_21[[ 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20',
                               'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               'Noviembre20', 'Diciembre20',]].sum(axis=1)
femi15_21['Total2021']= femi15_21[[ 'Enero21', 'Febrero21', 'Marzo21', 'Abril21', 'Mayo21',
                               'Junio21', 'Julio21',# 'Agosto21',# 'Septiembre21',# 'Octubre21',
                               #'Noviembre20', 'Diciembre20',
                                  ]].sum(axis=1)
femi15_21["GRAND TOTAL"]= femi15_21[["Total2015","Total2016","Total2017","Total2018","Total2019","Total2020",
                                    "Total2021",]].sum(axis=1)

totald = int(femi15_21["GRAND TOTAL"].sum())
totaldvg = f"{totald:,}"



#_____________________________________________________________________________________________
femi15_21["pob_GRAND_TOTAL"] = 128972439  #pob total sumada de 2015 al 2021, NOOOO, es solo pob 21, entiendes o no entiendes?
femi15_21["tasa_acumulada"] = (femi15_21["GRAND TOTAL"] / femi15_21.pob_GRAND_TOTAL)*100000


# tasa de totales delitos vg a totales anuales 15-21
femi15_21["tasa_tot2015"] = ((femi15_21['Total2015']/121347800)*100000).round(1)
femi15_21["tasa_tot2016"] = ((femi15_21['Total2016']/122715165)*100000).round(1)
femi15_21["tasa_tot2017"] = ((femi15_21['Total2017']/124041731)*100000).round(1)
femi15_21["tasa_tot2018"] = ((femi15_21['Total2018']/125327797)*100000).round(1)
femi15_21["tasa_tot2019"] = ((femi15_21['Total2019']/126577691)*100000).round(1)
femi15_21["tasa_tot2020"] = ((femi15_21['Total2020']/127792286)*100000).round(1)
femi15_21["tasa_tot2021"] = ((femi15_21['Total2021']/128972439)*100000).round(1)
femi15_21["Variac_ABS2015_2021"] = (-(femi15_21["Total2015"]-femi15_21["Total2020"])).round(1)
femi15_21["Variac_tasa2015_2021"]= (-(femi15_21["tasa_tot2015"]-femi15_21["tasa_tot2020"])).round(1)


#                              variaciones abs mensuales by tipo de delito
# Variaciones 2015-2016
femi15_21["var_ene15_16"] = femi15_21.Enero16 - femi15_21.Enero15
femi15_21["var_feb15_16"] = femi15_21.Febrero16 - femi15_21.Febrero15
femi15_21["var_mrz15_16"] = femi15_21.Marzo16 - femi15_21.Marzo15
femi15_21["var_abr15_16"] = femi15_21.Abril16 - femi15_21.Abril15
femi15_21["var_may15_16"] = femi15_21.Mayo16 - femi15_21.Mayo15
femi15_21["var_jun15_16"] = femi15_21.Junio16 - femi15_21.Junio15
femi15_21["var_jul15_16"] = femi15_21.Julio16 - femi15_21.Julio15
femi15_21["var_ago15_16"] = femi15_21.Agosto16 - femi15_21.Agosto15
femi15_21["var_sep15_16"] = femi15_21.Septiembre16 - femi15_21.Septiembre15
femi15_21["var_oct15_16"] = femi15_21.Octubre16 - femi15_21.Octubre15
femi15_21["var_nov15_16"] = femi15_21.Noviembre16 - femi15_21.Noviembre15
femi15_21["var_dic15_16"] = femi15_21.Diciembre16 - femi15_21.Diciembre15

# Variaciones 2016-2017
femi15_21["var_ene16_17"] = femi15_21.Enero17 - femi15_21.Enero16
femi15_21["var_feb16_17"] = femi15_21.Febrero17 - femi15_21.Febrero16
femi15_21["var_mrz16_17"] = femi15_21.Marzo17 - femi15_21.Marzo16
femi15_21["var_abr16_17"] = femi15_21.Abril17 - femi15_21.Abril16
femi15_21["var_may16_17"] = femi15_21.Mayo17 - femi15_21.Mayo16
femi15_21["var_jun16_17"] = femi15_21.Junio17 - femi15_21.Junio16
femi15_21["var_jul16_17"] = femi15_21.Julio17 - femi15_21.Julio16
femi15_21["var_ago16_17"] = femi15_21.Agosto17 - femi15_21.Agosto16
femi15_21["var_sep16_17"] = femi15_21.Septiembre17 - femi15_21.Septiembre16
femi15_21["var_oct16_17"] = femi15_21.Octubre17 - femi15_21.Octubre16
femi15_21["var_nov16_17"] = femi15_21.Noviembre17 - femi15_21.Noviembre16
femi15_21["var_dic16_17"] = femi15_21.Diciembre17 - femi15_21.Diciembre16

# Variaciones 2017-2018
femi15_21["var_ene17_18"] = femi15_21.Enero18 - femi15_21.Enero17
femi15_21["var_feb17_18"] = femi15_21.Febrero18 - femi15_21.Febrero17
femi15_21["var_mrz17_18"] = femi15_21.Marzo18 - femi15_21.Marzo17
femi15_21["var_abr17_18"] = femi15_21.Abril18 - femi15_21.Abril17
femi15_21["var_may17_18"] = femi15_21.Mayo18 - femi15_21.Mayo17
femi15_21["var_jun17_18"] = femi15_21.Junio18 - femi15_21.Junio17
femi15_21["var_jul17_18"] = femi15_21.Julio18 - femi15_21.Julio17
femi15_21["var_ago17_18"] = femi15_21.Agosto18 - femi15_21.Agosto17
femi15_21["var_sep17_18"] = femi15_21.Septiembre18 - femi15_21.Septiembre17
femi15_21["var_oct17_18"] = femi15_21.Octubre18 - femi15_21.Octubre17
femi15_21["var_nov17_18"] = femi15_21.Noviembre18 - femi15_21.Noviembre17
femi15_21["var_dic17_18"] = femi15_21.Diciembre18 - femi15_21.Diciembre17

# Variaciones 2018-2019
femi15_21["var_ene18_19"] = femi15_21.Enero19 - femi15_21.Enero18
femi15_21["var_feb18_19"] = femi15_21.Febrero19 - femi15_21.Febrero18
femi15_21["var_mrz18_19"] = femi15_21.Marzo19 - femi15_21.Marzo18
femi15_21["var_abr18_19"] = femi15_21.Abril19 - femi15_21.Abril18
femi15_21["var_may18_19"] = femi15_21.Mayo19 - femi15_21.Mayo18
femi15_21["var_jun18_19"] = femi15_21.Junio19 - femi15_21.Junio18
femi15_21["var_jul18_19"] = femi15_21.Julio19 - femi15_21.Julio18
femi15_21["var_ago18_19"] = femi15_21.Agosto19 - femi15_21.Agosto18
femi15_21["var_sep18_19"] = femi15_21.Septiembre19 - femi15_21.Septiembre18
femi15_21["var_oct18_19"] = femi15_21.Octubre19 - femi15_21.Octubre18
femi15_21["var_nov18_19"] = femi15_21.Noviembre19 - femi15_21.Noviembre18
femi15_21["var_dic18_19"] = femi15_21.Diciembre19 - femi15_21.Diciembre18

# Variaciones 2019-20120
femi15_21["var_ene19_20"] = femi15_21.Enero20 - femi15_21.Enero19
femi15_21["var_feb19_20"] = femi15_21.Febrero20 - femi15_21.Febrero19
femi15_21["var_mrz19_20"] = femi15_21.Marzo20 - femi15_21.Marzo19
femi15_21["var_abr19_20"] = femi15_21.Abril20 - femi15_21.Abril19
femi15_21["var_may19_20"] = femi15_21.Mayo20 - femi15_21.Mayo19
femi15_21["var_jun19_20"] = femi15_21.Junio20 - femi15_21.Junio19
femi15_21["var_jul19_20"] = femi15_21.Julio20 - femi15_21.Julio19
femi15_21["var_ago19_20"] = femi15_21.Agosto20 - femi15_21.Agosto19
femi15_21["var_sep19_20"] = femi15_21.Septiembre20 - femi15_21.Septiembre19
femi15_21["var_oct19_20"] = femi15_21.Octubre20 - femi15_21.Octubre19
femi15_21["var_nov19_20"] = femi15_21.Noviembre20 - femi15_21.Noviembre19
femi15_21["var_dic19_20"] = femi15_21.Diciembre20 - femi15_21.Diciembre19

# Variaciones 2020-2021
femi15_21["var_ene20_21"] = femi15_21.Enero21 - femi15_21.Enero20
femi15_21["var_feb20_21"] = femi15_21.Febrero21 - femi15_21.Febrero20
femi15_21["var_mrz20_21"] = femi15_21.Marzo21 - femi15_21.Marzo20
femi15_21["var_abr20_21"] = femi15_21.Abril21 - femi15_21.Abril20
femi15_21["var_may20_21"] = femi15_21.Mayo21 - femi15_21.Mayo20
femi15_21["var_jun20_21"] = femi15_21.Junio21 - femi15_21.Junio20
femi15_21["var_jul20_21"] = femi15_21.Julio21 - femi15_21.Julio20
#femi15_21["var_ago20_21"] = femi15_21.Agosto21 - femi15_21.Agosto20
#femi15_21["var_sep20_21"] = femi15_21.Septiembre21 - femi15_21.Septiembre20
#femi15_21["var_oct20_21"] = femi15_21.Octubre21 - femi15_21.Octubre20
#femi15_21["var_nov20_21"] = femi15_21.Noviembre21 - femi15_21.Noviembre20
#femi15_21["var_dic20_21"] = femi15_21.Diciembre21 - femi15_21.Diciembre20


#                variaciones mensuales seriadas (mismo año) by tipo de delito
# 2015
femi15_21["v_ene_feb_15"] = femi15_21.Febrero15 - femi15_21.Enero15
femi15_21["v_feb_mar_15"] = femi15_21.Marzo15 - femi15_21.Febrero15
femi15_21["v_mar_abr_15"] = femi15_21.Abril15 - femi15_21.Marzo15
femi15_21["v_abr_may_15"] = femi15_21.Mayo15 - femi15_21.Abril15
femi15_21["v_may_jun_15"] = femi15_21.Junio15 - femi15_21.Mayo15
femi15_21["v_jun_jul_15"] = femi15_21.Julio15 - femi15_21.Junio15
femi15_21["v_jul_ago_15"] = femi15_21.Agosto15 - femi15_21.Julio15
femi15_21["v_ago_sep_15"] = femi15_21.Septiembre15 - femi15_21.Agosto15
femi15_21["v_sep_oct_15"] = femi15_21.Octubre15 - femi15_21.Septiembre15
femi15_21["v_oct_nov_15"] = femi15_21.Noviembre15 - femi15_21.Octubre15
femi15_21["v_nov_dic_15"] = femi15_21.Diciembre15 - femi15_21.Noviembre15
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_15"] = femi15_21.Diciembre15 - femi15_21.Enero16

# 2016
femi15_21["v_ene_feb_16"] = femi15_21.Febrero16 - femi15_21.Enero16
femi15_21["v_feb_mar_16"] = femi15_21.Marzo16 - femi15_21.Febrero16
femi15_21["v_mar_abr_16"] = femi15_21.Abril16 - femi15_21.Marzo16
femi15_21["v_abr_may_16"] = femi15_21.Mayo16 - femi15_21.Abril16
femi15_21["v_may_jun_16"] = femi15_21.Junio16 - femi15_21.Mayo16
femi15_21["v_jun_jul_16"] = femi15_21.Julio16 - femi15_21.Junio16
femi15_21["v_jul_ago_16"] = femi15_21.Agosto16 - femi15_21.Julio16
femi15_21["v_ago_sep_16"] = femi15_21.Septiembre16 - femi15_21.Agosto16
femi15_21["v_sep_oct_16"] = femi15_21.Octubre16 - femi15_21.Septiembre16
femi15_21["v_oct_nov_16"] = femi15_21.Noviembre16 - femi15_21.Octubre16
femi15_21["v_nov_dic_16"] = femi15_21.Diciembre16 - femi15_21.Noviembre16
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_16"] = femi15_21.Diciembre16 - femi15_21.Enero17

# 2017
femi15_21["v_ene_feb_17"] = femi15_21.Febrero17 - femi15_21.Enero17
femi15_21["v_feb_mar_17"] = femi15_21.Marzo17 - femi15_21.Febrero17
femi15_21["v_mar_abr_17"] = femi15_21.Abril17 - femi15_21.Marzo17
femi15_21["v_abr_may_17"] = femi15_21.Mayo17 - femi15_21.Abril17
femi15_21["v_may_jun_17"] = femi15_21.Junio17 - femi15_21.Mayo17
femi15_21["v_jun_jul_17"] = femi15_21.Julio17 - femi15_21.Junio17
femi15_21["v_jul_ago_17"] = femi15_21.Agosto17 - femi15_21.Julio17
femi15_21["v_ago_sep_17"] = femi15_21.Septiembre17 - femi15_21.Agosto17
femi15_21["v_sep_oct_17"] = femi15_21.Octubre17 - femi15_21.Septiembre17
femi15_21["v_oct_nov_17"] = femi15_21.Noviembre17 - femi15_21.Octubre17
femi15_21["v_nov_dic_17"] = femi15_21.Diciembre17 - femi15_21.Noviembre17
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_17"] = femi15_21.Diciembre17 - femi15_21.Enero18

# 2018
femi15_21["v_ene_feb_18"] = femi15_21.Febrero18 - femi15_21.Enero18
femi15_21["v_feb_mar_18"] = femi15_21.Marzo18 - femi15_21.Febrero18
femi15_21["v_mar_abr_18"] = femi15_21.Abril18 - femi15_21.Marzo18
femi15_21["v_abr_may_18"] = femi15_21.Mayo18 - femi15_21.Abril18
femi15_21["v_may_jun_18"] = femi15_21.Junio18 - femi15_21.Mayo18
femi15_21["v_jun_jul_18"] = femi15_21.Julio18 - femi15_21.Junio18
femi15_21["v_jul_ago_18"] = femi15_21.Agosto18 - femi15_21.Julio18
femi15_21["v_ago_sep_18"] = femi15_21.Septiembre18 - femi15_21.Agosto18
femi15_21["v_sep_oct_18"] = femi15_21.Octubre18 - femi15_21.Septiembre18
femi15_21["v_oct_nov_18"] = femi15_21.Noviembre18 - femi15_21.Octubre18
femi15_21["v_nov_dic_18"] = femi15_21.Diciembre18 - femi15_21.Noviembre18
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_18"] = femi15_21.Diciembre18 - femi15_21.Enero19

# 2019
femi15_21["v_ene_feb_19"] = femi15_21.Febrero19 - femi15_21.Enero19
femi15_21["v_feb_mar_19"] = femi15_21.Marzo19 - femi15_21.Febrero19
femi15_21["v_mar_abr_19"] = femi15_21.Abril19 - femi15_21.Marzo19
femi15_21["v_abr_may_19"] = femi15_21.Mayo19 - femi15_21.Abril19
femi15_21["v_may_jun_19"] = femi15_21.Junio19 - femi15_21.Mayo19
femi15_21["v_jun_jul_19"] = femi15_21.Julio19 - femi15_21.Junio19
femi15_21["v_jul_ago_19"] = femi15_21.Agosto19 - femi15_21.Julio19
femi15_21["v_ago_sep_19"] = femi15_21.Septiembre19 - femi15_21.Agosto19
femi15_21["v_sep_oct_19"] = femi15_21.Octubre19 - femi15_21.Septiembre19
femi15_21["v_oct_nov_19"] = femi15_21.Noviembre19 - femi15_21.Octubre19
femi15_21["v_nov_dic_19"] = femi15_21.Diciembre19 - femi15_21.Noviembre19
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_19"] = femi15_21.Diciembre19 - femi15_21.Enero20

# 2020
femi15_21["v_ene_feb_20"] = femi15_21.Febrero20 - femi15_21.Enero20
femi15_21["v_feb_mar_20"] = femi15_21.Marzo20 - femi15_21.Febrero20
femi15_21["v_mar_abr_20"] = femi15_21.Abril20 - femi15_21.Marzo20
femi15_21["v_abr_may_20"] = femi15_21.Mayo20 - femi15_21.Abril20
femi15_21["v_may_jun_20"] = femi15_21.Junio20 - femi15_21.Mayo20
femi15_21["v_jun_jul_20"] = femi15_21.Julio20 - femi15_21.Junio20
femi15_21["v_jul_ago_20"] = femi15_21.Agosto20 - femi15_21.Julio20
femi15_21["v_ago_sep_20"] = femi15_21.Septiembre20 - femi15_21.Agosto20
femi15_21["v_sep_oct_20"] = femi15_21.Octubre20 - femi15_21.Septiembre20
femi15_21["v_oct_nov_20"] = femi15_21.Noviembre20 - femi15_21.Octubre20
femi15_21["v_nov_dic_20"] = femi15_21.Diciembre20 - femi15_21.Noviembre20
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_20"] = femi15_21.Diciembre20 - femi15_21.Enero21

# 2021
femi15_21["v_ene_feb_21"] = femi15_21.Febrero21 - femi15_21.Enero21
femi15_21["v_feb_mar_21"] = femi15_21.Marzo21 - femi15_21.Febrero21
femi15_21["v_mar_abr_21"] = femi15_21.Abril21 - femi15_21.Marzo21
femi15_21["v_abr_may_21"] = femi15_21.Mayo21 - femi15_21.Abril21
femi15_21["v_may_jun_21"] = femi15_21.Junio21 - femi15_21.Mayo21
femi15_21["v_jun_jul_21"] = femi15_21.Julio21 - femi15_21.Junio21
#femi15_21["v_jul_ago_21"] = femi15_21.Agosto21 - femi15_21.Julio21
#femi15_21["v_ago_sep_21"] = femi15_21.Septiembre21 - femi15_21.Agosto21
#femi15_21["v_sep_oct_21"] = femi15_21.Octubre21 - femi15_21.Septiembre21
#femi15_21["v_oct_nov_21"] = femi15_21.Noviembre21 - femi15_21.Octubre21
#femi15_21["v_nov_dic_21"] = femi15_21.Diciembre21 - femi15_21.Noviembre21
#variacion Diciembre-Enero (si llegamos...)
#femi15_21["v_dic_ene_21"] = femi15_21.Diciembre21 - femi15_21.Enero22


#                               variaciones porcentuales mensuales by tipo de delito
# Variaciones 2015-2016
femi15_21["var_ene15_16_%"] = (femi15_21["var_ene15_16"]*100)/femi15_21.Enero16
femi15_21["var_feb15_16_%"] = (femi15_21["var_feb15_16"]*100)/femi15_21.Febrero16
femi15_21["var_mrz15_16_%"] = (femi15_21["var_mrz15_16"]*100)/femi15_21.Marzo16
femi15_21["var_abr15_16_%"] = (femi15_21["var_abr15_16"]*100)/femi15_21.Abril16
femi15_21["var_may15_16_%"] = (femi15_21["var_may15_16"]*100)/femi15_21.Mayo16
femi15_21["var_jun15_16_%"] = (femi15_21["var_jun15_16"]*100)/femi15_21.Junio16
femi15_21["var_jul15_16_%"] = (femi15_21["var_jul15_16"]*100)/femi15_21.Julio16
femi15_21["var_ago15_16_%"] = (femi15_21["var_ago15_16"]*100)/femi15_21.Agosto16
femi15_21["var_sep15_16_%"] = (femi15_21["var_sep15_16"]*100)/femi15_21.Septiembre16
femi15_21["var_oct15_16_%"] = (femi15_21["var_oct15_16"]*100)/femi15_21.Octubre16
femi15_21["var_nov15_16_%"] = (femi15_21["var_nov15_16"]*100)/femi15_21.Noviembre16
femi15_21["var_dic15_16_%"] = (femi15_21["var_dic15_16"]*100)/femi15_21.Diciembre16

# Variaciones 2016-2017
femi15_21["var_ene16_17_%"] = (femi15_21["var_ene16_17"]*100)/femi15_21.Enero17
femi15_21["var_feb16_17_%"] = (femi15_21["var_feb16_17"]*100)/femi15_21.Febrero17
femi15_21["var_mrz16_17_%"] = (femi15_21["var_mrz16_17"]*100)/femi15_21.Marzo17
femi15_21["var_abr16_17_%"] = (femi15_21["var_abr16_17"]*100)/femi15_21.Abril17
femi15_21["var_may16_17_%"] = (femi15_21["var_may16_17"]*100)/femi15_21.Mayo17
femi15_21["var_jun16_17_%"] = (femi15_21["var_jun16_17"]*100)/femi15_21.Junio17
femi15_21["var_jul16_17_%"] = (femi15_21["var_jul16_17"]*100)/femi15_21.Julio17
femi15_21["var_ago16_17_%"] = (femi15_21["var_ago16_17"]*100)/femi15_21.Agosto17
femi15_21["var_sep16_17_%"] = (femi15_21["var_sep16_17"]*100)/femi15_21.Septiembre17
femi15_21["var_oct16_17_%"] = (femi15_21["var_oct16_17"]*100)/femi15_21.Octubre17
femi15_21["var_nov16_17_%"] = (femi15_21["var_nov16_17"]*100)/femi15_21.Noviembre17
femi15_21["var_dic16_17_%"] = (femi15_21["var_dic16_17"]*100)/femi15_21.Diciembre17

# Variaciones 2017-2018
femi15_21["var_ene17_18_%"] = (femi15_21["var_ene17_18"]*100)/femi15_21.Enero18
femi15_21["var_feb17_18_%"] = (femi15_21["var_feb17_18"]*100)/femi15_21.Febrero18
femi15_21["var_mrz17_18_%"] = (femi15_21["var_mrz17_18"]*100)/femi15_21.Marzo18
femi15_21["var_abr17_18_%"] = (femi15_21["var_abr17_18"]*100)/femi15_21.Abril18
femi15_21["var_may17_18_%"] = (femi15_21["var_may17_18"]*100)/femi15_21.Mayo18
femi15_21["var_jun17_18_%"] = (femi15_21["var_jun17_18"]*100)/femi15_21.Junio18
femi15_21["var_jul17_18_%"] = (femi15_21["var_jul17_18"]*100)/femi15_21.Julio18
femi15_21["var_ago17_18_%"] = (femi15_21["var_ago17_18"]*100)/femi15_21.Agosto18
femi15_21["var_sep17_18_%"] = (femi15_21["var_sep17_18"]*100)/femi15_21.Septiembre18
femi15_21["var_oct17_18_%"] = (femi15_21["var_oct17_18"]*100)/femi15_21.Octubre18
femi15_21["var_nov17_18_%"] = (femi15_21["var_nov17_18"]*100)/femi15_21.Noviembre18
femi15_21["var_dic17_18_%"] = (femi15_21["var_dic17_18"]*100)/femi15_21.Diciembre18

# Variaciones 2018-2019
femi15_21["var_ene18_19_%"] = (femi15_21["var_ene18_19"]*100)/femi15_21.Enero19
femi15_21["var_feb18_19_%"] = (femi15_21["var_feb18_19"]*100)/femi15_21.Febrero19
femi15_21["var_mrz18_19_%"] = (femi15_21["var_mrz18_19"]*100)/femi15_21.Marzo19
femi15_21["var_abr18_19_%"] = (femi15_21["var_abr18_19"]*100)/femi15_21.Abril19
femi15_21["var_may18_19_%"] = (femi15_21["var_may18_19"]*100)/femi15_21.Mayo19
femi15_21["var_jun18_19_%"] = (femi15_21["var_jun18_19"]*100)/femi15_21.Junio19
femi15_21["var_jul18_19_%"] = (femi15_21["var_jul18_19"]*100)/femi15_21.Julio19
femi15_21["var_ago18_19_%"] = (femi15_21["var_ago18_19"]*100)/femi15_21.Agosto19
femi15_21["var_sep18_19_%"] = (femi15_21["var_sep18_19"]*100)/femi15_21.Septiembre19
femi15_21["var_oct18_19_%"] = (femi15_21["var_oct18_19"]*100)/femi15_21.Octubre19
femi15_21["var_nov18_19_%"] = (femi15_21["var_nov18_19"]*100)/femi15_21.Noviembre19
femi15_21["var_dic18_19_%"] = (femi15_21["var_dic18_19"]*100)/femi15_21.Diciembre19

# Variaciones 2019-20120
femi15_21["var_ene19_20_%"] = (femi15_21["var_ene19_20"]*100)/femi15_21.Enero20
femi15_21["var_feb19_20_%"] = (femi15_21["var_feb19_20"]*100)/femi15_21.Febrero20
femi15_21["var_mrz19_20_%"] = (femi15_21["var_mrz19_20"]*100)/femi15_21.Marzo20
femi15_21["var_abr19_20_%"] = (femi15_21["var_abr19_20"]*100)/femi15_21.Abril20
femi15_21["var_may19_20_%"] = (femi15_21["var_may19_20"]*100)/femi15_21.Mayo20
femi15_21["var_jun19_20_%"] = (femi15_21["var_jun19_20"]*100)/femi15_21.Junio20
femi15_21["var_jul19_20_%"] = (femi15_21["var_jul19_20"]*100)/femi15_21.Julio20
femi15_21["var_ago19_20_%"] = (femi15_21["var_ago19_20"]*100)/femi15_21.Agosto20
femi15_21["var_sep19_20_%"] = (femi15_21["var_sep19_20"]*100)/femi15_21.Septiembre20
femi15_21["var_oct19_20_%"] = (femi15_21["var_oct19_20"]*100)/femi15_21.Octubre20
femi15_21["var_nov19_20_%"] = (femi15_21["var_nov19_20"]*100)/femi15_21.Noviembre20
femi15_21["var_dic19_20_%"] = (femi15_21["var_dic19_20"]*100)/femi15_21.Diciembre20

# Variaciones 2020-2021
femi15_21["var_ene20_21_%"] = (femi15_21["var_ene20_21"]*100)/femi15_21.Enero21
femi15_21["var_feb20_21_%"] = (femi15_21["var_feb20_21"]*100)/femi15_21.Febrero21
femi15_21["var_mrz20_21_%"] = (femi15_21["var_mrz20_21"]*100)/femi15_21.Marzo21
femi15_21["var_abr20_21_%"] = (femi15_21["var_abr20_21"]*100)/femi15_21.Abril21
femi15_21["var_may20_21_%"] = (femi15_21["var_may20_21"]*100)/femi15_21.Mayo21
femi15_21["var_jun20_21_%"] = (femi15_21["var_jun20_21"]*100)/femi15_21.Junio21
femi15_21["var_jul20_21_%"] = (femi15_21["var_jul20_21"]*100)/femi15_21.Julio21
#femi15_21["var_ago20_21_%"] = (femi15_21["var_ago20_21"]*100)/femi15_21.Agosto21
#femi15_21["var_sep20_21_%"] = (femi15_21["var_sep20_21"]*100)/femi15_21.Septiembre21
#femi15_21["var_oct20_21_%"] = (femi15_21["var_oct20_21"]*100)/femi15_21.Octubre21
#femi15_21["var_nov20_21_%"] = (femi15_21["var_nov20_21"]*100)/femi15_21.Noviembre21
#femi15_21["var_dic20_21_%"] = (femi15_21["var_dic20_21"]*100)/femi15_21.Diciembre21

#                variaciones anuales by tipo de delito
femi15_21["var_1516"] = femi15_21.Total2016 - femi15_21.Total2015
femi15_21["var_1617"] = femi15_21.Total2017 - femi15_21.Total2016
femi15_21["var_1718"] = femi15_21.Total2018 - femi15_21.Total2017
femi15_21["var_1819"] = femi15_21.Total2019 - femi15_21.Total2018
femi15_21["var_1920"] = femi15_21.Total2020 - femi15_21.Total2019
femi15_21["var_2021"] = femi15_21.Total2021 - femi15_21.Total2020



#_____ TABLA RESUMEN
tabla_sorted_vg = femi15_21[["Tipo de delito","GRAND TOTAL",#"Total2015","Total2020","tasa_tot2015","tasa_tot2020","Variac_ABS2015_2021","Variac_tasa2015_2021"
           "tasa_acumulada"]]




#_____merge con diccionario para get url´s
dicc = pd.read_csv("https://raw.githubusercontent.com/fdealbam/violenciadegenero/main/diccionariovg.csv")#, encoding="Latin-1")
dicc.drop("Unnamed: 0",1, inplace=True)



tabla1 = tabla_sorted_vg.merge(dicc, on="Tipo de delito").sort_values("tasa_acumulada", ascending=False, ignore_index=True).round(1)

#tabla1.sort_values("tasa_acumulada", ascending=False, ignore_index=True).round(1)







#_____________________________ I D E N T I F I C A D O R E S _____________________________
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
#tipodel18 = tabla1.iloc[17]["Tipo de delito"]

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
#totdel18 = tabla1.iloc[17]["GRAND TOTAL"]

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
#tasatotdel18 = tabla1.iloc[17]["tasa_acumulada"]


#url

urldel1 =  tabla1.iloc[0] ["url"]
urldel2 =  tabla1.iloc[1] ["url"]
urldel3 =  tabla1.iloc[2] ["url"]
urldel4 =  tabla1.iloc[3] ["url"]
urldel5 =  tabla1.iloc[4] ["url"]
urldel6 =  tabla1.iloc[5] ["url"]
urldel7 =  tabla1.iloc[6] ["url"]
urldel8 =  tabla1.iloc[7] ["url"]
urldel9 =  tabla1.iloc[8] ["url"]
urldel10 = tabla1.iloc[9] ["url"]
urldel11 = tabla1.iloc[10]["url"]
urldel12 = tabla1.iloc[11]["url"]
urldel13 = tabla1.iloc[12]["url"]
urldel14 = tabla1.iloc[13]["url"]
urldel15 = tabla1.iloc[14]["url"]
urldel16 = tabla1.iloc[15]["url"]
urldel17 = tabla1.iloc[16]["url"]
#urldel18 = tabla1.iloc[17]["url"]



#icono

iconodel1 =  tabla1.iloc[0] ["icono"]
iconodel2 =  tabla1.iloc[1] ["icono"]
iconodel3 =  tabla1.iloc[2] ["icono"]
iconodel4 =  tabla1.iloc[3] ["icono"]
iconodel5 =  tabla1.iloc[4] ["icono"]
iconodel6 =  tabla1.iloc[5] ["icono"]
iconodel7 =  tabla1.iloc[6] ["icono"]
iconodel8 =  tabla1.iloc[7] ["icono"]
iconodel9 =  tabla1.iloc[8] ["icono"]
iconodel10 = tabla1.iloc[9] ["icono"]
iconodel11 = tabla1.iloc[10]["icono"]
iconodel12 = tabla1.iloc[11]["icono"]
iconodel13 = tabla1.iloc[12]["icono"]
iconodel14 = tabla1.iloc[13]["icono"]
iconodel15 = tabla1.iloc[14]["icono"]
iconodel16 = tabla1.iloc[15]["icono"]
iconodel17 = tabla1.iloc[16]["icono"]
#iconodel18 = tabla1.iloc[17]["icono"]


#####################################################################################
#### _______________________________GRAFICA MESES
acumulado_meses = femi15_21[[
    'Enero15','Febrero15','Marzo15','Abril15','Mayo15','Junio15','Julio15','Agosto15','Septiembre15','Octubre15','Noviembre15','Diciembre15',
    'Enero16','Febrero16','Marzo16','Abril16','Mayo16','Junio16','Julio16','Agosto16','Septiembre16','Octubre16','Noviembre16','Diciembre16',
    'Enero17','Febrero17','Marzo17','Abril17','Mayo17','Junio17','Julio17','Agosto17','Septiembre17','Octubre17','Noviembre17','Diciembre17',
    'Enero18','Febrero18','Marzo18','Abril18','Mayo18','Junio18','Julio18','Agosto18','Septiembre18','Octubre18','Noviembre18','Diciembre18',
    'Enero19','Febrero19','Marzo19','Abril19','Mayo19','Junio19','Julio19','Agosto19','Septiembre19','Octubre19','Noviembre19','Diciembre19',
    'Enero20','Febrero20','Marzo20','Abril20','Mayo20','Junio20','Julio20','Agosto20','Septiembre20','Octubre20','Noviembre20','Diciembre20',
    'Enero21','Febrero21','Marzo21','Abril21','Mayo21','Junio21','Julio21']].stb.subtotal().tail(1).T.to_csv("0000procesoheadr.csv")

names = ["Meses","Total"]
acumulado_meses = pd.read_csv("0000procesoheadr.csv", names=names, skiprows=[0])

fig_meses = go.Figure()
fig_meses.add_trace(go.Bar(x=acumulado_meses.Meses,
                                 y=acumulado_meses.Total,
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))
fig_meses.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Acumulados mensuales',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    #width=1000,
    #height=400
    )

fig_meses.add_annotation(
        x=73,    #posición dada (punta row)
        y=36600,    #posición dada (punta row)
        xref="x",
        yref="y",
        text="Marzo, abril y mayo de 2021 registraron un aumento notorio",
        showarrow=True,
        font=dict(
            family="Montserrat",
            size=14,
            color="#000"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=-300,  # posición del txt respecto a la posición dada x
        ay=-60,  # posición del txt respecto a la posición dada y
        #bordercolor="#000",
        borderwidth=2,
        borderpad=4,
        bgcolor="white",
        opacity=0.8
        )

#####################################################################################
#### _______________________________GRAFICA COMPARATIVA 2015/2020
femi15_21_graf = femi15_21[["Tipo de delito", "tasa_acumulada", "Total2015","Total2020",
           "tasa_tot2015","tasa_tot2020", 
          "Variac_ABS2015_2021", 
           "Variac_tasa2015_2021" 
          ]].sort_values("Total2015", ascending=False, ignore_index=False).tail(16)


#femi15_21_graf= grap
import plotly.graph_objects as go

comparatot_2015_20 = go.Figure()
comparatot_2015_20.add_trace(go.Bar(
    x=femi15_21_graf["Tipo de delito"],
    y=femi15_21_graf["Total2015"],
    name='2015',
    marker_color='purple',
    orientation='v'
))
comparatot_2015_20.add_trace(go.Bar(
    x=femi15_21_graf["Tipo de delito"],
    y=femi15_21_graf["Total2020"],
    name='2020',
    #fontsize=8,
    marker_color='orchid',
    orientation='v'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
comparatot_2015_20.update_layout(paper_bgcolor= #"lightgray",
                      'rgba(0,0,0,0)',
                  plot_bgcolor= #"lightgray", 
                  'rgba(0,0,0,0)',
                  font_color="black",
                  title_font_family="Arial",
                  title_font_color="black",
                  barmode='group', 
                  xaxis_tickangle=-45, 
                  font=dict(family="Arial",
                            size=10,
                            color="gray"),
                  legend=dict(yanchor="top",
                              font_size=15,
                              y=0.99,
                              xanchor="left",
                              x=.7),              
                 # width=600,
                  #height=400
                                )






#                                    ____________________________________________________________________________
#                                     >>>>>>>>>>>>>>>>>>>>>>>>>>> POR ENTIDAD <<<<<<<<<<<<<<<<<<<<<<<<<<<<

#                               Tratamiento de la base de delitos de género (por estado)
d_vg.groupby(['Año','Entidad'])['Enero', 
                 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre',
       'Noviembre', 'Diciembre'].sum().to_csv("00.csv",  header=True)
fem= pd.read_csv("00.csv")
############################################### separación de años

year15= fem[fem.Año == 2015]
year16= fem[fem.Año == 2016]
year17= fem[fem.Año == 2017]
year18= fem[fem.Año == 2018]
year19= fem[fem.Año == 2019]
year20= fem[fem.Año == 2020]
year21= fem[fem.Año == 2021]

############################################### Agregar suffix de años

y15 = year15.add_suffix('15')
y15.rename(columns ={'Año15': 'Año', 'Entidad15': 'Entidad', 'Unnamed: 015' : 'Unnamed: 0',
                            'Entidad15': 'Entidad'}, inplace = True)

y16 = year16.add_suffix('16')
y16.rename(columns ={'Año16': 'Año', 'Entidad16': 'Entidad', 'Unnamed: 016' : 'Unnamed: 0',
                            'Entidad16': 'Entidad'}, inplace = True)

y17 = year17.add_suffix('17')
y17.rename(columns ={'Año17': 'Año', 'Entidad17': 'Entidad', 'Unnamed: 017' : 'Unnamed: 0',
                            'Entidad17': 'Entidad'}, inplace = True)

y18= year18.add_suffix('18')
y18.rename(columns ={'Año18': 'Año', 'Entidad18': 'Entidad','Unnamed: 018' : 'Unnamed: 0',
                            'Entidad18': 'Entidad'}, inplace = True)

y19= year19.add_suffix('19')
y19.rename(columns ={'Año19': 'Año', 'Entidad19': 'Entidad', 'Unnamed: 019' : 'Unnamed: 0',
                            'Entidad19': 'Entidad'}, inplace = True)

y20= year20.add_suffix('20')
y20.rename(columns ={'Año20': 'Año', 'Entidad20': 'Entidad','Unnamed: 020' : 'Unnamed: 0',
                            'Entidad20': 'Entidad'}, inplace = True)

y21= year21.add_suffix('21')
y21.rename(columns ={'Año21': 'Año', 'Entidad21': 'Entidad','Unnamed: 021' : 'Unnamed: 0',
                            'Entidad21': 'Entidad'}, inplace = True)


############################################### Concat todos los años

fa = y15.merge(y16, on="Entidad",  how="inner")
fb = fa.merge(y17, on="Entidad",  how="inner")
fc = fb.merge(y18, on="Entidad",  how="inner")
fd = fc.merge(y19, on="Entidad",  how="inner")
fe = fd.merge(y20, on="Entidad",  how="inner")
ff = fe.merge(y21, on="Entidad",  how="inner")
                      
femi15_21 = ff[[
 'Entidad','Enero15','Febrero15','Marzo15','Abril15','Mayo15','Junio15',
 'Julio15','Agosto15','Septiembre15','Octubre15','Noviembre15','Diciembre15',
 
 'Enero16','Febrero16','Marzo16','Abril16','Mayo16','Junio16','Julio16',
 'Agosto16','Septiembre16','Octubre16','Noviembre16','Diciembre16',

 'Enero17','Febrero17','Marzo17','Abril17','Mayo17','Junio17','Julio17',
 'Agosto17','Septiembre17','Octubre17','Noviembre17','Diciembre17',
    
 'Enero18','Febrero18','Marzo18','Abril18','Mayo18','Junio18','Julio18',
 'Agosto18','Septiembre18','Octubre18','Noviembre18','Diciembre18',
 
 'Enero19','Febrero19','Marzo19','Abril19','Mayo19','Junio19','Julio19',
 'Agosto19','Septiembre19','Octubre19','Noviembre19','Diciembre19',

 'Enero20','Febrero20','Marzo20','Abril20','Mayo20','Junio20','Julio20',
 'Agosto20','Septiembre20','Octubre20','Noviembre20','Diciembre20',

 'Enero21','Febrero21','Marzo21','Abril21','Mayo21',#'Junio21','Julio21',
 #'Agosto21','Septiembre21','Octubre21','Noviembre21','Diciembre21'
        ]]


##                               CRear columna de TOTAL ANUAL 
femi15_21['Total2015']= femi15_21[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               'Junio15', 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               'Noviembre15', 'Diciembre15',]].sum(axis=1)

#femi15_21['Total2015-21']= femi15_21[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               #'Junio15'#, 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               #'Noviembre15', 'Diciembre15',#
#                                     ]].sum(axis=1)

femi15_21['Total2016']= femi15_21[[ 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16',
                               'Junio16', 'Julio16', 'Agosto16', 'Septiembre16', 'Octubre16',
                               'Noviembre16', 'Diciembre16',]].sum(axis=1)
femi15_21['Total2017']= femi15_21[[ 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17',
                               'Junio17', 'Julio17', 'Agosto17', 'Septiembre17', 'Octubre17',
                               'Noviembre17', 'Diciembre17',]].sum(axis=1)
femi15_21['Total2018']= femi15_21[[ 'Enero18', 'Febrero18', 'Marzo18', 'Abril18', 'Mayo18',
                               'Junio18', 'Julio18', 'Agosto18', 'Septiembre18', 'Octubre18',
                               'Noviembre18', 'Diciembre18',]].sum(axis=1)
femi15_21['Total2019']= femi15_21[[ 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19',
                               'Junio19', 'Julio19', 'Agosto19', 'Septiembre19', 'Octubre19',
                               'Noviembre19', 'Diciembre19',]].sum(axis=1)
femi15_21['Total2020']= femi15_21[[ 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20',
                               'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               'Noviembre20', 'Diciembre20',]].sum(axis=1)
femi15_21['Total2021']= femi15_21[[ 'Enero21', 'Febrero21', 'Marzo21', 'Abril21', 'Mayo21',
                               #'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               #'Noviembre20', 'Diciembre20',
                                  ]].sum(axis=1)
femi15_21["GRAND TOTAL"]= femi15_21[["Total2015","Total2016","Total2017","Total2018","Total2019","Total2020",
                                    "Total2021",]].sum(axis=1)

#                                tasa anuales (2015-2021)
femi15_21["tasa_tot2015"] = ((femi15_21['Total2015']/121347800)*100000).round(1)
femi15_21["tasa_tot2016"] = ((femi15_21['Total2016']/122715165)*100000).round(1)
femi15_21["tasa_tot2017"] = ((femi15_21['Total2017']/124041731)*100000).round(1)
femi15_21["tasa_tot2018"] = ((femi15_21['Total2018']/125327797)*100000).round(1)
femi15_21["tasa_tot2019"] = ((femi15_21['Total2019']/126577691)*100000).round(1)
femi15_21["tasa_tot2020"] = ((femi15_21['Total2020']/127792286)*100000).round(1)
femi15_21["tasa_tot2021"] = ((femi15_21['Total2021']/128972439)*100000).round(1)
femi15_21["Variac_ABS2015_2021"] = (-(femi15_21["Total2015"]-femi15_21["Total2020"])).round(1)
femi15_21["Variac_tasa2015_2021"]= (-(femi15_21["tasa_tot2015"]-femi15_21["tasa_tot2020"])).round(1)


#                                variaciones mensuales mes.año-mes.año abs by estado
# Variaciones 2015-2016
femi15_21["var_ene15_16"] = femi15_21.Enero16 - femi15_21.Enero15
femi15_21["var_feb15_16"] = femi15_21.Febrero16 - femi15_21.Febrero15
femi15_21["var_mrz15_16"] = femi15_21.Marzo16 - femi15_21.Marzo15
femi15_21["var_abr15_16"] = femi15_21.Abril16 - femi15_21.Abril15
femi15_21["var_may15_16"] = femi15_21.Mayo16 - femi15_21.Mayo15
femi15_21["var_jun15_16"] = femi15_21.Junio16 - femi15_21.Junio15
femi15_21["var_jul15_16"] = femi15_21.Julio16 - femi15_21.Julio15
femi15_21["var_ago15_16"] = femi15_21.Agosto16 - femi15_21.Agosto15
femi15_21["var_sep15_16"] = femi15_21.Septiembre16 - femi15_21.Septiembre15
femi15_21["var_oct15_16"] = femi15_21.Octubre16 - femi15_21.Octubre15
femi15_21["var_nov15_16"] = femi15_21.Noviembre16 - femi15_21.Noviembre15
femi15_21["var_dic15_16"] = femi15_21.Diciembre16 - femi15_21.Diciembre15

# Variaciones 2016-2017
femi15_21["var_ene16_17"] = femi15_21.Enero17 - femi15_21.Enero16
femi15_21["var_feb16_17"] = femi15_21.Febrero17 - femi15_21.Febrero16
femi15_21["var_mrz16_17"] = femi15_21.Marzo17 - femi15_21.Marzo16
femi15_21["var_abr16_17"] = femi15_21.Abril17 - femi15_21.Abril16
femi15_21["var_may16_17"] = femi15_21.Mayo17 - femi15_21.Mayo16
femi15_21["var_jun16_17"] = femi15_21.Junio17 - femi15_21.Junio16
femi15_21["var_jul16_17"] = femi15_21.Julio17 - femi15_21.Julio16
femi15_21["var_ago16_17"] = femi15_21.Agosto17 - femi15_21.Agosto16
femi15_21["var_sep16_17"] = femi15_21.Septiembre17 - femi15_21.Septiembre16
femi15_21["var_oct16_17"] = femi15_21.Octubre17 - femi15_21.Octubre16
femi15_21["var_nov16_17"] = femi15_21.Noviembre17 - femi15_21.Noviembre16
femi15_21["var_dic16_17"] = femi15_21.Diciembre17 - femi15_21.Diciembre16

# Variaciones 2017-2018
femi15_21["var_ene17_18"] = femi15_21.Enero18 - femi15_21.Enero17
femi15_21["var_feb17_18"] = femi15_21.Febrero18 - femi15_21.Febrero17
femi15_21["var_mrz17_18"] = femi15_21.Marzo18 - femi15_21.Marzo17
femi15_21["var_abr17_18"] = femi15_21.Abril18 - femi15_21.Abril17
femi15_21["var_may17_18"] = femi15_21.Mayo18 - femi15_21.Mayo17
femi15_21["var_jun17_18"] = femi15_21.Junio18 - femi15_21.Junio17
femi15_21["var_jul17_18"] = femi15_21.Julio18 - femi15_21.Julio17
femi15_21["var_ago17_18"] = femi15_21.Agosto18 - femi15_21.Agosto17
femi15_21["var_sep17_18"] = femi15_21.Septiembre18 - femi15_21.Septiembre17
femi15_21["var_oct17_18"] = femi15_21.Octubre18 - femi15_21.Octubre17
femi15_21["var_nov17_18"] = femi15_21.Noviembre18 - femi15_21.Noviembre17
femi15_21["var_dic17_18"] = femi15_21.Diciembre18 - femi15_21.Diciembre17

# Variaciones 2018-2019
femi15_21["var_ene18_19"] = femi15_21.Enero19 - femi15_21.Enero18
femi15_21["var_feb18_19"] = femi15_21.Febrero19 - femi15_21.Febrero18
femi15_21["var_mrz18_19"] = femi15_21.Marzo19 - femi15_21.Marzo18
femi15_21["var_abr18_19"] = femi15_21.Abril19 - femi15_21.Abril18
femi15_21["var_may18_19"] = femi15_21.Mayo19 - femi15_21.Mayo18
femi15_21["var_jun18_19"] = femi15_21.Junio19 - femi15_21.Junio18
femi15_21["var_jul18_19"] = femi15_21.Julio19 - femi15_21.Julio18
femi15_21["var_ago18_19"] = femi15_21.Agosto19 - femi15_21.Agosto18
femi15_21["var_sep18_19"] = femi15_21.Septiembre19 - femi15_21.Septiembre18
femi15_21["var_oct18_19"] = femi15_21.Octubre19 - femi15_21.Octubre18
femi15_21["var_nov18_19"] = femi15_21.Noviembre19 - femi15_21.Noviembre18
femi15_21["var_dic18_19"] = femi15_21.Diciembre19 - femi15_21.Diciembre18

# Variaciones 2019-2020
femi15_21["var_ene19_20"] = femi15_21.Enero20 - femi15_21.Enero19
femi15_21["var_feb19_20"] = femi15_21.Febrero20 - femi15_21.Febrero19
femi15_21["var_mrz19_20"] = femi15_21.Marzo20 - femi15_21.Marzo19
femi15_21["var_abr19_20"] = femi15_21.Abril20 - femi15_21.Abril19
femi15_21["var_may19_20"] = femi15_21.Mayo20 - femi15_21.Mayo19
femi15_21["var_jun19_20"] = femi15_21.Junio20 - femi15_21.Junio19
femi15_21["var_jul19_20"] = femi15_21.Julio20 - femi15_21.Julio19
femi15_21["var_ago19_20"] = femi15_21.Agosto20 - femi15_21.Agosto19
femi15_21["var_sep19_20"] = femi15_21.Septiembre20 - femi15_21.Septiembre19
femi15_21["var_oct19_20"] = femi15_21.Octubre20 - femi15_21.Octubre19
femi15_21["var_nov19_20"] = femi15_21.Noviembre20 - femi15_21.Noviembre19
femi15_21["var_dic19_20"] = femi15_21.Diciembre20 - femi15_21.Diciembre19

# Variaciones 2020-2021
femi15_21["var_ene20_21"] = femi15_21.Enero21 - femi15_21.Enero20
femi15_21["var_feb20_21"] = femi15_21.Febrero21 - femi15_21.Febrero20
femi15_21["var_mrz20_21"] = femi15_21.Marzo21 - femi15_21.Marzo20
femi15_21["var_abr20_21"] = femi15_21.Abril21 - femi15_21.Abril20
femi15_21["var_may20_21"] = femi15_21.Mayo21 - femi15_21.Mayo20
#femi15_21["var_jun20_21"] = femi15_21.Junio21 - femi15_21.Junio20
#femi15_21["var_jul20_21"] = femi15_21.Julio21 - femi15_21.Julio20
#femi15_21["var_ago20_21"] = femi15_21.Agosto21 - femi15_21.Agosto20
#femi15_21["var_sep20_21"] = femi15_21.Septiembre21 - femi15_21.Septiembre20
#femi15_21["var_oct20_21"] = femi15_21.Octubre21 - femi15_21.Octubre20
#femi15_21["var_nov20_21"] = femi15_21.Noviembre21 - femi15_21.Noviembre20
#femi15_21["var_dic20_21"] = femi15_21.Diciembre21 - femi15_21.Diciembre20


#                                 variaciones mensuales seriadas (mismo año) by estado
# 2015
femi15_21["v_ene_feb_15"] = femi15_21.Febrero15 - femi15_21.Enero15
femi15_21["v_feb_mar_15"] = femi15_21.Marzo15 - femi15_21.Febrero15
femi15_21["v_mar_abr_15"] = femi15_21.Abril15 - femi15_21.Marzo15
femi15_21["v_abr_may_15"] = femi15_21.Mayo15 - femi15_21.Abril15
femi15_21["v_may_jun_15"] = femi15_21.Junio15 - femi15_21.Mayo15
femi15_21["v_jun_jul_15"] = femi15_21.Julio15 - femi15_21.Junio15
femi15_21["v_jul_ago_15"] = femi15_21.Agosto15 - femi15_21.Julio15
femi15_21["v_ago_sep_15"] = femi15_21.Septiembre15 - femi15_21.Agosto15
femi15_21["v_sep_oct_15"] = femi15_21.Octubre15 - femi15_21.Septiembre15
femi15_21["v_oct_nov_15"] = femi15_21.Noviembre15 - femi15_21.Octubre15
femi15_21["v_nov_dic_15"] = femi15_21.Diciembre15 - femi15_21.Noviembre15
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_15"] = femi15_21.Diciembre15 - femi15_21.Enero16

# 2016
femi15_21["v_ene_feb_16"] = femi15_21.Febrero16 - femi15_21.Enero16
femi15_21["v_feb_mar_16"] = femi15_21.Marzo16 - femi15_21.Febrero16
femi15_21["v_mar_abr_16"] = femi15_21.Abril16 - femi15_21.Marzo16
femi15_21["v_abr_may_16"] = femi15_21.Mayo16 - femi15_21.Abril16
femi15_21["v_may_jun_16"] = femi15_21.Junio16 - femi15_21.Mayo16
femi15_21["v_jun_jul_16"] = femi15_21.Julio16 - femi15_21.Junio16
femi15_21["v_jul_ago_16"] = femi15_21.Agosto16 - femi15_21.Julio16
femi15_21["v_ago_sep_16"] = femi15_21.Septiembre16 - femi15_21.Agosto16
femi15_21["v_sep_oct_16"] = femi15_21.Octubre16 - femi15_21.Septiembre16
femi15_21["v_oct_nov_16"] = femi15_21.Noviembre16 - femi15_21.Octubre16
femi15_21["v_nov_dic_16"] = femi15_21.Diciembre16 - femi15_21.Noviembre16
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_16"] = femi15_21.Diciembre16 - femi15_21.Enero17

# 2017
femi15_21["v_ene_feb_17"] = femi15_21.Febrero17 - femi15_21.Enero17
femi15_21["v_feb_mar_17"] = femi15_21.Marzo17 - femi15_21.Febrero17
femi15_21["v_mar_abr_17"] = femi15_21.Abril17 - femi15_21.Marzo17
femi15_21["v_abr_may_17"] = femi15_21.Mayo17 - femi15_21.Abril17
femi15_21["v_may_jun_17"] = femi15_21.Junio17 - femi15_21.Mayo17
femi15_21["v_jun_jul_17"] = femi15_21.Julio17 - femi15_21.Junio17
femi15_21["v_jul_ago_17"] = femi15_21.Agosto17 - femi15_21.Julio17
femi15_21["v_ago_sep_17"] = femi15_21.Septiembre17 - femi15_21.Agosto17
femi15_21["v_sep_oct_17"] = femi15_21.Octubre17 - femi15_21.Septiembre17
femi15_21["v_oct_nov_17"] = femi15_21.Noviembre17 - femi15_21.Octubre17
femi15_21["v_nov_dic_17"] = femi15_21.Diciembre17 - femi15_21.Noviembre17
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_17"] = femi15_21.Diciembre17 - femi15_21.Enero18

# 2018
femi15_21["v_ene_feb_18"] = femi15_21.Febrero18 - femi15_21.Enero18
femi15_21["v_feb_mar_18"] = femi15_21.Marzo18 - femi15_21.Febrero18
femi15_21["v_mar_abr_18"] = femi15_21.Abril18 - femi15_21.Marzo18
femi15_21["v_abr_may_18"] = femi15_21.Mayo18 - femi15_21.Abril18
femi15_21["v_may_jun_18"] = femi15_21.Junio18 - femi15_21.Mayo18
femi15_21["v_jun_jul_18"] = femi15_21.Julio18 - femi15_21.Junio18
femi15_21["v_jul_ago_18"] = femi15_21.Agosto18 - femi15_21.Julio18
femi15_21["v_ago_sep_18"] = femi15_21.Septiembre18 - femi15_21.Agosto18
femi15_21["v_sep_oct_18"] = femi15_21.Octubre18 - femi15_21.Septiembre18
femi15_21["v_oct_nov_18"] = femi15_21.Noviembre18 - femi15_21.Octubre18
femi15_21["v_nov_dic_18"] = femi15_21.Diciembre18 - femi15_21.Noviembre18
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_18"] = femi15_21.Diciembre18 - femi15_21.Enero19

# 2019
femi15_21["v_ene_feb_19"] = femi15_21.Febrero19 - femi15_21.Enero19
femi15_21["v_feb_mar_19"] = femi15_21.Marzo19 - femi15_21.Febrero19
femi15_21["v_mar_abr_19"] = femi15_21.Abril19 - femi15_21.Marzo19
femi15_21["v_abr_may_19"] = femi15_21.Mayo19 - femi15_21.Abril19
femi15_21["v_may_jun_19"] = femi15_21.Junio19 - femi15_21.Mayo19
femi15_21["v_jun_jul_19"] = femi15_21.Julio19 - femi15_21.Junio19
femi15_21["v_jul_ago_19"] = femi15_21.Agosto19 - femi15_21.Julio19
femi15_21["v_ago_sep_19"] = femi15_21.Septiembre19 - femi15_21.Agosto19
femi15_21["v_sep_oct_19"] = femi15_21.Octubre19 - femi15_21.Septiembre19
femi15_21["v_oct_nov_19"] = femi15_21.Noviembre19 - femi15_21.Octubre19
femi15_21["v_nov_dic_19"] = femi15_21.Diciembre19 - femi15_21.Noviembre19
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_19"] = femi15_21.Diciembre19 - femi15_21.Enero20

# 2020
femi15_21["v_ene_feb_20"] = femi15_21.Febrero20 - femi15_21.Enero20
femi15_21["v_feb_mar_20"] = femi15_21.Marzo20 - femi15_21.Febrero20
femi15_21["v_mar_abr_20"] = femi15_21.Abril20 - femi15_21.Marzo20
femi15_21["v_abr_may_20"] = femi15_21.Mayo20 - femi15_21.Abril20
femi15_21["v_may_jun_20"] = femi15_21.Junio20 - femi15_21.Mayo20
femi15_21["v_jun_jul_20"] = femi15_21.Julio20 - femi15_21.Junio20
femi15_21["v_jul_ago_20"] = femi15_21.Agosto20 - femi15_21.Julio20
femi15_21["v_ago_sep_20"] = femi15_21.Septiembre20 - femi15_21.Agosto20
femi15_21["v_sep_oct_20"] = femi15_21.Octubre20 - femi15_21.Septiembre20
femi15_21["v_oct_nov_20"] = femi15_21.Noviembre20 - femi15_21.Octubre20
femi15_21["v_nov_dic_20"] = femi15_21.Diciembre20 - femi15_21.Noviembre20
#variacion Diciembre-Enero 
femi15_21["v_dic_ene_20"] = femi15_21.Diciembre20 - femi15_21.Enero21

# 2021
femi15_21["v_ene_feb_21"] = femi15_21.Febrero21 - femi15_21.Enero21
femi15_21["v_feb_mar_21"] = femi15_21.Marzo21 - femi15_21.Febrero21
femi15_21["v_mar_abr_21"] = femi15_21.Abril21 - femi15_21.Marzo21
femi15_21["v_abr_may_21"] = femi15_21.Mayo21 - femi15_21.Abril21
#femi15_21["v_may_jun_21"] = femi15_21.Junio21 - femi15_21.Mayo21
#femi15_21["v_jun_jul_21"] = femi15_21.Julio21 - femi15_21.Junio21
#femi15_21["v_jul_ago_21"] = femi15_21.Agosto21 - femi15_21.Julio21
#femi15_21["v_ago_sep_21"] = femi15_21.Septiembre21 - femi15_21.Agosto21
#femi15_21["v_sep_oct_21"] = femi15_21.Octubre21 - femi15_21.Septiembre21
#femi15_21["v_oct_nov_21"] = femi15_21.Noviembre21 - femi15_21.Octubre21
#femi15_21["v_nov_dic_21"] = femi15_21.Diciembre21 - femi15_21.Noviembre21
#variacion Diciembre-Enero (si llegamos...)
#femi15_21["v_dic_ene_21"] = femi15_21.Diciembre21 - femi15_21.Enero22


#                                 variaciones anuales by estado
femi15_21["var_1516"] = femi15_21.Total2016 - femi15_21.Total2015
femi15_21["var_1617"] = femi15_21.Total2017 - femi15_21.Total2016
femi15_21["var_1718"] = femi15_21.Total2018 - femi15_21.Total2017
femi15_21["var_1819"] = femi15_21.Total2019 - femi15_21.Total2018
femi15_21["var_1920"] = femi15_21.Total2020 - femi15_21.Total2019
femi15_21["var_2021"] = femi15_21.Total2021 - femi15_21.Total2020


#                                 variaciones porcentuales mensuales by estado
# Variaciones 2015-2016
femi15_21["var_ene15_16_%"] = (femi15_21["var_ene15_16"]*100)/femi15_21.Enero16
femi15_21["var_feb15_16_%"] = (femi15_21["var_feb15_16"]*100)/femi15_21.Febrero16
femi15_21["var_mrz15_16_%"] = (femi15_21["var_mrz15_16"]*100)/femi15_21.Marzo16
femi15_21["var_abr15_16_%"] = (femi15_21["var_abr15_16"]*100)/femi15_21.Abril16
femi15_21["var_may15_16_%"] = (femi15_21["var_may15_16"]*100)/femi15_21.Mayo16
femi15_21["var_jun15_16_%"] = (femi15_21["var_jun15_16"]*100)/femi15_21.Junio16
femi15_21["var_jul15_16_%"] = (femi15_21["var_jul15_16"]*100)/femi15_21.Julio16
femi15_21["var_ago15_16_%"] = (femi15_21["var_ago15_16"]*100)/femi15_21.Agosto16
femi15_21["var_sep15_16_%"] = (femi15_21["var_sep15_16"]*100)/femi15_21.Septiembre16
femi15_21["var_oct15_16_%"] = (femi15_21["var_oct15_16"]*100)/femi15_21.Octubre16
femi15_21["var_nov15_16_%"] = (femi15_21["var_nov15_16"]*100)/femi15_21.Noviembre16
femi15_21["var_dic15_16_%"] = (femi15_21["var_dic15_16"]*100)/femi15_21.Diciembre16

# Variaciones 2016-2017
femi15_21["var_ene16_17_%"] = (femi15_21["var_ene16_17"]*100)/femi15_21.Enero17
femi15_21["var_feb16_17_%"] = (femi15_21["var_feb16_17"]*100)/femi15_21.Febrero17
femi15_21["var_mrz16_17_%"] = (femi15_21["var_mrz16_17"]*100)/femi15_21.Marzo17
femi15_21["var_abr16_17_%"] = (femi15_21["var_abr16_17"]*100)/femi15_21.Abril17
femi15_21["var_may16_17_%"] = (femi15_21["var_may16_17"]*100)/femi15_21.Mayo17
femi15_21["var_jun16_17_%"] = (femi15_21["var_jun16_17"]*100)/femi15_21.Junio17
femi15_21["var_jul16_17_%"] = (femi15_21["var_jul16_17"]*100)/femi15_21.Julio17
femi15_21["var_ago16_17_%"] = (femi15_21["var_ago16_17"]*100)/femi15_21.Agosto17
femi15_21["var_sep16_17_%"] = (femi15_21["var_sep16_17"]*100)/femi15_21.Septiembre17
femi15_21["var_oct16_17_%"] = (femi15_21["var_oct16_17"]*100)/femi15_21.Octubre17
femi15_21["var_nov16_17_%"] = (femi15_21["var_nov16_17"]*100)/femi15_21.Noviembre17
femi15_21["var_dic16_17_%"] = (femi15_21["var_dic16_17"]*100)/femi15_21.Diciembre17

# Variaciones 2017-2018
femi15_21["var_ene17_18_%"] = (femi15_21["var_ene17_18"]*100)/femi15_21.Enero18
femi15_21["var_feb17_18_%"] = (femi15_21["var_feb17_18"]*100)/femi15_21.Febrero18
femi15_21["var_mrz17_18_%"] = (femi15_21["var_mrz17_18"]*100)/femi15_21.Marzo18
femi15_21["var_abr17_18_%"] = (femi15_21["var_abr17_18"]*100)/femi15_21.Abril18
femi15_21["var_may17_18_%"] = (femi15_21["var_may17_18"]*100)/femi15_21.Mayo18
femi15_21["var_jun17_18_%"] = (femi15_21["var_jun17_18"]*100)/femi15_21.Junio18
femi15_21["var_jul17_18_%"] = (femi15_21["var_jul17_18"]*100)/femi15_21.Julio18
femi15_21["var_ago17_18_%"] = (femi15_21["var_ago17_18"]*100)/femi15_21.Agosto18
femi15_21["var_sep17_18_%"] = (femi15_21["var_sep17_18"]*100)/femi15_21.Septiembre18
femi15_21["var_oct17_18_%"] = (femi15_21["var_oct17_18"]*100)/femi15_21.Octubre18
femi15_21["var_nov17_18_%"] = (femi15_21["var_nov17_18"]*100)/femi15_21.Noviembre18
femi15_21["var_dic17_18_%"] = (femi15_21["var_dic17_18"]*100)/femi15_21.Diciembre18

# Variaciones 2018-2019
femi15_21["var_ene18_19_%"] = (femi15_21["var_ene18_19"]*100)/femi15_21.Enero19
femi15_21["var_feb18_19_%"] = (femi15_21["var_feb18_19"]*100)/femi15_21.Febrero19
femi15_21["var_mrz18_19_%"] = (femi15_21["var_mrz18_19"]*100)/femi15_21.Marzo19
femi15_21["var_abr18_19_%"] = (femi15_21["var_abr18_19"]*100)/femi15_21.Abril19
femi15_21["var_may18_19_%"] = (femi15_21["var_may18_19"]*100)/femi15_21.Mayo19
femi15_21["var_jun18_19_%"] = (femi15_21["var_jun18_19"]*100)/femi15_21.Junio19
femi15_21["var_jul18_19_%"] = (femi15_21["var_jul18_19"]*100)/femi15_21.Julio19
femi15_21["var_ago18_19_%"] = (femi15_21["var_ago18_19"]*100)/femi15_21.Agosto19
femi15_21["var_sep18_19_%"] = (femi15_21["var_sep18_19"]*100)/femi15_21.Septiembre19
femi15_21["var_oct18_19_%"] = (femi15_21["var_oct18_19"]*100)/femi15_21.Octubre19
femi15_21["var_nov18_19_%"] = (femi15_21["var_nov18_19"]*100)/femi15_21.Noviembre19
femi15_21["var_dic18_19_%"] = (femi15_21["var_dic18_19"]*100)/femi15_21.Diciembre19

# Variaciones 2019-20120
femi15_21["var_ene19_20_%"] = (femi15_21["var_ene19_20"]*100)/femi15_21.Enero20
femi15_21["var_feb19_20_%"] = (femi15_21["var_feb19_20"]*100)/femi15_21.Febrero20
femi15_21["var_mrz19_20_%"] = (femi15_21["var_mrz19_20"]*100)/femi15_21.Marzo20
femi15_21["var_abr19_20_%"] = (femi15_21["var_abr19_20"]*100)/femi15_21.Abril20
femi15_21["var_may19_20_%"] = (femi15_21["var_may19_20"]*100)/femi15_21.Mayo20
femi15_21["var_jun19_20_%"] = (femi15_21["var_jun19_20"]*100)/femi15_21.Junio20
femi15_21["var_jul19_20_%"] = (femi15_21["var_jul19_20"]*100)/femi15_21.Julio20
femi15_21["var_ago19_20_%"] = (femi15_21["var_ago19_20"]*100)/femi15_21.Agosto20
femi15_21["var_sep19_20_%"] = (femi15_21["var_sep19_20"]*100)/femi15_21.Septiembre20
femi15_21["var_oct19_20_%"] = (femi15_21["var_oct19_20"]*100)/femi15_21.Octubre20
femi15_21["var_nov19_20_%"] = (femi15_21["var_nov19_20"]*100)/femi15_21.Noviembre20
femi15_21["var_dic19_20_%"] = (femi15_21["var_dic19_20"]*100)/femi15_21.Diciembre20

# Variaciones 2020-2021
femi15_21["var_ene20_21_%"] = (femi15_21["var_ene20_21"]*100)/femi15_21.Enero21
femi15_21["var_feb20_21_%"] = (femi15_21["var_feb20_21"]*100)/femi15_21.Febrero21
femi15_21["var_mrz20_21_%"] = (femi15_21["var_mrz20_21"]*100)/femi15_21.Marzo21
femi15_21["var_abr20_21_%"] = (femi15_21["var_abr20_21"]*100)/femi15_21.Abril21
femi15_21["var_may20_21_%"] = (femi15_21["var_may20_21"]*100)/femi15_21.Mayo21
#femi15_21["var_jun20_21_%"] = (femi15_21["var_jun20_21"]*100)/femi15_21.Junio21
#femi15_21["var_jul20_21_%"] = (femi15_21["var_jul20_21"]*100)/femi15_21.Julio21
#femi15_21["var_ago20_21_%"] = (femi15_21["var_ago20_21"]*100)/femi15_21.Agosto21
#femi15_21["var_sep20_21_%"] = (femi15_21["var_sep20_21"]*100)/femi15_21.Septiembre21
#femi15_21["var_oct20_21_%"] = (femi15_21["var_oct20_21"]*100)/femi15_21.Octubre21
#femi15_21["var_nov20_21_%"] = (femi15_21["var_nov20_21"]*100)/femi15_21.Noviembre21
#femi15_21["var_dic20_21_%"] = (femi15_21["var_dic20_21"]*100)/femi15_21.Diciembre21






##os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\code\Dash\feminicidios")
#geo_df=gpd.read_file('México_Estados.shp')
#
#geo_df.replace(['Coahuila','Distrito Federal','Michoacán',"Veracruz"],
#               #por
#               ['Coahuila de Zaragoza','Ciudad de México','Michoacán de Ocampo','Veracruz de Ignacio de la Llave'],
#               inplace=True, )
#
#concat1 = geo_df.merge(femi15_21,
#                           left_on= "ESTADO",
#                           right_on="Entidad", how= "right").sort_values("GRAND TOTAL", ascending=False)
#
#fig = concat1.plot("GRAND TOTAL",
#                 cmap= "Oranges",
#                 legend=False,
#                 k=5,
#                 scheme= 'quantiles',
#                 linewidth=.6, 
#                 edgecolor= "white", 
#                 categorical=False,
#                 figsize=(5,5),)
##plt.axis("off")

# Ruta guardado
#os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_actualizacion\resultados\') #__Ruta Fe
#os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\Project_portadaVG\resultados') #____Ruta Wi
#os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')      #______________Ruta Ae

#plt.savefig("Mapa GRAND TOTAL.png", dpi= 300)
#print("Guardado GRAND TOTAL")
#plt.show()



# 1. separar los dos filtros y subirlos a GITHUB
# 2. hacer los 7 mapas sumas anuales (2015-2021)
# 3. hacer los 7 mapas tasas anuales (2015-2021) 
# 4. Hacer 2 mapas uno con GRAND TOTAL y otro con GRAND TASA









############################################################### GRAFICA TREEMAP

# GRAFICA COLORES
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
                  uniformtext_minsize=8,
                  uniformtext_mode='hide',
                  title_font_size = 4,
                  font_color="white",
                  title_font_family="Arial",
                  title_font_color="white",
                  margin = dict(autoexpand=False,
                              l=0, r=0, t=0, b=0),
                  showlegend=False,
                  #autosize=True,
                  width=650,
                  height=530    
                    ),
treedel.update_traces(marker=dict(colors=colors, line=dict(color='lightgray', width=.5)
                                        )
                              # marker=dict(#colors=colors)
)

#treedel.show()


################################################
# A P P 
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
                  width={'size': 3, 'offset': 0, "font-family": "Arial",}),
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
                           "color": "purple", 
                          "text-shadow": "10px 20px 30px black",}),
                  html.P(["17 delitos vinculados con la violencia de género reunieron "+ totaldvg +" incidencias " 
                          " entre 2015 hasta 2021."
                          "Es decir, un retrato que representa 15.5 %  del total de la incidencia"
                          " nacional. Aquí presentamos un análisis pormenorizado"
                          "de este fenómeno que requiere de la mayor atención posible. Esta información se actualiza "
                          "mensualmente, igualmente que nuestra fuente, el Secretariado Ejecutivo del Sistema Naconal de "
                          "Seguridad Pública",
                 ],style={'textAlign': 'justify',
                             "font-size": "18px",
                             "font-family": "Arial",
                           "color": "black",
                            "line-height":"120%",                            
                            "margin-left": "100px",
                            "margin-right": "100px",}
                          #"text-shadow": "10px 20px 30px black",
                      )])
         
                            ]),
                       
                       
       
    
   html.Br(),
   html.Br(),
   html.Br(),
   dbc.Row(
           [
               dbc.Col(html.P(["¿Cuáles delitos de género tienen mayor incidencia? " ],
                      style={"color": "purple", 
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
 
    html.Br(),
    html.Br(),
    html.Br(),
 
    
    ######## TABLA RANKING
    ################################################################# PRIMERA COLUMNA
    dbc.Button(([html.P("Tipo de delito", style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-weight": "bold",         
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }), 
                 html.P(tipodel1,#f"{int(num_zm):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "18px",
                               "font-weight": "bold",                                     
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel2,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel3,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel4,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel5,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel6,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),

#delito 7                 
                 html.P(tipodel7,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel8,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel9,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel10,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel11,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(tipodel12,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),

#delito 13                 
                 html.P(tipodel13,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel14,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel15,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
      html.P(tipodel16,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(tipodel17,#f"{int(num_zm):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
 #                html.P(tipodel18,#f"{int(num_zm):,}",  
 #                       style={
 #                              "color": "black", 
 #                              "font-size": "14px",
 #                              "font-family": "Arial",
 #                              "text-align": "right",
 #                           "line-height":"70%"                            
 #                       }),
                   
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '100px',
                 #"height":"140px" 
                 } ,disabled=True),

    
    
    
    
    #################################################################SEGUNDA COLUMNA
    dbc.Button(([html.P("Totales", style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-weight": "bold", 
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }), 
                 html.P(f"{int(totdel1):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "18px",
                               "font-weight": "bold", 
                               "font-family": "Arial",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel2):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel3):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel4):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel5):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel6):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),

                 html.P(f"{int(totdel7):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "14px",
                               "font-family": "Arial",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel8):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel9):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel10):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel11):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(totdel12):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                 
                 html.P(f"{int(totdel13):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel14):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel15):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"                            
                        }),
                    html.P(f"{int(totdel16):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                            "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(totdel17):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                               "widht":"100px",
                            "line-height":"70%"
                        }),
  #               html.P(f"{int(totdel18):,}",  
  #                      style={
  #                             "color": "black", 
  #                             "font-size": "14px",
  #                             "font-family": "Arial",
  #                             "text-align": "right",
  #                             "widht":"100px",
  #                          "line-height":"70%"                            
  #                      }),
                
       ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '5px',
                 } ,disabled=True),

    
    
    
    
    
    #################################################################TERCERA COLUMNA
    dbc.Button(([html.P("Tasa*", style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-weight": "bold", 
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }), 
                 html.P(f"{int(tasatotdel1):,}",  
                        style={
                               "color": "Purple", 
                               "font-size": "18px",
                               "font-weight": "bold", 
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel2):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel3):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel4):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel5):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel6):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),

                 html.P(f"{int(tasatotdel7):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                            "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel8):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"
                        }),
                 html.P(f"{int(tasatotdel9):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel10):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel11):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel12):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel13):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel14):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel15):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                     html.P(f"{int(tasatotdel16):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
                 html.P(f"{int(tasatotdel17):,}",  
                        style={
                               "color": "black", 
                               "font-size": "14px",
                               "font-family": "Arial",
                               "text-align": "right",
                            "line-height":"70%"                            
                        }),
 #                html.P(f"{int(tasatotdel18):,}",  
 #                       style={
 #                              "color": "black", 
 #                              "font-size": "14px",
 #                              "font-family": "Arial",
 #                              "text-align": "right",
 #                           "line-height":"70%"                            
 #                       }),
 #                

                 
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
                  'margin-left': '670px',
                 "width":"520px",
     "margin-top":"-550px"
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
                               "font-size": "14px",
                               "font-family": "Arial",        
                               #"text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                      )]),
 

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    
    
    
####### SECCION ICONOS
 ####################################################### ROW 1 (6 DELITOS)             
    
  dbc.Row(
           [
               dbc.Col(html.P(["17 dashboard analíticos" ],
                      style={"color": "Purple", 
                               #"font-weight": 'bold',
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px black",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )]),

    html.Br(),
    html.Br(),
   
    
 dbc.Row(
           [
  dbc.Col(html.P(["Enseguida se puede acceder a 17 dashboards analíticos, organizados  de mayor a menor tasa"
                  " de incidencia por cada 100 mil habitantes. En la primera línea, se encuentra   "
                  " la incidencia con tasas de "
                 + str(tasatotdel1)+ " a " + str (tasatotdel6)+" delitos (100k/hab). En la segunda línea,"
                  " se encuentra la incidencia con tasas de " 
                  +str(tasatotdel7)+ " a " + str (tasatotdel12)+" delitos (100k/hab). Finalmente, en la"
                  " tercera línea se encuentra la incidencia con tasas de "
                  +str(tasatotdel13)+ " a " + str (tasatotdel17)+ " delitos.",
                 ],style={'textAlign': 'justify',
                             "font-size": "18px",
                             "font-family": "Arial",
                           "color": "black",
                            "line-height":"120%",                            
                            "margin-left": "100px",
                            "margin-right": "100px",}
                          #"text-shadow": "10px 20px 30px black",
                      )),

 ]),
                   
        ################################# VIOLENCIA FAMILIAR
html.Br(),
    html.Br(),
   
    
  dbc.Row(
           [
               dbc.Col(

                   
                   
        ################################# VIOLENCIA FAMILIAR
        dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel1, 
                                           href=urldel1,
                       # href="https://violenciafamiliar.herokuapp.com/",
                        ), 
                        style={#'size': 2, 
                               "margin-left": "-30px",
                               "margin-right": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                             "font-weight": "bold",                                
                            "font-color": "white",
                              "text-shadow": "10px 20px 30px gray",})]),
        html.A([
        html.Img(src=iconodel1,
                        style={#'height' : '170px',
                    'width' : '90px',
                  #  'float' : 'center' ,
                            
                    #"margin-left":"100px"
                              })],
            href=urldel1,
            
     
                 # href="https://violenciafamiliar.herokuapp.com/", 
                  ),
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '100px',
                                "width":"180px", 
                                "height":"250px"
                 } ,disabled=True)),


               
       ################################# NO ASISTENCIA FAMILIAR
       dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel2, 
                                           href=urldel2,
                       # href="https://delncumplimientoviofam.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                               "margin-left": "-30px",
                               "margin-right": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
        html.A([
        html.Img(src=iconodel2,
                        style={#'height' : '150px',
                    'width' : '65px',
                    #'float' : 'center' ,
                  #  "margin-left":"-30px"
                              })],
            href=urldel2,
                 # href="https://delncumplimientoviofam.herokuapp.com/", 
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  #'margin-left': '100px',
                                "width":"180px", 
                                "height":"250px"
                 } ,disabled=True)),
               

               
       ################################# ABUSO SEXUAL 
       dbc.Col( #3
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel3, 
                                           href=urldel3,
                      #  href="https://abusosexual.herokuapp.com/"
                                          ), 
                        style={#'size': 2, 
                               #"margin-left": "-30px",
                               #"margin-right": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
        html.A([
        html.Img(src=iconodel3,
                        style={#'height' : '150px',
                    'width' : '60px',
                    #'float' : 'center' ,
                  #  "margin-left":"-30px"
                              })],
               #   href="https://abusosexual.herokuapp.com/", 
            href=urldel3,
                  ),
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
               #   'margin-left': '105px',
                                "width":"180px", 
                                "height":"250px"
                 } ,disabled=True)),
               

               
       ################################# Contra libertad personal 
       dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel4, 
                                           href=urldel4,
                        #href="https://delitovslibertadpersonal.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                               "margin-left": "-50px",
                               "margin-right": "-50px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
        html.A([
        html.Img(src=iconodel4,
                        style={#'height' : '150px',
                    'width' : '30px',
                    #'float' : 'center' ,
                  #  "margin-left":"-30px"
                              })],
            href=urldel4,
                 # href="https://delitovslibertadpersonal.herokuapp.com/", 
                  ),
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"250px"
                 } ,disabled=True)),
               
               
               

               
       ################################# Violaciónes 
       dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel5, 
                       href=urldel5,
                                           #href="https://violaciones.herokuapp.com/"
                                          ),
                        #active="exact"), 
                        style={#'size': 2, 
                               "margin-left": "-10px",
                               "margin-right": "-30px",  
                               "font-family": "Arial",
                               #'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
       html.A([
       html.Img(src=iconodel5,
                        style={#'height' : '150px',
                    'width' : '30px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
           href=urldel5,
                #  href="https://violaciones.herokuapp.com/", 
                  ),
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-right': '10px',
                                "width":"180px", 
                                "height":"250px"
                 } ,disabled=True)),
               
               

               
       ################################# Contra la familia 
                 dbc.Col(
     dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel6, 
                                           href=urldel6,
                       # href="https://delitovslafamilia.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                               "margin-left": "-30px",
                               "margin-right": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
            
        html.A([
        html.Img(src=iconodel6,
                        style={#'height' : '150px',
                    'width' : '70px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
            href=urldel6,
                  #href="https://delitovslafamilia.herokuapp.com/", 
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-right': '60px',
                                "width":"180px", 
                                "height":"250px"
                 } ,disabled=True))]),
        html.Br(),
               html.Br(),
               html.Br(),
       

    
    
    
    
 #### SECCION ICON   
 ####################################################### ROW 2 (6 DELITOS)             
       dbc.Row(
           [

       dbc.Col(

       #################################Contra integridad corporal 
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel7, 
                                           style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel7,
                       # href="https://delitootrosatentacontralavida.herokuapp.com/"
                                          ), 
                       )]),
            
        html.A([
        html.Img(src=iconodel7,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
            href=urldel7,
                #  href="https://delitootrosatentacontralavida.herokuapp.com/", 
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '100px',
                                "width":"180px", 
                                "height":"160px"
                 } ,disabled=True)),


               
       ################################# Contra seguridad sexual
                 dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel8, style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel8,
                    
                        ), 
                        style={#'size': 2, 
                               })]),
        html.A([
        html.Img(src=iconodel8,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
            href=urldel8,
      
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"160px"
                 } ,disabled=True)),

               
               
       ################################# POR DEFINIR 1
               
       dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel9, # BORRAR                                           
                                            style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel9,
 
#Aqui cambiar                    href="https://acososexual.herokuapp.com/",
                        ))]),
        html.A([
        html.Img(src=iconodel9,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
            href=urldel9,
                 # href="https://violaciones.herokuapp.com/", 
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"160px"
                 } ,disabled=True)),

               
               
       ################################# POR DEFINIR 2
       dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel10,  style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel10,
                      #  href="https://vgdistintavfam.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                          #     "margin-left": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
            
        html.A([
        html.Img(src=iconodel10,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
                #  href="https://vgdistintavfam.herokuapp.com/", 
            href=urldel10,
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"160px"
                 } ,disabled=True)),

               
               
               
       ################################# POR DEFINIR 3
                           dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel11,  style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel11,
                      #  href="https://delitocorrupciondemenores.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                          #     "margin-left": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
            
        html.A([
        html.Img(src=iconodel11,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
                 # href="https://delitocorrupciondemenores.herokuapp.com/",
            href=urldel11,
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"160px"
                 } ,disabled=True)),
               
               
       ################################# POR DEFINIR 4
                           dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel12,  style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                  "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel12,
                      # href="https://delitocorrupciondemenores.herokuapp.com/",
                        active="exact"),  
                        style={#'size': 2, 
                          #     "margin-left": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
            
        html.A([
        html.Img(src=iconodel12,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
            href=urldel12,
                 # href="https://delitocorrupciondemenores.herokuapp.com/", 
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-right': '60px',
                                "width":"180px", 
                                "height":"160px"
                 } ,disabled=True)),
               
               
        ]),
               
               
               
               
               
      html.Br(),
               html.Br(),
               html.Br(),
               html.Br(),
               html.Br(),
 #### SECCION ICON   
 ####################################################### ROW 3 (6 DELITOS)             
               
               
               
  dbc.Row(
           [
               
       ################################# POR DEFINIR 1 ROW 3
               
                           dbc.Col(
     dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel13,  style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel13,
                       
                        active="exact"), 
                        style={#'size': 2, 
                             })]),
            
        html.A([
        html.Img(src=iconodel13,
                        style={#'height' : '150px',
                    'width' : '80px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
               
            href=urldel13,
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                  'margin-left': '100px',
                                "width":"180px", 
                                "height":"140px"
                 } ,disabled=True)),
               

               
               
               
      dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel14, style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel14,
                    
                        ), 
                        style={#'size': 2, 
                               })]),
        html.A([
        html.Img(src=iconodel14,
                        style={#'height' : '150px',
                    'width' : '40px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
            href=urldel14,
      
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"140px"
                 } ,disabled=True)),

               
               
       ################################# POR DEFINIR 1
               
       dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel15, # BORRAR                                           
                                            style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel15,
 
#Aqui cambiar                    href="https://acososexual.herokuapp.com/",
                        ))]),
        html.A([
        html.Img(src=iconodel15,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
            href=urldel15,
                 # href="https://violaciones.herokuapp.com/", 
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"140px"
                 } ,disabled=True)),

               
               
       ################################# POR DEFINIR 2
       dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel16,  style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel16,
                      #  href="https://vgdistintavfam.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                          #     "margin-left": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
            
        html.A([
        html.Img(src=iconodel16,
                        style={#'height' : '150px',
                    'width' : '60px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
                #  href="https://vgdistintavfam.herokuapp.com/", 
            href=urldel16,
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"140px"
                 } ,disabled=True)),

               
               
               
       ################################# POR DEFINIR 3
                           dbc.Col(
       dbc.Button(([
            dbc.Nav([
                   dbc.NavLink(dbc.NavLink(tipodel17,  style={"font-size": 5, 
                                                  "line-height":"120%", 
                                                  "font-family": "Arial",
                                                  "width": "200px",
                                                  "font-size": 12,  
                                                  "text-align":"center",
                                                   "margin-left": "-50px",
                                                   "margin-right": "-50px",  
                                                   "margin-top": "-40px"
                                                 },
                                           href=urldel17,
                      #  href="https://delitocorrupciondemenores.herokuapp.com/",
                        active="exact"), 
                        style={#'size': 2, 
                          #     "margin-left": "-30px",  
                               "font-family": "Arial",
                               'float' : 'center' ,
                               "font-size": 15, 
                               "color": "lightsalmon",
                              "text-shadow": "10px 20px 30px gray",})]),
            
        html.A([
        html.Img(src=iconodel17,
                        style={#'height' : '150px',
                    'width' : '50px',
                    #'float' : 'center' ,
                   # "margin-left":"-30px"
                              })],
                 # href="https://delitocorrupciondemenores.herokuapp.com/",
            href=urldel17,
                  ),
    
                      ]),style={ "background-color": "light",
                  "box-shadow": "10px 20px 30px gray",
                 # 'margin-left': '105px',
                                "width":"180px", 
                                "height":"140px"
                 } ,disabled=True)),
               
               
#       ################################# POR DEFINIR 4
#                           dbc.Col(
#       dbc.Button(([
#            dbc.Nav([
#                   dbc.NavLink(dbc.NavLink(tipodel18,  style={"font-size": 5, 
#                                                  "line-height":"120%", 
#                                                  "font-family": "Arial",
#                                                  "width": "200px",
#                                                  "font-size": 12,  
#                                                  "text-align":"center",
#                                                   "margin-left": "-10px",
#                                                   "margin-right": "-10px",  
#                                                   "margin-top": "-40px"
#                                                 },
#                                           href=urldel18,
#                      # href="https://delitocorrupciondemenores.herokuapp.com/",
#                        active="exact"), 
#                        style={#'size': 2, 
#                          #     "margin-left": "-30px",  
#                               "font-family": "Arial",
#                               #'float' : 'center' ,
#                               "font-size": 15, 
#                               "color": "lightsalmon",
#                              "text-shadow": "10px 20px 30px gray",})]),
#            
#        html.A([
#        html.Img(src=iconodel18,
#                        style={#'height' : '150px',
#                    'width' : '30px',
#                    #'float' : 'center' ,
#                   # "margin-left":"-30px"
#                              })],
#            href=urldel18,
#                 # href="https://delitocorrupciondemenores.herokuapp.com/", 
#                  ),
#    
#                      ]),style={ "background-color": "light",
#                  "box-shadow": "10px 20px 30px gray",
#                  'margin-right': '60px',
#                                "width":"180px", 
#                                "height":"140px"
#                 } ,disabled=True)),
#               
               
        ]),
    #Estilo de fondo    
    
    
    
############################################################## TERCERA SECCION MAPAS     
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),

dbc.Row(
           [
               dbc.Col(html.P(["Mapas con sumas anuales por entidad" ],
                      style={"color": "purple", 
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
 
  dbc.Row(
           [
               dbc.Col(html.P(["A continuación se presenta un primer mapa que contiene las cifras acumuladas de  delitos de género en el periodo (2015-2021)  por entidad. Enseguida, abajo, hay 7 mapas con los acumulados anuales, destacando los cinco estados con mayor incidencia."
   ],
                              style={'textAlign': 'justify',
                             "font-size": "18px",
                             "font-family": "Arial",
                           "color": "black",
                            "line-height":"120%",                            
                            "margin-left": "100px",
                            "margin-right": "100px",}
                          #"text-shadow": "10px 20px 30px black",
                      )),
           ]),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),  
    ##New idea
   
     #ACUMULADO
          dbc.Col([
           dbc.Row( 
                dbc.Button(([html.Span("Acumulado",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
               id="tooltip-target-acumulado",
                    style={#"textDecoration": "underline",
                        "cursor": "pointer",
                          "font-size": 18,"color": "black","background-color": "lightgray"},),
          
        dbc.Tooltip("En el acumulado de 2015 a 2020, los estados con mayor incidencia son: Ciudad de México con 189,681 casos, "
            "seguido de Nuevo León con 177,235 casos,  México con 137,266 casos, Chihuahua con 110,304 casos, finalmente,"
            " Baja California con 102,634 casos.",
            target="tooltip-target-acumulado",
        ),
               dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/mapa%20Acumulado.jpg?raw=true",
                     style={"background-color":"lightgray"}, ),
               ]), style={"background-color":"lightgray",
                        # "box-shadow": "10px 20px 30px black",
                        "margin-left":"300px",
                        'width': '700px',
                          
                           },# disabled=True
                      ),),
          ]#,style={"margin-left":"50px"}
          ),
    
     #2015
         dbc.Row([
             dbc.Col(
            dbc.Button(([html.Span("2015",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
               id="tooltip-target-15",
                    style={#"textDecoration": "underline",
                        "cursor": "pointer",
                          "font-size": 18,"color": "black","background-color": "lightgray"},),
          
        dbc.Tooltip(
            "Los cinco estados con mayor incidencia en 2015 son: Nuevo León con 25,506 casos, seguido de Ciudad de México"
            " con 21,451 casos,  Chihuahua con 17,616 casos, Baja California con 15,108 casos, finalmente, México con 13,825 casos.",
            target="tooltip-target-15",
        ),
            dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2015.png?raw=true",
                                           ),
               ]), style={"background-color":"lightgray",
                        # "box-shadow": "10px 20px 30px black",
                        #  'margin-top': '-600px',
                        # 'margin-left': '800px',
                        'width': '300px'
                       },# disabled=True
                      ),),
    
    #########2016
        dbc.Col(
            dbc.Button(([html.Span("2016",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
               id="tooltip-target-16",
                    style={#"textDecoration": "underline",
                        "cursor": "pointer",
                          "font-size": 18,"color": "black","background-color": "lightgray"},),
          
        dbc.Tooltip(
            "Los cinco estados con mayor incidencia en 2016 son: Nuevo León con 26,870 casos, seguido de Ciudad de México"
            " con 24,047 casos,  Jalisco con 17,624 casos, Chihuahua con 16,704 casos, finalmente, México con 16,051 casos.",
            target="tooltip-target-16",
        ),
            dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2016.png?raw=true",
                                           ),
               ]), style={"background-color":"lightgray",
                        # "box-shadow": "10px 20px 30px black",
                        # 'margin-top': '-100px',
                        # 'margin-left': '800px',
                        'width': '300px'
                            },# disabled=True
                      ),),
             
    ############2017
             dbc.Col(
           dbc.Button(([html.Span("2017",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
               id="tooltip-target-17",
                    style={#"textDecoration": "underline",
                        "cursor": "pointer",
                          "font-size": 18,"color": "black","background-color": "lightgray"},),
          
        dbc.Tooltip(
            "Los cinco estados con mayor incidencia en 2017 son: Nuevo León con 26,721 casos, seguido de Ciudad de"
            " México con 23,112 casos,  México con 17,812 casos, Chihuahua con 16,956 casos, finalmente, Jalisco con 15,170 casos.",
            target="tooltip-target-17",
        ),
            dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2017.png?raw=true",
                                           ),
               ]), style={"background-color":"lightgray",
                        # "box-shadow": "10px 20px 30px black",
                         # 'margin-top': '-100px',
                        # 'margin-left': '800px',
                        'width': '300px'
                          },# disabled=True
                      ),),
         ],#style={"margin-top":"-500px"}
         
         
         ),
    
    
    
    
     dbc.Row([
             dbc.Col(
            dbc.Button(([html.Span("2018",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
               id="tooltip-target-18",
                    style={#"textDecoration": "underline",
                        "cursor": "pointer",
                          "font-size": 18,"color": "black","background-color": "lightgray"},),
          
        dbc.Tooltip(
          "Los cinco estados con mayor incidencia en 2018 son: Ciudad de México con 27980 casos, seguido de Nuevo León"
          " con 26,800 casos,  México con 17,979 casos, Chihuahua con 17,139 casos, finalmente, Baja California con 15,972 casos.",
          target="tooltip-target-18",
      ),
          dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2018.png?raw=true",
                                         ),
               ]), style={"background-color":"lightgray",
                        # "box-shadow": "10px 20px 30px black",
                        #  'margin-top': '-1100px',
                        # 'margin-left': '1200px',
                        'width': '300px'
                       },# disabled=True
                      ),),
    
    #########2016
        dbc.Col(
            dbc.Button(([html.Span("2019",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
               id="tooltip-target-19",
                    style={#"textDecoration": "underline",
                        "cursor": "pointer",
                          "font-size": 18,"color": "black","background-color": "lightgray"},),
          
        dbc.Tooltip(
          "Los cinco estados con mayor incidencia en 2019 son: Ciudad de México con 36,134 casos, "
          "seguido de Nuevo León con 27,228 casos,  México con 23,236 casos, Veracruz de Ignacio de la Llave"
          "con 19,125 casos, finalmente, Baja California con 17,117 casos.",
          target="tooltip-target-19",
      ),
                                         
          dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2019.png?raw=true",
                                      #style={'margin-right': '-300px',}  
                     ),
               ]), style={"background-color":"lightgray",
                        # "box-shadow": "10px 20px 30px black",
                        # 'margin-top': '-1000px',
                       #  'margin-left': '1200px',
                        'width': '300px'
                            },# disabled=True
                      ),),
             
    ############2017
             dbc.Col(
           dbc.Button(([html.Span("2020",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
               id="tooltip-target-20",
                    style={#"textDecoration": "underline",
                        "cursor": "pointer",
                          "font-size": 18,"color": "black","background-color": "lightgray"},),
          
       dbc.Tooltip(
          "Los cinco estados con mayor incidencia en 2020 son: Ciudad de México con 37,217 casos,"
          " seguido de México con 31,435 casos,  Nuevo León con 30,116 casos, Veracruz de Ignacio de la Llave "
          "con 18,152 casos, finalmente, Baja California con 18,044 casos.",

          target="tooltip-target-20",
      ),
                                      
          dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2020.png?raw=true",
                  style={"background-color":"lightgray",}            
                     ),
               ]), style={"background-color":"lightgray",
                        # "box-shadow": "10px 20px 30px black",
                         # 'margin-top': '-100px',
                        # 'margin-left': '1200px',
                        'width': '300px'
                          },# disabled=True
                      ),),
         dbc.Col(
           dbc.Button(([html.Span("2021",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
              id="tooltip-target-21",
                   style={#'margin-right': '-1100px',#"textDecoration": "underline",
                       "cursor": "pointer",
                         "font-size": 18,"color": "black","background-color": "lightgray"},),
         
       dbc.Tooltip(
           "Los cinco estados con mayor incidencia en 2021 son: Ciudad de México con 19,740 casos, seguido de México con 16,928 casos,"
           "  Nuevo León con 13,994 casos, Veracruz de Ignacio de la Llave con 8,815 casos, finalmente,"
           " Jalisco con 8,164 casos.",
           target="tooltip-target-21",
       ),
                                              
           dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2021.png?raw=true",
                             #style={#'margin-right': '-1100px',}         
                                 ),
              ]), style={"background-color":"lightgray",
                       # "box-shadow": "10px 20px 30px black",
                        # 'margin-top': '-200px',
                        #'margin-left': '500px',
                       'width': '300px'
                        },# disabled=True
                     ),),
         ]),
       
   ############################## POR DEFINIR MAPAS
    #IDEA wINIK
  #  #ACUMULADO
  #       dbc.Col([
  #        dbc.Row( 
  #             dbc.Button(([html.Span("Acumulado",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
  #            id="tooltip-target-acumulado",
  #                 style={#"textDecoration": "underline",
  #                     "cursor": "pointer",
  #                       "font-size": 18,"color": "black","background-color": "lightgray"},),
  #       
  #     dbc.Tooltip("En el acumulado de 2015 a 2020, los estados con mayor incidencia son: Ciudad de México con 189,681 casos, "
  #         "seguido de Nuevo León con 177,235 casos,  México con 137,266 casos, Chihuahua con 110,304 casos, finalmente,"
  #         " Baja California con 102,634 casos.",
  #         target="tooltip-target-acumulado",
  #     ),
  #            dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/mapa%20Acumulado.jpg?raw=true",
  #                  style={"background-color":"lightgray"}, ),
  #            ]), style={"background-color":"lightgray",
  #                     # "box-shadow": "10px 20px 30px black",
  #                     "margin-left":"10px",
  #                     'width': '700px',
  #                       
  #                        },# disabled=True
  #                   ),),
  #       ]#,style={"margin-left":"50px"}
  #       ),
  # 
  #  #2015
  #      dbc.Col([
  #          dbc.Row(
  #         dbc.Button(([html.Span("2015",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
  #            id="tooltip-target-15",
  #                 style={#"textDecoration": "underline",
  #                     "cursor": "pointer",
  #                       "font-size": 18,"color": "black","background-color": "lightgray"},),
  #       
  #     dbc.Tooltip(
  #         "Los cinco estados con mayor incidencia en 2015 son: Nuevo León con 25,506 casos, seguido de Ciudad de México"
  #         " con 21,451 casos,  Chihuahua con 17,616 casos, Baja California con 15,108 casos, finalmente, México con 13,825 casos.",
  #         target="tooltip-target-15",
  #     ),
  #         dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2015.png?raw=true",
  #                                        ),
  #            ]), style={"background-color":"lightgray",
  #                     # "box-shadow": "10px 20px 30px black",
  #                     #  'margin-top': '-600px',
  #                      'margin-left': '800px',
  #                     'width': '300px'
  #                    },# disabled=True
  #                   ),),
  # 
  # #########2016
  #     dbc.Row(
  #         dbc.Button(([html.Span("2016",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
  #            id="tooltip-target-16",
  #                 style={#"textDecoration": "underline",
  #                     "cursor": "pointer",
  #                       "font-size": 18,"color": "black","background-color": "lightgray"},),
  #       
  #     dbc.Tooltip(
  #         "Los cinco estados con mayor incidencia en 2016 son: Nuevo León con 26,870 casos, seguido de Ciudad de México"
  #         " con 24,047 casos,  Jalisco con 17,624 casos, Chihuahua con 16,704 casos, finalmente, México con 16,051 casos.",
  #         target="tooltip-target-16",
  #     ),
  #         dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2016.png?raw=true",
  #                                        ),
  #            ]), style={"background-color":"lightgray",
  #                     # "box-shadow": "10px 20px 30px black",
  #                     # 'margin-top': '-100px',
  #                      'margin-left': '800px',
  #                     'width': '300px'
  #                         },# disabled=True
  #                   ),),
  #          
  # ############2017
  #          dbc.Row(
  #        dbc.Button(([html.Span("2017",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
  #            id="tooltip-target-17",
  #                 style={#"textDecoration": "underline",
  #                     "cursor": "pointer",
  #                       "font-size": 18,"color": "black","background-color": "lightgray"},),
  #       
  #     dbc.Tooltip(
  #         "Los cinco estados con mayor incidencia en 2017 son: Nuevo León con 26,721 casos, seguido de Ciudad de"
  #         " México con 23,112 casos,  México con 17,812 casos, Chihuahua con 16,956 casos, finalmente, Jalisco con 15,170 casos.",
  #         target="tooltip-target-17",
  #     ),
  #         dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2017.png?raw=true",
  #                                        ),
  #            ]), style={"background-color":"lightgray",
  #                     # "box-shadow": "10px 20px 30px black",
  #                      # 'margin-top': '-100px',
  #                      'margin-left': '800px',
  #                     'width': '300px'
  #                       },# disabled=True
  #                   ),),
  #      ],style={"margin-top":"-500px"}),
  #  dbc.Col([
  #          dbc.Row(
  #         dbc.Button(([html.Span("2018",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
  #            id="tooltip-target-18",
  #                 style={#"textDecoration": "underline",
  #                     "cursor": "pointer",
  #                       "font-size": 18,"color": "black","background-color": "lightgray"},),
  #       
  #     dbc.Tooltip(
  #       "Los cinco estados con mayor incidencia en 2018 son: Ciudad de México con 27980 casos, seguido de Nuevo León"
  #       " con 26,800 casos,  México con 17,979 casos, Chihuahua con 17,139 casos, finalmente, Baja California con 15,972 casos.",
  #       target="tooltip-target-18",
  #   ),
  #       dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2018.png?raw=true",
  #                                      ),
  #            ]), style={"background-color":"lightgray",
  #                     # "box-shadow": "10px 20px 30px black",
  #                     #  'margin-top': '-1100px',
  #                      'margin-left': '1200px',
  #                     'width': '300px'
  #                    },# disabled=True
  #                   ),),
  # 
  # #########2016
  #     dbc.Row(
  #         dbc.Button(([html.Span("2019",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
  #            id="tooltip-target-19",
  #                 style={#"textDecoration": "underline",
  #                     "cursor": "pointer",
  #                       "font-size": 18,"color": "black","background-color": "lightgray"},),
  #       
  #     dbc.Tooltip(
  #       "Los cinco estados con mayor incidencia en 2019 son: Ciudad de México con 36,134 casos, "
  #       "seguido de Nuevo León con 27,228 casos,  México con 23,236 casos, Veracruz de Ignacio de la Llave"
  #       "con 19,125 casos, finalmente, Baja California con 17,117 casos.",
  #       target="tooltip-target-19",
  #   ),
  #                                      
  #       dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2019.png?raw=true",
  #                                   #style={'margin-right': '-300px',}  
  #                  ),
  #            ]), style={"background-color":"lightgray",
  #                     # "box-shadow": "10px 20px 30px black",
  #                     # 'margin-top': '-1000px',
  #                      'margin-left': '1200px',
  #                     'width': '300px'
  #                         },# disabled=True
  #                   ),),
  #          
  # ############2017
  #          dbc.Row(
  #        dbc.Button(([html.Span("2020",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
  #            id="tooltip-target-20",
  #                 style={#"textDecoration": "underline",
  #                     "cursor": "pointer",
  #                       "font-size": 18,"color": "black","background-color": "lightgray"},),
  #       
  #    dbc.Tooltip(
  #       "Los cinco estados con mayor incidencia en 2020 son: Ciudad de México con 37,217 casos,"
  #       " seguido de México con 31,435 casos,  Nuevo León con 30,116 casos, Veracruz de Ignacio de la Llave "
  #       "con 18,152 casos, finalmente, Baja California con 18,044 casos.",

  #       target="tooltip-target-20",
  #   ),
  #                                   
  #       dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2020.png?raw=true",
  #               style={"background-color":"lightgray",}            
  #                  ),
  #            ]), style={"background-color":"lightgray",
  #                     # "box-shadow": "10px 20px 30px black",
  #                      # 'margin-top': '-100px',
  #                      'margin-left': '1200px',
  #                     'width': '300px'
  #                       },# disabled=True
  #                   ),),
  #      ],style={"margin-top": "-900px"}),
    
    #Aqui termina op 2 
    
    ####  DESHABILITAR PARA                               Mapaas OP ESTRELLA op 1
    
    
    
    
         
    #    #2015
    #    dbc.Col([
    #        dbc.Row(
    #       dbc.Button(([html.Span("2015",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-15",
    #               style={#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #   dbc.Tooltip(
    #       "Los cinco estados con mayor incidencia en 2015 son: Nuevo León con 25,506 casos, seguido de Ciudad de México"
    #       " con 21,451 casos,  Chihuahua con 17,616 casos, Baja California con 15,108 casos, finalmente, México con 13,825 casos.",
    #       target="tooltip-target-15",
    #   ),
    #       dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2015.png?raw=true",
    #                                      ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                    # 'margin-top': '-100px',
    #                    'margin-left': '10px',
    #                   'width': '300px'
    #                  },# disabled=True
    #                 ),),
    
    #########2016
    #   dbc.Row(
    #       dbc.Button(([html.Span("2016",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-16",
    #               style={#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #   dbc.Tooltip(
    #       "Los cinco estados con mayor incidencia en 2016 son: Nuevo León con 26,870 casos, seguido de Ciudad de México"
    #       " con 24,047 casos,  Jalisco con 17,624 casos, Chihuahua con 16,704 casos, finalmente, México con 16,051 casos.",
    #       target="tooltip-target-16",
    #   ),
    #       dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2016.png?raw=true",
    #                                      ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                   # 'margin-top': '-100px',
    #                    'margin-left': '10px',
    #                   'width': '300px'
    #                       },# disabled=True
    #                 ),),
    #        
    ############2017
    #        dbc.Row(
    #      dbc.Button(([html.Span("2017",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-17",
    #               style={#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #   dbc.Tooltip(
    #       "Los cinco estados con mayor incidencia en 2017 son: Nuevo León con 26,721 casos, seguido de Ciudad de"
    #       " México con 23,112 casos,  México con 17,812 casos, Chihuahua con 16,956 casos, finalmente, Jalisco con 15,170 casos.",
    #       target="tooltip-target-17",
    #   ),
    #       dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2017.png?raw=true",
    #                                      ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                    # 'margin-top': '-100px',
    #                    'margin-left': '10px',
    #                   'width': '300px'
    #                     },# disabled=True
    #                 ),),
    #    ]),
    
    #    #ACUMULADO
    #     dbc.Col([
    #      dbc.Row( 
    #           dbc.Button(([html.Span("Acumulado",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-acumulado",
    #               style={#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #   dbc.Tooltip(
    #       "En el acumulado de 2015 a 2020, los estados con mayor incidencia son: Ciudad de México con 189,681 casos, "
    #       "seguido de Nuevo León con 177,235 casos,  México con 137,266 casos, Chihuahua con 110,304 casos, finalmente,"
    #       " Baja California con 102,634 casos.",
    #       target="tooltip-target-acumulado",
    #   ),
    #          dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/mapa%20Acumulado.jpg?raw=true",
    #                style={"background-color":"lightgray"}, ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                    'margin-left': '400px',
    #                   'width': '700px',
    #                     "margin-top":"-1000px",
    #                      },# disabled=True
    #                 ),),
    ###########2021
    #dbc.Row(
    #       dbc.Button(([html.Span("2021",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-21",
    #               style={#'margin-right': '-1100px',#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #   dbc.Tooltip(
    #       "Los cinco estados con mayor incidencia en 2021 son: Ciudad de México con 19,740 casos, seguido de México con 16,928 casos,"
    #       "  Nuevo León con 13,994 casos, Veracruz de Ignacio de la Llave con 8,815 casos, finalmente,"
    #       " Jalisco con 8,164 casos.",

    #       target="tooltip-target-21",
    #   ),
    #                                          
    #       dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2021.png?raw=true",
    #                         #style={#'margin-right': '-1100px',}         
    #                             ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                     'margin-top': '-200px',
    #                    'margin-left': '500px',
    #                   'width': '300px'
    #                    },# disabled=True
    #                 ),),
    #     ]),
    #    
    #    #2018
    
    # 
    #    #2015
    #    dbc.Col([
    #        dbc.Row(
    #       dbc.Button(([html.Span("2018",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-18",
    #               style={#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #   dbc.Tooltip(
    #     "Los cinco estados con mayor incidencia en 2018 son: Ciudad de México con 27980 casos, seguido de Nuevo León"
    #     " con 26,800 casos,  México con 17,979 casos, Chihuahua con 17,139 casos, finalmente, Baja California con 15,972 casos.",
    #     target="tooltip-target-18",
    # ),
    #     dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2018.png?raw=true",
    #                                    ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                   #  'margin-top': '-1100px',
    #                    'margin-left': '1000px',
    #                   'width': '300px'
    #                  },# disabled=True
    #                 ),),
    
    #########2016
    #   dbc.Row(
    #       dbc.Button(([html.Span("2019",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-19",
    #               style={#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #   dbc.Tooltip(
    #     "Los cinco estados con mayor incidencia en 2019 son: Ciudad de México con 36,134 casos, "
    #     "seguido de Nuevo León con 27,228 casos,  México con 23,236 casos, Veracruz de Ignacio de la Llave"
    #     "con 19,125 casos, finalmente, Baja California con 17,117 casos.",
    #     target="tooltip-target-19",
    # ),
    #                                    
    #     dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2019.png?raw=true",
    #                                 #style={'margin-right': '-300px',}  
    #                ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                   # 'margin-top': '-1000px',
    #                    'margin-left': '1000px',
    #                   'width': '300px'
    #                       },# disabled=True
    #                 ),),
    #        
    ############2017
    #        dbc.Row(
    #      dbc.Button(([html.Span("2020",# style={"font-size": 18,"color": "black","background-color": "lightgray"},
    #          id="tooltip-target-20",
    #               style={#"textDecoration": "underline",
    #                   "cursor": "pointer",
    #                     "font-size": 18,"color": "black","background-color": "lightgray"},),
    #     
    #  dbc.Tooltip(
    #     "Los cinco estados con mayor incidencia en 2020 son: Ciudad de México con 37,217 casos,"
    #     " seguido de México con 31,435 casos,  Nuevo León con 30,116 casos, Veracruz de Ignacio de la Llave "
    #     "con 18,152 casos, finalmente, Baja California con 18,044 casos.",

    #     target="tooltip-target-20",
    # ),
    #                                 
    #     dbc.CardImg(src="https://github.com/fdealbam/violenciadegenero/blob/main/application/static/Mapa%20v-g%20Total2020.png?raw=true",
    #             style={"background-color":"lightgray",}            
    #                ),
    #          ]), style={"background-color":"lightgray",
    #                   # "box-shadow": "10px 20px 30px black",
    #                    # 'margin-top': '-100px',
    #                    'margin-left': '1000px',
    #                   'width': '300px'
    #                     },# disabled=True
    #                 ),),
    #    ],style={"margin-top": "-1000px"}),
          

 
    html.Br(),
     html.Br(),
    html.Br(),
     html.Br(),
      html.Br(),
     html.Br(),
     html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

#   
    dbc.Row([
        dbc.Col(html.P("Cifras mensuales de delitos de genero", 
                        style={"color": "purple", 
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
    
    
     
    dbc.Row([dbc.Col(html.P("Los delitos de género representan 18%  de la incidencia delictiva acumulada entre 2015 hasta 2021", 
                       style={'textAlign': 'justify',
                            #  "left": "50%",
                             "font-size": "18px",
                             "font-family": "Arial",
                           "color": "black",
                            "line-height":"120%",                            
                            "margin-left": "100px",
                            "margin-right": "100px",
                          }
                      )),
        
            ]),
  dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_meses, ))
    ]),
    
      html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
   
    
    
    
         dbc.Row([
        dbc.Col(html.P("Comparativo de variación de cada delito", 
                        style={"color": "purple", 
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
 dbc.Row([
        dbc.Col(html.P(
            "El delito de inasistencia familiar es el único que muestra disminución, si se comparan las sumas anuales de 2015 respecto a las de 2020. En cambio, los delitos de abuso sexual y contra la seguridad corporal registraron los mayores incremento (cifra 1 y cifra 2, respectivamente).", 
                       style={'textAlign': 'justify',
                              "left": "50%",
                             "font-size": "18px",
                             "font-family": "Arial",
                           "font-color": "purple",
                           "line-height":"120%",
                               "margin-left": "100px",
                            "margin-right": "100px",
                          
                          },
            
        )),]),
  dbc.Row([
        dbc.Col(dcc.Graph(figure=comparatot_2015_20, ))
    
        
    ]),
   
    html.Br(),
      html.Br(),
     html.Br(),
     html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
#    html.Br(),
     html.Br(),     
     html.Br(),
    html.Br(), 
  dbc.Row([
        dbc.Col(html.P("Consideraciones generales", 
                        style={"color": "purple", 
                               "font-size": "32px",
                               "font-family": "Arial",        
                               "text-shadow": "10px 20px 30px gray",
                            "background-color": "lightgray"}),
                       width={'size': 20, "offset":1 },
                      )],justify="start",),
     dbc.Row(
           [
                   html.P("En este dashboard presentamos 17 delitos que reflejan la gravedad de la violencia de género en el país,"
                          " analizando las cifras desde el año 2015 hasta los datos más recientes, mayo de 2021. Con este instrumento"
                          " proporcionamos a las diputadas y diputados información basada en la evidencia,  de un fenómeno con alcance "
                          " nacional. Este análisis evoca la necesidad insoslayable de profundizar las políticas de equidad de género," 
                          " de acciones sustantivas de equidad; acciones que nos hagan más conscientes, más vigilantes respecto a sus"
                          " multiples manifestaciones. Se requiere también crear conciencia colectiva e intervención institucional para "
                          " que las políticas y acciones sean inclusivas e incluyentes.",
                          style={'textAlign': 'justify',
                             "font-size": "18px",
                             "font-family": "Arial",
                           "color": "black",
                            "line-height":"120%",                            
                            "margin-left": "100px",
                            "margin-right": "100px",}
                          #"text-shadow": "10px 20px 30px black",
                      )],justify="start",),
    
    
    
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
     html.Br(),
   
    
    #Logo
     dbc.Row([dbc.Col(
         dbc.CardImg(src="https://github.com/fdealbam/0entrada/blob/ce2cda9ccf7732861b8494b36562ebe9c8c642a6/application/static/logo%20cesopycamara.jpeg?raw=true"),
                        width=5, md={'size': 2,  "offset": 6, }),
         dbc.Col(html.H6(" Centro de Estudios Sociales y de Opinión Pública," 
                           " Cámara de Diputados"
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0, "font-family": "Arial",}),
               ], justify="start",),
    html.Br(),
  
    
    #Estilo de fondo
 
     
    ],style={
            'margin-top': '0px',
            'margin-left': '10px',
            'width': '1400px',
           # 'height': '1413px',
      'backgroundColor': 'lightgray'
         })



if __name__ == '__main__':
    app.run_server()
