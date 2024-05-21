import streamlit as st
import pandas as pd

st.markdown('<h1 style="text-align: center;">Exportação Brasileira de Vinhos</h1>', unsafe_allow_html=True)
st.markdown('<h5 style="text-align: center; font-style: italic;">Uma perspectiva ampliada</h5><br>', unsafe_allow_html=True)

st.markdown("""
<div style="font-size: 13px; text-align: right; max-width: 490px; margin-left: auto; display: block;">
    Elaborado por Alberto M. Marques Marson, Técnico em Informática, Analista e Desenvolvedor de Sistemas, atualmente cursando pós-graduação em Data Analytics.<br><br>
</div>
""", unsafe_allow_html=True)


st.write('''
<div style="display: flex; justify-content: center; align-items: center; margin: 0 auto;">
    <div style="border-left: 1px solid white; height: 100%; padding-left: 20px; text-align: justify;">
        O presente estudo, proposto pela FIAP como parte integrante do projeto de conclusão do primeiro trimestre da pós-graduação em Data Analytics, aborda uma análise detalhada sobre o consumo de vinhos. Utilizando como fonte primária de informações os dados providos pela Embrapa - <i>Empresa Brasileira de Pesquisa Agropecuária</i>.
    </div>
</div><br>
''', unsafe_allow_html=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Propósito</h4>
    <p>Este projeto está segmentado em 07 fases, que se inauguram com a aquisição de uma compreensão abrangente do cenário do comércio vinícola. Aprofundar-se nesse âmbito é essencial para uma análise meticulosa e substancial. Inicialmente, procedemos com uma avaliação panorâmica do mercado, investigando tendências e padrões pertinentes. Em seguida, avançamos para a coleta e preparação de dados, garantindo a edificação de um fundamento robusto para nossas análises. Posteriormente, serão extraídos e expostos insights valiosos dos dados. Por último, nossas conclusões serão expostas de maneira clara e concisa, conferindo recomendações pragmáticas aos interessados. Essa abordagem integrada proporciona uma compreensão holística do mercado vinícola e oferece diretrizes embasadas para futuras deliberações.</p>
</div>
''', unsafe_allow_html=True)


st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Introdução</h4>
    <p> 
A análise de dados desempenha um papel fundamental na compreensão e na tomada de decisões em diversas áreas, inclusive no mercado vinícola. Neste contexto, durante um desafio proposto pela especialização em Data Analytics da FIAP, assumi o papel de especialista em análise de dados em uma empresa fictícia recém-criada, focada na exportação de vinhos do Brasil para o mercado global. A minha missão consistia em fornecer relatórios iniciais para uma reunião crucial com investidores e acionistas, apresentando detalhes sobre a quantidade de vinhos exportados e os fatores externos que influenciam nas análises. Para atingir esse objetivo, conduzi uma análise detalhada das exportações brasileiras de vinho, empregando técnicas avançadas de Exploratory Data Analysis (EDA) e Data Visualization (DataViz). Meu foco principal recaiu sobre os dados relativos à comercialização de vinhos provenientes do Estado do Rio Grande do Sul, que detém a maior parte da produção nacional.

No contexto atual, o mercado vinícola tem testemunhado um crescimento significativo no consumo de vinho, conforme relata a Exame. Nos últimos 12 anos, o número de apreciadores da bebida dobrou, atingindo 44 milhões em 2022, segundo dados da Wine Intelligence. Esse cenário evidencia a relevância e a oportunidade presentes no mercado vinícola, demandando análises precisas e estratégicas para o sucesso das empresas atuantes neste segmento.

Além disso, de acordo com dados do G1, em 2022, o consumo mundial de vinho totalizou 232 milhões de hectolitros, mantendo-se praticamente estável em relação ao ano anterior. Essa estabilidade no consumo global reflete a constante demanda por essa bebida em diversas partes do mundo, destacando a importância contínua do mercado vinícola e a necessidade de análises precisas para acompanhar as tendências e as mudanças no comportamento do consumidor.</p>
</div>
''', unsafe_allow_html=True)


