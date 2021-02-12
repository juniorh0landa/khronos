# In[0]: Importa as bibliotecas
# -*- coding: utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt

# In[1]: Lê o arquivo

df = pd.read_csv('../dados/viagens.csv')

# In[2]: Trata os dados

def dataAnalyze(par):
    #Define os valores como string
    dfe = par.astype(str)
    
    aux = {}
    aux['atrasadas'] = []
    aux['adiantadas'] = []
    aux['realizadas'] = []
    aux['Empresa'] = []
    aux['NomeLinha'] = []
    index = list(dfe.unique())
    aux['NumeroLinha'] = index
    
    for i in index:
        
        #conta o total de viagens
        totals = len(df[dfe == i])
        
        #conta o total de atrasos e sua porcentagem
        atrasos = len(df[(df['hora_realizada'] > df['hora_prevista']) & (dfe == i)])
        aux['atrasadas'].append(round(atrasos*100/totals, 2))
        
        #conta o total de adiantamentos e sua porcentagem
        adiantamentos = len(df[(df['hora_realizada'] < df['hora_prevista']) & (dfe == i)])
        aux['adiantadas'].append(round(adiantamentos*100/totals, 2))
        
        #conta o total de viagens realizadas e sua porcentagem
        realizadas = df[dfe == i]['hora_realizada'].count()
        aux['realizadas'].append(round(realizadas/totals*100, 2))
        
        #define o nome da linha e da empresa
        dataLinha = df[dfe == i]
        aux['NomeLinha'].append(dataLinha.loc[dataLinha.index[0],'nome_linha'])
        aux['Empresa'].append(dataLinha.loc[dataLinha.index[0],'empresa'])
    
    return pd.DataFrame(aux,index=index)

# In[3]: Gera os gráficos
    
def createCharts(dfl, par1, par2, empresa = False):
    dfl = dfl.sort_values([par1], ascending = True)
        
    dfl.plot(kind='barh', figsize=(10,5), legend=None)
    plt.xlim(0,100.5)
    plt.grid()
    plt.title("Viagens "+par1+" por "+par2+" (%)")
    if empresa:
        media = round(dfl.mean()[0],2)
        qtde = len(dfl[dfl[par] > media])
        x = [media]*len(dfl)
        plt.plot(x, list(dfl.index), color = 'r')
        plt.legend(['Média'])
        plt.savefig('../output/src/'+par1+empresa+'.jpg')
        return {'media':str(media),
                'qtde':str(qtde),
                'dataframe':dfl,
                'link':'./src/'+par1+empresa+'.jpg'}
    plt.savefig('../output/src/'+par1+par2+'.jpg')
    return {'dataframe':dfl,
            'link': './src/'+par1+par2+'.jpg'}

# In[4]: Escreve o relatório

linhas = dataAnalyze(df['numero_linha'])
empresas = dataAnalyze(df['empresa'])
empresas.index = ['Real', 'Veleiro', 'S. Francisco', 'C. de Maceió']

try:
    os.makedirs("../output/src/")
except:
    None

r = open("../output/index.htm",'w') #Relatório resumido
r.write("<head><title>Relatório de Tempo de Viagem</title></head>")
r.write("<h1>Relatório de Tempo de Viagem</h1>")
r.write("<h2>Visão Geral</h2>")

for par in ['atrasadas', 'adiantadas', 'realizadas']:
    r.write("<h3><a href='"+par+".htm'>Viagens "+par+"</a></h3>")
    chart = createCharts(empresas[[par]], par, 'empresa')
    r.write("<img src='"+chart['link']+"'/>")
    
    d = open("../output/"+par+".htm",'w') #Relatórios detalhados
    d.write("<head><title>Relatório de Tempo de Viagem</title></head>")
    d.write("<h1><a href='index.htm'>Relatório de Tempo de Viagem</a></h1>")
    d.write("<h2>Viagens "+par+"</h2>")
    empresas = empresas.sort_values([par], ascending = False)
    for empresa in list(empresas['Empresa']):
        d.write("<h3>"+empresa+"</h3>")
        linha = linhas[linhas['Empresa'] == empresa]
        linha = linha.sort_values([par], ascending = False)
        chart = createCharts(linha[[par]], par, 'linha', empresa = empresa)
        d.write("<img src='"+chart['link']+"'/>")
        d.write("<br/><a>A empresa <b>"+empresa+"</b> possui uma média de viagens "+par+" de "+chart['media']+"%. E </a>")
        d.write(chart['qtde']+" das "+str(len(chart['dataframe']))+" linhas de ônibus ultrapassam essa média. São elas:</a><br/><ol>")
        lista = linha
        for i in range(0,int(chart['qtde'])):
            d.write("<li>"+lista.loc[lista.index[i],'NumeroLinha']+" - "+lista.loc[lista.index[i],'NomeLinha']+" ("+str(lista.loc[lista.index[i],par])+"%)</li>")
        d.write("<br/><a>E as que não ultrapassaram a média de viagens "+par+" da empresa foram as seguintes:</a><br/><br/>")
        for i in range(int(chart['qtde']),len(chart['dataframe'])):
            d.write("<li>"+lista.loc[lista.index[i],'NumeroLinha']+" - "+lista.loc[lista.index[i],'NomeLinha']+" ("+str(lista.loc[lista.index[i],par])+"%)</li>")
        d.write("</ol><br/>")
    d.close()

r.close()