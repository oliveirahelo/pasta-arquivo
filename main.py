import os
import flet as ft

def main(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"
    
    # Função para criar pastas
    def criar_pasta(e):
        nome = texto_recebido.value.strip()
        if not nome:
            informativo.value = "Digite um nome válido."
            page.update()
            return
        try:
            os.mkdir(nome)
            informativo.value = f"Pasta criada: '{nome}'"
        except FileExistsError:
            informativo.value = f"A pasta '{nome}' já existe."
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()
    
    # Função para criar arquivos na pasta atual
    def criar_arquivo_pasta_atual(e):
        nome = texto_recebido.value.strip()
        if not nome:
            informativo.value = "Digite um nome válido."
            page.update()
            return
        try:
            with open(nome, "w") as f:
                pass
            informativo.value = f"Arquivo criado na pasta atual: '{nome}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    # Função para criar arquivos dentro de uma pasta específica
    def criar_arquivo_em_pasta(e):
        texto = texto_recebido.value.strip()
        if not texto:
            informativo.value = "Digite no formato: pasta/arquivo.extensao"
            page.update()
            return
        
        # Verifica se tem pelo menos uma barra (/) para separar pasta do arquivo
        if "/" not in texto and "\\" not in texto:
            informativo.value = "Digite no formato: pasta/arquivo.extensao"
            page.update()
            return
        
        try:
            # Cria a pasta se não existir
            pasta = os.path.dirname(texto)
            if pasta and not os.path.exists(pasta):
                os.makedirs(pasta)
            
            # Cria o arquivo dentro da pasta
            with open(texto, "w") as f:
                pass
            informativo.value = f"Arquivo criado em '{texto}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    # Função para listar arquivos na pasta atual
    def listar_arquivos(e):
        try:
            arquivos = os.listdir()
            if arquivos:
                informativo.value = "Arquivos e pastas:\n" + "\n".join(arquivos)
            else:
                informativo.value = "Nenhum arquivo ou pasta na pasta atual."
        except Exception as erro:
            informativo.value = f"Erro ao listar: {erro}"
        page.update()

    # Função para renomear arquivo/pasta
    def renomear_arquivo(e):
        texto = texto_recebido.value.strip()
        if not texto or "->" not in texto:
            informativo.value = "Digite no formato: nome_antigo -> nome_novo"
            page.update()
            return
        
        try:
            antigo, novo = map(str.strip, texto.split("->"))
            os.rename(antigo, novo)
            informativo.value = f"Renomeado '{antigo}' para '{novo}'"
        except FileNotFoundError:
            informativo.value = f"Arquivo ou pasta '{antigo}' não encontrado."
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    # Função para verificar e excluir arquivo/pasta
    def verificar_excluir(e):
        nome = texto_recebido.value.strip()
        if not nome:
            informativo.value = "Digite um nome válido."
            page.update()
            return
        if os.path.exists(nome):
            try:
                if os.path.isfile(nome):
                    os.remove(nome)
                    informativo.value = f"Arquivo '{nome}' removido."
                elif os.path.isdir(nome):
                    os.rmdir(nome)
                    informativo.value = f"Pasta '{nome}' removida."
                else:
                    informativo.value = f"'{nome}' não é arquivo nem pasta comum."
            except OSError as erro:
                informativo.value = f"Erro ao remover: {erro}"
        else:
            informativo.value = f"'{nome}' não existe."
        page.update()

    # Campos e botões
    texto_recebido = ft.TextField(label="Nome ou comando (ex: nome_arquivo, pasta/arquivo, ou nome_antigo -> nome_novo)", width=400)
    
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="WHITE", width=150, on_click=criar_pasta)
    botao_arquivo_atual = ft.ElevatedButton("CRIAR ARQUIVO (PASTA ATUAL)", bgcolor="CYAN", color="BLACK", width=200, on_click=criar_arquivo_pasta_atual)
    botao_arquivo_em_pasta = ft.ElevatedButton("CRIAR ARQUIVO (EM PASTA)", bgcolor="GREEN", color="WHITE", width=200, on_click=criar_arquivo_em_pasta)
    botao_listar = ft.ElevatedButton("LISTAR ARQUIVOS", bgcolor="BLUE", color="WHITE", width=150, on_click=listar_arquivos)
    botao_renomear = ft.ElevatedButton("RENOMEAR (antigo -> novo)", bgcolor="ORANGE", color="BLACK", width=200, on_click=renomear_arquivo)
    botao_excluir = ft.ElevatedButton("VERIFICAR & EXCLUIR", bgcolor="RED", color="WHITE", width=150, on_click=verificar_excluir)
    
    informativo = ft.Text("", size=16, color="white")

    # Layout
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo_atual, botao_arquivo_em_pasta], alignment="center", spacing=10),
        ft.Row([botao_listar, botao_renomear, botao_excluir], alignment="center", spacing=10),
        ft.Row([informativo], alignment="center")
    )

ft.app(target=main)