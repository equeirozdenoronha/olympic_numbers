# olympic_numbers

#### Url de acesso à API hospedada no heroku: //

### Clonando a aplicação

Clone a aplicação através do comando:
```bash
> git clone https://github.com/equeirozdenoronha/olympic_numbers.git
```
## Instalar e configurar ambiente virtual (virtualenv)
```bash
> pip install virtualenv

> virtualenv nome_da_virtualenv
```
Ativação:

source nome_da_virtualenv/bin/activate (Linux ou macOS)
nome_da_virtualenv/Scripts/activate (Windows)

### Instalar as dependências da aplicação
```bash
> pip install requirements.txt
```
### Fazer as migrações
```bash
python manage.py makemigrations

python manage.py migrate
```

### Rodar Projeto
```bash
> python manage.py runserver
```

### Rodar Script para popular o banco de dados
```bash
> python manage.py import_from_csv
```
### Rodar Testes
```bash
> python manage.py test
```

## Documentação da API

A documentação (Swagger) da API está na raiz do projeto em formato JSON e pode ser importada em qualquer programa que suporte o formato como: Postman ou Insomnia.
Link público para documentação: https://www.getpostman.com/collections/c19f5cd95336dbc12a1e
