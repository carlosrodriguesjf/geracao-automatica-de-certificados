# PROJETO AUTOMAÇÃO PARA GERAÇÃO DE CERTIFICADOS

## 👤 Autor e Contato
- **Nome**: Carlos Rodrigues
- **E-mail**: carlosrodriguesjf@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/carlosrodriguesjf/
- **GitHub**: https://github.com/carlosrodriguesjf


## 📌 Descrição
Este projeto tem como objetivo automatizar a geração de certificados personalizados a partir de uma planilha contendo informações sobre os participantes e os seus cursos concluídos. Utilizei as bibliotecas  python  **PIL** para edição de imagens e **OpenPyXL** para manipulação de arquivos Excel.


## 🔍 Considerações Iniciais
- O modelo de certificado base deve estar localizado na pasta `arquivos_base/`.
- As informações dos alunos devem estar em um arquivo Excel (`planilha_cursos.xlsx`).
- As fontes utilizadas no certificado devem estar armazenadas na pasta `fontes/`.
- O arquivo com a assinatura do diretor no certificado deve estar na pasta `arquivos_base/`.
- Os certificados gerados serão salvos na pasta `certificados_emitidos/`.



## 🎯 Objetivos
- Automatizar o processo de geração de certificados.
- Reduzir o tempo de emissão de certificados para turmas grandes.
- Garantir a padronização dos certificados.



## 📂 Estrutura do Projeto
```
📁 geracao_certificados
│── 📂 arquivos_base          # Arquivos base (modelo do certificado, assinatura, etc.)
│── 📂 certificados_emitidos  # Certificados gerados automaticamente
│── 📂 fontes                 # Arquivos de fontes utilizadas
│── 📂 requisitos             # Pasta com os requisitos do projeto
│── app.py                    # Planilha com os dados dos alunos e cursos
│── README.md                 # Documentação do projeto
│── requirements.txt          # Dependências do projeto
│── LICENSE                   # Arquivos de licença
```



## 📊 Dados Utilizados
A planilha `planilha_cursos.xlsx` contém as seguintes colunas:
- **Nome do Curso**: Nome do curso concluído pelo aluno.
- **Nome do Aluno**: Nome completo do aluno.
- **Data de Início**: Data de início do curso.
- **Data de Término**: Data de conclusão do curso.
- **Carga Horária**: Duração do curso em horas.



## 🛠️ Tecnologias e Ferramentas
- **Python**
- **PIL (Pillow)**
- **OpenPyXL**



## 🚀 Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/geracao_certificados.git
   cd geracao_certificados
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python scripts/app.py
   ```



## 📈 Exemplo de Uso
Abaixo, um exemplo do formato esperado na planilha de entrada (`planilha_cursos.xlsx`):
```plaintext
| Nome do Curso  | Nome do Aluno    | Data de Início | Data de Término | Carga Horária |
|---------------|-----------------|--------------|--------------|--------------|
| Python Avançado | João Silva       | 01/01/2024  | 10/02/2024  | 40h          |
| Data Science  | Maria Oliveira   | 05/03/2024  | 20/04/2024  | 60h          |
```
Os certificados serão gerados automaticamente na pasta `certificados_emitidos/`.


## 🔮 Objetivos Futuros
- **Criação de uma interface gráfica**: criar uma interface gráfica para que o usuário possa anexar a planilha gerar
- **Ajustes no código**: Ajustar o código para que o programa epossa receber qualquer tamanho de nome e curso



## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