st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Fonte de Dados</h4>
    <p>A base fornecida pela Embrapa - <i> Empresa Brasileira de Pesquisa Agropecuária </i> apresenta dados anuais, abrangendo o período de 1970 a 2023 e organizados por país. Esta vasta base de dados nos permite analisar, interpretar e compreender as nuances do consumo de vinhos em diferentes contextos culturais e econômicos. Além disso, inclui informações detalhadas sobre a quantidade de vinhos exportados e importados, bem como seu respectivo valor em dólares americanos.

Todavia, visando trazer uma maior acurácia durante a análise, o período analisado compreende os últimos 15 anos (de 2008 a 2023), o que nos permite capturar uma ampla gama de eventos, tendências e mudanças relevantes para o estudo em questão.</p>
</div>
''', unsafe_allow_html=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Preparação e Análise da Base de Dados</h4>
    <p>Para iniciar nossa análise, é necessário realizar um processo de pré-processamento de dados, a fim de analisar de maneira precisa e direcionada os dados relativos à exportação de vinhos de mesa. Nosso objetivo principal é obter uma visão abrangente das tendências de exportação desses produtos ao longo dos anos.

Após o processamento inicial, identificamos as seguintes observações:

- Foi necessário renomear as colunas para distinguir entre os campos de quantidade e valor ao longo dos anos, notando a presença do sufixo ".1". Por exemplo, as colunas com o ano indicavam a quantidade, enquanto aquelas com o ano seguido de ".1" representavam o valor. Esses ajustes foram realizados visando aprimorar a clareza e a compreensão da análise.

- Além disso, houve a necessidade de corrigir os nomes de alguns países, como Alemanha, Chipre, Singapura e Coreia do Sul.

- Uma observação de destaque é a presença de duas entradas para Singapura, com nomes diferentes ("Cingapura" e "Singapura"). Diante disso, os valores dessas entradas foram consolidados em uma única entrada, utilizando o nome correto, "Singapura". Vale ressaltar que não foram encontradas outras colunas com nomes idênticos durante essa verificação.

- Adicionalmente, procedemos com a modificação dos nomes dos países que continham caracteres acentuados, removendo esses acentos para garantir a consistência e a limpeza dos dados.

- Após a correção dos nomes dos países, foram identificados 136 países únicos para análise.

- Realizamos também uma análise para verificar a presença de países com quantidade exportada mas sem valor, bem como países com valor mas sem quantidade exportada. Observou-se que Camarões não possui quantidade exportada, mas apresenta valor para o ano de 2020.

- Outro aspecto notável é que há onze países cuja quantidade exportada é igual a zero em todos os anos analisados: Anguilla, Costa do Marfim, Ilhas Virgens, Iraque, Jamaica, Líbano, Porto Rico, República Dominicana, Senegal, Tanzânia e Tunísia.

- A seguir, apresenta-se a tabela conforme solicitado pelo Head para referência:
                                                           
</div>
''', unsafe_allow_html=True)

# Exibição da primeira tabela, informando todos os países, bem como seus valores! 

df_primeiratabela = pd.read_csv('tabela_pedido_head.csv', sep=';', dtype={'Ano': int})

pais = st.text_input("Digite o nome do País que deseja filtrar:", "")

pais = pais.lower()

if pais:
    df_primeiratabela = df_primeiratabela[df_primeiratabela['País'].str.lower().str.contains(pais)]

st.dataframe(df_primeiratabela)

st.markdown("""
<div style="font-size: 13px; text-align: right; max-width: 490px; margin-left: auto; display: block;">
    Tabela 1: Base de Dados Utilizada<br><br>
</div>
""", unsafe_allow_html=True)  

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">

- Para garantir a precisão dos dados e avançar para as etapas subsequentes da análise, optamos por não considerar os seguintes países: Anguilla, Costa do Marfim, Ilhas Virgens, Iraque, Jamaica, Líbano, Porto Rico, República Dominicana, Senegal, Tanzânia e Tunísia. Essa decisão é fundamentada no fato de que esses países apresentam valores de exportação zerados e/ou ausência de quantidade de exportação com valores associados, e vice-versa. Esta medida visa assegurar a integridade dos dados utilizados na pesquisa.
                                                           
