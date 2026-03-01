🚀 Conversor de PDF para Imagem (Versão Pro)
Este repositório contém um utilitário robusto em Python que converte arquivos PDF em imagens (PNG/JPG) de alta resolução. O projeto conta com uma interface gráfica moderna e intuitiva.

✨ Novidades da Versão Atual
Interface Moderna: Utiliza a biblioteca CustomTkinter para um visual estilo Dark Mode.

Seleção de Destino: Agora você pode escolher exatamente em qual pasta as imagens serão salvas.

Fluxo Inteligente: O botão de conversão só é habilitado após a seleção de um arquivo válido.

Resolução Profissional: Renderização fixa em 300 DPI para garantir máxima legibilidade.

🛠️ Funcionalidades
Seleção de Arquivo: Interface nativa para navegar e escolher o PDF.

Definição de Destino: Botão dedicado para escolher a pasta de saída (por padrão, sugere a pasta de origem do PDF).

Processamento em Lote: Converte todas as páginas do documento automaticamente.

Feedback Visual: Labels dinâmicos que mostram o status da seleção e caixas de diálogo (messagebox) para confirmação de sucesso ou erro.

📋 Requisitos do Sistema
Python 3.8+

Bibliotecas Python:

PowerShell
pip install pdf2image customtkinter
Dependência Externa (Poppler): O motor de renderização. No Windows, extraia e aponte para a pasta bin.
Exemplo configurado no código: C:\poppler\Library\bin.

🚀 Como Executar
Via Python
Certifique-se de que o Poppler está no caminho correto.

Execute o script:

PowerShell
python conversor.py
Selecione o arquivo, escolha o destino e clique em Iniciar Conversão.

Criando o Executável (.exe)
Para gerar um arquivo único que funcione em outros PCs:

Instale o PyInstaller:

PowerShell
pip install pyinstaller
Gere o executável com suporte ao tema visual:

PowerShell
pyinstaller --noconsole --onefile --collect-all customtkinter conversor.py
O arquivo final estará na pasta dist/.

📂 Estrutura do Código
AppConversor(ctk.CTk): Classe principal que gerencia a janela e os eventos.

selecionar_arquivo(): Gerencia a busca do PDF.

selecionar_destino(): Gerencia a escolha da pasta de salvamento.

iniciar_conversao(): Realiza a chamada ao pdf2image e salva os arquivos individualmente.

📝 Observações
O formato padrão de saída é PNG, mas pode ser alterado no código para JPEG.

Certifique-se de ter permissões de escrita na pasta de destino escolhida.

--- Desenvolvido por André Luiz ---