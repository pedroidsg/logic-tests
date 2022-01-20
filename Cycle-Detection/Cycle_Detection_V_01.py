# TESTE Detecção de Ciclo

# PARTE 1
# Descrição do Código


# O algoritmo para detectar um ciclo em uma lista vinculada é descrito a seguir:

# 1. Declare dois ponteiros P1(lento) e P2( veloz);
# 2. Posicione P1 e P2 no início da lista definida;
# 3. Mova o ponteiro P1 para o próximo nó;
# 4. Mova o ponteiro P2 para o próximo nó e mais um;
# 5. Mova os ponteiros P1 e P2 até que se encontrem novamente;
# 6. Até P1, P2, ou ambos apontarem para None:
# 7. Se este ponto foi alcançado (um ou ambos são None), então não há ciclo na lista.


# PARTE 2
# Código em Python

        
def has_cycle(head):
    if head is None or head.next is None:
         return False

    P1 = head
    P2 = head.next

    while(P2 is not None):
        if P1 == P2:
            return True
        elif P2.next is None:
            return False
        else:
            P1 = P1.next
            P2 = P2.next.next
    return False