</div>
''', unsafe_allow_html=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Análise Exploratória</h4>
    <p>O comércio global de vinho tem desempenhado um papel fundamental na economia mundial, com as exportações desse produto representando uma parte significativa do mercado internacional de bebidas. 
    <p>No intervalo de 15 anos entre 2008 e 2023, observamos uma notável tendência de exportação de vinho de mesa, com um volume expressivo de aproximadamente 93,5 milhões de litros exportados. Essa atividade comercial gerou uma movimentação financeira considerável, totalizando cerca de 121,6 milhões de dólares em receitas de exportação.
''', unsafe_allow_html=True)

# Gráfico 1: Evolução dos Valores de Litros Exportados ao longo do tempo 
caminho_imagem = "graficos/timeline_15_anos_valores_litros_exportados.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Evolução dos Valores de Litros Exportados ao longo do tempo ", use_column_width=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">         
    <p>Dentre os países exportadores de vinho de mesa no período de 2008 a 2023, três se destacam como os principais protagonistas desse cenário: Paraguai, Rússia e Estados Unidos.                                   
</div>
''', unsafe_allow_html=True)

# Gráfico 2: Países com maior receita de exportação de vinhos
caminho_imagem = "graficos/paises_com_maior_exportacao_vinhos.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Países com Maior Exportação de Vinhos", use_column_width=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <p> No gráfico acima, podemos observar que o Paraguai se destaca como o principal país importador de vinho. Esse destaque se deve ao aumento do consumo de vinho nos últimos anos, impulsionado pela ascensão da classe média e por mudanças nos padrões de consumo. Essa tendência é evidenciada pelo crescimento constante das importações de vinho pelo Paraguai, conforme demonstrado no gráfico abaixo:                              
</div>
''', unsafe_allow_html=True)

# Gráfico 3: Ascensão do Paraguai
caminho_imagem = "graficos/Ascensao_Paraguai.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Ascensão do Paraguai", use_column_width=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <p> Podemos observar que, no período de 2009 até 2018, a receita de importação do Paraguai registrou um aumento significativo, refletindo possíveis melhorias na economia nacional, acordos comerciais favoráveis ou outras políticas de estímulo ao comércio. No entanto, nos anos de 2019 e 2020, os valores caíram aproximadamente 30,22%. Essa queda acentuada pode ser atribuída em grande parte ao impacto da pandemia do COVID-19. A crise sanitária global provocou uma série de efeitos adversos na economia mundial, incluindo disrupções nas cadeias de suprimentos, restrições comerciais e medidas de distanciamento social que afetaram diretamente o comércio internacional. Além disso, o setor de serviços, como o turismo e a hotelaria, foi particularmente atingido, o que pode ter contribuído para uma diminuição na demanda por bens importados. Assim, o declínio na receita de importação do Paraguai durante esses anos está intrinsecamente ligado aos desafios enfrentados pela economia global decorrentes da pandemia do COVID-19.                        
</div>
''', unsafe_allow_html=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <p>Durante o período analisado, o Produto Interno Bruto (PIB) do Paraguai apresentou uma variação média de aproximadamente 0.71% em relação ao valor inicial. Essa variação média é calculada como a média das diferenças entre os valores do PIB de um ano para o outro, expressa como uma porcentagem do PIB inicial.
    <p>Essa medida fornece uma visão resumida da tendência geral do PIB ao longo do período considerado. Embora essa variação possa parecer pequena em termos absolutos, é importante considerar seu impacto cumulativo ao longo dos anos. Essa variação pode ter influenciado diversos aspectos da economia do Paraguai, incluindo investimentos, consumo e políticas governamentais.
    <p>É relevante observar que essa variação média do PIB pode ter contribuído para a queda observada no período de 2022 a 2023. Durante esse período, a economia paraguaia pode ter enfrentado desafios ou choques que afetaram negativamente o crescimento econômico, levando a uma diminuição do PIB. Uma possível explicação para essa queda pode ser a ocorrência de eventos econômicos, políticos ou ambientais que impactaram a produção, o comércio ou a confiança dos investidores.
    <p>Por exemplo, flutuações nos preços das commodities, mudanças nas políticas comerciais internacionais ou crises econômicas em países vizinhos podem ter influenciado a economia do Paraguai durante esse período. Além disso, fatores internos, como instabilidade política, mudanças nas políticas fiscais ou regulatórias, também podem ter desempenhado um papel na queda do PIB.              
</div>
''', unsafe_allow_html=True)

