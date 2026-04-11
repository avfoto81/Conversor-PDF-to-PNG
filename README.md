🚀 Conversor de PDF para Imagem (Versão Pro)
Este repositório contém um utilitário robusto em Python que converte arquivos PDF em imagens (PNG/JPG) de alta resolução. O projeto conta com uma interface gráfica moderna, intuitiva e totalmente redesenhada.

✨ Novidades da Versão Atual
**Interface Ultra-Moderna**: Design em cards com layout limpo e profissional usando CustomTkinter.

**Barra de Progresso**: Acompanhe a conversão de cada página em tempo real.

**Feedback Visual Dinâmico**: Ícones e cores indicam o estado de cada etapa (✅ pronto, 🔄 processando, ❌ erro).

**Seleção Inteligente**: Escolha exatamente em qual pasta as imagens serão salvas.

**Fluxo por Passos**: Interface dividida em 3 passos claros com ícones visuais.

**Resolução Profissional**: Renderização fixa em 300 DPI para garantir máxima legibilidade.

**Executável Standalone**: `.exe` pronto para usar - não precisa de Python instalado!

🛠️ Funcionalidades
📁 **Seleção de Arquivo**: Interface nativa para navegar e escolher o PDF.

💾 **Definição de Destino**: Botão dedicado para escolher a pasta de saída (por padrão, sugere a pasta de origem do PDF).

⚡ **Processamento em Lote**: Converte todas as páginas do documento automaticamente.

📊 **Barra de Progresso**: Visualize o progresso de conversão em tempo real.

✨ **Feedback Visual**: Ícones emojis e cores dinâmicas mostram o status de cada etapa.

💬 **Mensagens Inteligentes**: Status detalhado durante a conversão (página X de Y).

🎨 **Design Moderno**: Novo layout em cards com paleta de cores profissional.

📋 Requisitos do Sistema
Python 3.8+

Bibliotecas Python:

PowerShell
pip install pdf2image customtkinter
Dependência Externa (Poppler): O motor de renderização. No Windows, extraia e aponte para a pasta bin.
Exemplo configurado no código: C:\poppler\Library\bin.

🚀 Como Executar

**Opção 1: Usar o Executável (Recomendado)**

1. Baixe o arquivo `conversor.exe` da pasta `dist/`
2. Execute diretamente (não precisa de Python instalado!)
3. Uma janela moderna da aplicação será aberta
4. Siga os 3 passos: selecione PDF → escolha destino → clique em converter

**Opção 2: Via Python**

Certifique-se de que o Poppler está no caminho correto.

Execute o script:

```powershell
python conversor.py
```

Selecione o arquivo, escolha o destino e clique em Iniciar Conversão.

**Opção 3: Gerar novo Executável**

Para gerar um arquivo único que funcione em outros PCs:

Instale o PyInstaller:

```powershell
pip install pyinstaller
```

Execute a compilação:

```powershell
pyinstaller conversor.spec
```

O arquivo final estará na pasta `dist/conversor.exe`.

📂 Estrutura do Código

**AppConversor(ctk.CTk)**: Classe principal que gerencia a janela e os eventos.

**_criar_cabecalho()**: Cria o cabeçalho com título e descrição.

**_criar_card_arquivo()**: Card para seleção de PDF.

**_criar_card_destino()**: Card para escolha da pasta de destino.

**_criar_card_conversao()**: Card com botão de conversão e barra de progresso.

**selecionar_arquivo()**: Gerencia a busca do PDF com feedback visual.

**selecionar_destino()**: Gerencia a escolha da pasta de salvamento.

**verificar_pronto()**: Valida se PDF e destino foram selecionados.

**iniciar_conversao()**: Realiza a conversão com barra de progresso em tempo real.

📝 Observações e Dicas

- O formato padrão de saída é **PNG** de alta qualidade (300 DPI).
- Certifique-se de ter permissões de escrita na pasta de destino escolhida.
- A barra de progresso atualiza em tempo real para cada página convertida.
- Mensagens coloridas indicam o status: verde ✅ (pronto), azul 🔄 (processando), vermelho ❌ (erro).
- O arquivo `conversor.exe` é standalone e pode ser distribuído livremente.
- Para modificar a qualidade/DPI, edite a linha `dpi=300` em `conversor.py`.

💡 **Dica**: Para melhor desempenho, coloque o `conversor.exe` em uma pasta raiz (ex: `C:\ConversorPDF\`) e crie um atalho no desktop.

---

Desenvolvido por André Luiz | Versão 2.0 - Interface Redesenhada