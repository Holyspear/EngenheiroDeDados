#! /usr/bin/python3
# -*- coding: utf-8 -*-

import oracledb, json, base64

usr = 'holyspear'
senha = 'showtime!'
cs = 'SERVIÇO/NOMEDB'

def converteBase64(path):
    with open(path, "rb") as arquivoImagem:
        arquivoImagem64 = base64.b64encode(arquivoImagem.read())
        return arquivoImagem64

def buscaOcorrencias():
    with oracledb.connect(user=usr, password=senha, dsn=cs) as connection:
        with connection.cursor() as cursor:
            sql =   " select " \
                    +       "colum1," \
                    +       "colum2," \
                    +       "colum3," \
                    +       "colum4," \
                    +       "colum5" \
                    + " from tabela_ocorrencias" \
                    + " where rownum <= 1" \
                    +       " and trim(colum1) is not null" #\
                    +       " and colum1 = myheart" \
            cursor.execute(sql)
            resultSet = [dict((cursor.description[i][0].lower(), value) for i, value in enumerate(row)) for row in cursor.fetchall()]
            return resultSet

def buscaImagens(param1):
    with oracledb.connect(user=usr, password=senha, dsn=cs) as connection:
        with connection.cursor() as cursor:
            sql =   " select " \
                    +       "colum1," \
                    +       "colum2," \
                    +       "colum3," \
                    +       "colum4," \
                    +       "colum5" \
                    + " from tabela_imagens" \
                    + " where rownum <= 1" \
                    +       " and trim(colum1) is not null" #\
                    +       " and colum1 = myheart" \
					+ " and colum2 = " + str(param1) #\
            cursor.execute(sql)
            resultSet = [dict((cursor.description[i][0].lower(), value) for i, value in enumerate(row)) for row in cursor.fetchall()]
            return resultSet

jsonOcorrencias = buscaOcorrencias()
index=0
if jsonOcorrencias:
    for i in jsonOcorrencias:
        jsonImagens = buscaImagens(i['ocorrencia_id'])
        if jsonImagens:
            jsonOcorrencias[index]['fotos'] = jsonImagens
        index += 1

jsonArray = str(jsonOcorrencias).replace("'",'"').replace("None","null")
print(jsonArray)

#if jsonOcorrencias:
#    print([buscaImagens(i['ocorrencia_id']) for i in jsonOcorrencias])



#jsonImagens = buscaImagens(59100)
#arquivoImagem64 = converteBase64(jsonImagens[0]['path'])
#print(arquivoImagem64)

#print(jsonImagens[0]['path'])
#with open(jsonImagens[0]['path'], "rb") as arquivoImagem:
#    arquivoImagem64 = base64.b64encode(arquivoImagem.read())
#    print(arquivoImagem64)

#for i in jsonOcorrencias:
 #   i['foto'] = 'foto1/testando'
  #  resultJson.append(i)

#print(resultJson)

#jsonImagens = [buscaImagens(i['ocorrencia_id']) for i in jsonOcorrencias]
#print(jsonImagens)

#jsonArray = str(jsonOcorrencias).replace("'",'"').replace("None","null")
#print(jsonArray)