# Gráfico 4: PIB do Paraguai
caminho_imagem = "graficos/Pib_Paraguai.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="PIB do Paraguai - Dados: https://paises.ibge.gov.br/#/dados/paraguai", use_column_width=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <p>Durante o período analisado, destacou-se que em 2013, a Rússia liderou as exportações, registrando um total de 14.8 milhões de dólares em 5.9 milhões de litros de vinho. No entanto, ao adotarmos uma perspectiva mais ampla e cronológica, percebemos que o Paraguai continua a se destacar como um país de destaque em termos de exportação de vinho de mesa. Desde 2015, o Paraguai tem mantido uma presença constante no mercado de exportação de vinho, com exportações anuais consistentes. Por outro lado, a Rússia emergiu como um participante significativo em apenas dois anos, 2009 e 2013, sem recorrência notável nos anos subsequentes. 
</div>
''', unsafe_allow_html=True)

# Gráfico 5: Perspectiva dos 10 maiores
caminho_imagem = "graficos/10_maiores_perspectiva.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Top 10 maiores", use_column_width=True)

# Gráfico 6: Receita Exportação Russia
caminho_imagem = "graficos/receita_exportacao_russia.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Receita Exportação Russia", use_column_width=True)

# Gráfico 7: Quantidade Exportação Russia
caminho_imagem = "graficos/Quantidade_Exportada_Russia.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Quantidade Exportação Russia", use_column_width=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <p>Certamente, pelos dados apresentados, torna-se evidente e incontestável que o Paraguai desponta como a melhor opção para nossos acionistas investirem, garantindo um retorno mais rápido e com menor exposição a riscos. Isso se fundamenta no expressivo desempenho do país, que se destaca como líder no mercado de exportação de vinho de mesa.
    <p>No entanto, é importante considerar o contexto geopolítico e econômico global. Por exemplo, o segundo país em destaque, a Rússia, encontra-se envolvido em um conflito com a Ucrânia. Essa contenda pode resultar em variações imprevisíveis nos custos das principais commodities, especialmente no setor vitivinícola. Além disso, a guerra teve impactos significativos no mercado global, incluindo o aumento dos preços dos fertilizantes agrícolas. A Rússia, como um dos principais produtores mundiais de Nitrogênio, Potássio e Fósforo, exerce considerável influência sobre esses mercados, impactando diretamente os custos de produção agrícola em escala internacional.
    <p>Além dessas transformações, é importante considerar o contexto do Mercosul, que pode influenciar significativamente o comércio de vinhos na região. A proximidade geográfica e os acordos comerciais entre os países membros do bloco podem facilitar e incentivar as transações comerciais, promovendo um ambiente favorável para a exportação e importação de vinhos entre os países membros.
    <p>A integração regional proporcionada pelo Mercosul não apenas simplifica os processos logísticos e reduz as barreiras comerciais, mas também estimula a cooperação econômica e a troca de experiências no setor vitivinícola. Nesse sentido, o fortalecimento do Mercosul pode desempenhar um papel crucial no impulso ao comércio de vinhos e na valorização dos produtos regionais nos mercados internacionais.
    <p>Dessa forma, ao considerar as circunstâncias atuais, o Paraguai emerge como uma escolha mais estável e promissora para investimentos no setor vitivinícola, proporcionando aos nossos acionistas um cenário mais seguro e vantajoso. 

</div>
''', unsafe_allow_html=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Valorização do Vinho nas Exportações: Tendência Crescente</h4>
    <p>A análise do comportamento do valor de litros exportados ao longo dos anos revela uma tendência interessante. Nos anos iniciais, especificamente em 2008 e 2009, observamos que a quantidade de litros exportados era significativamente maior do que o valor gerado. Essa disparidade sugere uma possível depreciação do produto ou uma precificação mais baixa no mercado de destino.
    <p>Entretanto, a partir de 2010 até 2023, com uma pequena variância em 2012, a dinâmica se inverteu, com o valor de litros exportados superando consistentemente a quantidade. Esse fenômeno indica uma valorização crescente do produto ao longo do tempo, refletindo possíveis melhorias na qualidade, estratégias de marketing mais eficazes ou uma demanda crescente por vinhos de determinada região.
    <p>Essa mudança de paradigma sugere uma evolução positiva no mercado de exportação de vinho, onde os produtores podem estar agregando mais valor aos seus produtos, em vez de simplesmente focar na maximização da quantidade exportada. Essa abordagem pode resultar em retornos financeiros mais sólidos e sustentáveis a longo prazo, além de contribuir para a valorização da marca e do produto no cenário internacional.
   </div>
