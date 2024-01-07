
<h1>Download Automático de IPVA - SEFAZ Ceará</h1>

<p>Este projeto permite o download automático do IPVA de uma série de veículos na SEFAZ do Ceará.</p>

<h2>Requisitos</h2>

<p>Para o funcionamento do robô, é necessário:</p>

<ul>
<li>Arquivo Excel contendo as informações de placa e RENAVAM.</li>
<li>Bibliotecas: pandas, selenium e pyautogui.</li>
</ul>

<h2>Como Funciona</h2>
<ol>
  <li>Coloque uma planilha no mesmo diretório do código contendo placa e RENAVAM dos veículos desejados.</li>
  <li>Indique o nome do arquivo Excel e o nome da planilha entre os aspas desta seção do código: <code>df = pd.read_excel("NOME_DA_PLANILHA_AQUI", sheet_name='NOMME_DA_PAGINA_DA_PLANILHA_AQUI')</li>
  <li>Entre as aspas desta seção do código voce indicara qual o nome da coluna com as placas <code>placa = linha['NOME_DA_COLUNA_DAS_PLACAS_AQUI']</code></li>
  <li>Nesta seção do código voce indicara qual o nome da coluna com o renavam <code>renavam = linha['NOME_DA_COLUNA_COM_RENAVAM_AQUI']</li>
  <li>Execute o código, e ele realizará o download dos documentos, renomeando-os de acordo com a placa do veículo.</li>
</ol>

<h2>Exemplo</h2>
<p>Abaixo você tem um exemplo de como preenchi com meus dados para que o codigo funcionasse.</p>
<p><code>df = pd.read_excel("IPVA 2024.xlsx", sheet_name='Planilha4')

for indice, linha in df.iterrows():
  placa = linha['PLACA']
  renavam = linha['RENAVAM']
  download_Dae(placa, renavam)</code></p>
