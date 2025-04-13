import streamlit as st

# Base de dados simulada
clientes = {
    'Ana': {'Cartão de Crédito': 1, 'Conta Corrente': 2, 'Poupança': 3, 'Renda Fixa': 4, 'Crédito Pessoal': 5},
    'Marcos': {'Cartão de Crédito': 2, 'Conta Corrente': 3, 'Poupança': 4, 'Renda Fixa': 5, 'Renda Variável': 0.6},
    'Pedro': {'Cartão de Crédito': 3, 'Conta Corrente': 4, 'Poupança': 5, 'Crédito Pessoal': 7},
    'Claudia': {'Cartão de Crédito': 4, 'Conta Corrente': 5, 'Poupança': 6},
    'José': {'Cartão de Crédito': 2, 'Conta Corrente': 5, 'Poupança': 6, 'Renda Fixa': 5,},
    'Renan': {'Cartão de Crédito': 1, 'Conta Corrente': 2, 'Poupança': 6, 'Renda Fixa': 2, 'Crédito Pessoal': 2}
}

# Descrições dos produtos
descricoes = {
    'Cartão de Crédito': "facilidade para compras do dia a dia",
    'Conta Corrente': "controle e movimentação do seu dinheiro",
    'Poupança': "ideal para guardar dinheiro com liquidez",
    'Renda Fixa': "segurança com bons rendimentos",
    'Crédito Pessoal': "ideal para emergências",
    'Renda Variável': "ótimo para quem busca maior rentabilidade"
}

# Função para recomendar produtos com base na similaridade (simulada)
def recomendar(nome_usuario):
    nome_usuario = nome_usuario.capitalize()

    if nome_usuario not in clientes:
        return []

    produtos_usuario = set(clientes[nome_usuario].keys())
    contagem_recomendacao = {}

    for outro_nome, produtos_outro in clientes.items():
        if outro_nome == nome_usuario:
            continue
        produtos_outro_set = set(produtos_outro.keys())
        similares = produtos_usuario.intersection(produtos_outro_set)

        if similares:
            novos = produtos_outro_set - produtos_usuario
            for produto in novos:
                contagem_recomendacao[produto] = contagem_recomendacao.get(produto, 0) + 1

    # Retorna os produtos mais recomendados
    recomendados = sorted(contagem_recomendacao.items(), key=lambda x: x[1], reverse=True)
    return [(produto, descricoes.get(produto, "")) for produto, _ in recomendados]

# Streamlit App
st.set_page_config(page_title="Fintech App", page_icon="💸", layout="centered",)
st.title("🤖 Fintech App - Sistema de Recomendação",)
st.markdown("### 💡 Veja recomendações personalizadas de produtos financeiros!")

if "acesso_recomendacao" not in st.session_state:
    st.session_state.acesso_recomendacao = False

if not st.session_state.acesso_recomendacao:
    if st.button("🚀 Acessar área de recomendações"):
        st.session_state.acesso_recomendacao = True

if st.session_state.acesso_recomendacao:
    nome_input = st.text_input("Digite seu nome para ver sugestões personalizadas:")
    if nome_input:
        nome = nome_input.strip().capitalize()
        st.markdown(f"### 👋 Olá, {nome}")

        recomendacoes = recomendar(nome)
        if recomendacoes:
            st.markdown("Temos sugestões personalizadas para você:")
            for produto, descricao in recomendacoes:
                st.success(f"✅ **{produto}** – {descricao}")
        else:
            st.warning("Nenhuma recomendação no momento. Explore nossos produtos!")
            st.markdown("Temos algumas sugestões para você:")
            st.markdown("✅ **Crédito Pessoal** – ideal para emergências\n✅ **Renda Fixa** – segurança com bons rendimentos")

        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.button("📊 Explorar Mais Produtos")
        with col2:
            st.button("🎯 Aceitar Oferta")


