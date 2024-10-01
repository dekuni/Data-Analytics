import streamlit as st
from PIL import Image
import time


# Set the theme of the page
st.set_page_config(layout="centered")  # Abas no meio da página
st.title("Análise de dados: explorando dados da Pesquisa Nacional por Amostra de Domicílios (PNAD) COVID19")  # Adicionado título

# Create tabs
tab1, tab2, tab3 = st.tabs(["Introdução", "Características clínicas dos sintomas", "Conclusão"])

# Tab 1: Introdução
with tab1:
    st.write("**Alunos:**\n\n Daniel Guimarães Carvalho,\n\n danielccl.gui.dc@gmail.com\n\n ALEX FELIPE PINHATARI RODRIGUES FILHO, \n\n ALEX.FRODRIGUES71@GMAIL.COM\n\n GABRIEL INACIO VIEIRA MARTINS,\n\n gabriel_inacio54@outlook.com")
    st.divider()
    st.header("Introdução")
    st.divider()
    st.write("A análise aqui apresentada se baseia nos dados da Pesquisa Nacional por Amostra de Domicílios (PNAD COVID-19), que foi elaborada para monitorar os impactos da pandemia sobre a saúde e o mercado de trabalho no Brasil. Utilizando o poder de processamento do Google Cloud BigQuery, organizamos e exploramos esses dados para obter uma visão clara sobre o comportamento da população e os desafios enfrentados durante o período mais crítico da COVID-19. O estudo foca em entender a distribuição dos sintomas mais comuns, as características demográficas dos indivíduos afetados, e como a pandemia impactou diferentes setores econômicos.")
    st.write("A pesquisa, realizada entre maio e novembro de 2020, investigou sintomas gripais associados à COVID-19 em mais de 193 mil domicílios por mês, cobrindo todo o território nacional. Os entrevistados foram questionados sobre o tipo de sintoma que apresentaram, as ações que tomaram para aliviá-los e se procuraram atendimento médico. No campo econômico, a pesquisa categorizou a força de trabalho entre ocupados, desocupados e indivíduos fora do mercado, abordando também temas como o trabalho remoto, afastamentos e rendimentos durante o período.")
    st.write("Este projeto foi desenvolvido com foco em três áreas principais: sintomas clínicos, comportamento populacional e características econômicas. Para realizar essas análises, foram elaboradas queries SQL no Google Cloud BigQuery, que permitiram o processamento de grandes volumes de dados de forma eficiente. A interface interativa foi desenvolvida utilizando Streamlit, possibilitando a visualização de dados de forma dinâmica e acessível, com gráficos e tabelas que detalham as informações mais relevantes.")
    st.write("Ao longo da análise, exploramos perguntas como 'Quais foram os sintomas mais frequentes entre aqueles que procuraram atendimento médico?', 'Como os resultados dos testes de COVID-19 variaram entre diferentes grupos demográficos?', e 'Quais setores da economia foram mais atingidos?'. As respostas a essas perguntas nos ajudam a identificar padrões de comportamento e fornecer recomendações para ações de saúde pública e políticas sociais em casos de futuros surtos.")
    st.write("Desta forma, este estudo não só oferece uma visão detalhada dos impactos da COVID-19, mas também fornece uma ferramenta poderosa para gestores de saúde e formuladores de políticas públicas, que podem utilizar essas informações para melhorar o planejamento e a resposta em situações de emergência sanitária.")
    st.divider()
    st.write("Repositório do GIT: \n\n https://github.com/dekuni/Data-Analytics")
