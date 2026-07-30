import streamlit as st
import pandas as pd

st.set_page_config(page_title="FantaHub Pro - Database Serie A", page_icon="⚽", layout="wide")

st.title("⚽ FantaHub Pro - Guida Asta Serie A (1500 Crediti)")
st.caption("Database completo di tutte le squadre e giocatori con valutazioni, titolarità e spesa consigliata.")

# --- DATABASE GIOCATORI COMPLETO ---
@st.cache_data
def load_data():
    giocatori = [
        # --- ATALANTA ---
        {"Nome": "Carnesecchi", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 25, "Status": "Consigliato - Titolare", "Convenienza": "Alta"},
        {"Nome": "Musso", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 5, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Rossi", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Scalvini", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 30, "Status": "Top Difesa / Giovane Prospetto", "Convenienza": "Alta"},
        {"Nome": "Toloi", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 12, "Status": "Riserva / Rotazione", "Convenienza": "Media"},
        {"Nome": "Zappacosta", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 22, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Bakker", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 8, "Status": "Scommessa / Alternativa", "Convenienza": "Bassa"},
        {"Nome": "Hateboer", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Holm", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 12, "Status": "Scommessa / Corsa", "Convenienza": "Media"},
        {"Nome": "Zortea", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Koopmeiners", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 65, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Pasalic", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 35, "Status": "Incursore / Gol", "Convenienza": "Alta"},
        {"Nome": "De Ketelaere", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 50, "Status": "Top Slot / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Adopo", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 3, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Lookman", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 75, "Status": "Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Højlund", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 70, "Status": "Bomber / Titolare", "Convenienza": "Alta"},
        {"Nome": "Touré", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 20, "Status": "Scommessa / Alternativa", "Convenienza": "Media"},

        # --- BOLOGNA ---
        {"Nome": "Calafiori", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 28, "Status": "Titolare / Ottimo Rendimento", "Convenienza": "Altissima"},
        {"Nome": "Lucumí", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Posch", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 25, "Status": "Titolare / Bonus", "Convenienza": "Alta"},
        {"Nome": "Ferguson", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 55, "Status": "Top / Incursore", "Convenienza": "Altissima"},
        {"Nome": "Freuler", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 22, "Status": "Titolare / Costanza", "Convenienza": "Alta"},
        {"Nome": "Fabbian", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 28, "Status": "Incursore da Gol", "Convenienza": "Alta"},
        {"Nome": "El Azzouzi", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 8, "Status": "Riserva / Rotazione", "Convenienza": "Media"},
        {"Nome": "Urbanski", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 10, "Status": "Giovane Scommessa", "Convenienza": "Media"},
        {"Nome": "Orsolini", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 58, "Status": "Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Saelemaekers", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 25, "Status": "Titolare / Assist", "Convenienza": "Alta"},
        {"Nome": "Ndoye", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 22, "Status": "Titolare / Corsa", "Convenienza": "Media"},
        {"Nome": "Zirkzee", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 80, "Status": "Super Top / Regista d'Attacco", "Convenienza": "Altissima"},
        {"Nome": "Castro", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 20, "Status": "Scommessa / Futuro", "Convenienza": "Media"},

        # --- CAGLIARI ---
        {"Nome": "Dossena", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 18, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Mina", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Titolare / Esperienza", "Convenienza": "Media"},
        {"Nome": "Obert", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Nandez", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 20, "Status": "Titolare / Garra", "Convenienza": "Alta"},
        {"Nome": "Gaetano", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 25, "Status": "Trequartista / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Deiola", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Makoumbou", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 12, "Status": "Titolare / Quantità", "Convenienza": "Media"},
        {"Nome": "Prati", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 14, "Status": "Regista / Giovane", "Convenienza": "Media"},
        {"Nome": "Viola", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 18, "Status": "Piazzati / Rigori", "Convenienza": "Alta"},
        {"Nome": "Luvumbo", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 30, "Status": "Titolare / Velocità", "Convenienza": "Alta"},
        {"Nome": "Lapadula", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 25, "Status": "Rigorista / Attacco", "Convenienza": "Media"},
        {"Nome": "Pavoletti", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 12, "Status": "Uomo Ultimi Minuti", "Convenienza": "Media"},
        {"Nome": "Petagna", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 15, "Status": "Alternativa", "Convenienza": "Bassa"},
        {"Nome": "Shomurodov", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},

        # --- COMO ---
        {"Nome": "Goldaniga", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 12, "Status": "Titolare Esperto", "Convenienza": "Media"},
        {"Nome": "Ioannou", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 10, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Odenthal", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 8, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Strefezza", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 40, "Status": "Top Slot Neopromossa", "Convenienza": "Altissima"},
        {"Nome": "Bellemo", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 14, "Status": "Capitano / Titolare", "Convenienza": "Media"},
        {"Nome": "Baselli", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 8, "Status": "Esperienza / Riserva", "Convenienza": "Bassa"},
        {"Nome": "Verdi", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 22, "Status": "Qualità / Piazzati", "Convenienza": "Media"},
        {"Nome": "Kone", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Cutrone", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 35, "Status": "Titolare / Bomber", "Convenienza": "Alta"},
        {"Nome": "Mancuso", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},

        # --- FIORENTINA ---
        {"Nome": "Biraghi", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 22, "Status": "Piazzati / Assist", "Convenienza": "Alta"},
        {"Nome": "Dodô", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 20, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Kayode", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 18, "Status": "Giovane Talento", "Convenienza": "Altissima"},
        {"Nome": "Milenkovic", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare / Saltatore", "Convenienza": "Alta"},
        {"Nome": "Martinez Quarta", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 20, "Status": "Difensore / Gol", "Convenienza": "Alta"},
        {"Nome": "Parisi", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Ballottaggio", "Convenienza": "Media"},
        {"Nome": "Bonaventura", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 42, "Status": "Top Slot / Incursore", "Convenienza": "Altissima"},
        {"Nome": "Arthur", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 20, "Status": "Regista / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Mandragora", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 18, "Status": "Titolare / Tiro da Fuori", "Convenienza": "Media"},
        {"Nome": "Castrovilli", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 12, "Status": "Scommessa Recupero", "Convenienza": "Bassa"},
        {"Nome": "Gonzalez", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 70, "Status": "Top Attacco / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Belotti", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 30, "Status": "Lotta / Titolare", "Convenienza": "Media"},
        {"Nome": "Nzola", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 20, "Status": "Alternativa", "Convenienza": "Bassa"},
        {"Nome": "Ikoné", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 18, "Status": "Scontinuità", "Convenienza": "Bassa"},
        {"Nome": "Kouamé", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 15, "Status": "Jolly Attacco", "Convenienza": "Media"},
        {"Nome": "Sottil", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 14, "Status": "Spunto / Alternativa", "Convenienza": "Bassa"},

        # --- INTER ---
        {"Nome": "Sommer", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 50, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Dimarco", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 65, "Status": "Super Top Difesa / Assist", "Convenienza": "Altissima"},
        {"Nome": "Bastoni", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 45, "Status": "Top Difesa", "Convenienza": "Altissima"},
        {"Nome": "Pavard", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 38, "Status": "Titolare Top", "Convenienza": "Alta"},
        {"Nome": "Acerbi", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 22, "Status": "Titolare / Esperienza", "Convenienza": "Alta"},
        {"Nome": "De Vrij", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 15, "Status": "Rotazione Centrali", "Convenienza": "Media"},
        {"Nome": "Darmian", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 20, "Status": "Jolly / Affidabile", "Convenienza": "Alta"},
        {"Nome": "Dumfries", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 35, "Status": "Bonus / Corsa", "Convenienza": "Alta"},
        {"Nome": "Carlos Augusto", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 25, "Status": "Jolly di Qualità", "Convenienza": "Alta"},
        {"Nome": "Bisseck", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 15, "Status": "Giovane in Crescita", "Convenienza": "Media"},
        {"Nome": "Calhanoglu", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 80, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Barella", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 55, "Status": "Top Centrocampo", "Convenienza": "Altissima"},
        {"Nome": "Frattesi", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 48, "Status": "Incursore Spietato da Gol", "Convenienza": "Altissima"},
        {"Nome": "Asllani", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 35, "Quotazione": 10, "Status": "Vice Calhanoglu", "Convenienza": "Bassa"},
        {"Nome": "Lautaro Martínez", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 130, "Status": "📌 TOP RE ASSOLUTO ASTA", "Convenienza": "Altissima"},
        {"Nome": "Thuram", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 95, "Status": "Super Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Arnautovic", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 20, "Status": "Riserva d'Attacco", "Convenienza": "Bassa"},

        # --- JUVENTUS ---
        {"Nome": "Szczesny", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 45, "Status": "Top Portiere", "Convenienza": "Alta"},
        {"Nome": "Bremer", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 50, "Status": "Muro Inamovibile", "Convenienza": "Altissima"},
        {"Nome": "Cambiaso", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 38, "Status": "Titolare / Assist", "Convenienza": "Altissima"},
        {"Nome": "Gatti", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 28, "Status": "Titolare / Gol di Testa", "Convenienza": "Alta"},
        {"Nome": "Danilo", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 32, "Status": "Capitano / Titolare", "Convenienza": "Alta"},
        {"Nome": "Rugani", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva Affidabile", "Convenienza": "Bassa"},
        {"Nome": "Rabiot", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 60, "Status": "Top Centrocampo / Gol", "Convenienza": "Altissima"},
        {"Nome": "Locatelli", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 25, "Status": "Titolare / Regista", "Convenienza": "Alta"},
        {"Nome": "McKennie", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 30, "Status": "Assistman / Titolare", "Convenienza": "Alta"},
        {"Nome": "Fagioli", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 20, "Status": "Qualità / Scommessa", "Convenienza": "Media"},
        {"Nome": "Miretti", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Alcaraz", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 12, "Status": "Alternativa", "Convenienza": "Bassa"},
        {"Nome": "Iling-Junior", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 14, "Status": "Spinta / Cambio", "Convenienza": "Media"},
        {"Nome": "Vlahovic", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 120, "Status": "Super Top Bomber / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Chiesa", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 75, "Status": "Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Yildiz", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 40, "Status": "Talento Puro / Scommessa Top", "Convenienza": "Altissima"},
        {"Nome": "Milik", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 22, "Status": "Riserva / Vice Vlahovic", "Convenienza": "Media"},
        {"Nome": "Kean", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 15, "Status": "Alternativa Attacco", "Convenienza": "Bassa"},

        # --- LAZIO ---
        {"Nome": "Provedel", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 40, "Status": "Titolare / Ottimo Portiere", "Convenienza": "Alta"},
        {"Nome": "Marusic", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare Multi-ruolo", "Convenienza": "Alta"},
        {"Nome": "Lazzari", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 18, "Status": "Spinta sulla Fascia", "Convenienza": "Media"},
        {"Nome": "Gila", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Titolare / Crescita", "Convenienza": "Alta"},
        {"Nome": "Patric", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 12, "Status": "Rotazione Centrali", "Convenienza": "Media"},
        {"Nome": "Zaccagni", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 70, "Status": "Top Slot / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Luis Alberto", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 60, "Status": "Qualità / Assist", "Convenienza": "Alta"},
        {"Nome": "Guendouzi", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 35, "Status": "Titolare / Sostanza", "Convenienza": "Alta"},
        {"Nome": "Felipe Anderson", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 50, "Status": "Bonus / Titolare", "Convenienza": "Alta"},
        {"Nome": "Rovella", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 20, "Status": "Regista Titolare", "Convenienza": "Media"},
        {"Nome": "Vecino", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 18, "Status": "Incursore / Gol Pesanti", "Convenienza": "Alta"},
        {"Nome": "Cataldi", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 10, "Status": "Riserva Regia", "Convenienza": "Bassa"},
        {"Nome": "Kamada", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 18, "Status": "Scontinuità", "Convenienza": "Bassa"},
        {"Nome": "Isaksen", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 20, "Status": "Scommessa / Ala", "Convenienza": "Media"},
        {"Nome": "Immobile", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 70, "Status": "Bomber Storico / Rigorista", "Convenienza": "Alta"},
        {"Nome": "Castellanos", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 40, "Status": "Lotta Titolare", "Convenienza": "Media"},
        {"Nome": "Pedro", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 12, "Status": "Jolly Esperto", "Convenienza": "Bassa"},

        # --- LECCE ---
        {"Nome": "Baschirotto", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 22, "Status": "Roccia / Titolare Inamovibile", "Convenienza": "Altissima"},
        {"Nome": "Dorgu", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 20, "Status": "Talento / Spinta", "Convenienza": "Altissima"},
        {"Nome": "Gendrey", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 14, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Pongracic", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 15, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Ramadani", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 15, "Status": "Titolare / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Oudin", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 22, "Status": "Qualità / Piazzati", "Convenienza": "Alta"},
        {"Nome": "Rafia", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Gonzalez", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 12, "Status": "Scommessa", "Convenienza": "Media"},
        {"Nome": "Strefezza", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 25, "Status": "Rigori / Bonus", "Convenienza": "Media"},
        {"Nome": "Krstovic", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 50, "Status": "Bomber Titolare Lecce", "Convenienza": "Altissima"},
        {"Nome": "Banda", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 25, "Status": "Velocità / Dribbling", "Convenienza": "Alta"},

        # --- MILAN ---
        {"Nome": "Maignan", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 50, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Hernandez", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 65, "Status": "Super Top Difesa", "Convenienza": "Altissima"},
        {"Nome": "Tomori", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 35, "Status": "Titolare Top", "Convenienza": "Alta"},
        {"Nome": "Thiaw", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 20, "Status": "Titolare / Rotazione", "Convenienza": "Media"},
        {"Nome": "Kalulu", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 18, "Status": "Jolly Difesa", "Convenienza": "Media"},
        {"Nome": "Calabria", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Capitano / Titolare", "Convenienza": "Alta"},
        {"Nome": "Florenzi", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Riserva / Piazzati", "Convenienza": "Bassa"},
        {"Nome": "Pulisic", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 80, "Status": "Super Top Centrocampo", "Convenienza": "Altissima"},
        {"Nome": "Loftus-Cheek", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 50, "Status": "Incursore / Fisico", "Convenienza": "Altissima"},
        {"Nome": "Reijnders", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 40, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Bennacer", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 25, "Status": "Regista", "Convenienza": "Media"},
        {"Nome": "Musah", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Adli", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 12, "Status": "Riserva Regia", "Convenienza": "Bassa"},
        {"Nome": "Chukwueze", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 30, "Status": "Spunto dal Banchina", "Convenienza": "Media"},
        {"Nome": "Leão", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 110, "Status": "Super Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Giroud", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 75, "Status": "Rigorista / Bomber", "Convenienza": "Alta"},
        {"Nome": "Okafor", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 22, "Status": "Jolly spacca-partite", "Convenienza": "Media"},
        {"Nome": "Jović", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 18, "Status": "Vice Giroud", "Convenienza": "Bassa"},

        # --- MONZA ---
        {"Nome": "Di Gregorio", "Squadra": "Monza", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 35, "Status": "Para-Rigori / Top", "Convenienza": "Altissima"},
        {"Nome": "Caldirola", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Birindelli", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 12, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Carboni", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 14, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "D’Ambrosio", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 12, "Status": "Esperienza", "Convenienza": "Bassa"},
        {"Nome": "Pessina", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 45, "Status": "Capitano / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Colpani", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 55, "Status": "Top Slot / Gol", "Convenienza": "Altissima"},
        {"Nome": "Gagliardini", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 15, "Status": "Titolare / Quantità", "Convenienza": "Media"},
        {"Nome": "Vignato", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 10, "Status": "Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Mota", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 25, "Status": "Titolare Attacco", "Convenienza": "Media"},
        {"Nome": "Maldini", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 20, "Status": "Talento / Scommessa", "Convenienza": "Alta"},
        {"Nome": "Petagna", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 12, "Status": "Riserva", "Convenienza": "Bassa"},

        # --- NAPOLI ---
        {"Nome": "Meret", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 40, "Status": "Titolare Portiere", "Convenienza": "Alta"},
        {"Nome": "Di Lorenzo", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 45, "Status": "Top Difesa / Capitano", "Convenienza": "Altissima"},
        {"Nome": "Rrahmani", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 25, "Status": "Titolare Centrali", "Convenienza": "Alta"},
        {"Nome": "Mario Rui", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 14, "Status": "Ballottaggio", "Convenienza": "Bassa"},
        {"Nome": "Juan Jesus", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Lobotka", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 30, "Status": "Metronomo / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Anguissa", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 35, "Status": "Titolare / Fisico", "Convenienza": "Alta"},
        {"Nome": "Zielinski", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 35, "Status": "Qualità", "Convenienza": "Media"},
        {"Nome": "Cajuste", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Gaetano", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Lindstrøm", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 18, "Status": "Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Kvaratskhelia", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 115, "Status": "Super Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Osimhen", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 125, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Politano", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 45, "Status": "Titolare / Rigori / Bonus", "Convenienza": "Alta"},
        {"Nome": "Raspadori", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 30, "Status": "Jolly Attacco", "Convenienza": "Media"},
        {"Nome": "Simeone", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 20, "Status": "Vice Osimhen da Gol", "Convenienza": "Media"},
        {"Nome": "Ngonge", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 22, "Status": "Spacca-partite", "Convenienza": "Media"},

        # --- PARMA ---
        {"Nome": "Del Prato", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 18, "Status": "Capitano / Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Circati", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 14, "Status": "Giovane Centralissimo", "Convenienza": "Alta"},
        {"Nome": "Coulibaly", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 12, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Valenti", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Bernabé", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 38, "Status": "🔥 Talento Top / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Man", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 45, "Status": "🔥 Rigorista / Gol e Assist", "Convenienza": "Altissima"},
        {"Nome": "Mihaila", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 22, "Status": "Velocità / Bonus", "Convenienza": "Media"},
        {"Nome": "Hernani", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 18, "Status": "Fisico / Rigori", "Convenienza": "Alta"},
        {"Nome": "Estevez", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 15, "Status": "Equilibrio", "Convenienza": "Media"},
        {"Nome": "Sohm", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 14, "Status": "Inserimenti", "Convenienza": "Media"},
        {"Nome": "Camara", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Partipilo", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Bonny", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 32, "Status": "Titolare Attacco Parma", "Convenienza": "Alta"},

        # --- ROMA ---
        {"Nome": "Rui Patricio", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 50, "Quotazione": 15, "Status": "Ballottaggio Porta", "Convenienza": "Bassa"},
        {"Nome": "Mancini", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 32, "Status": "Titolare / Bonus Testa", "Convenienza": "Alta"},
        {"Nome": "Ndicka", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 25, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Smalling", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 15, "Status": "Incognita Fisica", "Convenienza": "Bassa"},
        {"Nome": "Llorente", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Spinazzola", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 20, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Kristensen", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 12, "Status": "Ballottaggio", "Convenienza": "Bassa"},
        {"Nome": "Karsdorp", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Pellegrini", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 60, "Status": "Top Slot / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Cristante", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 28, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Paredes", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 25, "Status": "Regista / Rigori", "Convenienza": "Alta"},
        {"Nome": "Bove", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 18, "Status": "Polmoni / Inserimenti", "Convenienza": "Media"},
        {"Nome": "Aouar", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 15, "Status": "Qualità / Riserva", "Convenienza": "Bassa"},
        {"Nome": "Renato Sanches", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 35, "Quotazione": 10, "Status": "Troppi Infortuni", "Convenienza": "Bassa"},
        {"Nome": "Zalewski", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 15, "Status": "Jolly Fascia", "Convenienza": "Media"},
        {"Nome": "El Shaarawy", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 35, "Status": "Bonus Certi / Titolare", "Convenienza": "Alta"},
        {"Nome": "Dybala", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 100, "Status": "Super Top / Classe Purissima", "Convenienza": "Altissima"},
        {"Nome": "Lukaku", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 115, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Azmoun", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 15, "Status": "Riserva d'Attacco", "Convenienza": "Bassa"},

        # --- SASSUOLO ---
        {"Nome": "Berardi", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 90, "Status": "Top / Rigorista Assoluto", "Convenienza": "Altissima"},
        {"Nome": "Laurienté", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 45, "Status": "Titolare / Dribbling", "Convenienza": "Alta"},
        {"Nome": "Pinamonti", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 50, "Status": "Bomber Titolare", "Convenienza": "Alta"},
        {"Nome": "Defrel", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Matheus Henrique", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 22, "Status": "Titolare / Qualità", "Convenienza": "Alta"},
        {"Nome": "Boloca", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 16, "Status": "Titolare Centrocampo", "Convenienza": "Media"},
        {"Nome": "Castillejo", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Obiang", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Erlic", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Toljan", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Assistman Inaspettato", "Convenienza": "Alta"},
        {"Nome": "Viti", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},

        # --- TORINO ---
        {"Nome": "Buongiorno", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 42, "Status": "Muro Difensivo / Top Slot", "Convenienza": "Altissima"},
        {"Nome": "Bellanova", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 35, "Status": "Trennino / Tanti Assist", "Convenienza": "Altissima"},
        {"Nome": "Rodriguez", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Capitano / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Schuurs", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 22, "Status": "Top Se In Salute", "Convenienza": "Alta"},
        {"Nome": "Djidji", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Vlasic", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 42, "Status": "Trequartista Titolare", "Convenienza": "Alta"},
        {"Nome": "Ricci", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 22, "Status": "Regista / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Ilic", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 25, "Status": "Titolare / Tiro da Fuori", "Convenienza": "Media"},
        {"Nome": "Linetty", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Gineitis", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 10, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "Zapata", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 80, "Status": "Panzer / Bomber Titolare", "Convenienza": "Altissima"},
        {"Nome": "Sanabria", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 30, "Status": "Coppia con Zapata", "Convenienza": "Media"},
        {"Nome": "Pellegri", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},

        # --- UDINESE ---
        {"Nome": "Bijol", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 22, "Status": "Leader Difensivo", "Convenienza": "Alta"},
        {"Nome": "Kamara", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 14, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Ehizibue", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 12, "Status": "Corsa / Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Kabasele", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 10, "Status": "Esperienza", "Convenienza": "Bassa"},
        {"Nome": "Samardzic", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 50, "Status": "Talento Puro / Gol e Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Pereyra", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 42, "Status": "Rigorista / Leader", "Convenienza": "Altissima"},
        {"Nome": "Walace", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 16, "Status": "Diga / Voto Fisso Guaranteed", "Convenienza": "Alta"},
        {"Nome": "Lucca", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 45, "Status": "Centravanti Titolare", "Convenienza": "Alta"},
        {"Nome": "Thauvin", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 35, "Status": "Qualità / Piazzati", "Convenienza": "Alta"},
        {"Nome": "Success", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 14, "Status": "Lavoro Sporco / Pochi Gol", "Convenienza": "Bassa"},

        # --- VENEZIA ---
        {"Nome": "Idzes", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 15, "Status": "Titolare / Roccia", "Convenienza": "Alta"},
        {"Nome": "Candela", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 14, "Status": "Spinta sulla Fascia", "Convenienza": "Media"},
        {"Nome": "Altare", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 12, "Status": "Saltatore di Testa", "Convenienza": "Media"},
        {"Nome": "Svoboda", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 10, "Status": "Titolare", "Convenienza": "Bassa"},
        {"Nome": "Busio", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 22, "Status": "Inserimenti / Incursore", "Convenienza": "Alta"},
        {"Nome": "Tessmann", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 25, "Status": "Fisico / Tiro da Fuori", "Convenienza": "Alta"},
        {"Nome": "Ellertsson", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 12, "Status": "Dinamismo", "Convenienza": "Media"},
        {"Nome": "Jajalo", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 8, "Status": "Esperienza / Riserva", "Convenienza": "Bassa"},
        {"Nome": "Pohjanpalo", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 60, "Status": "🔥 IL DOGE / Rigorista Assoluto", "Convenienza": "Altissima"},
        {"Nome": "Gytkjaer", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 18, "Status": "Riserva di Lusso", "Convenienza": "Media"}
    ]
    return pd.DataFrame(giocatori)

df = load_data()

# --- SIDEBAR CONFIGURAZIONE BUDGET (1500 CREDITI) ---
st.sidebar.header("⚙️ Budget & Gestione Asta")
budget_totale = st.sidebar.number_input("Budget Iniziale (Crediti)", min_value=100, max_value=3000, value=1500)

st.sidebar.subheader("% Spesa Consigliata")
perc_p = st.sidebar.slider("Porta (%)", 1, 10, 4)      # ~60 crediti
perc_d = st.sidebar.slider("Difesa (%)", 5, 20, 10)     # ~150 crediti
perc_c = st.sidebar.slider("Centrocampo (%)", 10, 40, 26)# ~390 crediti
perc_a = st.sidebar.slider("Attacco (%)", 30, 80, 60)    # ~900 crediti

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

    # Calcolo proporzionale in base alla quotazione
    spesa = (quot / 100) * (budget_r * 0.8)
    return int(max(1, spesa))

df["Spesa_Max_Consigliata_(cr)"] = df.apply(calcola_spesa_max, axis=1)

# --- TABS ---
tab1, tab2 = st.tabs(["🔍 Cerca Giocatore & Scheda Asta", "📋 Listone Completo Serie A"])

# --- TAB 1: SEARCH BAR E SCHEDA ---
with tab1:
    st.subheader("🔎 Cerca un Giocatore nel Database")
    
    # BARRA DI RICERCA TESTUALE
    search_input = st.text_input("✍️ Scrivi il nome del giocatore (es. Lautaro, Pohjanpalo, Berardi):", "")
    
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
