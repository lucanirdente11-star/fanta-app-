import streamlit as st
import pandas as pd
import feedparser

# Impostazione pagina
st.set_page_config(page_title="FantaHub Pro - Guida Asta & News", page_icon="⚽", layout="wide")

st.title("⚽ FantaHub Pro: Asta, Giocatori & News")
st.caption("Il tuo assistente completo: database, percentuali di titolarità, calcoli asta e notizie in tempo reale.")

# --- DATABASE ESTESO GIOCATORI ---
@st.cache_data
def load_data():
    giocatori = [
        # PORTIERI
        {"Nome": "Sommer", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 95, "Status": "Titolare inamovibile", "Rigorista": "No", "Convenienza": 9.0, "Quotazione": 18, "Note": "Porta top, ottima difesa."},
        {"Nome": "Maignan", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 90, "Status": "Titolare", "Rigorista": "No", "Convenienza": 8.5, "Quotazione": 16, "Note": "Para-rigori, qualche infortunio di troppo."},
        {"Nome": "Di Gregorio", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 85, "Status": "Titolare", "Rigorista": "No", "Convenienza": 8.0, "Quotazione": 15, "Note": "Ottimo rendimento e modificatore."},
        {"Nome": "Svilar", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 90, "Status": "Titolare", "Rigorista": "No", "Convenienza": 8.2, "Quotazione": 14, "Note": "Crescita esponenziale, ottimi voti."},
        
        # DIFENSORI
        {"Nome": "Dimarco", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Status": "Titolare (Turnover calci piazzati)", "Rigorista": "No", "Convenienza": 9.5, "Quotazione": 22, "Note": "Bonus da centrocampista top."},
        {"Nome": "Theo Hernandez", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 90, "Status": "Titolare fisso", "Rigorista": "Vice", "Convenienza": 9.0, "Quotazione": 20, "Note": "Garantisce gol, assist ma anche qualche malus."},
        {"Nome": "Bremer", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 95, "Status": "Titolare inamovibile", "Rigorista": "No", "Convenienza": 8.8, "Quotazione": 17, "Note": "Pilastro da modificatore di difesa."},
        {"Nome": "Buongiorno", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 90, "Status": "Titolare", "Rigorista": "No", "Convenienza": 8.5, "Quotazione": 16, "Note": "Ottimo sia sui piazzati che nei voti."},

        # CENTROCAMPISTI
        {"Nome": "Pulisic", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Status": "Titolare / Rigorista", "Rigorista": "Sì", "Convenienza": 9.6, "Quotazione": 28, "Note": "Tra i migliori centrocampisti del listone."},
        {"Nome": "Calhanoglu", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Status": "Titolare / Rigorista principale", "Rigorista": "Sì", "Convenienza": 9.4, "Quotazione": 26, "Note": "Cecchino dagli undici metri."},
        {"Nome": "Zaccagni", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Status": "Capitano e Titolare", "Rigorista": "Sì", "Convenienza": 8.9, "Quotazione": 24, "Note": "Leader tecnico e d'attacco."},
        {"Nome": "Koopmeiners", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Status": "Titolare", "Rigorista": "Vice", "Convenienza": 8.7, "Quotazione": 25, "Note": "Inserimenti e tiri da fuori."},

        # ATTACCANTI
        {"Nome": "Lautaro Martinez", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 90, "Status": "Top Slot / Rigorista", "Rigorista": "Sì", "Convenienza": 9.8, "Quotazione": 42, "Note": "Super top d'attacco, puntare forte."},
        {"Nome": "Vlahovic", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 90, "Status": "Titolare / Rigorista", "Rigorista": "Sì", "Convenienza": 9.1, "Quotazione": 38, "Note": "Punto di riferimento offensivo."},
        {"Nome": "Retegui", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 80, "Status": "Titolare con concorrenza", "Rigorista": "Sì", "Convenienza": 8.8, "Quotazione": 32, "Note": "Macchina da bonus nel gioco di Gasperini."},
        {"Nome": "Thuram", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 85, "Status": "Titolare", "Rigorista": "No", "Convenienza": 9.0, "Quotazione": 35, "Note": "Assist e gol a raffica."}
    ]
    return pd.DataFrame(giocatori)

df = load_data()

# --- TAB DEDICATI ---
tab1, tab2, tab3 = st.tabs(["🔍 Cerca Giocatore & Calcolo Asta", "📊 Listone & Filtri", "📰 Calciomercato & News Live"])

# --- TAB 1: RICERCA & CALCOLO ASTA ---
with tab1:
    st.sidebar.header("⚙️ Impostazioni Tua Lega")
    budget_totale = st.sidebar.number_input("Budget Iniziale (Crediti)", min_value=100, max_value=1000, value=500)
    
    st.sidebar.subheader("% Spesa Consigliata")
    perc_p = st.sidebar.slider("Porta (%)", 1, 10, 4)
    perc_d = st.sidebar.slider("Difesa (%)", 5, 20, 10)
    perc_c = st.sidebar.slider("Centrocampo (%)", 10, 40, 26)
    perc_a = st.sidebar.slider("Attacco (%)", 30, 80, 60)

    # Calcoli budget per reparto
    b_p = (budget_totale * perc_p) / 100
    b_d = (budget_totale * perc_d) / 100
    b_c = (budget_totale * perc_c) / 100
    b_a = (budget_totale * perc_a) / 100

    st.subheader("🔎 Trova Scheda Giocatore")
    
    search_query = st.selectbox("Seleziona o cerca un giocatore:", ["-- Scegli un giocatore --"] + df["Nome"].tolist())

    if search_query != "-- Scegli un giocatore --":
        player = df[df["Nome"] == search_query].iloc[0]

        ruolo = player["Ruolo"]
        if ruolo == "Portiere":
            max_spesa = b_p * 0.7
        elif ruolo == "Difensore":
            max_spesa = b_d * 0.4
        elif ruolo == "Centrocampista":
            max_spesa = b_c * 0.45
        else:
            max_spesa = b_a * 0.55

        st.markdown(f"## 👤 {player['Nome']} ({player['Squadra']})")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Ruolo", player["Ruolo"])
        col2.metric("Titolarità stimata", f"{player['Titolarita_%']}%")
        col3.metric("Indice Convenienza", f"{player['Convenienza']}/10")
        col4.metric("PREZZO MAX CONSIGLIATO", f"{int(max_spesa)} cr")

        st.divider()

        st.markdown(f"""
        * **Status Titolare:** {player['Status']}
        * **Rigorista:** {player['Rigorista']}
        * **Quotazione Base:** {player['Quotazione']} crediti
        * **Analisi Tattica:** {player['Note']}
        """)

        if int(max_spesa) > 0:
            st.info(f"💡 **Consiglio Asta:** Non superare mai la soglia dei **{int(max_spesa)} crediti** per questo giocatore.")

# --- TAB 2: LISTONE COMPLETO & FILTRI ---
with tab2:
    st.subheader("📋 Database & Filtri Avanzati")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        filtro_ruolo = st.multiselect("Filtra per Ruolo:", options=df["Ruolo"].unique(), default=df["Ruolo"].unique())
    with col_f2:
        filtro_squadra = st.multiselect("Filtra per Squadra:", options=df["Squadra"].unique(), default=df["Squadra"].unique())

    df_filtered = df[(df["Ruolo"].isin(filtro_ruolo)) & (df["Squadra"].isin(filtro_squadra))]
    st.dataframe(df_filtered, use_container_width=True)

# --- TAB 3: CALCIOMERCATO E NEWS LIVE ---
with tab3:
    st.subheader("📰 Ultime Notizie Serie A & Calciomercato Live")
    
    rss_url = "https://www.gazzetta.it/rss/Calcio.xml"
    
    try:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:8]:
            with st.expander(f"📌 {entry.title}"):
                st.write(entry.summary if 'summary' in entry else "Leggi la notizia sul sito.")
                st.markdown(f"[Leggi la notizia completa]({entry.link})")
    except Exception as e:
        st.warning("Impossibile caricare il feed notizie al momento.")
