# logic-tests
# Detecção de Ciclo

O _**Cycle Detection**_ ou **Detecção de Ciclo** é um problema algorítmico que tem como propósito identificar um ciclo em uma sequência de valores pré-estabelecidos.



#### **- Declaração do Problema**

Diz-se que uma lista encadeada contém um ciclo se qualquer nó for visitado mais de uma vez ao percorrer a lista. Dado um ponteiro para o início de uma lista encadeada, determine se ela contém um ciclo. Se isso acontecer, retorne **1**. Caso contrário, retorne **0**.



#### **- Exemplo**

> *head* refere-se à lista de nós **1 > 2 > 3 > NULL**

Os números mostrados são os números dos nós, não seus valores de dados. Não há ciclo nesta lista, então retorne **0**.

> *head* refere-se à lista de nós 1 > 2 > 3 > 1 > NULL

Há um ciclo em que o nó 3 aponta de volta para o nó 1, então retorne **1**.



#### **- Descrição da Função**

Complete a função has_cycle no editor abaixo.

Tem o seguinte parâmetro:

> Cabeça do ponteiro SinglyLinkedListNode: uma referência ao cabeçalho da lista.



#### **- Devoluções**

> int: **1** se houver um ciclo ou **0** se não houver.

Nota: Se a lista estiver vazia, *head* será nulo.



#### **- Formato de Entrada**

O esboço do código lê do padrão e passa o argumento apropriado para a sua função. O formato de casos de teste personalizados não será descrito para esta questão devido à sua complexidade. Expanda a seção da função principal e revise o código se quiser descobrir como criar um caso personalizado.



#### **- Restrições**

> **0 <** *list size* **< 100**



#### **- Entrada de Amostra**

As referências a cada uma das seguintes listas vinculadas são passadas como argumentos para sua função:

![Listas](https://s3.amazonaws.com/hr-challenge-images/1163/1463778594-900a0ae522-inputs.png)



#### **- Saída de Amostra**

> 0

> 1

#### **- Explicação**

> 1. A primeira lista não tem ciclo, então retorne **0**.
> 2. A segunda lista tem um ciclo, então retorne **1**.


**Fonte**: **[HackerRank - Cycle Detection](https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem)**