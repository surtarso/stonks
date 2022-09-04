Na pasta [templates](templates/mainapp) os templates foram separados por função dentro da aplicação para melhor modularidade.
Assim como também o "views.py" foi repartido e separado na pasta [views](views) de acordo com sua área de atuação.
O arquivo [tasks.py](tasks.py) contém as background tasks do celery que controlam os emails e a busca de cotações.
Em [routing.py](routing.py) o conteúdo foi tirado diretamente da documentação do Celery.

Os [formulários](forms.py) foram feitos em ModelForm fazendo assim o uso de [classes](models.py) e suas propriedades para manipulação da DB.
