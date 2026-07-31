import streamlit as st
import pandas as pd

st.set_page_config(page_title="FantaHub Pro - Database Serie A", page_icon="⚽", layout="wide")

st.title("⚽ FantaHub Pro - Guida Asta Serie A (1500 Crediti)")
st.caption("Database completo di tutte le squadre e giocatori con valutazioni, titolarità, spesa consigliata e STATS 24/25.")

# --- DATABASE GIOCATORI COMPLETO CON STATS 24/25 ---
@st.cache_data
def load_data():
    giocatori = [

        {'Nome': 'Honest Ahanor', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 15, 'Quotazione': 2, 'Status': 'Giovane Promessa', 'Convenienza': 'Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Mitchel Bakker', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 45, 'Quotazione': 8, 'Status': 'Scommessa / Alternativa', 'Convenienza': 'Bassa', 'Pres_24_25': 10, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.75, 'FM_24_25': 5.85},
        {'Nome': 'Raoul Bellanova', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 85, 'Quotazione': 35, 'Status': 'Titolare / Spinta', 'Convenienza': 'Altissima', 'Pres_24_25': 33, 'Gol_24_25': 1, 'Assist_24_25': 4, 'MV_24_25': 6.05, 'FM_24_25': 6.35},
        {'Nome': 'Lorenzo Bernasconi', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 10, 'Quotazione': 1, 'Status': 'Riserva Giovanile', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Giovanni Bonfanti', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 25, 'Quotazione': 4, 'Status': 'Riserva', 'Convenienza': 'Bassa', 'Pres_24_25': 2, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.5, 'FM_24_25': 5.5},
        {'Nome': 'Marco Carnesecchi', 'Squadra': 'Atalanta', 'Ruolo': 'Portiere', 'Titolarita_%': 85, 'Quotazione': 25, 'Status': 'Consigliato - Titolare', 'Convenienza': 'Alta', 'Pres_24_25': 37, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.21, 'FM_24_25': 5.05},
        {'Nome': 'Berat Djimsiti', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 85, 'Quotazione': 20, 'Status': 'Titolare Fisso', 'Convenienza': 'Alta', 'Pres_24_25': 33, 'Gol_24_25': 1, 'Assist_24_25': 1, 'MV_24_25': 6.0, 'FM_24_25': 6.15},
        {'Nome': 'Gianluca Gaetano', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 60, 'Quotazione': 20, 'Status': 'Rotazione / Qualità', 'Convenienza': 'Media', 'Pres_24_25': 10, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.0},
        {'Nome': 'Isak Hien', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 22, 'Status': 'Titolare Difesa', 'Convenienza': 'Alta', 'Pres_24_25': 32, 'Gol_24_25': 2, 'Assist_24_25': 0, 'MV_24_25': 5.95, 'FM_24_25': 6.2},
        {'Nome': 'Charles De Ketelaere', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 80, 'Quotazione': 50, 'Status': 'Top Slot / Bonus', 'Convenienza': 'Altissima', 'Pres_24_25': 36, 'Gol_24_25': 10, 'Assist_24_25': 9, 'MV_24_25': 6.38, 'FM_24_25': 7.55},
        {'Nome': 'Sead Kolasinac', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 85, 'Quotazione': 24, 'Status': 'Titolare Esperto', 'Convenienza': 'Alta', 'Pres_24_25': 31, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 6.08, 'FM_24_25': 6.28},
        {'Nome': 'Odilon Kossounou', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 75, 'Quotazione': 22, 'Status': 'Rinforzo Difesa', 'Convenienza': 'Alta', 'Pres_24_25': 18, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.88, 'FM_24_25': 5.88},
        {'Nome': 'Nikola Krstovic', 'Squadra': 'Atalanta', 'Ruolo': 'Attaccante', 'Titolarita_%': 70, 'Quotazione': 35, 'Status': 'Rotazione Offensiva', 'Convenienza': 'Media', 'Pres_24_25': 37, 'Gol_24_25': 11, 'Assist_24_25': 3, 'MV_24_25': 5.98, 'FM_24_25': 6.95},
        {'Nome': 'Daniel Maldini', 'Squadra': 'Atalanta', 'Ruolo': 'Attaccante', 'Titolarita_%': 55, 'Quotazione': 18, 'Status': 'Talento / Jolly', 'Convenienza': 'Media', 'Pres_24_25': 30, 'Gol_24_25': 3, 'Assist_24_25': 2, 'MV_24_25': 5.95, 'FM_24_25': 6.25},
        {'Nome': 'Mario Pasalic', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 70, 'Quotazione': 35, 'Status': 'Incursore / Gol', 'Convenienza': 'Alta', 'Pres_24_25': 34, 'Gol_24_25': 6, 'Assist_24_25': 3, 'MV_24_25': 6.12, 'FM_24_25': 6.85},
        {'Nome': 'Giacomo Raspadori', 'Squadra': 'Atalanta', 'Ruolo': 'Attaccante', 'Titolarita_%': 70, 'Quotazione': 40, 'Status': 'Jolly / Bonus', 'Convenienza': 'Alta', 'Pres_24_25': 22, 'Gol_24_25': 3, 'Assist_24_25': 2, 'MV_24_25': 5.95, 'FM_24_25': 6.25},
        {'Nome': 'Marten De Roon', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 90, 'Quotazione': 22, 'Status': 'Titolare / Voto Fisso', 'Convenienza': 'Alta', 'Pres_24_25': 35, 'Gol_24_25': 0, 'Assist_24_25': 2, 'MV_24_25': 6.05, 'FM_24_25': 6.15},
        {'Nome': 'Francesco Rossi', 'Squadra': 'Atalanta', 'Ruolo': 'Portiere', 'Titolarita_%': 5, 'Quotazione': 1, 'Status': 'Terzo Portiere', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Lazar Samardzic', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 75, 'Quotazione': 45, 'Status': 'Qualità / Piazzati', 'Convenienza': 'Altissima', 'Pres_24_25': 31, 'Gol_24_25': 4, 'Assist_24_25': 5, 'MV_24_25': 6.1, 'FM_24_25': 6.65},
        {'Nome': 'Giorgio Scalvini', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 85, 'Quotazione': 30, 'Status': 'Top Difesa / Giovane Prospetto', 'Convenienza': 'Alta', 'Pres_24_25': 6, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.92, 'FM_24_25': 5.92},
        {'Nome': 'Gianluca Scamacca', 'Squadra': 'Atalanta', 'Ruolo': 'Attaccante', 'Titolarita_%': 85, 'Quotazione': 75, 'Status': 'Bomber Titolare', 'Convenienza': 'Altissima', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Éderson Silva', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 90, 'Quotazione': 32, 'Status': 'Titolare Inamovibile', 'Convenienza': 'Alta', 'Pres_24_25': 37, 'Gol_24_25': 4, 'Assist_24_25': 2, 'MV_24_25': 6.15, 'FM_24_25': 6.58},
        {'Nome': 'Marco Sportiello', 'Squadra': 'Atalanta', 'Ruolo': 'Portiere', 'Titolarita_%': 15, 'Quotazione': 5, 'Status': 'Secondo Portiere', 'Convenienza': 'Bassa', 'Pres_24_25': 5, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.0, 'FM_24_25': 4.8},
        {'Nome': 'Ibrahim Sulemana', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 50, 'Quotazione': 12, 'Status': 'Rotazione', 'Convenienza': 'Media', 'Pres_24_25': 17, 'Gol_24_25': 2, 'Assist_24_25': 1, 'MV_24_25': 5.85, 'FM_24_25': 6.15},
        {'Nome': 'Kamaldeen Sulemana', 'Squadra': 'Atalanta', 'Ruolo': 'Attaccante', 'Titolarita_%': 50, 'Quotazione': 20, 'Status': 'Scommessa Esterna', 'Convenienza': 'Media', 'Pres_24_25': 15, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 5.9, 'FM_24_25': 6.15},
        {'Nome': 'El Bilal Touré', 'Squadra': 'Atalanta', 'Ruolo': 'Attaccante', 'Titolarita_%': 50, 'Quotazione': 20, 'Status': 'Scommessa / Alternativa', 'Convenienza': 'Media', 'Pres_24_25': 11, 'Gol_24_25': 2, 'Assist_24_25': 0, 'MV_24_25': 5.8, 'FM_24_25': 6.1},
        {'Nome': 'Nicola Zalewski', 'Squadra': 'Atalanta', 'Ruolo': 'Centrocampista', 'Titolarita_%': 65, 'Quotazione': 20, 'Status': 'Jolly Fascia', 'Convenienza': 'Media', 'Pres_24_25': 29, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 5.9, 'FM_24_25': 6.05},
        {'Nome': 'Davide Zappacosta', 'Squadra': 'Atalanta', 'Ruolo': 'Difensore', 'Titolarita_%': 75, 'Quotazione': 22, 'Status': 'Titolare / Spinta', 'Convenienza': 'Alta', 'Pres_24_25': 30, 'Gol_24_25': 2, 'Assist_24_25': 3, 'MV_24_25': 6.02, 'FM_24_25': 6.37},
        {'Nome': 'Michel Aebischer', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 75, 'Quotazione': 18, 'Status': 'Titolare Affidabile', 'Convenienza': 'Alta', 'Pres_24_25': 32, 'Gol_24_25': 0, 'Assist_24_25': 2, 'MV_24_25': 6.0, 'FM_24_25': 6.1},
        {'Nome': 'Federico Bernardeschi', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 70, 'Quotazione': 35, 'Status': 'Esperienza / Qualità', 'Convenienza': 'Alta', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Nicolò Cambiaghi', 'Squadra': 'Bologna', 'Ruolo': 'Attaccante', 'Titolarita_%': 75, 'Quotazione': 30, 'Status': 'Titolare / Dribbling', 'Convenienza': 'Alta', 'Pres_24_25': 26, 'Gol_24_25': 3, 'Assist_24_25': 3, 'MV_24_25': 5.95, 'FM_24_25': 6.3},
        {'Nome': 'Nicolò Casale', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 75, 'Quotazione': 20, 'Status': 'Titolare Difesa', 'Convenienza': 'Alta', 'Pres_24_25': 21, 'Gol_24_25': 1, 'Assist_24_25': 0, 'MV_24_25': 5.9, 'FM_24_25': 6.0},
        {'Nome': 'Santiago Castro', 'Squadra': 'Bologna', 'Ruolo': 'Attaccante', 'Titolarita_%': 60, 'Quotazione': 25, 'Status': 'Attaccante in Crescita', 'Convenienza': 'Alta', 'Pres_24_25': 36, 'Gol_24_25': 8, 'Assist_24_25': 4, 'MV_24_25': 6.02, 'FM_24_25': 6.72},
        {'Nome': 'Thijs Dallinga', 'Squadra': 'Bologna', 'Ruolo': 'Attaccante', 'Titolarita_%': 75, 'Quotazione': 45, 'Status': 'Centravanti Titolare', 'Convenienza': 'Alta', 'Pres_24_25': 31, 'Gol_24_25': 3, 'Assist_24_25': 2, 'MV_24_25': 5.85, 'FM_24_25': 6.1},
        {'Nome': 'Lewis Ferguson', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 90, 'Quotazione': 55, 'Status': 'Top / Incursore', 'Convenienza': 'Altissima', 'Pres_24_25': 28, 'Gol_24_25': 4, 'Assist_24_25': 3, 'MV_24_25': 6.18, 'FM_24_25': 6.68},
        {'Nome': 'Remo Freuler', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 90, 'Quotazione': 22, 'Status': 'Titolare / Costanza', 'Convenienza': 'Alta', 'Pres_24_25': 33, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 6.05, 'FM_24_25': 6.25},
        {'Nome': 'Jhon Lucumí', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 18, 'Status': 'Titolare Fisso', 'Convenienza': 'Alta', 'Pres_24_25': 26, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.0, 'FM_24_25': 6.0},
        {'Nome': 'Juan Miranda', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 75, 'Quotazione': 22, 'Status': 'Titolare Fascia', 'Convenienza': 'Alta', 'Pres_24_25': 28, 'Gol_24_25': 0, 'Assist_24_25': 2, 'MV_24_25': 5.95, 'FM_24_25': 6.05},
        {'Nome': 'Riccardo Orsolini', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 80, 'Quotazione': 58, 'Status': 'Top / Rigorista', 'Convenienza': 'Altissima', 'Pres_24_25': 32, 'Gol_24_25': 12, 'Assist_24_25': 3, 'MV_24_25': 6.25, 'FM_24_25': 7.45},
        {'Nome': 'Tommaso Pobega', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 70, 'Quotazione': 22, 'Status': 'Incursore Fisico', 'Convenienza': 'Alta', 'Pres_24_25': 21, 'Gol_24_25': 1, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.0},
        {'Nome': 'Lukasz Skorupski', 'Squadra': 'Bologna', 'Ruolo': 'Portiere', 'Titolarita_%': 85, 'Quotazione': 32, 'Status': 'Titolare Affidabile', 'Convenienza': 'Alta', 'Pres_24_25': 36, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.15, 'FM_24_25': 4.95},
        {'Nome': 'Martin Vitík', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 70, 'Quotazione': 20, 'Status': 'Rinforzo Difensivo', 'Convenienza': 'Alta', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Emil Holm', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 65, 'Quotazione': 18, 'Status': 'Alternativa Fascia', 'Convenienza': 'Media', 'Pres_24_25': 24, 'Gol_24_25': 1, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.05},
        {'Nome': 'Jonathan Rowe', 'Squadra': 'Bologna', 'Ruolo': 'Attaccante', 'Titolarita_%': 65, 'Quotazione': 25, 'Status': 'Esterno Offensivo', 'Convenienza': 'Media', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Elia Caprile', 'Squadra': 'Cagliari', 'Ruolo': 'Portiere', 'Titolarita_%': 85, 'Quotazione': 28, 'Status': 'Titolare / Ottimo Potenziale', 'Convenienza': 'Alta', 'Pres_24_25': 26, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.1, 'FM_24_25': 4.8},
        {'Nome': 'Sebastiano Esposito', 'Squadra': 'Cagliari', 'Ruolo': 'Attaccante', 'Titolarita_%': 70, 'Quotazione': 25, 'Status': 'Titolare / Qualità', 'Convenienza': 'Alta', 'Pres_24_25': 33, 'Gol_24_25': 8, 'Assist_24_25': 2, 'MV_24_25': 6.0, 'FM_24_25': 6.6},
        {'Nome': 'Jacopo Fazzini', 'Squadra': 'Cagliari', 'Ruolo': 'Centrocampista', 'Titolarita_%': 75, 'Quotazione': 24, 'Status': 'Trequartista / Incursore', 'Convenienza': 'Alta', 'Pres_24_25': 24, 'Gol_24_25': 3, 'Assist_24_25': 3, 'MV_24_25': 5.95, 'FM_24_25': 6.35},
        {'Nome': 'Yerry Mina', 'Squadra': 'Cagliari', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 18, 'Status': 'Titolare / Esperienza', 'Convenienza': 'Media', 'Pres_24_25': 29, 'Gol_24_25': 3, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.25},
        {'Nome': 'Gabriele Zappa', 'Squadra': 'Cagliari', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 16, 'Status': 'Titolare Fascia', 'Convenienza': 'Media', 'Pres_24_25': 35, 'Gol_24_25': 3, 'Assist_24_25': 5, 'MV_24_25': 6.05, 'FM_24_25': 6.55},
        {'Nome': 'Harry Winks', 'Squadra': 'Cagliari', 'Ruolo': 'Centrocampista', 'Titolarita_%': 85, 'Quotazione': 25, 'Status': 'Regista Titolare', 'Convenienza': 'Alta', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Michel Adopo', 'Squadra': 'Cagliari', 'Ruolo': 'Centrocampista', 'Titolarita_%': 60, 'Quotazione': 14, 'Status': 'Titolare / Quantità', 'Convenienza': 'Media', 'Pres_24_25': 29, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.85, 'FM_24_25': 5.9},
        {'Nome': 'Emil Audero', 'Squadra': 'Como', 'Ruolo': 'Portiere', 'Titolarita_%': 85, 'Quotazione': 30, 'Status': 'Titolare Porta', 'Convenienza': 'Alta', 'Pres_24_25': 13, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.18, 'FM_24_25': 4.9},
        {'Nome': 'Martin Baturina', 'Squadra': 'Como', 'Ruolo': 'Centrocampista', 'Titolarita_%': 80, 'Quotazione': 35, 'Status': 'Talento Puro', 'Convenienza': 'Altissima', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Maxence Caqueret', 'Squadra': 'Como', 'Ruolo': 'Centrocampista', 'Titolarita_%': 85, 'Quotazione': 32, 'Status': 'Regista di Spessore', 'Convenienza': 'Alta', 'Pres_24_25': 16, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.95, 'FM_24_25': 6.0},
        {'Nome': 'Alberto Dossena', 'Squadra': 'Como', 'Ruolo': 'Difensore', 'Titolarita_%': 85, 'Quotazione': 20, 'Status': 'Titolare Inamovibile', 'Convenienza': 'Alta', 'Pres_24_25': 33, 'Gol_24_25': 1, 'Assist_24_25': 1, 'MV_24_25': 5.95, 'FM_24_25': 6.1},
        {'Nome': 'Tasos Douvikas', 'Squadra': 'Como', 'Ruolo': 'Attaccante', 'Titolarita_%': 75, 'Quotazione': 32, 'Status': 'Bomber Titolare', 'Convenienza': 'Alta', 'Pres_24_25': 32, 'Gol_24_25': 8, 'Assist_24_25': 1, 'MV_24_25': 6.0, 'FM_24_25': 6.6},
        {'Nome': 'Nico Paz', 'Squadra': 'Como', 'Ruolo': 'Centrocampista', 'Titolarita_%': 85, 'Quotazione': 45, 'Status': 'Top Slot / Qualità', 'Convenienza': 'Altissima', 'Pres_24_25': 35, 'Gol_24_25': 6, 'Assist_24_25': 8, 'MV_24_25': 6.35, 'FM_24_25': 7.15},
        {'Nome': 'Álvaro Morata', 'Squadra': 'Como', 'Ruolo': 'Attaccante', 'Titolarita_%': 90, 'Quotazione': 75, 'Status': 'Super Top / Stella Como', 'Convenienza': 'Altissima', 'Pres_24_25': 16, 'Gol_24_25': 5, 'Assist_24_25': 2, 'MV_24_25': 5.9, 'FM_24_25': 6.45},
        {'Nome': 'Máximo Perrone', 'Squadra': 'Como', 'Ruolo': 'Centrocampista', 'Titolarita_%': 75, 'Quotazione': 20, 'Status': 'Titolare / Visione', 'Convenienza': 'Media', 'Pres_24_25': 26, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 5.95},
        {'Nome': 'David De Gea', 'Squadra': 'Fiorentina', 'Ruolo': 'Portiere', 'Titolarita_%': 95, 'Quotazione': 48, 'Status': 'Top Portiere', 'Convenienza': 'Altissima', 'Pres_24_25': 33, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.45, 'FM_24_25': 5.35},
        {'Nome': 'Dodô', 'Squadra': 'Fiorentina', 'Ruolo': 'Difensore', 'Titolarita_%': 85, 'Quotazione': 24, 'Status': 'Titolare / Spinta', 'Convenienza': 'Alta', 'Pres_24_25': 31, 'Gol_24_25': 0, 'Assist_24_25': 3, 'MV_24_25': 6.1, 'FM_24_25': 6.25},
        {'Nome': 'Radu Dragusin', 'Squadra': 'Fiorentina', 'Ruolo': 'Difensore', 'Titolarita_%': 85, 'Quotazione': 28, 'Status': 'Muro Difensivo', 'Convenienza': 'Alta', 'Pres_24_25': 16, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.85, 'FM_24_25': 5.85},
        {'Nome': 'Albert Gudmundsson', 'Squadra': 'Fiorentina', 'Ruolo': 'Centrocampista', 'Titolarita_%': 90, 'Quotazione': 75, 'Status': 'Super Top / Rigorista', 'Convenienza': 'Altissima', 'Pres_24_25': 24, 'Gol_24_25': 6, 'Assist_24_25': 2, 'MV_24_25': 6.1, 'FM_24_25': 6.85},
        {'Nome': 'Moise Kean', 'Squadra': 'Fiorentina', 'Ruolo': 'Attaccante', 'Titolarita_%': 85, 'Quotazione': 65, 'Status': 'Bomber Titolare', 'Convenienza': 'Altissima', 'Pres_24_25': 32, 'Gol_24_25': 19, 'Assist_24_25': 3, 'MV_24_25': 6.32, 'FM_24_25': 8.15},
        {'Nome': 'Luca Ranieri', 'Squadra': 'Fiorentina', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 22, 'Status': 'Titolare Affidabile', 'Convenienza': 'Alta', 'Pres_24_25': 30, 'Gol_24_25': 1, 'Assist_24_25': 1, 'MV_24_25': 5.95, 'FM_24_25': 6.1},
        {'Nome': 'Nicolò Fagioli', 'Squadra': 'Fiorentina', 'Ruolo': 'Centrocampista', 'Titolarita_%': 80, 'Quotazione': 28, 'Status': 'Regista di Qualità', 'Convenienza': 'Alta', 'Pres_24_25': 26, 'Gol_24_25': 1, 'Assist_24_25': 3, 'MV_24_25': 6.0, 'FM_24_25': 6.25},
        {'Nome': 'Yann Sommer', 'Squadra': 'Inter', 'Ruolo': 'Portiere', 'Titolarita_%': 90, 'Quotazione': 35, 'Status': 'Top Portiere', 'Convenienza': 'Alta', 'Pres_24_25': 33, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.2, 'FM_24_25': 5.1},
        {'Nome': 'Alessandro Bastoni', 'Squadra': 'Inter', 'Ruolo': 'Difensore', 'Titolarita_%': 90, 'Quotazione': 35, 'Status': 'Top Difesa', 'Convenienza': 'Altissima', 'Pres_24_25': 33, 'Gol_24_25': 1, 'Assist_24_25': 4, 'MV_24_25': 6.15, 'FM_24_25': 6.45},
        {'Nome': 'Federico Dimarco', 'Squadra': 'Inter', 'Ruolo': 'Difensore', 'Titolarita_%': 90, 'Quotazione': 45, 'Status': 'Top / Bonus', 'Convenienza': 'Altissima', 'Pres_24_25': 33, 'Gol_24_25': 4, 'Assist_24_25': 6, 'MV_24_25': 6.25, 'FM_24_25': 6.9},
        {'Nome': 'Nicolò Barella', 'Squadra': 'Inter', 'Ruolo': 'Centrocampista', 'Titolarita_%': 90, 'Quotazione': 55, 'Status': 'Top Slot', 'Convenienza': 'Altissima', 'Pres_24_25': 32, 'Gol_24_25': 2, 'Assist_24_25': 6, 'MV_24_25': 6.28, 'FM_24_25': 6.75},
        {'Nome': 'Lautaro Martinez', 'Squadra': 'Inter', 'Ruolo': 'Attaccante', 'Titolarita_%': 95, 'Quotazione': 110, 'Status': 'Super Top', 'Convenienza': 'Altissima', 'Pres_24_25': 35, 'Gol_24_25': 12, 'Assist_24_25': 4, 'MV_24_25': 6.15, 'FM_24_25': 7.2},
        {'Nome': 'Marcus Thuram', 'Squadra': 'Inter', 'Ruolo': 'Attaccante', 'Titolarita_%': 90, 'Quotazione': 90, 'Status': 'Top Bomber', 'Convenienza': 'Altissima', 'Pres_24_25': 35, 'Gol_24_25': 14, 'Assist_24_25': 6, 'MV_24_25': 6.3, 'FM_24_25': 7.6},
        {'Nome': 'Alex Meret', 'Squadra': 'Napoli', 'Ruolo': 'Portiere', 'Titolarita_%': 85, 'Quotazione': 28, 'Status': 'Titolare', 'Convenienza': 'Alta', 'Pres_24_25': 32, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.1, 'FM_24_25': 4.9},
        {'Nome': 'Scott McTominay', 'Squadra': 'Napoli', 'Ruolo': 'Centrocampista', 'Titolarita_%': 85, 'Quotazione': 50, 'Status': 'Top / Incursore', 'Convenienza': 'Altissima', 'Pres_24_25': 36, 'Gol_24_25': 12, 'Assist_24_25': 4, 'MV_24_25': 6.4, 'FM_24_25': 7.5},
        {'Nome': 'Romelu Lukaku', 'Squadra': 'Napoli', 'Ruolo': 'Attaccante', 'Titolarita_%': 90, 'Quotazione': 85, 'Status': 'Bomber Titolare', 'Convenienza': 'Altissima', 'Pres_24_25': 36, 'Gol_24_25': 14, 'Assist_24_25': 10, 'MV_24_25': 6.2, 'FM_24_25': 7.5},
        {'Nome': 'Michele Di Gregorio', 'Squadra': 'Juventus', 'Ruolo': 'Portiere', 'Titolarita_%': 90, 'Quotazione': 40, 'Status': 'Top Portiere', 'Convenienza': 'Alta', 'Pres_24_25': 33, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.25, 'FM_24_25': 5.2},
        {'Nome': 'Kenan Yildiz', 'Squadra': 'Juventus', 'Ruolo': 'Centrocampista', 'Titolarita_%': 85, 'Quotazione': 55, 'Status': 'Top / Talento', 'Convenienza': 'Altissima', 'Pres_24_25': 35, 'Gol_24_25': 7, 'Assist_24_25': 4, 'MV_24_25': 6.15, 'FM_24_25': 6.8},
        {'Nome': 'Dusan Vlahovic', 'Squadra': 'Juventus', 'Ruolo': 'Attaccante', 'Titolarita_%': 85, 'Quotazione': 80, 'Status': 'Bomber / Rigorista', 'Convenienza': 'Altissima', 'Pres_24_25': 29, 'Gol_24_25': 15, 'Assist_24_25': 3, 'MV_24_25': 6.0, 'FM_24_25': 7.15},
        {'Nome': 'Mike Maignan', 'Squadra': 'Milan', 'Ruolo': 'Portiere', 'Titolarita_%': 90, 'Quotazione': 45, 'Status': 'Top Portiere', 'Convenienza': 'Altissima', 'Pres_24_25': 37, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.3, 'FM_24_25': 5.25},
        {'Nome': 'Rafael Leao', 'Squadra': 'Milan', 'Ruolo': 'Attaccante', 'Titolarita_%': 90, 'Quotazione': 95, 'Status': 'Super Top', 'Convenienza': 'Altissima', 'Pres_24_25': 34, 'Gol_24_25': 8, 'Assist_24_25': 9, 'MV_24_25': 6.05, 'FM_24_25': 7.0},
        {'Nome': 'Christian Pulisic', 'Squadra': 'Milan', 'Ruolo': 'Centrocampista', 'Titolarita_%': 90, 'Quotazione': 75, 'Status': 'Top / Bonus', 'Convenienza': 'Altissima', 'Pres_24_25': 34, 'Gol_24_25': 11, 'Assist_24_25': 8, 'MV_24_25': 6.35, 'FM_24_25': 7.6},
        {'Nome': 'Mile Svilar', 'Squadra': 'Roma', 'Ruolo': 'Portiere', 'Titolarita_%': 90, 'Quotazione': 35, 'Status': 'Top Portiere', 'Convenienza': 'Alta', 'Pres_24_25': 38, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.35, 'FM_24_25': 5.3},
        {'Nome': 'Paulo Dybala', 'Squadra': 'Roma', 'Ruolo': 'Attaccante', 'Titolarita_%': 80, 'Quotazione': 80, 'Status': 'Super Top', 'Convenienza': 'Altissima', 'Pres_24_25': 24, 'Gol_24_25': 6, 'Assist_24_25': 4, 'MV_24_25': 6.2, 'FM_24_25': 7.05},
        {'Nome': 'Artem Dovbyk', 'Squadra': 'Roma', 'Ruolo': 'Attaccante', 'Titolarita_%': 90, 'Quotazione': 85, 'Status': 'Bomber Titolare', 'Convenienza': 'Altissima', 'Pres_24_25': 32, 'Gol_24_25': 12, 'Assist_24_25': 3, 'MV_24_25': 5.95, 'FM_24_25': 6.9},
        {'Nome': 'Rahim Alhassane', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 20, 'Quotazione': 5, 'Status': 'Riserva', 'Convenienza': 'Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Mikel Amondarain', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 10, 'Quotazione': 1, 'Status': 'Giovane', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Oussama El Azzouzi', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 45, 'Quotazione': 8, 'Status': 'Riserva / Rotazione', 'Convenienza': 'Media', 'Pres_24_25': 6, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.6, 'FM_24_25': 5.6},
        {'Nome': 'Benja Domínguez', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 40, 'Quotazione': 14, 'Status': 'Scommessa Esterna', 'Convenienza': 'Media', 'Pres_24_25': 21, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 5.9, 'FM_24_25': 6.1},
        {'Nome': 'Torbjørn Heggem', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 30, 'Quotazione': 8, 'Status': 'Riserva', 'Convenienza': 'Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Eivind Helland', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 10, 'Quotazione': 2, 'Status': 'Giovane', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Mihajlo Ilic', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 25, 'Quotazione': 6, 'Status': 'Riserva', 'Convenienza': 'Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Jesper Karlsson', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 50, 'Quotazione': 20, 'Status': 'Scommessa', 'Convenienza': 'Media', 'Pres_24_25': 12, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.7, 'FM_24_25': 5.7},
        {'Nome': 'Nikola Moro', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 55, 'Quotazione': 12, 'Status': 'Rotazione', 'Convenienza': 'Bassa', 'Pres_24_25': 18, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.85, 'FM_24_25': 5.9},
        {'Nome': 'Jens Odgaard', 'Squadra': 'Bologna', 'Ruolo': 'Centrocampista', 'Titolarita_%': 60, 'Quotazione': 22, 'Status': 'Jolly Offensivo', 'Convenienza': 'Media', 'Pres_24_25': 24, 'Gol_24_25': 3, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.25},
        {'Nome': 'Orji Okwonkwo', 'Squadra': 'Bologna', 'Ruolo': 'Attaccante', 'Titolarita_%': 10, 'Quotazione': 1, 'Status': 'Marginale', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Massimo Pessina', 'Squadra': 'Bologna', 'Ruolo': 'Portiere', 'Titolarita_%': 5, 'Quotazione': 1, 'Status': 'Terzo Portiere', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Antonio Raimondo', 'Squadra': 'Bologna', 'Ruolo': 'Attaccante', 'Titolarita_%': 25, 'Quotazione': 8, 'Status': 'Giovane Promessa', 'Convenienza': 'Bassa', 'Pres_24_25': 2, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.5, 'FM_24_25': 5.5},
        {'Nome': 'Federico Ravaglia', 'Squadra': 'Bologna', 'Ruolo': 'Portiere', 'Titolarita_%': 15, 'Quotazione': 5, 'Status': 'Secondo Portiere', 'Convenienza': 'Bassa', 'Pres_24_25': 3, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 6.0, 'FM_24_25': 4.5},
        {'Nome': 'Lorenzo De Silvestri', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 30, 'Quotazione': 6, 'Status': 'Esperienza / Riserva', 'Convenienza': 'Bassa', 'Pres_24_25': 13, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.8, 'FM_24_25': 5.9},
        {'Nome': 'Nadir Zortea', 'Squadra': 'Bologna', 'Ruolo': 'Difensore', 'Titolarita_%': 50, 'Quotazione': 12, 'Status': 'Rotazione Fascia', 'Convenienza': 'Media', 'Pres_24_25': 32, 'Gol_24_25': 2, 'Assist_24_25': 3, 'MV_24_25': 5.95, 'FM_24_25': 6.25},
        {'Nome': 'Demi Akarakiri', 'Squadra': 'Cagliari', 'Ruolo': 'Centrocampista', 'Titolarita_%': 10, 'Quotazione': 1, 'Status': 'Giovane', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Agustín Albarracín', 'Squadra': 'Cagliari', 'Ruolo': 'Attaccante', 'Titolarita_%': 20, 'Quotazione': 5, 'Status': 'Scommessa', 'Convenienza': 'Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Gennaro Borrelli', 'Squadra': 'Cagliari', 'Ruolo': 'Attaccante', 'Titolarita_%': 50, 'Quotazione': 16, 'Status': 'Alternativa Attacco', 'Convenienza': 'Media', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Giuseppe Ciocci', 'Squadra': 'Cagliari', 'Ruolo': 'Portiere', 'Titolarita_%': 5, 'Quotazione': 1, 'Status': 'Terzo Portiere', 'Convenienza': 'Molto Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Alessandro Deiola', 'Squadra': 'Cagliari', 'Ruolo': 'Centrocampista', 'Titolarita_%': 60, 'Quotazione': 12, 'Status': 'Rotazione', 'Convenienza': 'Bassa', 'Pres_24_25': 28, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.75, 'FM_24_25': 5.85},
        {'Nome': 'Mattia Felici', 'Squadra': 'Cagliari', 'Ruolo': 'Attaccante', 'Titolarita_%': 45, 'Quotazione': 12, 'Status': 'Scommessa Fascia', 'Convenienza': 'Bassa', 'Pres_24_25': 20, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.8, 'FM_24_25': 5.85},
        {'Nome': 'Adam Obert', 'Squadra': 'Cagliari', 'Ruolo': 'Difensore', 'Titolarita_%': 50, 'Quotazione': 8, 'Status': 'Riserva', 'Convenienza': 'Bassa', 'Pres_24_25': 20, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.7, 'FM_24_25': 5.7},
        {'Nome': 'Matteo Prati', 'Squadra': 'Cagliari', 'Ruolo': 'Centrocampista', 'Titolarita_%': 75, 'Quotazione': 16, 'Status': 'Regista / Giovane', 'Convenienza': 'Media', 'Pres_24_25': 25, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.85, 'FM_24_25': 5.9},
        {'Nome': 'Boris Radunovic', 'Squadra': 'Cagliari', 'Ruolo': 'Portiere', 'Titolarita_%': 15, 'Quotazione': 4, 'Status': 'Secondo Portiere', 'Convenienza': 'Bassa', 'Pres_24_25': 4, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.9, 'FM_24_25': 4.4},
        {'Nome': 'Mateusz Wieteska', 'Squadra': 'Cagliari', 'Ruolo': 'Difensore', 'Titolarita_%': 45, 'Quotazione': 10, 'Status': 'Rotazione Difesa', 'Convenienza': 'Bassa', 'Pres_24_25': 16, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.8, 'FM_24_25': 5.8},
        {'Nome': 'Jayden Addai', 'Squadra': 'Como', 'Ruolo': 'Attaccante', 'Titolarita_%': 35, 'Quotazione': 10, 'Status': 'Giovane Scommessa', 'Convenienza': 'Bassa', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Iván Azón', 'Squadra': 'Como', 'Ruolo': 'Attaccante', 'Titolarita_%': 40, 'Quotazione': 12, 'Status': 'Rotazione', 'Convenienza': 'Bassa', 'Pres_24_25': 11, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.6, 'FM_24_25': 5.6},
        {'Nome': 'Ignace Van Der Brempt', 'Squadra': 'Como', 'Ruolo': 'Difensore', 'Titolarita_%': 75, 'Quotazione': 18, 'Status': 'Titolare Fascia', 'Convenienza': 'Alta', 'Pres_24_25': 22, 'Gol_24_25': 0, 'Assist_24_25': 2, 'MV_24_25': 5.9, 'FM_24_25': 6.0},
        {'Nome': 'Alessandro Gabrielloni', 'Squadra': 'Como', 'Ruolo': 'Attaccante', 'Titolarita_%': 40, 'Quotazione': 10, 'Status': 'Uomo Spogliatoio', 'Convenienza': 'Bassa', 'Pres_24_25': 10, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.6, 'FM_24_25': 5.6},
        {'Nome': 'Edoardo Goldaniga', 'Squadra': 'Como', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 12, 'Status': 'Titolare Esperto', 'Convenienza': 'Media', 'Pres_24_25': 27, 'Gol_24_25': 1, 'Assist_24_25': 0, 'MV_24_25': 5.85, 'FM_24_25': 5.95},
        {'Nome': 'Marc Oliver Kempf', 'Squadra': 'Como', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 16, 'Status': 'Titolare Difesa', 'Convenienza': 'Alta', 'Pres_24_25': 29, 'Gol_24_25': 1, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.05},
        {'Nome': 'Nicolas Kühn', 'Squadra': 'Como', 'Ruolo': 'Attaccante', 'Titolarita_%': 70, 'Quotazione': 24, 'Status': 'Esterno Rapido', 'Convenienza': 'Media', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Luca Mazzitelli', 'Squadra': 'Como', 'Ruolo': 'Centrocampista', 'Titolarita_%': 80, 'Quotazione': 24, 'Status': 'Titolare / Inserimenti', 'Convenienza': 'Alta', 'Pres_24_25': 23, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 5.95, 'FM_24_25': 6.15},
        {'Nome': 'Luis Milla', 'Squadra': 'Como', 'Ruolo': 'Centrocampista', 'Titolarita_%': 85, 'Quotazione': 26, 'Status': 'Regista di Classe', 'Convenienza': 'Alta', 'Pres_24_25': 0, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 0.0, 'FM_24_25': 0.0},
        {'Nome': 'Alieu Fadera', 'Squadra': 'Como', 'Ruolo': 'Attaccante', 'Titolarita_%': 65, 'Quotazione': 18, 'Status': 'Rotazione Attacco', 'Convenienza': 'Media', 'Pres_24_25': 28, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 5.85, 'FM_24_25': 6.0},
        {'Nome': 'Stefan Posch', 'Squadra': 'Como', 'Ruolo': 'Difensore', 'Titolarita_%': 80, 'Quotazione': 22, 'Status': 'Titolare / Bonus', 'Convenienza': 'Alta', 'Pres_24_25': 23, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.85, 'FM_24_25': 5.9},
        {'Nome': 'Álex Valle', 'Squadra': 'Como', 'Ruolo': 'Difensore', 'Titolarita_%': 70, 'Quotazione': 18, 'Status': 'Terzino Spinta', 'Convenienza': 'Media', 'Pres_24_25': 15, 'Gol_24_25': 0, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.0},
        {'Nome': 'Marco Brescianini', 'Squadra': 'Fiorentina', 'Ruolo': 'Centrocampista', 'Titolarita_%': 75, 'Quotazione': 28, 'Status': 'Incursore da Gol', 'Convenienza': 'Alta', 'Pres_24_25': 32, 'Gol_24_25': 4, 'Assist_24_25': 1, 'MV_24_25': 6.0, 'FM_24_25': 6.45},
        {'Nome': 'Giovanni Fabbian', 'Squadra': 'Fiorentina', 'Ruolo': 'Centrocampista', 'Titolarita_%': 75, 'Quotazione': 32, 'Status': 'Incursore Pericoloso', 'Convenienza': 'Alta', 'Pres_24_25': 29, 'Gol_24_25': 3, 'Assist_24_25': 1, 'MV_24_25': 6.0, 'FM_24_25': 6.35},
        {'Nome': 'Rolando Mandragora', 'Squadra': 'Fiorentina', 'Ruolo': 'Centrocampista', 'Titolarita_%': 70, 'Quotazione': 18, 'Status': 'Tiro da Fuori', 'Convenienza': 'Media', 'Pres_24_25': 21, 'Gol_24_25': 1, 'Assist_24_25': 0, 'MV_24_25': 5.85, 'FM_24_25': 6.0},
        {'Nome': 'Roberto Piccoli', 'Squadra': 'Fiorentina', 'Ruolo': 'Attaccante', 'Titolarita_%': 60, 'Quotazione': 24, 'Status': 'Vice Kean / Gol', 'Convenienza': 'Media', 'Pres_24_25': 32, 'Gol_24_25': 6, 'Assist_24_25': 1, 'MV_24_25': 5.9, 'FM_24_25': 6.4},
        {'Nome': 'Marin Pongracic', 'Squadra': 'Fiorentina', 'Ruolo': 'Difensore', 'Titolarita_%': 75, 'Quotazione': 16, 'Status': 'Titolare Difesa', 'Convenienza': 'Media', 'Pres_24_25': 18, 'Gol_24_25': 0, 'Assist_24_25': 0, 'MV_24_25': 5.8, 'FM_24_25': 5.8},
        {'Nome': 'Simon Sohm', 'Squadra': 'Fiorentina', 'Ruolo': 'Centrocampista', 'Titolarita_%': 60, 'Quotazione': 15, 'Status': 'Rotazione Fisica', 'Convenienza': 'Media', 'Pres_24_25': 29, 'Gol_24_25': 1, 'Assist_24_25': 2, 'MV_24_25': 5.9, 'FM_24_25': 6.1},
    
    ]
    return pd.DataFrame(giocatori)

df = load_data()

# --- SIDEBAR CONFIGURAZIONE BUDGET (1500 CREDITI) ---
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
tab1, tab2, tab3 = st.tabs(["🔍 Cerca Giocatore & Scheda Asta", "📋 Listone Completo", "📊 Stats 24/25"])

with tab1:
    st.subheader("🔎 Cerca un Giocatore nel Database")
    search_input = st.text_input("✍ Scrivi il nome del giocatore (es. Lautaro, De Bruyne, Berardi):", "")
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
        col2.metric("Titolarità", f"{player['Titolarita_%']}%")
        col3.metric("SPESA MAX", f"{player['Spesa_Max_Consigliata_(cr)']} cr")
        col4.metric("Convenienza", player["Convenienza"])
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("Presenze 24/25", player.get("Pres_24_25", 0))
        c2.metric("Gol 24/25", player.get("Gol_24_25", 0))
        c3.metric("Assist 24/25", player.get("Assist_24_25", 0))
        c1.metric("Media Voto 24/25", player.get("MV_24_25", 0))
        c2.metric("FantaMedia 24/25", player.get("FM_24_25", 0))
        c3.metric("Quotazione", player["Quotazione"])
        st.info(f"**Status:** {player['Status']}")
    else:
        st.warning("⚠ Nessun giocatore trovato!")

with tab2:
    st.subheader(f"📋 Database Completo ({len(df)} Giocatori)")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        filtro_ruolo = st.multiselect("Ruolo:", options=df["Ruolo"].unique(), default=df["Ruolo"].unique())
    with col_f2:
        filtro_squadra = st.multiselect("Squadra:", options=sorted(df["Squadra"].unique()), default=sorted(df["Squadra"].unique()))
    with col_f3:
        filtro_conv = st.multiselect("Convenienza:", options=df["Convenienza"].unique(), default=df["Convenienza"].unique())
    df_filtered = df[(df["Ruolo"].isin(filtro_ruolo)) & (df["Squadra"].isin(filtro_squadra)) & (df["Convenienza"].isin(filtro_conv))]
    st.dataframe(df_filtered[["Nome", "Squadra", "Ruolo", "Titolarita_%", "Spesa_Max_Consigliata_(cr)", "Convenienza", "Status"]], use_container_width=True, hide_index=True)

with tab3:
    st.subheader("📊 Statistiche Stagione 2024/25")
    st.dataframe(df[["Nome","Squadra","Ruolo","Pres_24_25","Gol_24_25","Assist_24_25","MV_24_25","FM_24_25"]].sort_values("FM_24_25", ascending=False), use_container_width=True, hide_index=True)