# Tab 2: Características clínicas dos sintomas
with tab2:
    st.header("Questões")
    st.write("Questões relacionadas a características clínicas dos sintomas!")
    sintomas_tabs = st.tabs(["Característica da População", "Dados Socioeconômicos", "Características clínicas dos sintomas"])
    
    for i, tab_name in enumerate(sintomas_tabs):
        with sintomas_tabs[i]:
            if i == 0:
                st.header("Característica da População")
                questions = ["Qual a distribuição etária entre os entrevistados?", "Qual é a distribuição de cor/raça entre os estados brasileiros?", "Como era a frequência de infecção por COVID-19 por faixa etária?", "Como está a distribuição dos entrevistados com escolaridade por estado?"]
                descriptions = ["**ANÁLISE**:\n\nA distribuição etária dos entrevistados mostra que a maior parte está nas faixas de 21 a 50 anos, indicando uma predominância de adultos em idade economicamente ativa. As faixas de 0 a 10 anos e acima de 80 anos têm menos representatividade, apesar de os idosos serem mais vulneráveis à COVID-19. A distribuição entre homens e mulheres é semelhante, com uma leve predominância feminina nas faixas de 41 a 60 anos. Essas informações são importantes para entender como diferentes grupos etários foram impactados pela pandemia.",
                                "**ANÁLISE**:\n\nA distribuição de cor/raça entre os estados brasileiros revela uma grande diversidade, refletindo as diferenças regionais e históricas do país. Nos estados do Norte e Nordeste, como Amazonas, Bahia e Maranhão, observa-se uma predominância da população parda, que representa uma parte significativa da população local. A população preta é mais representativa em estados como Bahia e Minas Gerais, que possuem uma forte influência de descendentes africanos.\n\nPor outro lado, a população branca tem uma maior concentração em estados do Sul, como Rio Grande do Sul, Paraná e Santa Catarina, além de São Paulo e Espírito Santo, onde há uma forte herança de imigração europeia. A presença de indígenas é mais acentuada em estados da região Norte, como Amazonas e Roraima, áreas que abrigam muitas comunidades indígenas.\n\nEsses padrões demográficos refletem a diversidade étnica e cultural do Brasil, resultante de fatores como colonização, imigração e a presença de povos originários em diferentes regiões.",
                                "**ANÁLISE**:\n\nA análise da frequência de infecção por COVID-19 por faixa etária, com base nos resultados dos testes, demonstra que as faixas etárias de 31 a 50 anos possuem a maior incidência de testes, tanto positivos quanto negativos, sendo a faixa de 31 a 40 anos a que apresenta o maior número de testes positivos. No entanto, os testes negativos predominam em todas as faixas etárias.\n\nOs indivíduos de 21 a 30 anos e de 41 a 50 anos também foram amplamente testados, mas com uma maior quantidade de testes negativos, o que sugere uma ampla testagem, mas com menor confirmação de infecções. A faixa de 51 a 60 anos segue uma tendência semelhante, com um equilíbrio relativo entre resultados positivos e negativos, mas os testes negativos continuam sendo majoritários.\n\nAs faixas etárias de 0 a 10 anos e acima de 80 anos têm o menor número de testes realizados, tanto positivos quanto negativos, o que pode indicar menor testagem ou menor exposição ao vírus em comparação com outros grupos.\n\nEm relação aos resultados pendentes, representados pela cor verde, eles são distribuídos de maneira relativamente uniforme entre as faixas etárias, mas em menor número. Os resultados inconclusivos e ignorados são mínimos, sugerindo uma alta precisão nos resultados obtidos.\n\nDe modo geral, a análise indica que, apesar de todas as faixas etárias serem testadas, os grupos de 31 a 60 anos são os mais afetados em termos de quantidade de testes positivos e negativos, evidenciando uma maior exposição ou preocupação com essa população específica.",
                                "**ANÁLISE**:\n\nA distribuição dos entrevistados por estado, em termos de escolaridade, revela variações significativas entre os diferentes estados do Brasil. Estados como Minas Gerais, São Paulo, Bahia e Paraná se destacam por ter o maior número de entrevistados, sendo Minas Gerais o que mais se sobressai. Nesses estados, a escolaridade predominante é o Fundamental Incompleto, o que indica que uma parte considerável da população ainda não completou os níveis educacionais básicos, refletindo um padrão comum em diversas partes do país.\n\nPor outro lado, o Médio Completo é uma categoria de destaque em estados como São Paulo, Paraná e Rio Grande do Sul, que são regiões mais desenvolvidas economicamente. Isso sugere que, nessas áreas, há maior acesso à educação e uma parte significativa da população consegue concluir o ensino médio. No entanto, em estados do Norte e Nordeste, como Bahia, Maranhão e Pará, é notória a presença de entrevistados sem instrução, evidenciando dificuldades no acesso à educação nessas regiões.\n\nO nível de escolaridade mais elevado, como Superior Completo e Pós-graduação, aparece com menos frequência em todo o país, sendo mais comum em estados economicamente mais fortes, como o Distrito Federal, que concentra a maior proporção de pessoas com educação superior, devido à sua natureza como centro administrativo. Esse padrão se reflete também em estados como São Paulo e Rio Grande do Sul, onde a população tem maior acesso a oportunidades de ensino superior.\n\nPor fim, estados menos populosos, como Acre e Roraima, têm menor número de entrevistados, o que reflete suas populações mais reduzidas e, muitas vezes, menor infraestrutura educacional. Nesses locais, há uma maior prevalência de pessoas com Fundamental Incompleto e Sem Instrução, em contraste com os estados do Sul e Sudeste, que possuem maior equilíbrio entre os diferentes níveis educacionais. A análise geral sugere que o desenvolvimento socioeconômico tem uma forte correlação com o nível de escolaridade alcançado pela população em cada estado."]
                
                for j, (question, description) in enumerate(zip(questions, descriptions)):  # Alterado para usar lista de perguntas e descrições
                    st.write(question)  # Mostrar a pergunta antes do botão  # Adicionando o divider após a pergunta
                    if st.button(f"Gráfico {j+1}", key=f"grafico_populacao_{j}"):
                        with st.spinner('Gráfico Carregando..'):
                            time.sleep(1)
                        image = Image.open(f'caracteristica_populacao_{j+1}.jpg')
                        st.image(image, caption=f'Gráfico {j+1} de Característica da População')
                        st.divider()  # Adicionando o divider após o gráfico
                        st.write(description)
                        st.divider()
                    # Adicionando o divider após a descrição
                    if st.button(f"Query {j+1}", key=f"query_populacao_{j}"):
                        with st.spinner('Carregando Query..'):
                            time.sleep(1)                        # Adicionado botão para mostrar Query
                        st.write(f'Query sobre a população')
                        if j == 0:
                            st.code("""WITH 
dicionario_a003 AS (
    SELECT
        chave AS chave_a003,
        valor AS descricao_a003
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        nome_coluna = 'a003'
        AND id_tabela = 'microdados'
)
SELECT
    descricao_a003 AS Genero,
    CASE
        WHEN CAST(dados.a002 AS INT64) BETWEEN 0 AND 10 THEN '0 a 10 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 11 AND 20 THEN '11 a 20 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 21 AND 30 THEN '21 a 30 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 31 AND 40 THEN '31 a 40 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 41 AND 50 THEN '41 a 50 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 51 AND 60 THEN '51 a 60 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 61 AND 70 THEN '61 a 70 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 71 AND 80 THEN '71 a 80 anos' 
        WHEN CAST(dados.a002 AS INT64) > 80 THEN 'Acima de 80 anos'
        ELSE 'Idade não especificada'
    END AS Faixa_Etaria,
    COUNT(*) AS Frequencia
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN `dicionario_a003`
    ON dados.a003 = chave_a003
WHERE CAST(dados.a002 AS INT64) IS NOT NULL
GROUP BY 1, 2 
ORDER BY Frequencia DESC;
""", language="sql")
                            
                        if j == 1:
                            st.code("""WITH 
dicionario_a004 AS (
    SELECT
        chave AS chave_a004,
        valor AS descricao_a004
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        nome_coluna = 'a004'
        AND id_tabela = 'microdados'
)
SELECT
    dados.sigla_uf AS sigla_uf,
    diretorio_sigla_uf.nome AS Estados,
    descricao_a004 AS Raca,
    COUNT(*) AS frequencia  -- Contando a frequência de cada combinação
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN (SELECT DISTINCT sigla, nome FROM `basedosdados.br_bd_diretorios_brasil.uf`) AS diretorio_sigla_uf
    ON dados.sigla_uf = diretorio_sigla_uf.sigla
LEFT JOIN `dicionario_a004`
    ON dados.a004 = chave_a004
GROUP BY dados.sigla_uf, diretorio_sigla_uf.nome, descricao_a004;
""", language="sql")
                        st.divider()
                        if j == 2:
                            st.code("""WITH 
dicionario_b009b AS (
    SELECT
        chave AS chave_b009b,
        valor AS descricao_b009b
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b009b'
        AND id_tabela = 'microdados'
)
SELECT
    CASE 
        WHEN CAST(dados.a002 AS INT64) BETWEEN 0 AND 10 THEN '0 a 10 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 11 AND 20 THEN '11 a 20 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 21 AND 30 THEN '21 a 30 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 31 AND 40 THEN '31 a 40 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 41 AND 50 THEN '41 a 50 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 51 AND 60 THEN '51 a 60 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 61 AND 70 THEN '61 a 70 anos'
        WHEN CAST(dados.a002 AS INT64) BETWEEN 71 AND 80 THEN '71 a 80 anos'
        WHEN CAST(dados.a002 AS INT64) > 80 THEN 'Acima de 80 anos'
        ELSE 'Idade não especificada'
    END AS Faixa_Etaria,
    descricao_b009b AS Teste_Covid,
    COUNT(*) AS contagem 
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN `dicionario_b009b`
    ON dados.b009b = chave_b009b
WHERE
    dados.a002 IS NOT NULL
    AND descricao_b009b IS NOT NULL
GROUP BY
    Faixa_Etaria, descricao_b009b;
""", language="sql")
                        if j == 3:
                            st.code("""WITH 
dicionario_a005 AS (
    SELECT
        chave AS chave_a005,
        valor AS descricao_a005
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'a005'
        AND id_tabela = 'microdados'
)
SELECT
    diretorio_sigla_uf.nome AS Estados,
    descricao_a005 AS Escolaridade
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN (SELECT DISTINCT sigla, nome FROM `basedosdados.br_bd_diretorios_brasil.uf`) AS diretorio_sigla_uf
    ON dados.sigla_uf = diretorio_sigla_uf.sigla
LEFT JOIN `dicionario_a005`
    ON dados.a005 = chave_a005
WHERE 
    descricao_a005 IS NOT NULL
    AND diretorio_sigla_uf.nome IS NOT NULL;
""", language="sql")

