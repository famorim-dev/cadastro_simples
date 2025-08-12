# Sistema de Registro de Usuários

Este é um projeto **pessoal** em desenvolvimento utilizando **Python**, **Django**, **HTML** e **CSS**. O objetivo principal é criar um sistema web para **registro de usuários**, com funcionalidades básicas de **autenticação**, **edição de cadastros com permissões específicas** e **busca de registros**.

## Funcionalidades
Cadastro de usuários (com formulário personalizado)

Login e logout de usuários

Edição de perfil do usuário logado

Listagem e busca de registros

Controle de acesso para editar/deletar somente os registros do usuário (owner)

## Tecnologias utilizadas

- Python
- Django
- HTML
- CSS
- **SQLite** (durante o desenvolvimento)
- **MySQL** (para produção)

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
bash
Copiar
Editar
python manage.py migrate
5. (Opcional) Crie um superusuário
bash
Copiar
Editar
python manage.py createsuperuser
6. Rode o servidor de desenvolvimento
bash
Copiar
Editar
python manage.py runserver
7. Acesse no navegador
http://127.0.0.1:8000/



Estrutura do projeto
registro/ - app principal

templates/ - arquivos HTML dos templates

forms.py - formulários personalizados

views.py - lógica das páginas

urls.py - rotas do projeto

static/ - arquivos CSS, JS e imagens

Contato
Felipe Amorim - lipeamorim191@gmail.com
https://www.linkedin.com/in/felipe-amorim-04a6172a5/

## Observações

Este projeto tem fins de aprendizado e aprimoramento pessoal. Não se trata de uma aplicação pronta para produção.



