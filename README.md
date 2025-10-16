Projeto Escola API (CRUD Básico)
Este é um projeto de API simples construída com Django REST Framework (DRF) para gerenciar matérias de uma escola.

🚀 Inicialização do Projeto
Siga os passos abaixo para configurar e rodar o projeto localmente.

Pré-requisitos
Você precisa ter o Python instalado na sua máquina.

1. Clonar e Acessar o Diretório
Bash

# Entre no diretório onde o projeto está localizado (se já não estiver lá)
cd MeuProjetoDRF/escola_api
2. Configurar e Ativar o Ambiente Virtual
É essencial ativar o ambiente virtual para garantir que as dependências corretas sejam usadas.

Bash

# 2.1. Ativar o Ambiente Virtual (Windows - PowerShell)
..\venv\Scripts\Activate

# 2.2. Se o comando acima falhar, tente:
# ..\venv\Scripts\Activate.ps1
💡 Após a ativação, você deve ver (venv) no início da linha de comando.

3. Rodar as Migrações do Banco de Dados
Caso este seja o primeiro deploy (ou se houver novas alterações de modelo), você precisa garantir que o banco de dados esteja atualizado:

Bash

# Comando que prepara as migrações (se houver mudanças nos modelos)
python manage.py makemigrations

# Comando que aplica as migrações (cria as tabelas no db.sqlite3)
python manage.py migrate
4. Iniciar o Servidor
Com o ambiente ativo e o banco de dados pronto, inicie o servidor de desenvolvimento:

Bash

python manage.py runserver
O servidor estará rodando em: http://127.0.0.1:8000/

🛠️ Endpoints da API (CRUD Materias)
A API é acessível no endpoint /api/materias/.

Você pode testar diretamente no navegador ou usando ferramentas como o curl (terminal) ou Postman/Insomnia.

Método	Endpoint	Descrição
GET	/api/materias/	Lista todas as matérias.
POST	/api/materias/	Cria uma nova matéria.
GET	/api/materias/{id}/	Retorna os detalhes de uma matéria específica.
PUT/PATCH	/api/materias/{id}/	Atualiza uma matéria existente.
DELETE	/api/materias/{id}/	Remove uma matéria.

Link de acesso ao DRF http://127.0.0.1:8000/api/materias/
