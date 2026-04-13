# PROJETO: GESTÃO DE PEÇAS E QUALIDADE
# Autora: Tatiana Maschio
# Disciplina: Algoritmos e Lógica de Programação


def calcular_caixas(pecas_aprovadas):
    caixas = []
    for i in range(0, len(pecas_aprovadas), 10):
        grupo = pecas_aprovadas[i:i + 10]
        if len(grupo) == 10:
            caixas.append(grupo)
    return caixas


def cadastrar_peca(pecas_aprovadas, pecas_reprovadas):
    print("\n--- CADASTRO DE PEÇA ---")

    id_peca = input("Digite o identificador da peça: ").strip()

    try:
        peso = float(input("Digite o peso da peça (95g a 105g): "))
        comprimento = float(input("Digite o comprimento da peça (10cm a 20cm): "))
    except ValueError:
        print("❌ Erro: peso e comprimento devem ser números.")
        return

    cor = input("Digite a cor da peça (Azul ou Verde): ").strip().capitalize()

    motivos_reprovacao = []

    if not (95 <= peso <= 105):
        motivos_reprovacao.append(f"Peso fora do padrão ({peso}g)")

    if cor not in ["Azul", "Verde"]:
        motivos_reprovacao.append(f"Cor inválida ({cor})")

    if not (10 <= comprimento <= 20):
        motivos_reprovacao.append(f"Comprimento fora do padrão ({comprimento}cm)")

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    if len(motivos_reprovacao) == 0:
        peca["status"] = "Aprovada"
        pecas_aprovadas.append(peca)
        print("✅ RESULTADO: PEÇA APROVADA!")

        caixas = calcular_caixas(pecas_aprovadas)
        if len(pecas_aprovadas) % 10 == 0:
            print(f"📦 LOGÍSTICA: Caixa {len(caixas)} fechada com sucesso!")

    else:
        peca["status"] = "Reprovada"
        peca["motivos"] = motivos_reprovacao
        pecas_reprovadas.append(peca)
        print("❌ RESULTADO: PEÇA REPROVADA!")
        print("Motivo(s):")
        for motivo in motivos_reprovacao:
            print(f"- {motivo}")


def listar_pecas(pecas_aprovadas, pecas_reprovadas):
    print("\n=== PEÇAS APROVADAS ===")
    if len(pecas_aprovadas) == 0:
        print("Nenhuma peça aprovada cadastrada.")
    else:
        for peca in pecas_aprovadas:
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm | "
                f"Status: {peca['status']}"
            )

    print("\n=== PEÇAS REPROVADAS ===")
    if len(pecas_reprovadas) == 0:
        print("Nenhuma peça reprovada cadastrada.")
    else:
        for peca in pecas_reprovadas:
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm | "
                f"Status: {peca['status']}"
            )
            print("Motivo(s):")
            for motivo in peca["motivos"]:
                print(f"  - {motivo}")


def remover_peca(pecas_aprovadas, pecas_reprovadas):
    id_remover = input("\nDigite o ID da peça que deseja remover: ").strip()

    removida = False

    for i, peca in enumerate(pecas_aprovadas):
        if peca["id"] == id_remover:
            del pecas_aprovadas[i]
            removida = True
            break

    if not removida:
        for i, peca in enumerate(pecas_reprovadas):
            if peca["id"] == id_remover:
                del pecas_reprovadas[i]
                removida = True
                break

    if removida:
        print(f"✅ Peça {id_remover} removida com sucesso.")
    else:
        print(f"❌ Nenhuma peça com ID {id_remover} foi encontrada.")


def listar_caixas_fechadas(pecas_aprovadas):
    caixas = calcular_caixas(pecas_aprovadas)

    print("\n=== CAIXAS FECHADAS ===")
    if len(caixas) == 0:
        print("Nenhuma caixa fechada ainda.")
    else:
        for indice, caixa in enumerate(caixas, start=1):
            ids = [peca["id"] for peca in caixa]
            print(f"Caixa {indice}: {ids}")


def gerar_relatorio(pecas_aprovadas, pecas_reprovadas):
    total_cadastradas = len(pecas_aprovadas) + len(pecas_reprovadas)
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)

    if total_cadastradas > 0:
        percentual_aprovacao = (total_aprovadas / total_cadastradas) * 100
        percentual_reprovacao = (total_reprovadas / total_cadastradas) * 100
    else:
        percentual_aprovacao = 0
        percentual_reprovacao = 0

    caixas = calcular_caixas(pecas_aprovadas)
    quantidade_caixas = len(caixas)
    pecas_fora_de_caixa = total_aprovadas % 10

    contagem_motivos = {}

    for peca in pecas_reprovadas:
        for motivo in peca["motivos"]:
            if motivo in contagem_motivos:
                contagem_motivos[motivo] += 1
            else:
                contagem_motivos[motivo] = 1

    print("\n=== RELATÓRIO FINAL DE PRODUTIVIDADE ===")
    print(f"Total de peças cadastradas: {total_cadastradas}")
    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")
    print(f"Percentual de reprovação: {percentual_reprovacao:.2f}%")
    print(f"Quantidade de caixas fechadas: {quantidade_caixas}")
    print(f"Peças aprovadas fora de caixa fechada: {pecas_fora_de_caixa}")

    print("\nMotivos de reprovação:")
    if len(contagem_motivos) == 0:
        print("Nenhum motivo de reprovação registrado.")
    else:
        for motivo, quantidade in contagem_motivos.items():
            print(f"- {motivo}: {quantidade} ocorrência(s)")


def mostrar_menu():
    print("\n" + "=" * 45)
    print("      SISTEMA DE AUTOMAÇÃO INDUSTRIAL")
    print("=" * 45)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas e reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final de produtividade")
    print("0. Sair")
    print("=" * 45)


def sistema_automacao():
    pecas_aprovadas = []
    pecas_reprovadas = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca(pecas_aprovadas, pecas_reprovadas)

        elif opcao == "2":
            listar_pecas(pecas_aprovadas, pecas_reprovadas)

        elif opcao == "3":
            remover_peca(pecas_aprovadas, pecas_reprovadas)

        elif opcao == "4":
            listar_caixas_fechadas(pecas_aprovadas)

        elif opcao == "5":
            gerar_relatorio(pecas_aprovadas, pecas_reprovadas)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":

    sistema_automacao()
    
    sistema_automacao()
