#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import pandas as pd


# In[6]:


import numpy as np


# In[82]:


# schemes = {    'OrRd': ['#FEF0D9', '#FDD49E', '#FDBB84',
#                         '#FC8D59', '#EF6548', '#D7301F', '#990000'],
#            'YlOrBr': ['#FFFFD4', '#FEE391', '#FEC44F',
#                           '#FE9929', '#EC7014', '#CC4C02', '#8C2D04'],
#                'YlOrRd': ['#FFFFB2', '#FED976', '#FEB24C',
#                           '#FD8D3C', '#FC4E2A', '#E31A1C', '#B10026'],
#                'PuBu': ['#F1EEF6', '#D0D1E6', '#A6BDDB',
#                         '#74A9CF', '#3690C0', '#0570B0', '#034E7B'],
#                'PuBuGn': ['#F6EFF7', '#D0D1E6', '#A6BDDB',
#                           '#67A9CF', '#3690C0', '#02818A', '#016450'],
#                'PuRd': ['#F1EEF6', '#D4B9DA', '#C994C7',
#                         '#DF65B0', '#E7298A', '#CE1256', '#91003F'],
#                'RdPu': ['#FEEBE2', '#FCC5C0', '#FA9FB5',
#                         '#F768A1', '#DD3497', '#AE017E', '#7A0177'],
#                'YlGn': ['#FFFFCC', '#D9F0A3', '#ADDD8E',
#                         '#78C679', '#41AB5D', '#238443', '#005A32'],
#                'YlGnBu': ['#FFFFCC', '#C7E9B4', '#7FCDBB',
#                           '#41B6C4', '#1D91C0', '#225EA8', '#0C2C84'],
#                'BrBg': ['#8c510a', '#d8b365', '#f6e8c3',
#                         '#c7eae5', '#5ab4ac', '#01665e'],
#                'PiYG': ['#c51b7d', '#e9a3c9', '#fde0ef',
#                         '#e6f5d0', '#a1d76a', '#4d9221'],
#                'PRGn': ['#762a83', '#af8dc3', '#e7d4e8',
#                         '#d9f0d3', '#7fbf7b', '#1b7837'],
#                'PuOr': ['#b35806', '#f1a340', '#fee0b6',
#                         '#d8daeb', '#998ec3', '#542788'],
#                'RdBu': ['#b2182b', '#ef8a62', '#fddbc7',
#                         '#d1e5f0', '#67a9cf', '#2166ac'],
#                'RdGy': ['#b2182b', '#ef8a62', '#fddbc7',
#                         '#e0e0e0', '#999999', '#4d4d4d'],
#                'RdYlBu': ['#d73027', '#fc8d59', '#fee090',
#                           '#e0f3f8', '#91bfdb', '#4575b4'],
#                'RdYlGn': ['#d73027', '#fc8d59', '#fee08b',
#                           '#d9ef8b', '#91cf60', '#1a9850'],
#                'Accent': ['#7fc97f', '#beaed4', '#fdc086',
#                           '#ffff99', '#386cb0', '#f0027f'],
#                'Dark2': ['#1b9e77', '#d95f02', '#7570b3',
#                          '#e7298a', '#66a61e', '#e6ab02'],
#                'Paired': ['#a6cee3', '#1f78b4', '#b2df8a',
#                           '#33a02c', '#fb9a99', '#e31a1c'],
#                'Pastel1': ['#fbb4ae', '#b3cde3', '#ccebc5',
#                            '#decbe4', '#fed9a6', '#ffffcc'],
#                'Pastel2': ['#b3e2cd', '#fdcdac', '#cbd5e8',
#                            '#f4cae4', '#e6f5c9', '#fff2ae'],
#                'Set1': ['#e41a1c', '#377eb8', '#4daf4a',
#                         '#984ea3', '#ff7f00', '#ffff33'],
#                'Set2': ['#66c2a5', '#fc8d62', '#8da0cb',
#                         '#e78ac3', '#a6d854', '#ffd92f'],
#                'Set3': ['#8dd3c7', '#ffffb3', '#bebada',
#                         '#fb8072', '#80b1d3', '#fdb462'],
#                'BuGn': ['#EDF8FB', '#CCECE6', '#CCECE6',
#                         '#66C2A4', '#41AE76', '#238B45', '#005824'],
#                'BuPu': ['#EDF8FB', '#BFD3E6', '#9EBCDA',
#                         '#8C96C6', '#8C6BB1', '#88419D', '#6E016B'],
#                'GnBu': ['#F0F9E8', '#CCEBC5', '#A8DDB5',
#                         '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E'],
#                }

# schemes_list = []
# for each in schemes:
#     for e in range(len(each)-1):
#         schemes_list.append(schemes[each][e])
        
# schemes_list = pd.DataFrame(schemes_list, columns = ['color']).reset_index()
# schemes_list.columns = [['cluster_num', 'color']]
# schemes_list.to_csv('color_list_folium.csv', sep = '|')


# In[2]:


def create_mapping():
    color_schemes = pd.read_csv('color_list_folium.csv', sep = '|')
    color_schemes['cluster_num'] = np.arange(0.0, 11.0, 0.1)[:-3]
    mapping = dict(color_schemes[['cluster_num', 'color']].values)
    return mapping


# In[84]:


def assign_color(col, mapping):
    color_selected = col.map(mapping)
    return color_selected


# In[ ]:




