# responsible-votes

🔗 github: https://github.com/Lebackrobot/responsible-votes

Backend usando python e o biblioteca Flask para tratamento de rodas e renderização de html.

Nessa aplicação de votos, você poderá votar em cinco candidatos para dominar o mundo: Rick Sanchez, Jesus Cristo, Darth Vader, Romer Simpson e Michael Jackson.

![Screenshot from 2023-05-19 23-27-00](https://github.com/Lebackrobot/responsible-votes/assets/49316490/6bc0aa57-1d8c-412a-8c07-e899d9359930)


## Arquitetura do Projeto
Foi utilizado uma arquitetura MVC (model, view e controller) para maior organização. Também foi necessário simular o banco de dados com um arquivo CSV. Portanto temos:

📁 controllers /votesController.py <br>
📁 service /votesService.py <br>
📁 templates/<br>

  &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /index.py      <br>
  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /votes.py    <br>
   
 📁 requirements / requirements.txt     <br>
 📝 app.py <br>
 🗂️ db.csv

## Rotas
Foram utilizadas algumas rotas no backend

A rota de votos (votes):

Method |  EndPoint | Body Params | Query Params |Returns
:---------: | :------ | :-------: | :--------: | :--------:
<strong>GET</strong>| /votes |   -  | candidate_name | type : Dictionary
<strong>POST<strong>  | /votes/ |   candidate_name | - | type : redirect('votes')

## Dependências
Antes de executar o código, é necessário instalar a biblioteca <strong>Prettytable</strong>, utilizada para printar tabelas. Para isso, basta:
```console
pip install -r requirements.txt
```
## Executar o código
  Para executar o código basta:
  ```console
python3 app.py
```
 Posteriomente abra seu navegador e coloque na url a rota: http://127.0.0.1:5000/
  
  ### Vote responsável!
