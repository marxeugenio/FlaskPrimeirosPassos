# FlaskPrimeirosPassos


### Backend (Python/Flask)
Utiliza Flask, um framework web em Python.
Importa dependências e configura rotas usando Blueprint.
Define rotas para diferentes propósitos:
home(): Renderiza uma página inicial com variáveis inseridas no template HTML.
profile(username): Renderiza a página de perfil usando um parâmetro username da URL ou name dos parâmetros da requisição.
get_json(): Retorna um JSON específico.
get_data(): Retorna dados recebidos no formato JSON.
vai_para_casa(): Redireciona para a página inicial.
Frontend (HTML, Jinja2 template, JavaScript)
Arquivo index.html:

### Define a estrutura da página HTML.
Usa um bloco de conteúdo para inserir dados dinâmicos passados a partir do backend.
Inclui um arquivo JavaScript chamado index.js usando url_for.
Arquivo profile.html:

### Herda do index.html.
Define um bloco de conteúdo para criar uma página de perfil específica.
Arquivo index.js:

### Contém uma instrução para imprimir uma mensagem no console.
Setup e Execução
Cria uma instância Flask.
Registra o Blueprint views com um prefixo de URL.
Inicia o servidor Flask localmente para executar a aplicação.
