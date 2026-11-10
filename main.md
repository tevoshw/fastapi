Verbo  || Ação	|| Exemplo
GET	   || Ler/Consultar/Buscar/Verificar  || GET /models/42
POST   || Criar/Enviar	|| POST /models
PUT	   || Substituir || PUT /models/42
PATCH  || Atualizar parcialmente || PATCH /models/42
DELETE || Remover	||  DELETE /models/42


----

raise HTTPException(status = x, detail)

    - 404

HTTPExpection uma exceção Python do FastAPI que, quando levantada, interrompe a função e faz o FastAPI devolver uma resposta HTTP de erro ao cliente.



---


Como passar escrever endpoints, quando temos uma func só por exemplo '/soma'


e nela temos que passar 3 argumentos

usamos

soma?a=3&b=3&c=3

? = significa que estamos passando argumentos para as variaveis, marca o inicio da query

e depois passar 

chave = valor

e separar chaves com &

---


Para enviar um body request, ou seja um json, podemos usar o POST, que não é somente para criar e sim tambem para enviar e etc

POST SDJFSDFK/SFSDF