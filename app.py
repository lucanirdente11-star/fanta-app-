import streamlit as st
import pandas as pd

st.set_page_config(page_title="FantaHub Pro - Listone Serie A", page_icon="⚽", layout="wide")

st.title("⚽ FantaHub Pro - Listone Completo Serie A")

st.sidebar.header("📂 Carica Listone Serie A")
uploaded_file = st.sidebar.file_uploader("Carica il file Excel o CSV (es. di Fantacalcio.it):", type=["csv", "xlsx"])

# Se l'utente carica un file, usa quello; altrimenti mostra le istruzioni
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success(f"✅ Listone caricato con successo! Trovati **{len(df)}** giocatori.")

        # Tab dell'app
        tab1, tab2 = st.tabs(["🔍 Cerca Giocatore & Calcolo Asta", "📋 Listone Completo & Filtri"])

        with tab1:
            st.subheader("🔎 Cerca un giocatore")
            # Cerca per colonna Nome o Giocatore
            col_nome = "Nome" if "Nome" in df.columns else df.columns[0]
            
            giocatore_scelto = st.selectbox("Seleziona o cerca:", sorted(df[col_nome].astype(str).unique()))
            scheda = df[df[col_nome] == giocatore_scelto].iloc[0]
            
            st.write(scheda)

        with tab2:
            st.subheader("📋 Tabelle Filtri")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Errore nella lettura del file: {e}")
else:
    st.info("👋 **Come avere TUTTI i giocatori della Serie A:**")
    st.markdown("""
    1. Scarica il listone ufficiale in Excel o CSV da **Fantacalcio.it** (o da un altro sito di Fantacalcio).
    2. Apri il menu a sinistra dell'app (**`📂 Carica Listone Serie A`**).
    3. Trascina o seleziona il file scaricato.
    
    L'app leggerà all'istante l'intero database di tutti i 500+ giocatori con quotazioni, ruoli e squadre aggiornate!
    """)