# Adicionado Query
            elif i == 1:
                st.header("Dados Socioeconômicos")
                questions = ["Qual é a proporção de pessoas que frequentam escola ou faculdade em áreas urbanas em comparação com áreas rurais?", "Quantas pessoas, no total, estavam temporariamente afastadas do trabalho durante o período da pandemia e por quais motivos?", "Qual é a distribuição dos tipos de contrato de trabalho (formal/informal) entre os diferentes estados?", "Como a pandemia afetou o nível de renda dos trabalhadores (quantos continuaram a ser remunerados, mesmo que parcialmente)?"]
                descriptions = ["**ANÁLISE**:\n\nO gráfico analisa o impacto da COVID-19 na frequência de pessoas que frequentam escolas ou faculdades, destacando as diferenças entre áreas urbanas e rurais. No eixo horizontal, temos as diferentes regiões categorizadas como 'Capital', 'Resto da Região Metropolitana (Resto RM)', 'Resto da Região Integrada de Desenvolvimento Econômico (Resto RIDE)' e 'Resto da Unidade da Federação (Resto UF)'. Já o eixo vertical mostra o número de pessoas em cada região, divididas entre aquelas que continuam frequentando (Sim) e aquelas que pararam (Não) durante a pandemia.\n\nNas capitais, observa-se uma distribuição mais equilibrada entre aqueles que continuam frequentando escolas ou faculdades (representado pela barra azul) e aqueles que não frequentam mais (barra vermelha). Em contrapartida, nas regiões rurais e menos urbanizadas, como no 'Resto da UF', a proporção de pessoas que pararam de frequentar instituições de ensino é muito maior, indicando um impacto mais forte da COVID-19 nessas áreas. As áreas rurais, como 'Resto RM' e 'Resto RIDE', mostram uma queda significativa na frequência escolar, com uma predominância de barras vermelhas, sugerindo dificuldades de adaptação ao ensino remoto e à continuidade dos estudos.\n\nEsses dados evidenciam as desigualdades no impacto da pandemia sobre a educação entre áreas urbanas e rurais. Enquanto nas capitais e regiões metropolitanas (Resto RM), o impacto foi menos severo, com muitas pessoas ainda frequentando instituições, as áreas mais afastadas (Resto UF e Resto RIDE) enfrentaram um declínio acentuado, sugerindo problemas de acesso à infraestrutura educacional, especialmente em tempos de ensino remoto forçado pela pandemia.",
                                "**ANÁLISE**:\n\nDurante a pandemia, o afastamento temporário de trabalhadores foi amplamente motivado por fatores diretamente relacionados às medidas de contenção da COVID-19, com o isolamento, quarentena e distanciamento social representando a principal razão para a interrupção das atividades laborais. Isso reflete o impacto generalizado das restrições sanitárias, que forçaram muitos profissionais a se afastarem temporariamente de seus postos de trabalho, especialmente em setores que não podiam operar remotamente.\n\nAlém do isolamento preventivo, outros motivos de afastamento, como licenças remuneradas por problemas de saúde ou acidentes, também foram significativos. Isso indica que, além da pandemia em si, havia uma parcela de trabalhadores que enfrentava complicações de saúde durante o período, o que pode ou não estar relacionado à COVID-19. As férias e folgas também aparecem entre os motivos, mostrando que alguns aproveitaram o contexto para usufruir de pausas programadas.\n\nOutros fatores como licenças por maternidade ou paternidade, assim como questões ocasionais, tiveram uma presença menor no total de afastamentos. Isso destaca que o afastamento foi principalmente impulsionado pela necessidade de isolamento social, com motivos tradicionais de licença tendo um papel mais secundário no contexto do período pandêmico.",
                                "**ANÁLISE**:\n\nA distribuição dos tipos de contrato de trabalho, formal e informal, varia significativamente entre os diferentes estados. Em estados como São Paulo e Minas Gerais, o trabalho formal tem maior prevalência em relação ao informal, sugerindo uma economia mais estruturada e com maior inserção de trabalhadores em empregos regulamentados. Em contrapartida, em estados como Maranhão, Alagoas e Pará, a informalidade é dominante, o que pode refletir desafios econômicos e sociais, como a falta de oportunidades de empregos formais ou a dependência de setores com menos regulamentação.\n\nEstados como Rio de Janeiro e Rio Grande do Sul apresentam uma distribuição mais equilibrada entre trabalhadores formais e informais, indicando uma coexistência significativa de ambos os tipos de contrato. Isso pode ser resultado de uma economia diversificada, onde tanto grandes empresas quanto setores mais informais têm espaço.\n\nA presença de altos índices de trabalho informal em diversas regiões do país reflete desigualdades econômicas e a dificuldade de formalização em determinadas áreas. Já nos estados onde o trabalho formal prevalece, pode-se perceber maior integração das normas trabalhistas e uma economia mais robusta, capaz de oferecer empregos com carteira assinada.",
                                "**ANÁLISE**:\n\nA pandemia de COVID-19 causou uma série de impactos econômicos significativos no Brasil, afetando de maneira profunda o mercado de trabalho. Milhões de trabalhadores enfrentaram cortes de salário, demissões e perda de oportunidades de emprego devido ao fechamento de empresas e às medidas de isolamento social. Esse cenário trouxe à tona a vulnerabilidade de muitas categorias profissionais e revelou disparidades na maneira como diferentes regiões foram afetadas pela crise.\n\n Em estados como Rio de Janeiro (RJ) e Rio Grande do Norte (RN), observa-se uma disparidade acentuada entre trabalhadores remunerados e não remunerados, indicando uma vulnerabilidade maior desses mercados de trabalho durante o período da crise. Essas regiões, em particular, destacam-se pelo número alarmante de pessoas que perderam sua fonte de renda, seja devido ao fechamento de empresas, demissões ou suspensões temporárias de contrato.\n\n Apesar desse cenário generalizado, alguns estados como Maranhão (MA), Ceará (CE) e Mato Grosso (MT) apresentam uma proporção mais equilibrada de trabalhadores que conseguiram manter algum tipo de remuneração, o que pode indicar a presença de políticas locais ou setores econômicos mais resilientes. Esses resultados mostram que, embora o impacto da pandemia tenha sido nacional, os efeitos sobre a renda dos trabalhadores foram sentidos de maneira desigual entre as regiões, refletindo as particularidades econômicas e políticas de cada estado."]
                for j, (question, description) in enumerate(zip(questions, descriptions)):  # Alterado para usar lista de perguntas e descrições
                    st.write(question)  # Mostrar a pergunta antes do botão
                    if st.button(f"Gráfico {j+1}", key=f"grafico_socioeconomicos_{j}"):
                        with st.spinner('Gráfico Carregando..'):
                            time.sleep(1)# Adicionado key
                        image = Image.open(f'dados_socioeconomicos_{j+1}.jpg')
                        st.image(image, caption=f'Gráfico {j+1} de Dados Socioeconômicos')
                        st.write(description)  # Mostrar a descrição específica para cada gráfico
                    if st.button(f"Query {j+1}", key=f"query_socioeconomicos_{j}"):
                        with st.spinner('Gráfico Carregando..'):
                            time.sleep(1)# Adicionado botão para mostrar Query
                        st.write("Query para a análise dos dados socioeconômicos")
                        if j == 0:
                            st.code("""WITH 
dicionario_v1023 AS (
    SELECT
        chave AS chave_v1023,
        valor AS descricao_v1023
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        nome_coluna = 'v1023'
        AND id_tabela = 'microdados'
),
dicionario_a006 AS (
    SELECT
        chave AS chave_a006,
        valor AS descricao_a006
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        nome_coluna = 'a006'
        AND id_tabela = 'microdados'
)
SELECT
    descricao_v1023 AS Area,
    COALESCE(descricao_a006, 'Não') AS Frequencia,
    COUNT(*) AS Frequencia_uso
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN `dicionario_v1023`
    ON dados.v1023 = chave_v1023
LEFT JOIN `dicionario_a006`
    ON dados.a006 = chave_a006
WHERE
    descricao_v1023 IS NOT NULL
    AND descricao_a006 IS NOT NULL
GROUP BY descricao_v1023, COALESCE(descricao_a006, 'Não');
""", language="sql")
                        if j == 1:
                            st.code("""WITH 
dicionario_c002 AS (
    SELECT
        chave AS chave_c002,
        valor AS descricao_c002
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c002'
        AND id_tabela = 'microdados'
),
dicionario_c003 AS (
    SELECT
        chave AS chave_c003,
        valor AS descricao_c003
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c003'
        AND id_tabela = 'microdados'
)
SELECT
    descricao_c002 AS Foi_Afastado,
    descricao_c003 AS Motivo,
    COUNT(*) AS frequencia  
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN `dicionario_c002`
    ON dados.c002 = chave_c002
LEFT JOIN `dicionario_c003`
    ON dados.c003 = chave_c003
WHERE
    descricao_c002 IS NOT NULL 
    AND descricao_c003 IS NOT NULL
GROUP BY 
    descricao_c002, 
    descricao_c003;  
""", language="sql")
                        if j == 2:
                            st.code("""WITH 
dicionario_c007 AS (
    SELECT
        chave AS chave_c007,
        valor AS descricao_c007
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c007'
        AND id_tabela = 'microdados'
)
SELECT
    dados.sigla_uf AS sigla_uf,
    diretorio_sigla_uf.nome AS Estados,
    descricao_c007 AS Trabalho,
    COUNT(*) AS frequencia  
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN (SELECT DISTINCT sigla, nome FROM `basedosdados.br_bd_diretorios_brasil.uf`) AS diretorio_sigla_uf
    ON dados.sigla_uf = diretorio_sigla_uf.sigla
LEFT JOIN `dicionario_c007`
    ON dados.c007 = chave_c007
WHERE 
    dados.sigla_uf IS NOT NULL
    AND descricao_c007 IS NOT NULL 
GROUP BY 
    dados.sigla_uf, 
    diretorio_sigla_uf.nome, 
    descricao_c007
""", language='sql')
                        if j == 3:
                            st.code("""WITH 
dicionario_c004 AS (
    SELECT
        chave AS chave_c004,
        valor AS descricao_c004
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c004'
        AND id_tabela = 'microdados'
)
SELECT
    dados.sigla_uf AS sigla_uf,
    diretorio_sigla_uf.nome AS Estados,
    descricao_c004 AS Remunerado,
    COUNT(*) AS frequencia  
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN (SELECT DISTINCT sigla, nome FROM `basedosdados.br_bd_diretorios_brasil.uf`) AS diretorio_sigla_uf
    ON dados.sigla_uf = diretorio_sigla_uf.sigla
LEFT JOIN `dicionario_c004`
    ON dados.c004 = chave_c004
WHERE
    descricao_c004 IS NOT NULL 
GROUP BY
    dados.sigla_uf,
    diretorio_sigla_uf.nome,
    descricao_c004;  
""", language='sql')                    
 # Adicionado Query
            else:
                st.header("Características clínicas dos sintomas")
                questions = ["Qual é a frequência dos sintomas mais relatados entre aqueles que procuraram ajuda médica?", "Qual foi o resultado de teste de covid por cor/raça?", "Qual é a comparação entre os entrevistados que foram internados e os que foram entubados?", "Quais foram as áreas de trabalho mais afetadas pela Covid entre os entrevistados?"]
                descriptions = ["**ANÁLISE**:\n\nA análise da frequência dos sintomas mais reportados por pessoas que procuraram ajuda médica revela que os sintomas mais comuns foram dor de cabeça, tosse, e nariz entupido. A dor de cabeça, em particular, se destaca com mais de 70.000 registros, sendo o sintoma mais frequente entre os entrevistados. A tosse, um sinal clássico de problemas respiratórios, teve mais de 40.000 ocorrências, refletindo a preocupação das pessoas com sintomas respiratórios, especialmente no contexto da pandemia de COVID-19. Esses dois sintomas, juntamente com o nariz entupido, são indicativos de infecções respiratórias e possivelmente foram os mais preocupantes para quem procurou atendimento médico.\n\nOutros sintomas, como febre e dor de garganta, também foram bastante reportados, com ambos os sintomas sendo comumente associados a infecções virais, reforçando seu papel como indicadores primários que motivam a busca por cuidados de saúde. Sintomas mais graves, como dificuldade para respirar e dor no peito, embora menos frequentes, são notáveis pela sua gravidade. Esses sintomas muitas vezes estão associados a casos mais sérios e, portanto, podem ter sido razões para uma resposta médica mais imediata, mesmo que não tenham sido tão comuns quanto os sintomas mais leves.\n\nPor outro lado, sintomas como diarreia e náusea foram menos frequentes, sugerindo que, embora sejam conhecidos como sintomas da COVID-19 e outras infecções, não foram os principais motivos para buscar atendimento médico. Fadiga, dor muscular e perda de cheiro ou sabor tiveram uma presença significativa, o que pode estar relacionado ao fato de serem sintomas persistentes e distintivos da COVID-19, levando uma parcela relevante das pessoas a procurar ajuda médica. O gráfico reflete uma distribuição variada de sintomas, com destaque para aqueles mais associados a infecções respiratórias e seus impactos na decisão de buscar atendimento.",
                                "**ANÁLISE**:\n\nO gráfico de frequência dos resultados de testes de COVID-19 por cor/raça revela diferenças claras nos números de testes e nos resultados entre os diversos grupos raciais. A maior concentração de resultados está entre as pessoas que se identificam como brancas e pardas. Esses grupos apresentaram o maior número de testes, com predominância de resultados negativos, seguidos pelos positivos. Nos dois casos, o número de resultados negativos ultrapassa os 20.000, enquanto os positivos ficam em torno de 10.000 para o grupo branco e 8.000 para o pardo.\n\nPessoas que se identificam como pretas aparecem em menor quantidade de testes comparado aos grupos branco e pardo. Ainda assim, o número de resultados negativos (cerca de 5.000) e positivos (aproximadamente 2.500) é relevante, mas significativamente menor. Já para os grupos de raça amarela e indígena, as frequências de testes são extremamente baixas, quase insignificantes quando comparadas aos outros grupos, com poucos resultados reportados tanto como positivos quanto negativos.\n\nAlém disso, há uma pequena quantidade de testes que ainda não receberam resultado em todas as categorias, com destaque para os grupos branco e pardo. Casos inconclusivos e resultados ignorados são mínimos em todas as raças. Isso pode refletir fatores como a acessibilidade a testes, variáveis socioeconômicas ou demográficas que influenciam o acesso aos exames, além de possíveis diferenças na exposição ao vírus entre os grupos raciais.",
                                "**ANÁLISE**:\n\nO gráfico mostra uma clara distinção entre os sintomas apresentados por entrevistados internados e aqueles que foram entubados. Para todos os três sintomas analisados — tosse, dor no peito e dificuldade para respirar —, os internados apresentam uma frequência maior em comparação com os entubados.\n\nA tosse aparece como o sintoma mais comum entre os internados, enquanto os entubados também relatam esse sintoma, mas em menor proporção. A dor no peito segue um padrão semelhante, sendo mais prevalente entre os internados. No entanto, a dificuldade para respirar, embora mais comum entre os internados, é um sintoma fortemente associado aos entubados, sugerindo sua gravidade em casos mais críticos.\n\nEsses dados indicam que, apesar de os internados apresentarem mais sintomas de forma geral, a dificuldade para respirar se destaca como um possível fator determinante na necessidade de entubação.",
                                "**ANÁLISE**:\n\nO gráfico sobre a frequência de testes positivos para COVID-19 por área de trabalho mostra que os setores mais afetados entre os entrevistados foram os de saúde humana e assistência social. Esse campo aparece como o mais impactado, com uma frequência consideravelmente maior de casos positivos em comparação com as demais áreas. Esse resultado pode ser explicado pela exposição constante dos trabalhadores desse setor a ambientes de risco, especialmente no contato direto com pacientes.\n\nOutras áreas afetadas incluem a administração pública (governo federal, estadual e municipal) e a indústria da transformação, ambas apresentando uma quantidade relevante de casos positivos, embora bem menores em relação ao setor de saúde. A educação também aparece como uma das áreas afetadas, sugerindo que profissionais dessa área foram expostos ao vírus, possivelmente durante interações com o público ou devido à reabertura de atividades escolares durante a pandemia.\n\nPor fim, o gráfico também mostra uma categoria denominada outros, que agrupa áreas diversas e apresenta uma quantidade de casos semelhantes à da educação. Isso indica que, embora a pandemia tenha afetado muitos setores, os profissionais de saúde foram os mais impactados, provavelmente devido à natureza de seu trabalho em ambientes de alto risco de contágio."]
            
                # Move o loop for acima da definição de sql_queries
                for j, (question, description) in enumerate(zip(questions, descriptions)):  # Alterado para usar lista de perguntas e descrições
                    st.write(question)  # Mostrar a pergunta antes do botão
                    if st.button(f"Gráfico {j+1}", key=f"grafico_sintomas_{j}"):
                        with st.spinner('Gráfico Carregando..'):
                            time.sleep(1)# Adicionado key
                        image = Image.open(f'sintomas_{j+1}.jpg')
                        st.image(image, caption=f'Gráfico {j+1} de Sintomas')
                        st.write(description)
                    if st.button(f"Query {j+1}", key=f"query_sintomas_{j}"):
                        with st.spinner('Gráfico Carregando..'):
                            time.sleep(1)# Adicionado botão para mostrar Query
                        if j == 0:
                            st.code("""
                    WITH 
                    dicionario_b0011 AS (
                        SELECT
                            chave AS chave_b0011,
                            valor AS descricao_b0011
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0011'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0012 AS (
                        SELECT
                            chave AS chave_b0012,
                            valor AS descricao_b0012
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0012'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0013 AS (
                        SELECT
                            chave AS chave_b0013,
                            valor AS descricao_b0013
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0013'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0014 AS (
                        SELECT
                            chave AS chave_b0014,
                            valor AS descricao_b0014
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0014'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0015 AS (
                        SELECT
                            chave AS chave_b0015,
                            valor AS descricao_b0015
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0015'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0016 AS (
                        SELECT
                            chave AS chave_b0016,
                            valor AS descricao_b0016
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0016'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0017 AS (
                        SELECT
                            chave AS chave_b0017,
                            valor AS descricao_b0017
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0017'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0018 AS (
                        SELECT
                            chave AS chave_b0018,
                            valor AS descricao_b0018
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0018'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b0019 AS (
                        SELECT
                            chave AS chave_b0019,
                            valor AS descricao_b0019
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b0019'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b00110 AS (
                        SELECT
                            chave AS chave_b00110,
                            valor AS descricao_b00110
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b00110'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b00111 AS (
                        SELECT
                            chave AS chave_b00111,
                            valor AS descricao_b00111
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b00111'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b00112 AS (
                        SELECT
                            chave AS chave_b00112,
                            valor AS descricao_b00112
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b00112'
                        AND id_tabela = 'microdados'
                    ),
                    dicionario_b00113 AS (
                        SELECT
                            chave AS chave_b00113,
                            valor AS descricao_b00113
                        FROM `basedosdados.br_ibge_pnad_covid.dicionario`
                        WHERE nome_coluna = 'b00113'
                        AND id_tabela = 'microdados'
                    )
                    SELECT 
                        'Febre' AS Sintoma, 
                        COUNT(CASE WHEN dados.b0011 = '1' THEN 1 END) AS Sim,
                        COUNT(CASE WHEN dados.b0011 = '2' THEN 1 END) AS Nao
                    FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
                    LEFT JOIN dicionario_b0011 ON dados.b0011 = chave_b0011
                    WHERE dados.b0011 IS NOT NULL
                    UNION ALL
                    SELECT 
                        'Tosse' AS Sintoma, 
                        COUNT(CASE WHEN dados.b0012 = '1' THEN 1 END) AS Sim,
                        COUNT(CASE WHEN dados.b0012 = '2' THEN 1 END) AS Nao
                    FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
                    LEFT JOIN dicionario_b0012 ON dados.b0012 = chave_b0012
                    WHERE dados.b0012 IS NOT NULL
                    UNION ALL
                    SELECT 
                        'Dor de Garganta' AS Sintoma, 
                        COUNT(CASE WHEN dados.b0013 = '1' THEN 1 END) AS Sim,
                        COUNT(CASE WHEN dados.b0013 = '2' THEN 1 END) AS Nao
                    FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
                    LEFT JOIN dicionario_b0013 ON dados.b0013 = chave_b0013
                    WHERE dados.b0013 IS NOT NULL
                    UNION ALL
                    SELECT 
                        'Dificuldade para Respirar' AS Sintoma, 
                        COUNT(CASE WHEN dados.b0014 = '1' THEN 1 END) AS Sim,
                        COUNT(CASE WHEN dados.b0014 = '2' THEN 1 END) AS Nao
                    FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
                    LEFT JOIN dicionario_b0014 ON dados.b0014 = chave_b0014
                    WHERE dados.b0014 IS NOT NULL
                    UNION ALL
                    SELECT 
                        'Dor de Cabeça' AS Sintoma, 
                        COUNT(CASE WHEN dados.b0015 = '1' THEN 1 END) AS Sim,
                        COUNT(CASE WHEN dados.b0015 = '2' THEN 1 END) AS Nao
                    FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
                    LEFT JOIN dicionario_b0015 ON dados.b0015 = chave_b0015
                    WHERE dados.b0015 IS NOT NULL
                    UNION ALL
                    SELECT 
                        'Dor no Peito' AS Sintoma, 
                        COUNT(CASE WHEN dados.b0016 = '1' THEN 1 END) AS Sim,
                        COUNT(CASE WHEN dados.b0016 = '2' THEN 1 END) AS Nao
""", language="sql")
                        if j == 1:  # Verifica se é o gráfico 2
                            st.code(""" 
WITH 
dicionario_a004 AS (
    SELECT
        chave AS chave_a004,
        valor AS descricao_a004
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'a004'
        AND id_tabela = 'microdados'
),
dicionario_b009b AS (
    SELECT
        chave AS chave_b009b,
        valor AS descricao_b009b
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b009b'
        AND id_tabela = 'microdados'
)
SELECT
    descricao_a004 AS Raca,
    descricao_b009b AS Teste_de_Covid,
    COUNT(*) AS Frequencia
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN `dicionario_a004`
    ON dados.a004 = chave_a004
LEFT JOIN `dicionario_b009b`
    ON dados.b009b = chave_b009b
WHERE
    descricao_a004 IS NOT NULL
    AND descricao_b009b IS NOT NULL
GROUP BY
    descricao_a004,
    descricao_b009b
ORDER BY
    Raca, Teste_de_Covid;
                            """, language="sql")  # Adicionado código SQL para gráfico 2
                        elif j == 2:  # Verifica se é o gráfico 3
                            st.code(""" 
WITH 
dicionario_b0012 AS (
    SELECT
        chave AS chave_b0012,
        valor AS descricao_b0012
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0012'
        AND id_tabela = 'microdados'
),
dicionario_b0014 AS (
    SELECT
        chave AS chave_b0014,
        valor AS descricao_b0014
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0014'
        AND id_tabela = 'microdados'
),
dicionario_b0016 AS (
    SELECT
        chave AS chave_b0016,
        valor AS descricao_b0016
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b0016'
        AND id_tabela = 'microdados'
),
dicionario_b005 AS (
    SELECT
        chave AS chave_b005,
        valor AS descricao_b005
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b005'
        AND id_tabela = 'microdados'
),
dicionario_b006 AS (
    SELECT
        chave AS chave_b006,
        valor AS descricao_b006
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'b006'
        AND id_tabela = 'microdados'
)
SELECT
    descricao_b0012 AS Tosse,
    descricao_b0014 AS Dor_no_Peito,
    descricao_b0016 AS Dificuldade_para_Respirar,
    descricao_b005 AS Internado,
    descricao_b006 AS Entubado
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN `dicionario_b0012`
    ON dados.b0012 = chave_b0012
LEFT JOIN `dicionario_b0014`
    ON dados.b0014 = chave_b0014
LEFT JOIN `dicionario_b0016`
    ON dados.b0016 = chave_b0016
LEFT JOIN `dicionario_b005`
    ON dados.b005 = chave_b005
LEFT JOIN `dicionario_b006`
    ON dados.b006 = chave_b006
WHERE 
    descricao_b0012 IS NOT NULL AND descricao_b0012 != 'Não sabe'
    AND descricao_b0014 IS NOT NULL AND descricao_b0014 != 'Não sabe'
    AND descricao_b0016 IS NOT NULL AND descricao_b0016 != 'Não sabe'
    AND descricao_b005 IS NOT NULL AND descricao_b005 != 'Não sabe'
    AND descricao_b006 IS NOT NULL AND descricao_b006 != 'Não sabe';
                            """, language="sql")  # Adicionado código SQL para gráfico 3
                        elif j == 3:  # Verifica se é o gráfico 4
                            st.code(""" 
WITH 
dicionario_c007 AS (
    SELECT
        chave AS chave_c007,
        valor AS descricao_c007
    FROM `basedosdados.br_ibge_pnad_covid.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'c007'
        AND id_tabela = 'microdados'
)
SELECT
    dados.sigla_uf AS sigla_uf,
    diretorio_sigla_uf.nome AS Estados,
    descricao_c007 AS Trabalho,
    COUNT(*) AS frequencia  -- Adiciona a frequência de cada linha
FROM `basedosdados.br_ibge_pnad_covid.microdados` AS dados
LEFT JOIN (SELECT DISTINCT sigla, nome FROM `basedosdados.br_bd_diretorios_brasil.uf`) AS diretorio_sigla_uf
    ON dados.sigla_uf = diretorio_sigla_uf.sigla
LEFT JOIN `dicionario_c007`
    ON dados.c007 = chave_c007
WHERE 
    dados.sigla_uf IS NOT NULL  -- Remove valores nulos da sigla_uf
    AND descricao_c007 IS NOT NULL  -- Remove valores nulos da descrição
GROUP BY 
    dados.sigla_uf, 
    diretorio_sigla_uf.nome, 
    descricao_c007;
                            """, language="sql")  # Adicionado código SQL para gráfico 4

