import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Previsão de Renda", layout="centered")
st.image("https://cdn-icons-png.flaticon.com/512/2886/2886661.png", width=100)
st.title("📊 Previsão de Renda")
st.markdown("### ✨ Insira seus dados abaixo e veja sua previsão de renda em tempo real!")

col1, col2 = st.columns(2)

with col1:
    sexo = st.selectbox("Sexo", ["F", "M"])
    veiculo = st.checkbox("Possui veículo?")
    imovel = st.checkbox("Possui imóvel?")
    filhos = st.number_input("Quantidade de filhos", min_value=0, max_value=10, value=0)

with col2:
    tipo_renda = st.selectbox("Tipo de renda", ["Assalariado", "Autônomo", "Pensionista", "Servidor público", "Bolsista"])
    educacao = st.selectbox("Escolaridade", ["Superior completo", "Superior incompleto", "Ensino médio", "Ensino fundamental"])
    estado_civil = st.selectbox("Estado civil", ["Casado", "Solteiro", "Separado", "Viúvo"])
    tipo_residencia = st.selectbox("Tipo de residência", ["Casa", "Apartamento", "Alugada", "Com os pais", "Outros"])

idade = st.slider("Idade", 18, 100, 30)
tempo_emprego = st.slider("Tempo de emprego (anos)", 0.0, 50.0, 5.0)
pessoas_residencia = st.slider("Pessoas na residência", 1.0, 20.0, 2.0)

# Carregar modelo salvo
# modelo = pickle.load(open("modelo_renda.pkl", "rb"))

# Transformar dados em formato adequado para o modelo
# entrada = np.array([[valores transformados...]])

# if st.button("Prever Renda"):
#     predicao = modelo.predict(entrada)
#     st.success(f"💰 A renda mensal prevista é: **R$ {predicao[0]:,.2f}**")

st.markdown("---")
st.caption("Desenvolvido por Marcos José - Projeto EBAC")
