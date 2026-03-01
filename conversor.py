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

        self.title("Conversor de PDF Moderno")
        self.geometry("600x400")
        
        self.caminho_pdf = ""
        self.pasta_destino = ""

        # --- Elementos da Interface ---
        self.label_titulo = ctk.CTkLabel(self, text="Conversor de PDF para Imagem", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # 1. Selecionar Arquivo
        self.btn_selecionar = ctk.CTkButton(self, text="1. Selecionar Arquivo PDF", command=self.selecionar_arquivo)
        self.btn_selecionar.pack(pady=10)
        self.label_arquivo = ctk.CTkLabel(self, text="Nenhum arquivo selecionado", text_color="gray")
        self.label_arquivo.pack()

        # 2. Selecionar Destino
        self.btn_destino = ctk.CTkButton(self, text="2. Escolher Local de Salvamento", command=self.selecionar_destino, fg_color="#555555")
        self.btn_destino.pack(pady=15)
        self.label_destino = ctk.CTkLabel(self, text="Pasta padrão: (Pasta do PDF)", text_color="gray")
        self.label_destino.pack()

        # 3. Botão Converter
        self.btn_converter = ctk.CTkButton(self, text="3. Iniciar Conversão", 
                                          command=self.iniciar_conversao, 
                                          fg_color="#2c7a2c", hover_color="#1e521e",
                                          state="disabled")
        self.btn_converter.pack(pady=25)

    def selecionar_arquivo(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        if caminho:
            self.caminho_pdf = caminho
            self.label_arquivo.configure(text=f"PDF: {os.path.basename(caminho)}", text_color="white")
            # Se ainda não escolheu destino, sugere a pasta do PDF
            if not self.pasta_destino:
                self.pasta_destino = os.path.dirname(caminho)
                self.label_destino.configure(text=f"Destino: {self.pasta_destino}")
            self.verificar_pronto()

    def selecionar_destino(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.pasta_destino = pasta
            self.label_destino.configure(text=f"Destino: {pasta}", text_color="white")
            self.verificar_pronto()

    def verificar_pronto(self):
        """Ativa o botão de converter se houver arquivo e pasta"""
        if self.caminho_pdf and self.pasta_destino:
            self.btn_converter.configure(state="normal")

    def iniciar_conversao(self):
        PATH_POPPLER = r'C:\poppler\Library\bin' # Verifique se este caminho está correto no seu PC
        
        try:
            self.btn_converter.configure(state="disabled", text="Processando...")
            self.update()

            # Converte o PDF
            paginas = convert_from_path(self.caminho_pdf, dpi=300, poppler_path=PATH_POPPLER)

            # Salva na pasta escolhida
            for i, pagina in enumerate(paginas, start=1):
                nome_saida = os.path.join(self.pasta_destino, f"pagina_{i}.png")
                pagina.save(nome_saida, "PNG")

            messagebox.showinfo("Sucesso", f"Concluído!\n{len(paginas)} imagens salvas em:\n{self.pasta_destino}")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um problema: {e}")
        finally:
            self.btn_converter.configure(state="normal", text="3. Iniciar Conversão")

if __name__ == "__main__":
    app = AppConversor()
    app.mainloop()