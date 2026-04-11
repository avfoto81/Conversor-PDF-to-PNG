import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path

# Configuração de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppConversor(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de PDF para Imagem")
        self.geometry("700x850")
        self.resizable(True, True)
        self.minsize(700, 850)
        
        # Configuração de cores modernas
        self.cor_bg = "#1a1a1a"
        self.cor_frame = "#2d2d2d"
        self.cor_accent = "#3b82f6"
        self.cor_sucesso = "#10b981"
        self.cor_erro = "#ef4444"
        
        self.configure(fg_color=self.cor_bg)
        
        self.caminho_pdf = ""
        self.pasta_destino = ""

        # ---  Container Principal ---
        self.main_container = ctk.CTkScrollableFrame(self, fg_color=self.cor_bg)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Cabeçalho ---
        self._criar_cabecalho()

        # --- Card 1: Selecionar Arquivo ---
        self._criar_card_arquivo()

        # --- Separador ---
        self._criar_separador()

        # --- Card 2: Selecionar Destino ---
        self._criar_card_destino()

        # --- Separador ---
        self._criar_separador()

        # --- Card 3: Converter ---
        self._criar_card_conversao()

        # --- Rodapé ---
        self._criar_rodape()

    def _criar_cabecalho(self):
        """Cria o cabeçalho da aplicação"""
        header_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 30))

        # Título principal
        titulo = ctk.CTkLabel(
            header_frame,
            text="📄 Conversor de PDF",
            font=("Roboto", 32, "bold"),
            text_color="white"
        )
        titulo.pack(anchor="w")

        # Subtítulo
        subtitulo = ctk.CTkLabel(
            header_frame,
            text="Converta seus PDFs em imagens de alta qualidade",
            font=("Roboto", 14),
            text_color="#a0a0a0"
        )
        subtitulo.pack(anchor="w", pady=(5, 0))

    def _criar_card_arquivo(self):
        """Cria o card para seleção de arquivo"""
        card = ctk.CTkFrame(self.main_container, fg_color=self.cor_frame, corner_radius=12)
        card.pack(fill="x", pady=(0, 15))

        # Ícone e títuilo do card
        header_card = ctk.CTkFrame(card, fg_color="transparent")
        header_card.pack(fill="x", padx=20, pady=(15, 10))

        titulo_card = ctk.CTkLabel(
            header_card,
            text="📁 Passo 1: Selecione o PDF",
            font=("Roboto", 16, "bold"),
            text_color="white"
        )
        titulo_card.pack(anchor="w")

        # Botão
        self.btn_selecionar = ctk.CTkButton(
            card,
            text="Selecionar Arquivo PDF",
            command=self.selecionar_arquivo,
            fg_color=self.cor_accent,
            hover_color="#2563eb",
            height=40,
            font=("Roboto", 13, "bold"),
            corner_radius=8
        )
        self.btn_selecionar.pack(fill="x", padx=20, pady=(0, 15))

        # Label de arquivo
        self.label_arquivo = ctk.CTkLabel(
            card,
            text="Nenhum arquivo selecionado",
            text_color="#808080",
            font=("Roboto", 12)
        )
        self.label_arquivo.pack(anchor="w", padx=20, pady=(0, 15))

    def _criar_card_destino(self):
        """Cria o card para seleção de destino"""
        card = ctk.CTkFrame(self.main_container, fg_color=self.cor_frame, corner_radius=12)
        card.pack(fill="x", pady=(0, 15))

        # Ícone e título do card
        header_card = ctk.CTkFrame(card, fg_color="transparent")
        header_card.pack(fill="x", padx=20, pady=(15, 10))

        titulo_card = ctk.CTkLabel(
            header_card,
            text="💾 Passo 2: Escolha o Local de Salvamento",
            font=("Roboto", 16, "bold"),
            text_color="white"
        )
        titulo_card.pack(anchor="w")

        # Botão
        self.btn_destino = ctk.CTkButton(
            card,
            text="Selecionar Pasta de Destino",
            command=self.selecionar_destino,
            fg_color="#8b5cf6",
            hover_color="#7c3aed",
            height=40,
            font=("Roboto", 13, "bold"),
            corner_radius=8
        )
        self.btn_destino.pack(fill="x", padx=20, pady=(0, 15))

        # Label de destino
        self.label_destino = ctk.CTkLabel(
            card,
            text="Pasta padrão: (Mesmo local do PDF)",
            text_color="#808080",
            font=("Roboto", 12)
        )
        self.label_destino.pack(anchor="w", padx=20, pady=(0, 15))

    def _criar_card_conversao(self):
        """Cria o card para conversão"""
        card = ctk.CTkFrame(self.main_container, fg_color=self.cor_frame, corner_radius=12)
        card.pack(fill="x", pady=(0, 15))

        # Ícone e título do card
        header_card = ctk.CTkFrame(card, fg_color="transparent")
        header_card.pack(fill="x", padx=20, pady=(15, 10))

        titulo_card = ctk.CTkLabel(
            header_card,
            text="⚡ Passo 3: Iniciar Conversão",
            font=("Roboto", 16, "bold"),
            text_color="white"
        )
        titulo_card.pack(anchor="w")

        # Botão converter
        self.btn_converter = ctk.CTkButton(
            card,
            text="Iniciar Conversão",
            command=self.iniciar_conversao,
            fg_color=self.cor_sucesso,
            hover_color="#059669",
            height=45,
            font=("Roboto", 14, "bold"),
            corner_radius=8,
            state="disabled"
        )
        self.btn_converter.pack(fill="x", padx=20, pady=(0, 15))

        # Barra de progresso
        self.progresso = ctk.CTkProgressBar(
            card,
            fg_color="#444444",
            progress_color=self.cor_sucesso,
            height=6,
            corner_radius=3
        )
        self.progresso.pack(fill="x", padx=20, pady=(0, 10))
        self.progresso.set(0)

        # Label de status
        self.label_status = ctk.CTkLabel(
            card,
            text="Pronto para converter",
            text_color="#808080",
            font=("Roboto", 11)
        )
        self.label_status.pack(anchor="w", padx=20, pady=(0, 15))

    def _criar_separador(self):
        """Cria um separador visual"""
        sep = ctk.CTkFrame(self.main_container, fg_color="#3a3a3a", height=1)
        sep.pack(fill="x", pady=(0, 15))

    def _criar_rodape(self):
        """Cria o rodapé da aplicação"""
        footer = ctk.CTkFrame(self.main_container, fg_color="transparent")
        footer.pack(fill="x", pady=(15, 0), side="bottom")

        info = ctk.CTkLabel(
            footer,
            text="✨ Interface moderna com customtkinter | Qualidade: 300 DPI",
            text_color="#606060",
            font=("Roboto", 10)
        )
        info.pack()

    def selecionar_arquivo(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        if caminho:
            self.caminho_pdf = caminho
            nome_arquivo = os.path.basename(caminho)
            self.label_arquivo.configure(
                text=f"✅ {nome_arquivo}",
                text_color="#10b981"
            )
            # Se ainda não escolheu destino, sugere a pasta do PDF
            if not self.pasta_destino:
                self.pasta_destino = os.path.dirname(caminho)
                self.label_destino.configure(
                    text=f"📂 {os.path.basename(self.pasta_destino) or self.pasta_destino}",
                    text_color="#10b981"
                )
            self.verificar_pronto()

    def selecionar_destino(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.pasta_destino = pasta
            self.label_destino.configure(
                text=f"📂 {os.path.basename(pasta) or pasta}",
                text_color="#10b981"
            )
            self.verificar_pronto()

    def verificar_pronto(self):
        """Ativa o botão de converter se houver arquivo e pasta"""
        if self.caminho_pdf and self.pasta_destino:
            self.btn_converter.configure(state="normal")
            self.label_status.configure(text="Tudo pronto! Clique para converter", text_color="#10b981")
        else:
            self.label_status.configure(text="Complete os 2 passos anteriores", text_color="#f59e0b")

    def iniciar_conversao(self):
        PATH_POPPLER = r'C:\poppler\Library\bin'
        
        try:
            self.btn_converter.configure(state="disabled", text="⏳ Processando...")
            self.label_status.configure(text="Convertendo PDF para imagens...rença", text_color="#3b82f6")
            self.progresso.set(0)
            self.update()

            # Converte o PDF
            paginas = convert_from_path(self.caminho_pdf, dpi=300, poppler_path=PATH_POPPLER)
            total_paginas = len(paginas)

            # Salva na pasta escolhida com barra de progresso
            for i, pagina in enumerate(paginas, start=1):
                nome_saida = os.path.join(self.pasta_destino, f"pagina_{i}.png")
                pagina.save(nome_saida, "PNG")
                
                # Atualiza a barra de progresso
                progresso_valor = i / total_paginas
                self.progresso.set(progresso_valor)
                self.label_status.configure(
                    text=f"Convertendo página {i} de {total_paginas}...",
                    text_color="#3b82f6"
                )
                self.update()

            # Sucesso!
            self.progresso.set(1)
            self.label_status.configure(
                text=f"✅ Concluído! {total_paginas} imagens salvas",
                text_color=self.cor_sucesso
            )
            messagebox.showinfo(
                "Sucesso! 🎉",
                f"Conversão realizada com sucesso!\n\n"
                f"📊 {total_paginas} imagens criadas\n"
                f"📁 Salvas em:\n{self.pasta_destino}"
            )
            
        except Exception as e:
            self.progresso.set(0)
            self.label_status.configure(
                text=f"❌ Erro na conversão",
                text_color=self.cor_erro
            )
            messagebox.showerror("Erro", f"Ocorreu um problema:\n\n{e}")
        finally:
            self.btn_converter.configure(state="normal", text="Iniciar Conversão")

if __name__ == "__main__":
    app = AppConversor()
    app.mainloop()