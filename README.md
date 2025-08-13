# Sistema de Registro de Usuários

Este é um projeto **pessoal** em desenvolvimento utilizando **Python**, **Django**, **HTML** e **CSS**. O objetivo principal é criar um sistema web para **registro de usuários**, com funcionalidades básicas de **autenticação**, **edição de cadastros com permissões específicas** e **busca de registros**.

Funcionalidades
Cadastro de usuários com validação de senha

Login e logout

Edição do perfil do usuário

CRUD (Criar, Ler, Atualizar, Deletar) de registros associados ao usuário

Controle de acesso baseado no usuário logado

## Tecnologias utilizadas

- Python
- Django
- HTML
- CSS
- **SQLite** (durante o desenvolvimento)

Como rodar o projeto localmente
Pré-requisitos
Python 3 instalado

Ambiente virtual (venv)

Git (se for clonar do repositório)

Passos para rodar
### 1. Clone o repositório

```bash
git clone https://github.com/famorim-dev/cadastro_simples.git
cd cadastro_simples
```


2. Crie e ative o ambiente virtual
```bash
No Linux/macOS:

python -m venv venv
source venv/bin/activate
No Windows:

python -m venv venv
venv\Scripts\activate

```

3. Instale as dependências

```bash
pip install -r requirements.txt

```
4. Execute as migrações para criar o banco de dados
```bash
python manage.py migrate
```
5. (Opcional) Crie um superusuário
```bash
python manage.py createsuperuser
```
6. Rode o servidor de desenvolvimento
```bash
python manage.py runserver
```
8. Acesse no navegador
```bash
http://127.0.0.1:8000/
```

Estrutura do projeto

```bash
registro/            - app principal

templates/           - arquivos HTML dos templates

forms.py             - formulários personalizados

views.py             - lógica das páginas

urls.py              - rotas do projeto

static/              - arquivos CSS, JS e imagens
```

Contato
Felipe Amorim - lipeamorim191@gmail.com

linkedin - https://www.linkedin.com/in/felipe-amorim-04a6172a5/

## Observações

Este projeto tem fins de aprendizado e aprimoramento pessoal. Não se trata de uma aplicação pronta para produção.