''', unsafe_allow_html=True)

# Gráfico 8: Quantidade x Valor
caminho_imagem = "graficos/quantidade_valor.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Exportaçãoe e Valorização - Tendência Crescente", use_column_width=True)


st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Indicadores de Rentabilidade</h4>
    <p>Ao analisarmos os 10 maiores e principais países exportadores, observamos uma média de 2.15 para a taxa de dólar por litro de exportação. Em outras palavras, cada litro exportado gerou aproximadamente US$ 2.15 em receita para esses países, em média. Vale ressaltar que quanto maior essa média, maior será o valor agregado aos produtos exportados, o que pode ser um indicador positivo para a rentabilidade das exportações.
    <p>Ao analisar os valores médios de exportação por litro em uma seleção dos principais países exportadores, podemos observar uma variedade de taxas de dólar por litro, o que é crucial para entender a rentabilidade das exportações e o valor agregado dos produtos.

- **Alemanha**: Com uma média de US$ 2.82 por litro, a Alemanha demonstra uma alta rentabilidade em suas exportações, sugerindo um forte valor agregado em seus produtos.
- **China**: Apesar de ser um dos maiores exportadores, a China apresenta uma média mais baixa, indicando uma possível predominância de produtos de menor valor agregado, com uma média de US$ 1.91 por litro.
- **Espanha**: Com uma média de US$ 1.91 por litro, a Espanha também mostra uma rentabilidade sólida em suas exportações.
- **Estados Unidos**: Com uma média de US$ 2.67 por litro, os Estados Unidos também demonstram uma rentabilidade sólida em suas exportações.
- **Haiti**: O Haiti apresenta uma média mais baixa, sugerindo que seus produtos exportados possam ter um valor agregado relativamente menor, com uma média de US$ 1.36 por litro.
- **Japão**: Com uma média de US$ 2.02 por litro, o Japão mostra uma rentabilidade sólida em suas exportações.
- **Países Baixos**: Com uma média de US$ 3.07 por litro, os Países Baixos exibem uma das taxas mais altas, indicando um forte valor agregado em seus produtos.
- **Paraguai**: O Paraguai apresenta uma média mais baixa, sugerindo que seus produtos exportados possam ter um valor agregado relativamente menor, com uma média de US$ 1.34 por litro.
- **Reino Unido**: Com uma média de US$ 3.83 por litro, o Reino Unido demonstra uma alta rentabilidade em suas exportações, sugerindo um forte valor agregado em seus produtos.
- **Rússia**: Com a média mais baixa, sugerindo que seus produtos exportados possam ter um valor agregado relativamente menor, com uma média de US$ 0.65 por litro.
</div>
''', unsafe_allow_html=True)

# Exibição da segunda tabela, informando a média do dolar. 

df_segundatabela = pd.read_csv('media_taxa_dolar.csv', sep=';', dtype={'Ano': int})

