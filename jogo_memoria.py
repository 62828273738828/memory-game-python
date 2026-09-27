import random
import time
import os

# ─── Cores para o terminal ─────────────────────────────────────────────────────
VERMELHO = "\033[91m"
VERDE    = "\033[92m"
AMARELO  = "\033[93m"
AZUL     = "\033[94m"
MAGENTA  = "\033[95m"
CIANO    = "\033[96m"
BRANCO   = "\033[97m"
RESET    = "\033[0m"
NEGRITO  = "\033[1m"

# ─── Símbolos das cartas (pares) ───────────────────────────────────────────────
SIMBOLOS = ["🐉", "⚔️ ", "🛡️ ", "🏆", "💎", "🔥", "⚡", "🎮"]

def limpar():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def criar_tabuleiro(tamanho):
    """Cria e embaralha o tabuleiro com pares de símbolos."""
    simbolos = (SIMBOLOS * 2)[:tamanho * tamanho]
    random.shuffle(simbolos)
    tabuleiro = [simbolos[i * tamanho:(i + 1) * tamanho] for i in range(tamanho)]
    return tabuleiro

def mostrar_tabuleiro(tabuleiro, revelado, tamanho):
    """Mostra o estado atual do tabuleiro."""
    print(f"\n  {NEGRITO}{CIANO}=== JOGO DA MEMÓRIA ==={RESET}\n")

    # Números das colunas
    cabecalho = "     "
    for col in range(tamanho):
        cabecalho += f"  {AMARELO}{col + 1}{RESET}  "
    print(cabecalho)
    print("     " + "─────" * tamanho)

    for linha in range(tamanho):
        linha_display = f"  {AMARELO}{linha + 1}{RESET}  |"
        for col in range(tamanho):
            if revelado[linha][col]:
                linha_display += f" {tabuleiro[linha][col]} |"
            else:
                linha_display += f"  {AZUL}?{RESET}  |"
        print(linha_display)
        print("     " + "─────" * tamanho)

def obter_entrada(prompt, tamanho):
    """Obtém uma entrada válida de linha/coluna do jogador."""
    while True:
        try:
            valor = int(input(prompt)) - 1
            if 0 <= valor < tamanho:
                return valor
            else:
                print(f"{VERMELHO}  Digite um número entre 1 e {tamanho}.{RESET}")
        except ValueError:
            print(f"{VERMELHO}  Entrada inválida. Digite um número.{RESET}")

