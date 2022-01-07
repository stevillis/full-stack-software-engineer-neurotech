# Cadastro de Contatos integrado ao HubSpot

Desafio para a vaga de Engenharia de Software Full Stack da Neurotech.
Desenvolvido com Django e Bootstrap.


## Como executar 
### Instalação das dependências
    $ pip install -r requirements.txt

### Migrações
    $ python manage.py migrate

### Execução do projeto
    $ python manage.py runserver

<p>
Acessar o endereço http://127.0.0.1:8000/ no navegador e dar
permissão de acesso ao aplicativo no HubSpot. 
</p>

![Permissão HubSpot](https://github.com/stevillis/full-stack-software-engineer-neurotech/blob/master/img/autorizacao_hubspot.png?raw=true)

<br/>
<p>
Informar a API KEY
</p>

![Permissão HubSpot](https://github.com/stevillis/full-stack-software-engineer-neurotech/blob/master/img/apikey.png?raw=true)

<br/>
<p>Serão exibidos então os Contatos Cadastrados com as opções de Cadastro, Edição e Exclusão</p>

![Permissão HubSpot](https://github.com/stevillis/full-stack-software-engineer-neurotech/blob/master/img/contatos.png?raw=true)