st.dataframe(df_segundatabela)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <p>Embora a Europa lidere em termos de quantidade total de litros exportados, é interessante observar que o principal país exportador não pertence a esse continente. O Paraguai se destaca como o principal protagonista, demonstrando uma alta rentabilidade em suas exportações, com uma média de US$ 1.34 por litro. Essa descoberta sugere que, ao considerar investimentos no mercado vinícola, a América do Sul, especialmente devido ao desempenho do Paraguai, emerge como uma opção atrativa e promissora.
    <p>Além disso, é relevante notar que a Europa continua sendo um dos continentes mais desejados pelos turistas em todo o mundo, atraindo milhões de visitantes todos os anos. Essa preferência por destinos europeus pode influenciar indiretamente o mercado vinícola, criando uma demanda sustentada por vinhos europeus em mercados internacionais. Portanto, embora o foco possa estar na América do Sul devido ao desempenho notável do Paraguai, não se pode ignorar a influência e a relevância da Europa no mercado vinícola internacional.
</div>
''', unsafe_allow_html=True)

# Gráfico 9: Continente
caminho_imagem = "graficos/continente.png"
imagem_grafico = open(caminho_imagem, "rb").read()
st.image(imagem_grafico, caption="Exportação por Continente", use_column_width=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Conclusão</h4>
    <p>A análise aprofundada das exportações brasileiras de vinho revela insights valiosos sobre o desempenho do mercado e as oportunidades de investimento na indústria vitivinícola. Ao examinarmos os dados fornecidos pela Embrapa - <i> Empresa Brasileira de Pesquisa Agropecuária , fica evidente que o Paraguai emerge como um dos principais protagonistas no cenário das exportações de vinho de mesa. Com uma média de US$ 1.34 por litro, o Paraguai demonstra uma alta rentabilidade em suas exportações, tornando-se um ponto focal para investidores interessados em retornos sólidos e consistentes.
    <p>No entanto, embora o Paraguai se destaque como líder em termos de rentabilidade, é importante reconhecer a influência contínua da Europa no mercado vinícola global. A Europa não só lidera em termos de quantidade total de litros exportados, mas também continua sendo um dos destinos mais desejados para turistas em todo o mundo. Essa preferência por destinos europeus pode influenciar indiretamente o mercado vinícola, criando uma demanda sustentada por vinhos europeus em mercados internacionais.
    <p>Portanto, ao considerar investimentos no mercado vinícola, é essencial avaliar cuidadosamente as oportunidades oferecidas tanto pela América do Sul, com destaque para o Paraguai, quanto pela Europa. Enquanto o Paraguai oferece uma rentabilidade sólida e um potencial de crescimento significativo, a Europa continua sendo um mercado crucial devido à sua influência e reputação estabelecida na indústria vinícola.
    <p>Além disso, é importante destacar que a análise dos dados revela uma tendência crescente de valorização do vinho nas exportações ao longo do tempo. Essa mudança de paradigma sugere uma evolução positiva no mercado de exportação de vinho, onde os produtores estão agregando mais valor aos seus produtos, em vez de simplesmente focar na maximização da quantidade exportada. Essa abordagem pode resultar em retornos financeiros mais sólidos e sustentáveis a longo prazo, contribuindo para a valorização da marca e do produto no cenário internacional.
    <p>Em resumo, a análise detalhada das exportações brasileiras de vinho oferece uma visão abrangente do mercado vinícola e das oportunidades de investimento disponíveis. Ao considerar o desempenho notável do Paraguai, a influência contínua da Europa e a tendência crescente de valorização do vinho, os investidores podem tomar decisões informadas e estratégicas para maximizar seus retornos e garantir um futuro próspero no mercado global de vinho.     
         </div>
''', unsafe_allow_html=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Projeções Futuras</h4>
    <p>Com base nas análises realizadas e nos insights obtidos sobre as exportações brasileiras de vinho, bem como nas tendências observadas no mercado global de vinícolas, é possível vislumbrar projeções significativas para o futuro da indústria vitivinícola:

- **Expansão Regional e Internacionalização**: A perspectiva de expansão da indústria vitivinícola sul-americana é promissora, especialmente considerando o desempenho excepcional do Paraguai como líder em rentabilidade nas exportações de vinho. Espera-se que países como Argentina, Chile e Brasil, dotados de recursos naturais propícios e expertise vitivinícola, continuem a desempenhar um papel crucial na expansão e diversificação dos mercados de exportação.

