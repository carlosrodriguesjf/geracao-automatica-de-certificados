# PROJETO AUTOMAÇÃO PARA GERAÇÃO DE CERTIFICADOS


import openpyxl
from PIL import Image, ImageDraw, ImageFont

## Carregando os dados da planilha

# abrindo a pasta de trabalho
workbook_alunos = openpyxl.load_workbook(r'arquivos_base/planilha_cursos.xlsx')

# abrindo a planilha
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):

    # preenchendo as variáveis com os dados da planilha
    nome_curso = linha[0].value
    nome_aluno = linha[1].value
    data_inicio = linha[2].value
    data_termino = linha[3].value
    carga_horaria = linha[4].value

    
    ## Preenchimento dinâmico dos seguintes campos no certificado:

    # carregamento das fontes
    fonte_nome = ImageFont.truetype('./fontes/TAHOMABD.TTF',90)
    fonte_geral = ImageFont.truetype('./fontes/TAHOMA.TTF',45)

    imagem = Image.open('./arquivos_base/certificado_padrao.png')
    desenho = ImageDraw.Draw(imagem)

    # Preenchendo o nome
    desenho.text((700,585),nome_aluno, fill='black', font= fonte_nome)

    # Preenchendo o curso
    desenho.text((630,733),nome_curso, fill='black', font= fonte_geral)

    # Preenchendo a carga horária
    desenho.text((1620,733),carga_horaria, fill='black', font= fonte_geral)

    # Preenchendo a data de início
    desenho.text((1520,800),data_inicio, fill='black', font= fonte_geral)

    # Preenchendo a data de término
    desenho.text((350,870),data_inicio, fill='black', font= fonte_geral)
    

    # carregando imagem da assinatura
    assinatura = Image.open('./arquivos_base/assinatura.png')

    # colando a imagem da assinatura
    imagem.paste(assinatura,(920,955))

    # salvando o arquivo
    imagem.save(f'./certificados_emitidos/{indice+1} {nome_aluno}.png')


