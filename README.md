
![apm](https://img.shields.io/badge/PROGRAMMING-WEB_1-blue.svg?longCache=true&style=flat-square)

<p align="center">
  <img src="https://i.imgur.com/zCJvNXg.png" width="300">
</p>


## Abstração de arquitetura do projeto
<p align="center">
  <img src="https://i.imgur.com/6YtcMp3.png" width="300">
</p>

## Problematica 

> Desenvolver um sistema bibliotecário com a utilização do framework Django para avaliação da matéria de Programação Web 1

# Como usar projeto

```
git clone https://github.com/jadilson12/project_BooksFind.git
```
ou
```
git clone https://github.com/gabriel-roque/project_BooksFind.git
```

No Linux/Ubuntu não precisamos instalar Python, porque já é nativo em sistemas operacionais baseados em Unix, mas para termos certeza basta executar o comando no terminal:

```
$ python –version
```

o resultado será:

```
Python 3.6.*
```

Vamos começar instalando os pacotes necessários no Sistema Operacional:

```
$ sudo apt-get update
$ sudo apt-get install python-dev python-setuptools
$ sudo apt install python3-venv
$ sudo apt install pip
```

Para testarmos se o virtualenv está instalado corretamente executaremos no terminal:

# Configurações do Projeto

Agora vamos entrar dentro do ambiente virtual que criamos e vamos ativá-lo:

```
$ cd project_BooksFind
$ python3 -m venv venv
$ source project_BooksFind/bin/activate
```

Neste momento temos o ambiente virtual criado e ativado, pronto para instalar o **django**:

```
$ pip install django
```

Quando executamos o comando **pip install django** sem especificarmos a versão desejada, o pip instala a ultima versão disponivel. Se quizermos instalar uma versão específica devemos executar assim:

```
$ pip install django==1.5.4
```

Logo apos iremos executar as migrations do projeto

```
$ ./manage.py migrate
```

Depois basta iniciar o servidor de desenvolvimento

```
$ ./manage.py run server
```

Basta acessar: `localhost:8000`
