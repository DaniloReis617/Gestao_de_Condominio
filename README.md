# Gestao_de_Condominio

É um exemplo básico de um sistema web para administração de condomínios usando Python e Streamlit. O sistema será multiempresas e multiusuários, com perfis como síndico, subsíndico, administrador (ADM) e moradores. Vou focar em algumas funcionalidades principais como gestão financeira, controle de estoque, pagamentos de moradores, geração de comprovantes de pagamento e dashboard financeiro.

Estrutura do Projeto
Descrições de Cada Página
app.py: Gerencia a navegação entre as diferentes páginas do aplicativo com base no perfil do usuário logado.
auth.py: Contém funções para login e autenticação, valida o login do usuário e retorna o perfil do usuário logado.
dashboard.py: Exibe o dashboard financeiro com gráficos de receita, despesa e saldo mensal.
database.py: Inicializa e gerencia o banco de dados SQLite, incluindo a criação de tabelas.
finance.py: Permite adicionar e visualizar registros financeiros de receitas e despesas.
inventory.py: Permite adicionar e visualizar itens no estoque do condomínio.
payments.py: Permite registrar e visualizar pagamentos efetuados pelos moradores.
providers.py: Permite adicionar e visualizar prestadores de serviço que trabalham para o condomínio.
settings.py: Permite ao administrador adicionar e editar usuários e condomínios. Contém formulários para essas ações e funções de envio de email de convite.
invite_residents.py: Permite enviar convites por e-mail para novos moradores completarem seu cadastro.
complete_registration.py: Permite que novos usuários completem seu cadastro após receberem um convite por e-mail.