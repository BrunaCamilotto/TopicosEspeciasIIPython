# TopicosEspeciasIIPython
Exercicios e materiais desenvolvidos em sala de aula no IFSC


🚀 Comandos do Projeto

    1️⃣ Migrações (ordem correta)
    ⚡  # 1º - Criar as migrações
        python manage.py makemigrations

    ⚡  # 2º - Aplicar as migrações
        python manage.py migrate

    👤 Criar Superusuário
        python manage.py createsuperuser

    ⚡ Rodar o Servidor (porta 8080(usado no IFSC))
        python manage.py runserver 8080

📦 Dependências do Projeto

    ⚡ Instalar django-localflavor
        pip install django-localflavor

        💻 Uso no código:
        from localflavor.br.models import BRCPFField

    ⚡ Instalar tzdata
         python -m pip install tzdata
    
    ⚡ Instalar bootstrap V5
         pip install django-bootstrap-v5
