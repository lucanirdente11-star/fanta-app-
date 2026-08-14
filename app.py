
import streamlit as st
import pandas as pd

st.set_page_config(page_title="FantaHub Pro - Database Serie A COMPLETO", page_icon="⚽", layout="wide")

st.title("⚽ FantaHub Pro - Guida Asta Serie A (1500 Crediti) - TUTTI I GIOCATORI")
st.caption("Database completo 587 giocatori - Tutti i ruoli con valutazioni, titolarità e spesa consigliata.")

# Carica dati completi parsati dal tuo listone
@st.cache_data
def load_data():
    df = pd.read_csv("listone_completo.csv")
    # rinomina per compatibilità con codice precedente
    df_ren = df.rename(columns={"Nome_Completo":"Nome", "Squadra_Estesa":"Squadra_Lunga"})
    # Mantieni anche codice squadra
    df_ren["Squadra"] = df_ren["Squadra"].apply(lambda x: x) # placeholder
    # Usa Squadra_Estesa come visual
    df_ren["Squadra_Display"] = df_ren["Squadra_Lunga"] + " (" + df["Squadra"] + ")"
    return df_ren

# Fallback se csv non trovato (per deployment) - usa dati incorporati
try:
    df = load_data()
except:
    # Se non trova csv, carica da fallback inline (verrà rigenerato)
    import os
    st.error("CSV non trovato, uso fallback")
    df = pd.DataFrame()

# --- SIDEBAR BUDGET ---
st.sidebar.header("⚙ Budget & Gestione Asta")
budget_totale = st.sidebar.number_input("Budget Iniziale (Crediti)", min_value=100, max_value=3000, value=1500)

st.sidebar.subheader("% Spesa Consigliata")
perc_p = st.sidebar.slider("Porta (%)", 1, 10, 4)
perc_d = st.sidebar.slider("Difesa (%)", 5, 20, 10)
perc_c = st.sidebar.slider("Centrocampo (%)", 10, 40, 26)
perc_a = st.sidebar.slider("Attacco (%)", 30, 80, 60)

b_p = (budget_totale * perc_p) / 100
b_d = (budget_totale * perc_d) / 100
b_c = (budget_totale * perc_c) / 100
b_a = (budget_totale * perc_a) / 100

def calcola_spesa_max(row):
    ruolo = row["Ruolo"]
    quot = row["Costo"]
    if ruolo == "Portiere":
        budget_r = b_p
    elif ruolo == "Difensore":
        budget_r = b_d
    elif ruolo == "Centrocampista":
        budget_r = b_c
    else:
        budget_r = b_a
    spesa = (quot / 100) * (budget_r * 0.8)
    return int(max(1, spesa))

df["Spesa_Max_Consigliata_(cr)"] = df.apply(calcola_spesa_max, axis=1)

# --- TABS ---
tab1, tab2 = st.tabs(["🔍 Cerca Giocatore & Scheda Asta", "📋 Listone Completo 587 Giocatori"])

with tab1:
    st.subheader(f"🔎 Cerca tra {len(df)} giocatori")
    search_input = st.text_input("✍ Scrivi il nome (es. LEAO, DYbALA, SOMMER):", "")
    if search_input:
        filtered_names = df[df["Nome"].str.contains(search_input, case=False, na=False)]["Nome"].tolist()
    else:
        filtered_names = sorted(df["Nome"].tolist())

    if filtered_names:
        selected_player = st.selectbox("Seleziona il calciatore:", filtered_names)
        player = df[df["Nome"] == selected_player].iloc[0]

        st.markdown(f"## 👤 {player['Nome']} - {player['Squadra_Lunga']} ({player['Squadra']})")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Ruolo", player["Ruolo"])
        col2.metric("Titolarità", f"{player['Titolarita_%']}%")
        col3.metric("SPESA MAX", f"{player['Spesa_Max_Consigliata_(cr)']} cr")
        col4.metric("Convenienza", player["Convenienza"])

        st.divider()
        st.markdown(f"""
        * **Status:** {player['Status']}
        * **Quotazione Fantamilioni:** {player['Costo']}
        * **Budget Ruolo Disponibile:** {int(b_p if player['Ruolo']=='Portiere' else b_d if player['Ruolo']=='Difensore' else b_c if player['Ruolo']=='Centrocampista' else b_a)} cr
        * **Squadra:** {player['Squadra_Lunga']}
        """)
    else:
        st.warning("Nessun giocatore trovato!")

with tab2:
    st.subheader(f"📋 Database Completo - {len(df)} Giocatori (TUTTI)")
    
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1:
        filtro_ruolo = st.multiselect("Ruolo:", options=sorted(df["Ruolo"].unique()), default=sorted(df["Ruolo"].unique()))
    with col_f2:
        filtro_squadra = st.multiselect("Squadra:", options=sorted(df["Squadra_Lunga"].unique()), default=sorted(df["Squadra_Lunga"].unique()))
    with col_f3:
        filtro_conv = st.multiselect("Convenienza:", options=sorted(df["Convenienza"].unique()), default=sorted(df["Convenienza"].unique()))
    with col_f4:
        min_costo = st.slider("Costo Minimo:", 0, 100, 0)

    df_filtered = df[
        (df["Ruolo"].isin(filtro_ruolo)) & 
        (df["Squadra_Lunga"].isin(filtro_squadra)) &
        (df["Convenienza"].isin(filtro_conv)) &
        (df["Costo"] >= min_costo)
    ]

    st.dataframe(
        df_filtered[["Nome", "Squadra_Lunga", "Squadra", "Ruolo", "Costo", "Titolarita_%", "Spesa_Max_Consigliata_(cr)", "Convenienza", "Status"]].sort_values(by="Costo", ascending=False),
        use_container_width=True,
        hide_index=True,
        height=800
    )
    st.download_button("📥 Scarica CSV Completo", df_filtered.to_csv(index=False).encode('utf-8'), "fanta_completo_587.csv", "text/csv")
