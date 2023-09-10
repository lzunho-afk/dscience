#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
# MIT (c) Lucas Zunho <lucaszunho17@gmail.com>
"""!
@file mapeamento_ubs.py
@brief Script de visualização do conjunto de dados de localização de UBSs.

Esse script analisa os dados do dataset aberto das Unidades Básicas de Saúde
disponíveis em https://dados.gov.br/dados/conjuntos-dados/unidades-basicas-de-saude-ubs2
e cria a sua visualização com interação com o usuário.

O dataset (CSV) tem as seguintes chaves:
- CNES
- UF
- NOME
- LOGRADOURO
- BAIRRO
- LATITUDE
- LONGITUDE
"""

import folium
from folium.plugins import MarkerCluster

map = folium.Map(location=[-30, -51], zoom_start=6, min_zoom=5)

marker_cluster = MarkerCluster().add_to(map)

ubses = dict()

with open('Unidades_Basicas_Saude-UBS.csv', 'r') as csv:
    print(csv.readline())
    for line in csv:
        a = line[:-1].split(';')
        lat = a[6]
        lon = a[7]
        uf = a[1]
        if lat != '' and lon != '' and uf == "43":
            nome = a[3][1:-1]
            logr = a[4][1:-1]
            bairro = a[5][1:-1]
            lat = float(lat.replace(',', '.'))
            lon = float(lon.replace(',', '.'))
            ubses[nome] = (logr, bairro, lat, lon)
            folium.Marker(popup=nome, location=[lat,lon]).add_to(marker_cluster)

map.save("mapa_output.html")