def jogar():
    """Loop principal do jogo."""
    limpar()
    print(f"\n  {NEGRITO}{MAGENTA}Bem-vindo ao Jogo da Memória!{RESET}")
    print(f"  {BRANCO}Encontre todos os pares para vencer.\n{RESET}")

    # Escolher dificuldade
    print(f"  {AMARELO}Escolha a dificuldade:{RESET}")
    print(f"  {VERDE}1{RESET} - Fácil  (2x2)")
    print(f"  {VERDE}2{RESET} - Médio  (4x4)")
    print(f"  {VERDE}3{RESET} - Difícil (4x4 com timer)\n")

    while True:
        escolha = input("  Sua escolha (1/2/3): ").strip()
        if escolha in ("1", "2", "3"):
            break
        print(f"{VERMELHO}  Digite 1, 2 ou 3.{RESET}")

    if escolha == "1":
        tamanho = 2
        limite_tempo = None
    elif escolha == "2":
        tamanho = 4
        limite_tempo = None
    else:
        tamanho = 4
        limite_tempo = 60  # segundos

    # Configuração
    tabuleiro = criar_tabuleiro(tamanho)
    revelado = [[False] * tamanho for _ in range(tamanho)]
    jogadas = 0
    pares_encontrados = 0
    total_pares = (tamanho * tamanho) // 2
    inicio = time.time()

    while pares_encontrados < total_pares:
        limpar()

        # Timer
        if limite_tempo:
            decorrido = int(time.time() - inicio)
            restante = limite_tempo - decorrido
            if restante <= 0:
                limpar()
                print(f"\n  {VERMELHO}{NEGRITO}⏰ Tempo esgotado! Fim de jogo!{RESET}")
                print(f"  Você encontrou {VERDE}{pares_encontrados}{RESET} de {total_pares} pares.\n")
                return
            cor_timer = VERMELHO if restante < 10 else AMARELO if restante < 20 else VERDE
            print(f"\n  ⏱️  Tempo restante: {cor_timer}{restante}s{RESET}")

        mostrar_tabuleiro(tabuleiro, revelado, tamanho)
        print(f"\n  {BRANCO}Jogadas: {AMARELO}{jogadas}{RESET}   |   "
              f"Pares encontrados: {VERDE}{pares_encontrados}/{total_pares}{RESET}\n")

        # Primeira carta
        print(f"  {CIANO}--- Primeira carta ---{RESET}")
        linha1 = obter_entrada("  Linha:  ", tamanho)
        col1   = obter_entrada("  Coluna: ", tamanho)

        if revelado[linha1][col1]:
            print(f"{VERMELHO}  Carta já revelada! Escolha outra.{RESET}")
            time.sleep(1)
            continue

        revelado[linha1][col1] = True
        limpar()
        if limite_tempo:
            decorrido = int(time.time() - inicio)
            restante = limite_tempo - decorrido
            cor_timer = VERMELHO if restante < 10 else AMARELO if restante < 20 else VERDE
            print(f"\n  ⏱️  Tempo restante: {cor_timer}{restante}s{RESET}")
        mostrar_tabuleiro(tabuleiro, revelado, tamanho)
        print(f"\n  Jogadas: {AMARELO}{jogadas}{RESET}   |   Pares encontrados: {VERDE}{pares_encontrados}/{total_pares}{RESET}\n")

        # Segunda carta
        print(f"  {CIANO}--- Segunda carta ---{RESET}")
        while True:
            linha2 = obter_entrada("  Linha:  ", tamanho)
            col2   = obter_entrada("  Coluna: ", tamanho)
            if (linha2, col2) == (linha1, col1) or revelado[linha2][col2]:
                print(f"{VERMELHO}  Escolha uma carta diferente que ainda esteja oculta.{RESET}")
            else:
                break

        revelado[linha2][col2] = True
        jogadas += 1

        limpar()
        if limite_tempo:
            decorrido = int(time.time() - inicio)
            restante = limite_tempo - decorrido
            cor_timer = VERMELHO if restante < 10 else AMARELO if restante < 20 else VERDE
            print(f"\n  ⏱️  Tempo restante: {cor_timer}{restante}s{RESET}")
        mostrar_tabuleiro(tabuleiro, revelado, tamanho)
        print(f"\n  Jogadas: {AMARELO}{jogadas}{RESET}   |   Pares encontrados: {VERDE}{pares_encontrados}/{total_pares}{RESET}\n")

        # Verificar par
        if tabuleiro[linha1][col1] == tabuleiro[linha2][col2]:
            print(f"  {VERDE}{NEGRITO}✅ Par encontrado! {tabuleiro[linha1][col1]}{RESET}")
            pares_encontrados += 1
            time.sleep(1.2)
        else:
            print(f"  {VERMELHO}❌ Não é um par. As cartas serão ocultadas novamente.{RESET}")
            time.sleep(1.5)
            revelado[linha1][col1] = False
            revelado[linha2][col2] = False

    # Tela de vitória
    decorrido = int(time.time() - inicio)
    limpar()
    print(f"\n  {NEGRITO}{VERDE}🏆 Parabéns! Você venceu! 🏆{RESET}\n")
    print(f"  {BRANCO}Jogadas: {AMARELO}{jogadas}{RESET}")
    print(f"  {BRANCO}Tempo:   {AMARELO}{decorrido} segundos{RESET}\n")

    # Avaliação
    if jogadas <= total_pares + 2:
        print(f"  Avaliação: {AMARELO}⭐⭐⭐ Perfeito!{RESET}\n")
    elif jogadas <= total_pares * 2:
        print(f"  Avaliação: {AMARELO}⭐⭐ Muito bom!{RESET}\n")
    else:
        print(f"  Avaliação: {AMARELO}⭐ Bom esforço!{RESET}\n")

def main():
    while True:
        jogar()
        again = input(f"  {CIANO}Jogar novamente? (s/n): {RESET}").strip().lower()
        if again != "s":
            print(f"\n  {MAGENTA}Obrigado por jogar! Até a próxima. 👋{RESET}\n")
            break

if __name__ == "__main__":
    main()
