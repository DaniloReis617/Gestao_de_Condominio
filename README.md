# Gestao_de_Condominio

Descrição Geral
O seu aplicativo é uma plataforma de gerenciamento de condomínios que permite a administração de recursos financeiros, estoque de materiais, pagamentos efetuados pelos moradores, e gestão de prestadores de serviços. Ele suporta múltiplos usuários com diferentes perfis (Administrador, Síndico, Subsíndico, Morador) e múltiplos condomínios. Abaixo está uma explicação detalhada das funcionalidades e componentes do aplicativo.

Funcionalidades Principais
Autenticação de Usuários

Os usuários podem fazer login utilizando email e senha.
Diferentes perfis de usuários (Administrador, Síndico, Subsíndico, Morador) têm diferentes níveis de acesso e permissões.
Dashboard Financeiro

Exibe gráficos e tabelas com informações sobre receitas, despesas e saldo do condomínio.
Permite a visualização mensal de receitas, despesas e saldo acumulado.
Gerenciamento Financeiro

Permite a adição e visualização de registros financeiros, categorizados como receitas ou despesas.
Os registros incluem detalhes como data, descrição e valor.
Gerenciamento de Estoque

Permite a adição e visualização de itens no estoque do condomínio.
Os registros de estoque incluem detalhes como nome do item, quantidade e data de adição.
Gerenciamento de Pagamentos

Permite o registro e visualização de pagamentos efetuados pelos moradores.
Os registros de pagamentos incluem detalhes como ID do morador, valor e data do pagamento.
Gerenciamento de Prestadores de Serviços

Permite a adição e visualização de prestadores de serviços que trabalham para o condomínio.
Os registros de prestadores incluem detalhes como nome, serviço prestado e informações de contato.
Configurações de Usuários e Condomínios

Permite ao administrador adicionar e editar usuários e condomínios.
Envia convites por e-mail para novos usuários completarem seu cadastro.
Convite de Moradores

Permite enviar convites por e-mail para novos moradores completarem seu cadastro.
Completar Cadastro

Permite que novos usuários completarem seu cadastro após receberem um convite por e-mail.
Estrutura e Fluxo de Trabalho
app.py

Arquivo principal do aplicativo.
Gerencia a navegação entre as diferentes páginas com base nos parâmetros da URL.
Define a estrutura da aplicação e configurações gerais.
auth.py

Gerencia a autenticação de usuários.
Funções de login e validação de usuários.
Função get_user_profile retorna o perfil do usuário logado.
dashboard.py

Exibe o dashboard financeiro.
Mostra gráficos de receita, despesa e saldo acumulado.
database.py

Inicializa e gerencia o banco de dados SQLite.
Cria as tabelas necessárias para o funcionamento do aplicativo.
finance.py

Gerencia as operações financeiras.
Permite adicionar novos registros financeiros e visualizar registros existentes.
inventory.py

Gerencia o estoque de materiais do condomínio.
Permite adicionar novos itens ao estoque e visualizar itens existentes.
payments.py

Gerencia os pagamentos efetuados pelos moradores.
Permite registrar novos pagamentos e visualizar pagamentos existentes.
providers.py

Gerencia os prestadores de serviços do condomínio.
Permite adicionar novos prestadores e visualizar prestadores existentes.
settings.py

Gerencia as configurações de usuários e condomínios.
Permite adicionar e editar usuários e condomínios.
Envia convites por e-mail para novos usuários completarem seu cadastro.
invite_residents.py

Permite enviar convites por e-mail para novos moradores completarem seu cadastro.
complete_registration.py

Permite que novos usuários completem seu cadastro após receberem um convite por e-mail.
Explicação das Páginas
Página de Login (auth.py)
Função: login()
Descrição: Permite aos usuários fazer login no sistema usando seu email e senha. Valida as credenciais e, se corretas, direciona o usuário para a página inicial.
Dashboard Financeiro (dashboard.py)
Função: show_dashboard()
Descrição: Exibe um resumo financeiro do condomínio com gráficos de receitas, despesas e saldo acumulado mensalmente.
Gerenciamento Financeiro (finance.py)
Função: manage_finance()
Descrição: Permite aos usuários adicionar novos registros financeiros e visualizar registros existentes. Inclui campos para data, descrição, valor e tipo (receita ou despesa).
Gerenciamento de Estoque (inventory.py)
Função: manage_inventory()
Descrição: Permite aos usuários adicionar novos itens ao estoque e visualizar os itens existentes. Inclui campos para nome do item, quantidade e data de adição.
Gerenciamento de Pagamentos (payments.py)
Função: manage_payments()
Descrição: Permite aos usuários registrar novos pagamentos efetuados pelos moradores e visualizar pagamentos existentes. Inclui campos para ID do morador, valor e data do pagamento.
Gerenciamento de Prestadores de Serviços (providers.py)
Função: manage_providers()
Descrição: Permite aos usuários adicionar novos prestadores de serviços e visualizar prestadores existentes. Inclui campos para nome, serviço prestado e informações de contato.
Configurações de Usuários e Condomínios (settings.py)
Função: manage_settings()
Descrição: Centraliza as configurações de usuários e condomínios. Permite adicionar e editar usuários e condomínios, e enviar convites por e-mail para novos usuários completarem seu cadastro.
Convite de Moradores (invite_residents.py)
Função: invite_residents()
Descrição: Permite enviar convites por e-mail para novos moradores completarem seu cadastro.
Completar Cadastro (complete_registration.py)
Função: complete_registration()
Descrição: Permite que novos usuários completem seu cadastro após receberem um convite por e-mail. Inclui campos para email, nome de usuário e senha.

Fluxo de Trabalho
Login: O usuário faz login com email e senha.
Navegação: O usuário navega entre as páginas usando a barra lateral. O nome da página atual aparece na URL.
Dashboard: O usuário visualiza o resumo financeiro do condomínio.
Gerenciamento: Dependendo do perfil, o usuário pode gerenciar finanças, estoque, pagamentos e prestadores de serviços.
Configurações: O administrador pode adicionar e editar usuários e condomínios, e enviar convites por e-mail.
Convites e Cadastros: Novos usuários recebem convites por e-mail para completar seu cadastro no sistema.