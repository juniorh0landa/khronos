# khronos
Khronos é uma programação em python desenvolvida para gerar relatórios de tempo de viagem como atividade do processo seletivo para vaga de estágio da SMTT.

### Bibliotecas
Foram utilizadas as seguintes bibliotecas para a execução correta do programa:
- **pandas**: Para leitura, organização e análise dos dados fornecidos de forma simples e prática;
- **matplotlib**: Utilizado para a visualização de dados;
- **os**: Utilizado para a criação do diretório onde o relatório com os resultados ficará armazenado.

### Considerações Iniciais
Um dos relatórios que serve como base para tomada de decisão é o **Relatório de Tempo de Viagem**, no qual é possível ter acesso a indicadores importantes para a avaliação da qualidade do sistema, como atraso, adiantamento e cumprimento de viagem.
- Se caracteriza como atraso a viagem com horário realizado após o horário previsto;
- Adiantamento de viagem é quando o horário realizado é antes do horário previsto;
- Cumprimento de viagem é quando a viagem foi realizada (as não realizadas não possuem valor em "hora realizada").

### Objetivos
A partir do problema proposto, os objetivos seguidos para que fosse possível a conclusão do projeto foram os seguintes:
1. Ler os dados;
2. Cálculo dos indicadores de viagens (atrasos, adiantamentos, realizações);
3. Gerar os gráficos da melhor maneira possível;
4. Gerar os relatórios (Visão geral dos indicadores por empresa, e outro mais detalhado para cada indicador).

### Passo a passo
A seguir, os passos seguidos a fim de concluir os objetivos estabelecidos anteriormente:

1. Foram lidos os dados localizados na pasta **_"/dados/"_** com a própria função do pandas;

2. Para análise dos dados, foi criada uma função, **_dataAnalyze()_**, que permitisse a criação de DataFrames com os indicadores calculados e outras informações relevantes para a criação dos relatórios mais a frente, levando em consideração qual o tipo de informação a ser levado em conta. Para este caso, foram considerados as colunas referente a **_empresas_** e ao **_número da linha_**;

3. Para a geração dos gráficos, foi criada uma função, **_createCharts()_**, onde recebe o DataFrame já com as restrições de dados, para que fosse possível a criação de gráficos mais detalhados se requerido pelo usuário. Além disso, para a criação de gráficos mais detalhados, outras informações são retornadas, como a média de determinado indicador (seja ele, atrasos, adiantamentos, ou cumprimentos de viagens) por empresa e quantas linhas de ônibus daquela empresa ultrapassaram esta média;

4. Para isso, antes de tudo, foi verificado se a pasta de resultados existia, caso contrário, seria criada e os relatórios seriam escritos. O primeiro, contém gráficos com todos os indicadores de maneira resumida por empresa separado em tópicos, e que ao clicar no título de cada tópico, o usuário é encaminhado para o relatório mais detalhado sobre o indicador escolhido. Após o encaminhamento, é possível ver uma página com dados sobre o indicador em cada tópico separado por empresas, as quais estão ordenadas de acordo com a página anterior. Além do gráfico, mostrando o indicador por linha de cada empresa, é possível saber qual foi a média, e quais as linhas daquela empresa ultrapassaram e quais não ultrapassaram ela.

### Informações complementares
1. O arquivo em python a ser executado, encontra-se na pasta **_"/base/"_**;
2. A página inicial do relatório, que será criada a partir da execução do código na pasta **_/output/_**, foi gerada em html e tem o nome **_'index.htm'_**