- **Inovação e Diferenciação de Produtos**: Em um mercado altamente competitivo e em constante evolução, a inovação e a diferenciação de produtos tornam-se imperativas para as vinícolas que buscam manter uma vantagem competitiva sustentável. A pesquisa contínua, o desenvolvimento de novas variedades de uvas, métodos de vinificação aprimorados e a criação de vinhos distintivos em sabor e qualidade serão elementos-chave para atrair consumidores exigentes e explorar novos nichos de mercado.

- **Exploração de Mercados Emergentes**: Além dos tradicionais mercados consumidores de vinho, como Europa e Estados Unidos, as vinícolas têm a oportunidade de expandir sua presença em mercados emergentes, como China, Índia e Rússia. O crescente poder aquisitivo e o aumento do interesse por vinhos nessas regiões oferecem um potencial considerável para o crescimento das exportações e a penetração de novos segmentos de mercado.

- **Sustentabilidade e Responsabilidade Social Corporativa**: À medida que a conscientização ambiental e social ganha destaque globalmente, as vinícolas são chamadas a adotar práticas sustentáveis de produção e a incorporar a responsabilidade social corporativa em suas operações. A implementação de técnicas agrícolas sustentáveis, a redução do uso de agroquímicos e a promoção do bem-estar das comunidades locais emergem como pilares essenciais para uma indústria vinícola responsável e ética.

- **Digitalização e Transformação Tecnológica**: A digitalização desempenhará um papel cada vez mais preponderante na indústria vitivinícola, abrangendo desde a gestão eficiente das vinhas até as estratégias de marketing e distribuição. O aproveitamento de tecnologias digitais e ferramentas de análise de dados permitirá às vinícolas otimizar processos, identificar oportunidades de mercado e estabelecer conexões diretas com os consumidores, promovendo a fidelização da marca e a expansão dos negócios.

<p>Em síntese, o futuro da indústria vitivinícola está intrinsecamente ligado à capacidade das vinícolas de se adaptarem e inovarem em um ambiente de negócios dinâmico e globalizado. Ao antecipar tendências, abraçar a sustentabilidade, investir em diferenciação de produtos e aproveitar as oportunidades oferecidas pela tecnologia, as vinícolas podem garantir uma posição de destaque em um setor em constante evolução. 
         </div>
''', unsafe_allow_html=True)

st.write('''
<style>
    .text-justify {
        text-align: justify;
    }
</style>

<div class="text-justify">
    <h4>Referências Bibliográficas</h4>
    <p> EXAME. (2024, 1 de abril). Apesar da ressaca no mercado de vinhos, o interesse por novidades traz oportunidades para o setor. Disponível em: https://exame.com/casual/apesar-da-ressaca-no-mercado-de-vinhos-o-interesse-por-novidades-traz-oportunidades-para-o-setor/. Acesso em: 1 de maio de 2024.</p>
    <p> EXAME. (2024, 10 de abril). As expectativas para o mercado de vinhos para 2024. Disponível em: https://exame.com/casual/as-expectativas-para-o-mercado-de-vinhos-para-2024/. Acesso em: 1 de maio de 2024.</p>
    <p> Elite Vinho. (s.d.). Diversificação de produtos impulsiona o mercado de vinhos. Recuperado de https://elitevinho.com.br/blog/diversificacao-de-produtos-impulsiona-o-mercadodevinhos/</p>
    <p> SEBRAE RS. Setor vitivinícola enfrenta desafios no Brasil e no exterior. Disponível em: https://sebraers.com.br/vitivinicultura/setor-vitivinicola-enfrenta-desafios-no-brasil-e-no-exterior/. Acesso em: 2 de maio de 2024.</p>
    <p> G1. (2023, 19 de maio). E o país que toma mais vinho é? Recuperado de https://g1.globo.com/pr/parana/especial-publicitario/porto-a-porto/guia-do-vinho-e-da-gastronomia/noticia/2023/05/19/e-o-pais-que-toma-mais-vinho-e.ghtml</p>
</div>
''', unsafe_allow_html=True)