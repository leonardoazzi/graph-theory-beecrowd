# Graph Theory - Beecrowd (URI) Challenges

## [1148 - Países em Guerra](https://www.beecrowd.com.br/judge/pt/problems/view/1148)


No ano 2050, após diversas tentativas da ONU de manter a paz no mundo, explode a terceira guerra mundial. Segredos industriais, comerciais e militares obrigaram todos os países a utilizar serviços de espionagem extremamente sofisticados, de forma que em cada cidade do mundo há ao menos um espião de cada país. Esses espiões precisam se comunicar com outros espiões, com informantes e mesmo com as suas centrais durante as suas ações. Infelizmente não existe uma forma segura de um espião se comunicar em um período de guerra, então as mensagens são sempre enviadas em código para que somente o destinatário consiga ler a mensagem e entender o seu significado.

Os espiões utilizam o unico serviço que funciona no período de guerra, os correios. Cada cidade possui uma agência postal onde as cartas são enviadas. As cartas podem ser enviadas diretamente ao seu destino ou a outras agências postais, até que a carta chegue à agência postal da cidade de destino, se isso for possível.

Uma agência postal na cidade A pode enviar diretamente uma carta impressa para a agência postal da cidade B se houver um acordo de envio de cartas, que determina o tempo, em horas, que uma carta leva para chegar da cidade A à cidade B (e não necessariamente o contrário). Se não houver um acordo entre as agências A e B, a agência A pode tentar enviar a carta a quantas agências for necessário para que a carta chegue ao seu destino, se isso for possível.

Algumas agências são interligadas por meios eletrônicos de comunicação, como satélites e fibras ópticas. Antes da guerra, essas ligações atingiam todas as agências, fazendo com que uma carta fosse enviada de forma instantânea, mas durante o período de hostilidades cada país passou a controlar a comunicação eletrônica e uma agência somente pode enviar uma carta a outra agência por meio eletrônico (ou seja, instantaneamente) se ela estiver no mesmo país. Duas agências, A e B, estão no mesmo país se houver uma forma de uma carta impressa enviada de uma das agências ser entregue na outra agência.

O serviço de espionagem do seu país conseguiu obter o conteúdo de todos os acordos de envios de mensagens existentes no mundo e deseja descobrir o tempo mínimo para se enviar uma carta entre diversos pares de cidades. Você seria capaz de ajudá-lo?

### Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém dois inteiros separados por um espaço, N (1 ≤ N ≤ 500) e E (0 ≤ E ≤ N2), indicando o número de cidades (numeradas de 1 a N) e de acordos de envio de mensagens, respectivamente. Seguem-se, então, E linhas, cada uma com três inteiros separados por espaços, X, Y e H (1 ≤ X, Y ≤ N, 1 ≤ H ≤ 1000), indicando que existe um acordo para enviar uma carta impressa da cidade X à cidade Y , e que tal carta será entregue em H horas.

Em seguida, haverá uma linha com um inteiro K (0 ≤ K ≤ 100), o número de consultas. Finalmente, virão K linhas, cada uma representando uma consulta e contendo dois inteiros separados por um espaço, O e D (1 ≤ O, D ≤ N). Você deve determinar o tempo mínimo para se enviar uma carta da cidade O à cidade D. A entrada termina quando N = E = 0.

### Saída
Para cada caso de teste da entrada seu programa deve produzir K linhas na saída. A I-ésima linha deve conter um inteiro M , o tempo mínimo, em horas, para se enviar uma carta na I-ésima consulta. Se não houver meio de comunicação entre as cidades da consulta, você deve imprimir ”Nao e possivel entregar a carta”(sem acentos).

Imprima uma linha em branco após cada caso de teste.


---

## [1583 - Contaminação](https://www.beecrowd.com.br/judge/pt/problems/view/1583)

Estamos no ano 2241, e a colonização de outros planetas já é uma realidade. Você trabalha no centro de controle de recursos, no planeta URI-942, controlando principalmente os estoques de água. A água é armazenada em tanques subterrâneos, protegida das altas temperaturas da superfície.

Porém, seus colegas Márcio e Ana descobriram falhas nas paredes de alguns tanques, o que pode levar a contaminação do estoque de água. Seus colegas conseguiram identificar os pontos com falhas onde pode haver a infiltração de contaminantes. Sabendo que os agentes contaminantes se espalham por todo o tanque de água afetado, sua tarefa é estimar a contaminação da água de acordo com os mapas fornecidos por seus colegas.

Os mapas foram discretizados em células, sendo que as células podem corresponder a uma região com rocha, água (tanque) ou agente contaminante. Devido as rachaduras, uma célula com agente contaminante contamina as células adjacentes (esquerda, direita, acima e abaixo) contendo água, porém a contaminação é barrada por células de rocha.

### Entrada

A entrada é composta por vários mapas, sendo que a descrição de cada mapa começa com uma linha contendo dois inteiros N e M, correspondente ao número de linhas e de colunas do mapa. As N linhas a seguir descrevem o mapa, cada linha contendo M caracteres, além do pulo de linha. Os caracteres possíveis são: A, que representa uma célula contendo água, X, que representa uma célula com rocha e T que representa uma célula com agente contaminante.

A entrada termina quando N = M = 0, caso que não deve ser processado. Em todos os mapas, N e M são menores ou iguais a 50.

### Saída

Para cada mapa, imprima uma estimação da contaminação futura. Esta estimação deverá corresponder ao mapa original (como visto na entrada), porém trocando as células com água que foram contaminadas pelo caractere T. Deixe uma linha em branco após cada mapa (incluindo o último mapa).


---
## [1774 - Roteadores](https://www.beecrowd.com.br/judge/pt/problems/view/1774)

Bruno é o responsável por configurar os roteadores de uma empresa. Os roteadores transmitem os dados entre si através dos cabos de internet, Os dados transmitidos podem trafegar por uma ou mais rotas para serem entregues ao destinatário.

O preço dos cabos de rede utilizados nos roteadores da empresa pode chegar a ser muito caro, e a empresa precisa cortar gastos. Pensando nisso a empresa decidiu fazer algumas alterações na infra-estrutura de redes.

Bruno deve modificar a infra-estrutura da rede da empresa de forma com que todos os roteadores consigam transmitir dados entre si e exista somente uma rota entre cada par de roteadores, economizando o máximo possível de cabos de internet.

A sua tarefa é descobrir qual será o custo total com cabos que a empresa terá após as modificações feitas por Bruno. A figura abaixo mostra (a) a infraestrutura de redes atual; e (b) a infraestrutura de redes após as modificação feitas.

### Entrada

A primeira linha é composta por dois inteiros R (3 ≤ R ≤ 60) e C (R ≤ C ≤ 200) representado respectivamente a quantidade de roteadores e a quantidade de cabos de internet utilizados atualmente.

Seguem C linhas, cada uma contendo três inteiros V (1 ≤ V ≤ R), W (1 ≤ W ≤ R) e P (1 ≤ P ≤ 10000), sendo V e W um par de roteadores que estão conectados por um cabo de internet e P o preço do cabo de internet utilizado.

### Saída

Seu programa deve imprimir um único valor inteiro que representa o custo total que a empresa gastará com cabos após as modificações.

| Exemplo de Entrada | Exemplo de Saída |
| --- | --- |
| 7 12 | 12 |
| 1 3 6 
| 1 4 9
| 2 3 17
| 2 5 32
| 2 7 27
| 3 4 11
| 3 5 4
| 4 5 3
| 4 6 19
| 5 6 13
| 5 7 15
| 6 7 5