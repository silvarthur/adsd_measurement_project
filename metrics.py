# coding: utf-8
import pandas as p
import matplotlib.pyplot as plt
import numpy as n

def plot(label, title, key_data, data1, data2):
    x = n.array([i for i in range(0, 100)])
    y1 = n.array(data1[key_data])
    y2 = n.array(data2[key_data])
    plt.xlabel('')
    plt.ylabel(label)
    plt.title(title)
    plt.plot(x, y1, label='Log Ativo')
    plt.plot(x, y2, label='Log Inativo')
    plt.legend()
    plt.savefig(label + '.pdf')
    plt.show()

data_get_1 = p.read_csv('100-ativo/metricas-get.csv', encoding='utf-8')
data_get_2 = p.read_csv('100-inativo/metricas-get.csv', encoding='utf-8')

data_get_3 = p.read_csv('2000-ativo/metricas-get.csv', encoding='utf-8')
data_get_4 = p.read_csv('2000-inativo/metricas-get.csv', encoding='utf-8')


plot('server_resp_timef','Tempo de Reposta do Servidor','server_resp_timef', data_get_1,data_get_2)
plot('bd_timef','Tempo de uso do Banco de Dados','bd_timef', data_get_1,data_get_2)
plot('cpu_usage','Uso de CPU','cpu_usage', data_get_1,data_get_2)
plot('memory_usage','Uso de Memoria','memory_usage', data_get_1,data_get_2)

plot('server_resp_timef','Tempo de Reposta do Servidor','server_resp_timef', data_get_3,data_get_4)
plot('bd_timef','Tempo de uso do Banco de Dados','bd_timef', data_get_3,data_get_4)
plot('cpu_usage','Uso de CPU','cpu_usage', data_get_3,data_get_4)
plot('memory_usage','Uso de Memoria','memory_usage', data_get_3,data_get_4)


data_post_1 = p.read_csv('100-ativo/metricas-post.csv', encoding='utf-8')
data_post_2 = p.read_csv('100-inativo/metricas-post.csv', encoding='utf-8')

data_post_3 = p.read_csv('2000-ativo/metricas-post.csv', encoding='utf-8')
data_post_4 = p.read_csv('2000-inativo/metricas-post.csv', encoding='utf-8')


plot('server_resp_timef','Tempo de Reposta do Servidor','server_resp_timef', data_post_1,data_post_2)
plot('bd_timef','Tempo de uso do Banco de Dados','bd_timef', data_post_1,data_post_2)
plot('cpu_usage','Uso de CPU','cpu_usage', data_post_1,data_post_2)
plot('memory_usage','Uso de Memoria','memory_usage', data_post_1,data_post_2)

plot('server_resp_timef','Tempo de Reposta do Servidor','server_resp_timef', data_post_3,data_post_4)
plot('bd_timef','Tempo de uso do Banco de Dados','bd_timef', data_post_3,data_post_4)
plot('cpu_usage','Uso de CPU','cpu_usage', data_post_3,data_post_4)
plot('memory_usage','Uso de Memoria','memory_usage', data_post_3,data_post_4)