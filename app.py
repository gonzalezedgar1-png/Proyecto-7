import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Análisis de anuncios de vehículos en EE.UU.")

@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

df = load_data()

st.write("Vista previa del dataset:")
st.dataframe(df.head())

if st.checkbox("Mostrar histograma de precios"):
    fig_price = px.histogram(df, x="price", title="Distribución de precios")
    st.plotly_chart(fig_price)

if st.checkbox("Mostrar relación entre año y precio"):
    fig_year_price = px.scatter(
        df,
        x="model_year",
        y="price",
        title="Precio vs año del vehículo"
    )
    st.plotly_chart(fig_year_price)

st.subheader("Filtrar por tipo de vehículo")
vehicle_type = st.selectbox("Selecciona un tipo:", sorted(df['type'].dropna().unique()))

filtered_df = df[df['type'] == vehicle_type]

st.write(f"Mostrando vehículos tipo: {vehicle_type}")
st.dataframe(filtered_df.head())

fig_type = px.histogram(filtered_df, x="price", title=f"Distribución de precios para {vehicle_type}")
st.plotly_chart(fig_type)




