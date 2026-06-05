from fpdf import FPDF

class GitCheatSheet(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(30, 144, 255) # Blue
        self.cell(0, 10, 'Guia de Comandos Git - Referência Rápida', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 10, label, 0, 1, 'L', 1)
        self.ln(2)

    def command_line(self, cmd, desc):
        self.set_font('Courier', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.cell(60, 8, cmd, 0, 0)
        self.set_font('Arial', '', 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 8, desc)
        self.ln(1)

def create_pdf():
    pdf = GitCheatSheet()
    pdf.add_page()
    
    # Seção 1: Configuração e Início
    pdf.chapter_title('1. Configuração e Início')
    pdf.command_line('git init', 'Inicializa um novo repositório Git na pasta atual.')
    pdf.command_line('git clone [url]', 'Clona um repositório existente do GitHub/GitLab.')
    pdf.command_line('git status', 'Mostra o estado atual dos arquivos (modificados, novos, etc).')
    
    # Seção 2: Salvando Alterações
    pdf.chapter_title('2. Ciclo de Alterações')
    pdf.command_line('git add .', 'Adiciona todas as mudanças para a área de preparação (staging).')
    pdf.command_line('git commit -m "texto"', 'Cria um ponto na história com uma mensagem explicativa.')
    pdf.command_line('git log', 'Mostra o histórico de commits do projeto.')
    
    # Seção 3: Branches (Ramos)
    pdf.chapter_title('3. Branches e Organização')
    pdf.command_line('git branch', 'Lista todos os ramos (branches) locais.')
    pdf.command_line('git checkout -b [nome]', 'Cria um novo ramo e muda para ele imediatamente.')
    pdf.command_line('git checkout [nome]', 'Muda para um ramo já existente.')
    pdf.command_line('git merge [nome]', 'Une as alterações de outro ramo ao seu ramo atual.')
    
    # Seção 4: Sincronização Remota (GitHub)
    pdf.chapter_title('4. Trabalhando com o GitHub')
    pdf.command_line('git remote add origin [url]', 'Conecta seu código local a um repositório no GitHub.')
    pdf.command_line('git push origin [branch]', 'Envia suas alterações locais para o servidor remoto.')
    pdf.command_line('git pull origin [branch]', 'Baixa e mescla as alterações do servidor para o seu PC.')
    
    # Dica de Ouro
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 10)
    pdf.set_text_color(128, 0, 0)
    pdf.multi_cell(0, 8, 'Dica: Nunca suba a pasta venv/ ou arquivos .env (com senhas) para o Git. Use sempre o .gitignore!')

    pdf.output('Comandos_Git_Referencia.pdf')

if __name__ == "__main__":
    create_pdf()
