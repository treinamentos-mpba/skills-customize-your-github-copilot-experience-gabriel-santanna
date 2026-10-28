
# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Construa um jogo da Forca em Python para praticar manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória.

## 📝 Tasks

### 🛠️ Implementar as Regras do Jogo

#### Descrição
Crie a lógica principal do jogo: selecione uma palavra secreta de uma lista predefinida e permita que o jogador descubra suas letras antes de esgotar seis tentativas incorretas.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Mostrar cada letra ainda não descoberta como `_` e revelar as letras acertadas nas posições correspondentes.
- Aceitar palpites de uma letra por vez e atualizar o progresso após cada palpite.
- Reduzir o número de tentativas restantes somente quando o palpite estiver incorreto.
- Encerrar a partida quando a palavra for descoberta ou quando não houver tentativas restantes.

### 🛠️ Conduzir a Partida

#### Descrição
Integre a lógica em um fluxo interativo que informe o estado do jogo e comunique claramente o resultado ao jogador.

#### Requisitos
O programa concluído deve:

- Exibir as tentativas incorretas restantes a cada rodada.
- Informar quando o jogador acertar ou errar uma letra.
- Exibir uma mensagem de vitória quando todas as letras forem descobertas.
- Exibir uma mensagem de derrota e revelar a palavra secreta quando as tentativas acabarem.
- Impedir que palpites repetidos sejam contabilizados novamente como erro.

Exemplo de progresso para a palavra `python` após acertar `p` e `o`:

```text
p _ _ _ o _
```