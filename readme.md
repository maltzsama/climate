# Climate Endpoint API

* GET/climate - É necessário implementar um sistema de paginação neste microserviço. Optei por exibir apenas as 100 últimas posições do serviço. Estou analisando como fazer a paginação com o flask. confesso que não estou muito a vontade com ele, me sinto um tanto enferrujado.

* GET/climate/<id> - Implementado com base no id do dia de previsão do tempo

* POST/climate - a introdução de um novo dia de previsão, eu optei por armazenar o dia corrente ao invés de deixar o usuário fazer o post dessa informação.

* DELETE/climate/<id> - remove da tabela uma informação baseada no código enviado

* GET/predict - retorna a previsão do último dia. Eu fiquei um pouco em dúvida nesse caso, eu estou retornando o último dia. É provavel que eu precise reimplementar para retornar o dia corrente. Mas como eu resolvi usar um dataset do site que vocês me indicaram, as coisas não estão exatamente atualizadas quando o assunto é clima.

Uma instancia foi colocada no meu servidor pessoal. Esse é o link de acesso. http://galileolab.io/climate/
