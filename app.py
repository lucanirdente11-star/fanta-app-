import pandas as pd
import streamlit as st

st.set_page_config(page_title="FantaHub Pro - Database Serie A", page_icon="⚽️", layout="wide")

st.title("⚽️ FantaHub Pro - Guida Asta Serie A (1500 Crediti)")
st.caption("Database completo di tutte le squadre e giocatori con valutazioni, titolarità e spesa consigliata. Listone Ufficiale 26/27.")

# --- DATABASE GIOCATORI COMPLETO ---
@st.cache_data
def load_data():
    giocatori = [
        # === EXTRA (non nel listone ufficiale) ===
        {"Nome": "Kevin De Bruyne", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 110, "Status": "Super Top Assoluto / Assist", "Convenienza": "Altissima"},
        {"Nome": "Luka Modric", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 55, "Status": "Leggenda / Super Classe", "Convenienza": "Altissima"},
        {"Nome": "Jonathan David", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 90, "Status": "Super Top Bomber", "Convenienza": "Altissima"},

        # === ATALANTA ===
        {"Nome": "Carnesecchi", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 62, "Status": "Titolare", "Convenienza": "Alta"},
        {"Nome": "Rossi F.", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Sportiello", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Vismara", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Ahanor", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 23, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "Bakker", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 23, "Status": "Alternativa", "Convenienza": "Bassa"},
        {"Nome": "Bellanova", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 23, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Bernasconi", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 23, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Djimsiti", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 27, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Hien", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 30, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Kolasinac", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 19, "Status": "Titolare Esperto", "Convenienza": "Media"},
        {"Nome": "Kossounou", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 11, "Status": "Rinforzo Difesa", "Convenienza": "Bassa"},
        {"Nome": "Kristensen T.", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 27, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Scalvini", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 38, "Status": "Top Difesa / Giovane", "Convenienza": "Alta"},
        {"Nome": "Zappacosta", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 30, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Zalewski", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 23, "Status": "Jolly Fascia", "Convenienza": "Media"},
        {"Nome": "De Roon", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 15, "Status": "Titolare / Voto Fisso", "Convenienza": "Media"},
        {"Nome": "Ederson D.S.", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 46, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Gaetano", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 27, "Status": "Rotazione / Qualità", "Convenienza": "Media"},
        {"Nome": "Pasalic", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 34, "Status": "Incursore / Gol", "Convenienza": "Alta"},
        {"Nome": "Samardzic", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 46, "Status": "Qualità / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Sulemana I.", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 11, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Sulemana K.", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 23, "Status": "Scommessa Esterna", "Convenienza": "Media"},
        {"Nome": "De Ketelaere", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 65, "Status": "Top Slot / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Krstovic", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 68, "Status": "Rotazione Offensiva", "Convenienza": "Media"},
        {"Nome": "Raspadori", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 50, "Status": "Jolly / Bonus", "Convenienza": "Alta"},
        {"Nome": "Scamacca", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 72, "Status": "Bomber Titolare", "Convenienza": "Altissima"},

        # === BOLOGNA ===
        {"Nome": "Happonen", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Skorupski", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 38, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Pessina Mas.", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Alhassane", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Casale", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 11, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "De Silvestri", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 4, "Status": "Esperienza / Riserva", "Convenienza": "Bassa"},
        {"Nome": "Heggem", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 23, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Helland", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Holm", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 19, "Status": "Alternativa Fascia", "Convenienza": "Media"},
        {"Nome": "Lucumì", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 30, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Miranda J.", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 30, "Status": "Titolare Fascia", "Convenienza": "Alta"},
        {"Nome": "Vitik", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 19, "Status": "Rinforzo Difensivo", "Convenienza": "Media"},
        {"Nome": "Zortea", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 23, "Status": "Rotazione Fascia", "Convenienza": "Media"},
        {"Nome": "Amondarain", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 19, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Bernardeschi", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 34, "Status": "Esperienza / Qualità", "Convenienza": "Alta"},
        {"Nome": "El Azzouzi O.", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 8, "Status": "Riserva / Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ferguson", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 27, "Status": "Top / Incursore", "Convenienza": "Alta"},
        {"Nome": "Moro N.", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Odgaard", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 30, "Status": "Jolly Offensivo", "Convenienza": "Media"},
        {"Nome": "Pobega", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 23, "Status": "Incursore Fisico", "Convenienza": "Media"},
        {"Nome": "Rowe", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 42, "Status": "Esterno Offensivo", "Convenienza": "Alta"},
        {"Nome": "Cambiaghi", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 30, "Status": "Titolare / Dribbling", "Convenienza": "Alta"},
        {"Nome": "Castro S.", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 53, "Status": "Attaccante in Crescita", "Convenienza": "Alta"},
        {"Nome": "Dallinga", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 30, "Status": "Centravanti Titolare", "Convenienza": "Alta"},
        {"Nome": "Dominguez B.", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 11, "Status": "Scommessa Esterna", "Convenienza": "Bassa"},
        {"Nome": "Orsolini", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 99, "Status": "Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Piccoli", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 30, "Status": "Vice / Gol", "Convenienza": "Media"},

        # === CAGLIARI ===
        {"Nome": "Caprile", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 34, "Status": "Titolare", "Convenienza": "Alta"},
        {"Nome": "Ciocci", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Sherri", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Riserva", "Convenienza": "Molto Bassa"},
        {"Nome": "Raterink", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Idrissi R.", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 11, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Kofler", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 19, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Mina", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 30, "Status": "Titolare / Esperienza", "Convenienza": "Media"},
        {"Nome": "Obert", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 27, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Zè Pedro", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 19, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Zappa", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Titolare Fascia", "Convenienza": "Media"},
        {"Nome": "Aurelio", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Adopo", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 23, "Status": "Titolare / Quantità", "Convenienza": "Media"},
        {"Nome": "Akarakiri", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Deiola", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 11, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Liteta", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Prati", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 15, "Status": "Regista / Giovane", "Convenienza": "Media"},
        {"Nome": "Romano", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 19, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Winks", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 23, "Status": "Regista Titolare", "Convenienza": "Alta"},
        {"Nome": "Albarracin", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 1, "Status": "Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Borrelli", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 15, "Status": "Alternativa Attacco", "Convenienza": "Bassa"},
        {"Nome": "Esposito Se.", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 50, "Status": "Titolare / Qualità", "Convenienza": "Alta"},
        {"Nome": "Felici", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 19, "Status": "Scommessa Fascia", "Convenienza": "Bassa"},
        {"Nome": "Maldini", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 19, "Status": "Talento / Jolly", "Convenienza": "Media"},
        {"Nome": "Mutandwa", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 23, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Trepy", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Molto Bassa"},

        # === COMO ===
        {"Nome": "Audero", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Butez", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 62, "Status": "Titolare Porta", "Convenienza": "Altissima"},
        {"Nome": "Tornqvist", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Vigorito", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Cuenca A.", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 4, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Dosenna", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 30, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Goldaniga", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 1, "Status": "Titolare Esperto", "Convenienza": "Media"},
        {"Nome": "Kaiki", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 27, "Status": "Riserva", "Convenienza": "Molto Bassa"},
        {"Nome": "Kempf", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 19, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Smolcic I.", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Valle", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 23, "Status": "Terzino Spinta", "Convenienza": "Media"},
        {"Nome": "Van Der Brempt", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 8, "Status": "Titolare Fascia", "Convenienza": "Media"},
        {"Nome": "Couto", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 30, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Baturina", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 84, "Status": "Talento Puro / Trequartista", "Convenienza": "Altissima"},
        {"Nome": "Caqueret", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 23, "Status": "Regista di Spessore", "Convenienza": "Alta"},
        {"Nome": "Da Cunha", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 68, "Status": "Esterno Offensivo", "Convenienza": "Altissima"},
        {"Nome": "Liberali", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 23, "Status": "Giovane Talento", "Convenienza": "Bassa"},
        {"Nome": "Milla", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 19, "Status": "Regista di Classe", "Convenienza": "Alta"},
        {"Nome": "Paz N.", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 114, "Status": "Top Slot / Qualità", "Convenienza": "Altissima"},
        {"Nome": "Perrone", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 38, "Status": "Titolare / Visione", "Convenienza": "Media"},
        {"Nome": "Rodriguez Je.", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 35, "Quotazione": 46, "Status": "Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Addai", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 19, "Status": "Giovane Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Azon", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 1, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Diao", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 42, "Status": "Talento / Velocità", "Convenienza": "Alta"},
        {"Nome": "Douvikas", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 76, "Status": "Bomber Titolare", "Convenienza": "Altissima"},
        {"Nome": "Fadera", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 8, "Status": "Rotazione Attacco", "Convenienza": "Bassa"},
        {"Nome": "Kuhn", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 11, "Status": "Esterno Rapido", "Convenienza": "Bassa"},
        {"Nome": "Lahdo", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Morata", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 15, "Status": "Super Top / Stella Como", "Convenienza": "Media"},

        # === FIORENTINA ===
        {"Nome": "Christensen O.", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "De Gea", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 50, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Lezzerini", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Dodò", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 38, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Dragusin", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 30, "Status": "Muro Difensivo", "Convenienza": "Alta"},
        {"Nome": "Fortini", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 38, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Jimenez A.", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 30, "Status": "Giovane Fascia", "Convenienza": "Media"},
        {"Nome": "Joao Mario", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 11, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Parisi", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 19, "Status": "Alternativa Fascia", "Convenienza": "Media"},
        {"Nome": "Pongracic", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 15, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Ranieri L.", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 11, "Status": "Titolare Affidabile", "Convenienza": "Media"},
        {"Nome": "Viery", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 23, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Atta", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 65, "Status": "Rotazione Dinamica", "Convenienza": "Media"},
        {"Nome": "Brescianini", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 11, "Status": "Incursore da Gol", "Convenienza": "Media"},
        {"Nome": "Fabbian", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 15, "Status": "Incursore Pericoloso", "Convenienza": "Media"},
        {"Nome": "Fagioli", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 30, "Status": "Regista di Qualità", "Convenienza": "Alta"},
        {"Nome": "Gudmundsson A.", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 50, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Mandragora", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 34, "Status": "Tiro da Fuori / Piazzati", "Convenienza": "Media"},
        {"Nome": "Ndour", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 30, "Status": "Scommessa", "Convenienza": "Media"},
        {"Nome": "Oulai", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 23, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Valdepenas", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 23, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Braschi", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Kean", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 95, "Status": "Bomber Titolare", "Convenienza": "Altissima"},
        {"Nome": "Mastantuono", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 46, "Status": "Talento", "Convenienza": "Media"},
        {"Nome": "Pellegrino M.", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 57, "Status": "Attaccante di Movimento", "Convenienza": "Alta"},

        # === GENOA ===
        {"Nome": "Bijlow", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 30, "Status": "Portiere Top", "Convenienza": "Alta"},
        {"Nome": "Sommariva", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Stolz", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Calvani", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Marcandalli", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 23, "Status": "In Crescita", "Convenienza": "Media"},
        {"Nome": "Martin", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 19, "Status": "Titolare", "Convenienza": "Media"},
        {"Nome": "Matturro", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 1, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Mitaj", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 15, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Norton-Cuffy", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 30, "Status": "Spinta e Fisico", "Convenienza": "Alta"},
        {"Nome": "Ostigard", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 42, "Status": "Titolare / Goleador", "Convenienza": "Alta"},
        {"Nome": "Otoa", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Puczka", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Sabelli", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 8, "Status": "Affidabile / Titolare", "Convenienza": "Media"},
        {"Nome": "Vasquez", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 34, "Status": "Leader Difensivo", "Convenienza": "Alta"},
        {"Nome": "Vogliacco", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 1, "Status": "Titolare / Rotazione", "Convenienza": "Media"},
        {"Nome": "Amorim", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Ellertsson", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 23, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Frendrup", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 27, "Status": "Recupera-palloni / Voto Top", "Convenienza": "Alta"},
        {"Nome": "Masini", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Meichtry", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 19, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Messias", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 11, "Status": "Qualità / Bonus", "Convenienza": "Media"},
        {"Nome": "Sow", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 27, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Traorè Hj.", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 19, "Status": "Top Slot / Trequartista", "Convenienza": "Alta"},
        {"Nome": "Venturino", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Vitinha O.", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 30, "Status": "Titolare / Attacco", "Convenienza": "Alta"},
        {"Nome": "Colombo", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 42, "Status": "Titolare / Bomber", "Convenienza": "Alta"},
        {"Nome": "Havel", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Molto Bassa"},

        # *** CONTINUA NELLA PARTE 2 DI 3 ***
        # *** NON CHIUDERE LA LISTA QUI ***        # === INTER ===
        {"Nome": "Di Gennaro", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Martinez Jo.", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 65, "Status": "Titolare", "Convenienza": "Altissima"},
        {"Nome": "Provedel", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 8, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Akanji", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 62, "Status": "Top Difesa", "Convenienza": "Altissima"},
        {"Nome": "Bastoni", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 53, "Status": "Top Difesa", "Convenienza": "Altissima"},
        {"Nome": "Bisseck", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 42, "Status": "In Crescita", "Convenienza": "Media"},
        {"Nome": "Carlos Augusto", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 27, "Status": "Jolly di Qualità", "Convenienza": "Alta"},
        {"Nome": "Dimarco", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 122, "Status": "Super Top Difesa / Assist", "Convenienza": "Altissima"},
        {"Nome": "Luis Henrique", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 15, "Status": "Esterno Spinta", "Convenienza": "Media"},
        {"Nome": "Pavard", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 23, "Status": "Titolare Top", "Convenienza": "Alta"},
        {"Nome": "Stones", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 46, "Status": "Rinforzo", "Convenienza": "Alta"},
        {"Nome": "Asllani", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 19, "Status": "Vice Regia", "Convenienza": "Bassa"},
        {"Nome": "Barella", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 65, "Status": "Top Centrocampo", "Convenienza": "Altissima"},
        {"Nome": "Calhanoglu", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 103, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Diouf", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 30, "Status": "Dinamismo", "Convenienza": "Media"},
        {"Nome": "Frattesi", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 27, "Status": "Incursore Spietato da Gol", "Convenienza": "Alta"},
        {"Nome": "Mkhitaryan", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 19, "Status": "Titolare / Quantità e Qualità", "Convenienza": "Alta"},
        {"Nome": "Stankovic A.", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Sucic P.", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 30, "Status": "Interessante Novità", "Convenienza": "Media"},
        {"Nome": "Zielinski", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 38, "Status": "Qualità / Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Akinsanmiro", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 23, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Bonny", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 27, "Status": "Rinforzo Attacco", "Convenienza": "Media"},
        {"Nome": "Esposito F.P.", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 62, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "Martinez L.", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 95, "Quotazione": 133, "Status": "📌 TOP RE ASSOLUTO ASTA", "Convenienza": "Altissima"},
        {"Nome": "Thuram", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 110, "Status": "Super Top Attacco", "Convenienza": "Altissima"},

        # === JUVENTUS ===
        {"Nome": "Di Gregorio", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 34, "Status": "Top Portiere", "Convenienza": "Alta"},
        {"Nome": "Perin", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 23, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Pinsoglio", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Bremer", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 57, "Status": "Muro Inamovibile", "Convenienza": "Altissima"},
        {"Nome": "Cabal", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 4, "Status": "Rotazione Difesa", "Convenienza": "Bassa"},
        {"Nome": "Cambiaso", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 34, "Status": "Titolare / Assist", "Convenienza": "Altissima"},
        {"Nome": "Celik", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 30, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Gatti", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Titolare / Gol di Testa", "Convenienza": "Alta"},
        {"Nome": "Kalulu", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 50, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Kelly L.", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 19, "Status": "Rinforzo Solido", "Convenienza": "Alta"},
        {"Nome": "Rugani", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 35, "Quotazione": 1, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Adzic", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 19, "Status": "Talento / Scommessa", "Convenienza": "Media"},
        {"Nome": "Douglas Luiz", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 15, "Status": "Top Centrocampo / Piazzati", "Convenienza": "Media"},
        {"Nome": "Koopmeiners", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 19, "Status": "Super Top / Rigorista", "Convenienza": "Alta"},
        {"Nome": "Locatelli", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 30, "Status": "Regista Titolare", "Convenienza": "Alta"},
        {"Nome": "McKennie", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 65, "Status": "Jolly / Inserimenti", "Convenienza": "Altissima"},
        {"Nome": "Miretti", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 11, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Thuram K.", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 38, "Status": "Top / Fisicità e Dribbling", "Convenienza": "Altissima"},
        {"Nome": "Alajbegovic", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 46, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "Boga", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 23, "Status": "Dribbling e Bonus", "Convenienza": "Media"},
        {"Nome": "Conceicao", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 46, "Status": "Spaccapartite / Bonus", "Convenienza": "Altissima"},
        {"Nome": "David J.", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 90, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Ekhator", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 25, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Kolo Muani", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 99, "Status": "Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Yildiz", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 87, "Status": "Talento Puro / Scommessa Top", "Convenienza": "Altissima"},
        {"Nome": "Zhegrova", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 23, "Status": "Esterno Fantasia", "Convenienza": "Media"},

        # === LAZIO ===
        {"Nome": "Mandas", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 34, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Motta", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Renzetti", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Doekhi", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 27, "Status": "Titolare / Goleador di Testa", "Convenienza": "Alta"},
        {"Nome": "Lazzari", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 8, "Status": "Spinta sulla Fascia", "Convenienza": "Media"},
        {"Nome": "Marusic", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 23, "Status": "Titolare Multi-ruolo", "Convenienza": "Alta"},
        {"Nome": "Patric", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 15, "Status": "Rotazione Centrali", "Convenienza": "Media"},
        {"Nome": "Pedraza", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 19, "Status": "Spinta a Sinistra", "Convenienza": "Alta"},
        {"Nome": "Provstgaard", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 11, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Romagnoli", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 27, "Status": "Leader Difensivo", "Convenienza": "Alta"},
        {"Nome": "Tavares N.", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 23, "Status": "Treno sulla Fascia / Assist", "Convenienza": "Alta"},
        {"Nome": "Belahyane", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 1, "Status": "Quantità e Titolare", "Convenienza": "Media"},
        {"Nome": "Cataldi", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 15, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Dele-Bashiru", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 19, "Status": "Incursore Fisico", "Convenienza": "Media"},
        {"Nome": "Floriani Mussolini", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Isaksen", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 34, "Status": "Spunto / Ala", "Convenienza": "Media"},
        {"Nome": "Pellegrini Lu.", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Przyborek", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Rovella", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 23, "Status": "Regista Titolare", "Convenienza": "Alta"},
        {"Nome": "Taylor K.", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 50, "Status": "Qualità e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Cancellieri", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 34, "Status": "Jolly d'Attacco", "Convenienza": "Media"},
        {"Nome": "Dia", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 38, "Status": "Top Slot / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Noslin", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 23, "Status": "Velocità e Gol", "Convenienza": "Alta"},
        {"Nome": "Ratkov", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 38, "Status": "Centravanti / Gol", "Convenienza": "Media"},
        {"Nome": "Zaccagni", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 62, "Status": "Top Slot / Rigorista", "Convenienza": "Altissima"},

        # === LECCE ===
        {"Nome": "Falcone", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 30, "Status": "Saracinesca Titolare", "Convenienza": "Alta"},
        {"Nome": "Fruchtl", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Samooja", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Penev", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Gallo", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 23, "Status": "Titolare / Assist", "Convenienza": "Alta"},
        {"Nome": "Gaspar K.", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 19, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Jean", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ndaba", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 1, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Siebert", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 15, "Status": "Titolare / Roccia", "Convenienza": "Media"},
        {"Nome": "Tiago Gabriel", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 27, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Veiga D.", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 19, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Berisha M.", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 19, "Status": "In Crescita", "Convenienza": "Media"},
        {"Nome": "Coulibaly L.", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 23, "Status": "Titolare / Quantità", "Convenienza": "Alta"},
        {"Nome": "Fofana Sa.", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Gandelman", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 19, "Status": "Inserimenti / Gol", "Convenienza": "Media"},
        {"Nome": "Geubbels", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 34, "Status": "Talento", "Convenienza": "Media"},
        {"Nome": "Gorter", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Kaba", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 1, "Status": "In Recupero", "Convenienza": "Media"},
        {"Nome": "Maleh", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ngom", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "N'Dri", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 11, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Pierotti", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 23, "Status": "Lotta / Sponda", "Convenienza": "Media"},
        {"Nome": "Stulic", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 27, "Status": "Centravanti", "Convenienza": "Media"},
        {"Nome": "Banda", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 122, "Status": "Velocità / Dribbling", "Convenienza": "Altissima"},

        # === MILAN ===
        {"Nome": "Maignan", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 57, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Terracciano", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Torriani", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Athekame", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 11, "Status": "Riserva Fascia", "Convenienza": "Bassa"},
        {"Nome": "Bartesaghi", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 35, "Quotazione": 30, "Status": "Giovane / Riserva", "Convenienza": "Bassa"},
        {"Nome": "De Winter", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 11, "Status": "Rotazione Difesa", "Convenienza": "Media"},
        {"Nome": "Estupinan", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 11, "Status": "Titolare / Assist a Sinistra", "Convenienza": "Media"},
        {"Nome": "Gabbia", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 27, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Gila", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 46, "Status": "Rinforzo Difensivo", "Convenienza": "Alta"},
        {"Nome": "Pavlovic", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 53, "Status": "Titolare / Grinta", "Convenienza": "Alta"},
        {"Nome": "Tomori", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 27, "Status": "Titolare Top", "Convenienza": "Alta"},
        {"Nome": "Bennacer", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 38, "Status": "Regista", "Convenienza": "Media"},
        {"Nome": "Chukwueze", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 23, "Status": "Spunto da Panchina", "Convenienza": "Media"},
        {"Nome": "Diawara S.", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Fofana Y.", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 19, "Status": "Diga Titolare / Voto Alto", "Convenienza": "Alta"},
        {"Nome": "Jashari", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 15, "Status": "Regia e Sostanza", "Convenienza": "Media"},
        {"Nome": "Loftus-Cheek", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 15, "Status": "Incursore / Fisico", "Convenienza": "Media"},
        {"Nome": "Musah", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ricci S.", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 15, "Status": "Regista Affidabile", "Convenienza": "Alta"},
        {"Nome": "Rabiot", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 84, "Status": "Top Centrocampo / Gol", "Convenienza": "Altissima"},
        {"Nome": "Saelemaekers", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 38, "Status": "Jolly Tattico", "Convenienza": "Alta"},
        {"Nome": "Camarda", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 19, "Status": "Talento Puro / Scommessa", "Convenienza": "Media"},
        {"Nome": "Gimenez", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 23, "Status": "Super Top Bomber", "Convenienza": "Alta"},
        {"Nome": "Leao", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 68, "Status": "Super Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Modric", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 55, "Status": "Leggenda / Super Classe", "Convenienza": "Altissima"},
        {"Nome": "Nkunku", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 50, "Status": "Super Top / Fantasia e Gol", "Convenienza": "Altissima"},
        {"Nome": "Pulisic", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 95, "Status": "Super Top Centrocampo / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Ramos G.", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 103, "Status": "Top Attacco / Bomber", "Convenienza": "Altissima"},

        # === NAPOLI ===
        {"Nome": "Contini", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Meret", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 42, "Status": "Titolare Portiere", "Convenienza": "Alta"},
        {"Nome": "Milinkovic-Savic V.", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 19, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Beukema", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 23, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Buongiorno", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 27, "Status": "Muro Difensivo / Top Slot", "Convenienza": "Alta"},
        {"Nome": "Di Lorenzo", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 46, "Status": "Top Difesa / Capitano", "Convenienza": "Altissima"},
        {"Nome": "Gutierrez", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 30, "Status": "Spinta e Assist a Sinistra", "Convenienza": "Alta"},
        {"Nome": "Marin R.", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 8, "Status": "Rotazione Difesa", "Convenienza": "Bassa"},
        {"Nome": "Marianucci", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Olivera", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 19, "Status": "Titolare Fascia", "Convenienza": "Alta"},
        {"Nome": "Rrahmani", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 53, "Status": "Titolare Centrali", "Convenienza": "Alta"},
        {"Nome": "Spinazzola", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 30, "Status": "Rotazione / Spinta", "Convenienza": "Media"},
        {"Nome": "Anguissa", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 42, "Status": "Titolare / Fisico", "Convenienza": "Alta"},
        {"Nome": "De Bruyne", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 110, "Status": "Super Top Assoluto / Assist", "Convenienza": "Altissima"},
        {"Nome": "Folorunsho", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 15, "Status": "Incursore Potente", "Convenienza": "Media"},
        {"Nome": "Gilmour", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 11, "Status": "Regia e Geometrie", "Convenienza": "Media"},
        {"Nome": "Giovane", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Lang", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 11, "Status": "Esterno Top / Dribbling e Gol", "Convenienza": "Media"},
        {"Nome": "Lobotka", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 27, "Status": "Metronomo / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "McTominay", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 106, "Status": "Top Centrocampo / Inserimenti Top", "Convenienza": "Altissima"},
        {"Nome": "Santos A.", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 53, "Status": "Giovane", "Convenienza": "Media"},
        {"Nome": "Vergara", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 30, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Cheddira", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 72, "Status": "Attaccante / Gol", "Convenienza": "Alta"},
        {"Nome": "Hojlund", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 106, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Lucca", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 11, "Status": "Centravanti / Torre", "Convenienza": "Media"},
        {"Nome": "Lukaku", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 38, "Status": "Super Top Bomber", "Convenienza": "Alta"},
        {"Nome": "Neres", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 23, "Status": "Top Slot / Assist e Gol", "Convenienza": "Alta"},
        {"Nome": "Politano", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 38, "Status": "Titolare / Rigori / Bonus", "Convenienza": "Alta"},

        # *** CONTINUA NELLA PARTE 3 DI 3 (ULTIMA PARTE) ***
        # *** NON CHIUDERE ANCORA LA LISTA ***        # === PARMA ===
        {"Nome": "Corvi", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Daffara", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 27, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Suzuki", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 27, "Status": "Portiere Titolare Reattivo", "Convenienza": "Alta"},
        {"Nome": "Carboni F.", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 1, "Status": "Rotazione Fascia", "Convenienza": "Bassa"},
        {"Nome": "Circati", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 23, "Status": "Giovane Centrale Titolare", "Convenienza": "Alta"},
        {"Nome": "Delprato", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 30, "Status": "Capitano / Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Ndiaye", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 1, "Status": "Rinforzo Difensivo", "Convenienza": "Media"},
        {"Nome": "Troilo", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Valenti", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 15, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Valeri", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 30, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Bernabè", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 27, "Status": "🔥 Talento Top / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Britschgi", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Cremaschi", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 1, "Status": "Talento / Inserimenti", "Convenienza": "Media"},
        {"Nome": "Diallo O.", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 11, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Elphege", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Keita M.", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 19, "Status": "Diga di Centrocampo", "Convenienza": "Alta"},
        {"Nome": "Nicolussi Caviglia", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 23, "Status": "Regia e Tiro dalla Distanza", "Convenienza": "Alta"},
        {"Nome": "Ordonez C.", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 8, "Status": "Interessante Novità", "Convenienza": "Media"},
        {"Nome": "Sorensen O.", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 11, "Status": "Quantità e Inserimenti", "Convenienza": "Media"},
        {"Nome": "Tourè E.", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 42, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Almqvist", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 15, "Status": "Velocità e Assist", "Convenienza": "Media"},
        {"Nome": "Frigan", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 19, "Status": "Attaccante / Gol", "Convenienza": "Media"},
        {"Nome": "Ondrejka", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 19, "Status": "Esterno Offensivo", "Convenienza": "Media"},
        {"Nome": "Pellegrino M.", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 57, "Status": "Attaccante di Movimento", "Convenienza": "Alta"},

        # === ROMA ===
        {"Nome": "Gollini", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Svilar", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 68, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Vasquez", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Zelezny", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Angelino", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 11, "Status": "Titolare / Assist a Sinistra", "Convenienza": "Media"},
        {"Nome": "De Marzi", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Ghilardi", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 15, "Status": "Giovane / Rotazione", "Convenienza": "Media"},
        {"Nome": "Hermoso", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 38, "Status": "Titolare / Impostazione", "Convenienza": "Alta"},
        {"Nome": "Koulierakis", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 30, "Status": "Rinforzo", "Convenienza": "Media"},
        {"Nome": "Mancini", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 57, "Status": "Titolare / Bonus Testa", "Convenienza": "Altissima"},
        {"Nome": "N'Dicka", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 50, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Rensch", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 19, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Wesley", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 65, "Status": "Terzino di Spinta", "Convenienza": "Altissima"},
        {"Nome": "Ziolkowski", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Cristante", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 30, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "El Aynaoui", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 15, "Status": "Dinamismo e Interdizione", "Convenienza": "Media"},
        {"Nome": "Konè M.", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 38, "Status": "Top Centrocampo / Fisico", "Convenienza": "Altissima"},
        {"Nome": "Pellegrini Lo.", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 38, "Status": "Top Slot / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Pisilli", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 19, "Status": "Inserimenti / Gol Pesanti", "Convenienza": "Alta"},
        {"Nome": "Arena", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 11, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Castro S.", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 53, "Status": "Attaccante in Crescita", "Convenienza": "Alta"},
        {"Nome": "Dovbyk", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 62, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Dybala", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 53, "Status": "Super Top / Classe Purissima", "Convenienza": "Altissima"},
        {"Nome": "Malen", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 129, "Status": "Top Slot / Velocità e Gol", "Convenienza": "Altissima"},
        {"Nome": "Molina N.", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 68, "Status": "Esterno", "Convenienza": "Alta"},
        {"Nome": "Soulè", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 46, "Status": "Top Attacco / Fantasia", "Convenienza": "Altissima"},
        {"Nome": "Vaz", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},

        # === TORINO ===
        {"Nome": "Israel", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 1, "Status": "Portiere Titolare", "Convenienza": "Media"},
        {"Nome": "Mascardi", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Paleari", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Siviero", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Biraghi", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 8, "Status": "Piazzati e Assist", "Convenienza": "Media"},
        {"Nome": "Coco", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 27, "Status": "Titolare / Gol dalla Distanza", "Convenienza": "Alta"},
        {"Nome": "Comert", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Comuzzo", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 23, "Status": "Titolare Difesa Solida", "Convenienza": "Alta"},
        {"Nome": "Ismajli", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 27, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Pedersen", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 19, "Status": "Spinta sulla Fascia", "Convenienza": "Alta"},
        {"Nome": "Anjorin", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 1, "Status": "Qualità in Mezzo", "Convenienza": "Media"},
        {"Nome": "Casadei", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 38, "Status": "Inserimenti Pericolosi / Gol", "Convenienza": "Altissima"},
        {"Nome": "Fitz-Jim", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Gineitis", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 19, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "Ilkhan", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 15, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Ilic", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 1, "Status": "Titolare / Tiro da Fuori", "Convenienza": "Media"},
        {"Nome": "Oristanio", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 27, "Status": "Fantasia / Trequartista", "Convenienza": "Alta"},
        {"Nome": "Aboukhlal", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 11, "Status": "Velocità e Bonus", "Convenienza": "Media"},
        {"Nome": "Adams C.", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 34, "Status": "Titolare / Gol e Lavoro Sporco", "Convenienza": "Alta"},
        {"Nome": "Kulenovic", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 15, "Status": "Alternativa in Attacco", "Convenienza": "Bassa"},
        {"Nome": "Njie", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 11, "Status": "Giovane Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Simeone", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 57, "Status": "Bomber / Titolare", "Convenienza": "Alta"},
        {"Nome": "Vlasic", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 53, "Status": "Trequartista Titolare", "Convenienza": "Alta"},
        {"Nome": "Zapata D.", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 27, "Status": "Panzer / Bomber Titolare", "Convenienza": "Alta"},

        # === UDINESE ===
        {"Nome": "Okoye", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 34, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Padelli", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Piana", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Abankwah", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Bertola", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 15, "Status": "Giovane Centrale", "Convenienza": "Media"},
        {"Nome": "Camara A.", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Ebosse", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Goglichidze", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 34, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Kabasele", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 15, "Status": "Esperienza", "Convenienza": "Bassa"},
        {"Nome": "Kamara H.", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 23, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Kristensen T.", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 27, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Palma", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Solet", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 50, "Status": "Top Difesa / Fisicità", "Convenienza": "Altissima"},
        {"Nome": "Vojvoda", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 30, "Status": "Rotazione / Affidabile", "Convenienza": "Media"},
        {"Nome": "Zanoli", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 15, "Status": "Spinta Fascia", "Convenienza": "Media"},
        {"Nome": "Arizala", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Chakvetadze", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 8, "Status": "Dribbling e Assist", "Convenienza": "Media"},
        {"Nome": "Ekkelenkamp", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 38, "Status": "Inserimenti / Gol", "Convenienza": "Alta"},
        {"Nome": "Gueye", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Karlstrom", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 23, "Status": "Diga / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Miller L.", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 11, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Piotrowski", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 19, "Status": "Inserimenti e Gol", "Convenienza": "Alta"},
        {"Nome": "Unai Gomez", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 27, "Status": "Qualità in Mezzo", "Convenienza": "Media"},
        {"Nome": "Zarraga", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Bayo V.", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 1, "Status": "Rotazione Attacco", "Convenienza": "Media"},
        {"Nome": "Buksa", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 8, "Status": "Centravanti / Gol di Testa", "Convenienza": "Media"},
        {"Nome": "Davis K.", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 72, "Status": "Lavoro Sporco / Titolare", "Convenienza": "Altissima"},
        {"Nome": "Zaniolo", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 68, "Status": "Top Slot / Scommessa di Classe", "Convenienza": "Altissima"},

        # === VENEZIA ===
        {"Nome": "Grandi", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 1, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Pozzi", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Stankovic F.", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 23, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Gomes", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Bella-Kotchap", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 23, "Status": "Muro Difensivo", "Convenienza": "Alta"},
        {"Nome": "Correia T.", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Terzino Spinta", "Convenienza": "Alta"},
        {"Nome": "Franjic", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Halhal", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 15, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Haps", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 19, "Status": "Spinta a Sinistra", "Convenienza": "Media"},
        {"Nome": "Moreno M.", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 19, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Rrahmani Al.", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 30, "Status": "Bomber Titolare", "Convenienza": "Alta"},
        {"Nome": "Sagrado", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 15, "Status": "Rotazione Fascia", "Convenienza": "Bassa"},
        {"Nome": "Schingtienne", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 11, "Status": "Difensore Centrale", "Convenienza": "Media"},
        {"Nome": "Sverko", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 11, "Status": "Titolare / Rotazione", "Convenienza": "Media"},
        {"Nome": "Basic", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 23, "Status": "Qualità e Tiro", "Convenienza": "Alta"},
        {"Nome": "Bjarkason", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 1, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Bohinen", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 23, "Status": "Regia", "Convenienza": "Media"},
        {"Nome": "Busio", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 19, "Status": "Inserimenti / Incursore", "Convenienza": "Alta"},
        {"Nome": "Dagasso", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Duncan", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 8, "Status": "Quantità ed Esperienza", "Convenienza": "Media"},
        {"Nome": "Hainaut", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 11, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Helgason", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 11, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Lauberbach", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 1, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Lisman", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Perez K.", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 19, "Status": "Quantità e Qualità", "Convenienza": "Media"},
        {"Nome": "Sohm", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 19, "Status": "Rotazione Fisica", "Convenienza": "Media"},
        {"Nome": "Adams A.", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 46, "Status": "Bomber Titolare / Potenza", "Convenienza": "Alta"},
        {"Nome": "Adorante", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 19, "Status": "Riserva / Gol", "Convenienza": "Bassa"},
        {"Nome": "Yeboah J.", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 30, "Status": "Esterno Offensivo / Dribbling", "Convenienza": "Alta"},
    ]
    return pd.DataFrame(giocatori)

df = load_data()

# --- SIDEBAR CONFIGURAZIONE BUDGET (1500 CREDITI) ---
st.sidebar.header("⚙️ Budget & Gestione Asta")
budget_totale = st.sidebar.number_input("Budget Iniziale (Crediti)", min_value=100, max_value=3000, value=1500)

st.sidebar.subheader("% Spesa Consigliata")
perc_p = st.sidebar.slider("Porta (%)", 1, 10, 4)
perc_d = st.sidebar.slider("Difesa (%)", 5, 20, 10)
perc_c = st.sidebar.slider("Centrocampo (%)", 10, 40, 26)
perc_a = st.sidebar.slider("Attacco (%)", 30, 80, 60)

# Budget per ruolo
b_p = (budget_totale * perc_p) / 100
b_d = (budget_totale * perc_d) / 100
b_c = (budget_totale * perc_c) / 100
b_a = (budget_totale * perc_a) / 100

# Funzione Calcolo Spesa Max Consigliata
def calcola_spesa_max(row):
    ruolo = row["Ruolo"]
    quot = row["Quotazione"]
    
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
tab1, tab2 = st.tabs(["🔍 Cerca Giocatore & Scheda Asta", "📋 Listone Completo Serie A"])

# --- TAB 1: SEARCH BAR E SCHEDA ---
with tab1:
    st.subheader("🔎 Cerca un Giocatore nel Database")
    
    search_input = st.text_input("✍️ Scrivi il nome del giocatore (es. Lautaro, De Bruyne, Berardi):", "")
    
    if search_input:
        filtered_names = df[df["Nome"].str.contains(search_input, case=False, na=False)]["Nome"].tolist()
    else:
        filtered_names = sorted(df["Nome"].tolist())

    if filtered_names:
        selected_player = st.selectbox("Seleziona il calciatore trovato:", filtered_names)
        
        player = df[df["Nome"] == selected_player].iloc[0]

        st.markdown(f"## 👤 {player['Nome']} ({player['Squadra']})")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Ruolo", player["Ruolo"])
        col2.metric("Titolarità Esperta", f"{player['Titolarita_%']}%")
        col3.metric("SPESA MAX CONSIGLIATA", f"{player['Spesa_Max_Consigliata_(cr)']} cr")
        col4.metric("Convenienza Asta", player["Convenienza"])

        st.divider()
        st.markdown(f"""
        * **Status & Consigli:** {player['Status']}
        * **Quotazione di Riferimento:** {player['Quotazione']} crediti
        * **Budget Ruolo Disponibile:** {int(b_p if player['Ruolo']=='Portiere' else b_d if player['Ruolo']=='Difensore' else b_c if player['Ruolo']=='Centrocampista' else b_a)} cr
        """)
    else:
        st.warning("⚠️ Nessun giocatore trovato con questo nome. Prova a digitare diversamente!")

# --- TAB 2: LISTONE COMPLETO ---
with tab2:
    st.subheader(f"📋 Database Completo Serie A ({len(df)} Giocatori)")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        filtro_ruolo = st.multiselect("Filtra per Ruolo:", options=df["Ruolo"].unique(), default=df["Ruolo"].unique())
    with col_f2:
        filtro_squadra = st.multiselect("Filtra per Squadra:", options=sorted(df["Squadra"].unique()), default=sorted(df["Squadra"].unique()))
    with col_f3:
        filtro_conv = st.multiselect("Filtra per Convenienza:", options=df["Convenienza"].unique(), default=df["Convenienza"].unique())

    df_filtered = df[
        (df["Ruolo"].isin(filtro_ruolo)) & 
        (df["Squadra"].isin(filtro_squadra)) &
        (df["Convenienza"].isin(filtro_conv))
    ]

    st.dataframe(
        df_filtered[["Nome", "Squadra", "Ruolo", "Titolarita_%", "Spesa_Max_Consigliata_(cr)", "Convenienza", "Status"]],
        use_container_width=True,
        hide_index=True
    )