# Tab 3: Conclusão
with tab3:
    st.header("Conclusão")
    st.divider()
    st.write("A investigação realizada com os dados da PNAD-COVID 19, utilizando a infraestrutura do Google Cloud BigQuery, trouxe insights valiosos para a formulação de estratégias que podem ser implementadas em caso de um novo surto de COVID-19. No decorrer do estudo, focamos em três áreas essenciais: os sintomas clínicos reportados, o comportamento da população ao longo da pandemia e as condições econômicas que permeiam a sociedade.")
    st.write("Os dados coletados revelaram que os sintomas mais frequentes incluíram dor de cabeça, tosse e dificuldade para respirar, sugerindo que esses sinais devem ser priorizados no monitoramento futuro. Também ficou claro que as populações mais vulneráveis enfrentaram maiores desafios e complicações, o que reforça a necessidade de um foco especial no atendimento a esses grupos em situações semelhantes no futuro.")
    st.write("Além disso, a análise do comportamento da população durante a pandemia destacou como as restrições e mudanças nos padrões de trabalho afetaram a vida de muitos, especialmente dos trabalhadores informais e dos agentes de saúde, que foram os mais impactados. Esses dados indicam que, em um possível novo surto, as instituições de saúde precisarão estar preparadas não apenas para a gestão de casos médicos, mas também para lidar com as consequências sociais e econômicas que surgirão.")
    st.write("Para se preparar adequadamente, os hospitais e instituições de saúde devem desenvolver planos de contingência que incluam a formação de equipes dedicadas a atender as populações mais vulneráveis. Isso pode envolver a criação de unidades de atendimento móvel e parcerias com organizações comunitárias para garantir que a assistência chegue a todos. Além disso, é essencial implementar campanhas de conscientização para informar a população sobre os sinais de alerta e os cuidados necessários, além de garantir que haja um estoque adequado de medicamentos e insumos essenciais.")
    st.write("A avaliação das condições econômicas revelou uma carência significativa de suporte em comunidades que possuem menos acesso a serviços de saúde. Essa descoberta enfatiza a urgência de desenvolver políticas que garantam uma resposta eficiente e rápida, especialmente em regiões com maior vulnerabilidade social.")
    st.write("Em suma, a pesquisa proporcionou uma visão abrangente e fundamentada, permitindo que as instituições de saúde se preparem melhor para os desafios que podem surgir em um novo surto de COVID-19. Esta análise é um passo importante para entender a dinâmica dos sintomas e elaborar ações que sejam não apenas eficazes, mas também justas e inclusivas, levando em conta a realidade social e econômica da população.")
    st.divider()
    st.header("Referências:")
    st.divider()
    st.write("Pesquisa Nacional por Amostra de Domicílios - PNAD COVID19, DISPONÍVEL EM: https://basedosdados.org/dataset/c747a59f-b695-4d19-82e4-fef703e74c17?table=5dcaf8f0-6509-4dea-958b-4d23bc2a8695")
    st.write("BANCO DE DADOS IBGE: https://covid19.ibge.gov.br/pnad-covid/")
    st.write("Documentação BigQuery: https://basedosdados.github.io/mais/access_data_bq/")
    st.write("Biblioteca para criação do site: https://streamlit.io")
    