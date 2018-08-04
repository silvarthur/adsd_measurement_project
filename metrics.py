# coding: utf-8
import pandas as p
import matplotlib.pyplot as plt
import numpy as n

def plot(label, factor, title, key_data, data1, data2):
    x = n.array([i for i in range(0, 100)])
    y1 = n.array(data1[key_data])
    y2 = n.array(data2[key_data])
    plt.xlabel('')
    plt.ylabel(label)
    plt.title(title)
    plt.plot(x, y1, label='Log Ativo')
    plt.plot(x, y2, label='Log Inativo')
    plt.legend()
    plt.savefig(label + factor + '.pdf')
    """ plt.show() """

def plot_dois_mil(label, factor, title, key_data, data1, data2):
    x = n.array([i for i in range(0, 2000)])
    y1 = n.array(data1[key_data])
    y2 = n.array(data2[key_data])
    plt.xlabel('')
    plt.ylabel(label)
    plt.title(title)
    plt.plot(x, y1, label='Log Ativo')
    plt.plot(x, y2, label='Log Inativo')
    plt.legend()
    plt.savefig(label + factor + '.pdf')
    """ plt.show() """

data_get_1 = p.read_csv('100-ativo/metricas-get.csv', encoding='utf-8')
data_get_2 = p.read_csv('100-inativo/metricas-get.csv', encoding='utf-8')

data_get_3 = p.read_csv('2000-ativo/metricas-get.csv', encoding='utf-8')
data_get_4 = p.read_csv('2000-inativo/metricas-get.csv', encoding='utf-8')


plot('server_resp_timef', '_get100' ,'Tempo de Reposta do Servidor','server_resp_timef', data_get_1,data_get_2)
plot('bd_timef', '_get100'          ,'Tempo de uso do Banco de Dados','bd_timef', data_get_1,data_get_2)
plot('cpu_usage', '_get100'         ,'Uso de CPU','cpu_usage', data_get_1,data_get_2)
plot('memory_usage', '_get100'      ,'Uso de Memoria','memory_usage', data_get_1,data_get_2)

plot_dois_mil('server_resp_timef', '_get2000','Tempo de Reposta do Servidor','server_resp_timef', data_get_3,data_get_4)
plot_dois_mil('bd_timef', '_get2000'         ,'Tempo de uso do Banco de Dados','bd_timef', data_get_3,data_get_4)
plot_dois_mil('cpu_usage', '_get2000'        ,'Uso de CPU','cpu_usage', data_get_3,data_get_4)
plot_dois_mil('memory_usage', '_get2000'     ,'Uso de Memoria','memory_usage', data_get_3,data_get_4)


data_post_1 = p.read_csv('100-ativo/metricas-post.csv', encoding='utf-8')
data_post_2 = p.read_csv('100-inativo/metricas-post.csv', encoding='utf-8')

data_post_3 = p.read_csv('2000-ativo/metricas-post.csv', encoding='utf-8')
data_post_4 = p.read_csv('2000-inativo/metricas-post.csv', encoding='utf-8')


plot('server_resp_timef', '_post100','Tempo de Reposta do Servidor','server_resp_timef', data_post_1,data_post_2)
plot('bd_timef', '_post100', 'Tempo de uso do Banco de Dados','bd_timef', data_post_1,data_post_2)
plot('cpu_usage', '_post100','Uso de CPU','cpu_usage', data_post_1,data_post_2)
plot('memory_usage', '_post100','Uso de Memoria','memory_usage', data_post_1,data_post_2)

plot_dois_mil('server_resp_timef', '_post2000', 'Tempo de Reposta do Servidor','server_resp_timef', data_post_3,data_post_4)
plot_dois_mil('bd_timef', '_post2000', 'Tempo de uso do Banco de Dados','bd_timef', data_post_3,data_post_4)
plot_dois_mil('cpu_usage', '_post2000', 'Uso de CPU','cpu_usage', data_post_3,data_post_4)
plot_dois_mil('memory_usage', '_post2000', 'Uso de Memoria','memory_usage', data_post_3,data_post_4)