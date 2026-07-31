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
        {"Nome": "Honest Ahanor", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Mitchel Bakker", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 8, "Status": "Scommessa / Alternativa", "Convenienza": "Bassa"},
        {"Nome": "Raoul Bellanova", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 35, "Status": "Titolare / Spinta", "Convenienza": "Altissima"},
        {"Nome": "Lorenzo Bernasconi", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Riserva Giovanile", "Convenienza": "Molto Bassa"},
        {"Nome": "Giovanni Bonfanti", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 4, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Marco Carnesecchi", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 25, "Status": "Consigliato - Titolare", "Convenienza": "Alta"},
        {"Nome": "Berat Djimsiti", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 20, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Gianluca Gaetano", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 20, "Status": "Rotazione / Qualità", "Convenienza": "Media"},
        {"Nome": "Isak Hien", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 22, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Charles De Ketelaere", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 50, "Status": "Top Slot / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Sead Kolasinac", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 24, "Status": "Titolare Esperto", "Convenienza": "Alta"},
        {"Nome": "Odilon Kossounou", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 22, "Status": "Rinforzo Difesa", "Convenienza": "Alta"},
        {"Nome": "Nikola Krstovic", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 35, "Status": "Rotazione Offensiva", "Convenienza": "Media"},
        {"Nome": "Daniel Maldini", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 18, "Status": "Talento / Jolly", "Convenienza": "Media"},
        {"Nome": "Mario Pasalic", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 35, "Status": "Incursore / Gol", "Convenienza": "Alta"},
        {"Nome": "Giacomo Raspadori", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 40, "Status": "Jolly / Bonus", "Convenienza": "Alta"},
        {"Nome": "Marten De Roon", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 22, "Status": "Titolare / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Francesco Rossi", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Lazar Samardzic", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 45, "Status": "Qualità / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Giorgio Scalvini", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 30, "Status": "Top Difesa / Giovane Prospetto", "Convenienza": "Alta"},
        {"Nome": "Gianluca Scamacca", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 75, "Status": "Bomber Titolare", "Convenienza": "Altissima"},
        {"Nome": "éderson Silva", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 32, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Marco Sportiello", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 5, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Ibrahim Sulemana", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Kamaldeen Sulemana", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 20, "Status": "Scommessa Esterna", "Convenienza": "Media"},
        {"Nome": "El Bilal Touré", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 20, "Status": "Scommessa / Alternativa", "Convenienza": "Media"},
        {"Nome": "Nicola Zalewski", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 20, "Status": "Jolly Fascia", "Convenienza": "Media"},
        {"Nome": "Davide Zappacosta", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 22, "Status": "Titolare / Spinta", "Convenienza": "Alta"},

        # --- BOLOGNA ---
        {"Nome": "Michel Aebischer", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 18, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Rahim Alhassane", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 5, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Mikel Amondarain", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Oussama El Azzouzi", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 8, "Status": "Riserva / Rotazione", "Convenienza": "Media"},
        {"Nome": "Federico Bernardeschi", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 35, "Status": "Esperienza / Qualità", "Convenienza": "Alta"},
        {"Nome": "Nicolò Cambiaghi", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 30, "Status": "Titolare / Dribbling", "Convenienza": "Alta"},
        {"Nome": "Nicolò Casale", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 20, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Santiago Castro", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 25, "Status": "Attaccante in Crescita", "Convenienza": "Alta"},
        {"Nome": "Thijs Dallinga", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 45, "Status": "Centravanti Titolare", "Convenienza": "Alta"},
        {"Nome": "Benja Domínguez", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 14, "Status": "Scommessa Esterna", "Convenienza": "Media"},
        {"Nome": "Lewis Ferguson", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 55, "Status": "Top / Incursore", "Convenienza": "Altissima"},
        {"Nome": "Remo Freuler", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 22, "Status": "Titolare / Costanza", "Convenienza": "Alta"},
        {"Nome": "Torbjørn Heggem", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Eivind Helland", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Emil Holm", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 18, "Status": "Alternativa Fascia", "Convenienza": "Media"},
        {"Nome": "Mihajlo Ilic", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Jesper Karlsson", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 20, "Status": "Scommessa", "Convenienza": "Media"},
        {"Nome": "Jhon Lucumí", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Juan Miranda", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 22, "Status": "Titolare Fascia", "Convenienza": "Alta"},
        {"Nome": "Nikola Moro", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Jens Odgaard", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 22, "Status": "Jolly Offensivo", "Convenienza": "Media"},
        {"Nome": "Orji Okwonkwo", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Marginale", "Convenienza": "Molto Bassa"},
        {"Nome": "Riccardo Orsolini", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 58, "Status": "Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Massimo Pessina", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Tommaso Pobega", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 22, "Status": "Incursore Fisico", "Convenienza": "Alta"},
        {"Nome": "Antonio Raimondo", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 25, "Quotazione": 8, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Federico Ravaglia", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 5, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Jonathan Rowe", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 25, "Status": "Esterno Offensivo", "Convenienza": "Media"},
        {"Nome": "Lorenzo De Silvestri", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 6, "Status": "Esperienza / Riserva", "Convenienza": "Bassa"},
        {"Nome": "Lukasz Skorupski", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 32, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Martin Vitík", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 20, "Status": "Rinforzo Difensivo", "Convenienza": "Alta"},
        {"Nome": "Nadir Zortea", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Rotazione Fascia", "Convenienza": "Media"},

        # --- CAGLIARI ---
        {"Nome": "Michel Adopo", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 14, "Status": "Titolare / Quantità", "Convenienza": "Media"},
        {"Nome": "Demi Akarakiri", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Agustín Albarracín", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 5, "Status": "Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Gennaro Borrelli", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 16, "Status": "Alternativa Attacco", "Convenienza": "Media"},
        {"Nome": "Elia Caprile", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 28, "Status": "Titolare / Ottimo Potenziale", "Convenienza": "Alta"},
        {"Nome": "Nicolò Cavuoti", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Giuseppe Ciocci", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Alessandro Deiola", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Sebastiano Esposito", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 25, "Status": "Titolare / Qualità", "Convenienza": "Alta"},
        {"Nome": "Jacopo Fazzini", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 24, "Status": "Trequartista / Incursore", "Convenienza": "Alta"},
        {"Nome": "Mattia Felici", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 12, "Status": "Scommessa Fascia", "Convenienza": "Bassa"},
        {"Nome": "Nicola Grandu", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Riyad Idrissi", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Velizar-iliya Iliev", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Joseph Liteta", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Paul Mendy", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Yerry Mina", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Titolare / Esperienza", "Convenienza": "Media"},
        {"Nome": "Kingstone Mutandwa", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Adam Obert", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Sebastiano Di Paolo", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Zé Pedro", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 6, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Matteo Prati", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 16, "Status": "Regista / Giovane", "Convenienza": "Media"},
        {"Nome": "Boris Radunovic", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 4, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Othniël Raterink", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Juan Rodríguez", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Alessandro Romano", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Alen Sherri", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 2, "Status": "Riserva", "Convenienza": "Molto Bassa"},
        {"Nome": "Ivan Sulev", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Yael Trepy", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mateusz Wieteska", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 10, "Status": "Rotazione Difesa", "Convenienza": "Bassa"},
        {"Nome": "Harry Winks", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 25, "Status": "Regista Titolare", "Convenienza": "Alta"},
        {"Nome": "Gabriele Zappa", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 16, "Status": "Titolare Fascia", "Convenienza": "Media"},

        # --- COMO ---
        {"Nome": "Jayden Addai", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 10, "Status": "Giovane Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Emil Audero", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 30, "Status": "Titolare Porta", "Convenienza": "Alta"},
        {"Nome": "Iván Azón", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Martin Baturina", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 35, "Status": "Talento Puro / Trequartista", "Convenienza": "Altissima"},
        {"Nome": "Andréa Le Borgne", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Riserva", "Convenienza": "Molto Bassa"},
        {"Nome": "Matthias Braunöder", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Ignace Van Der Brempt", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Titolare Fascia", "Convenienza": "Alta"},
        {"Nome": "Jean Butez", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 6, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Maxence Caqueret", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 32, "Status": "Regista di Spessore", "Convenienza": "Alta"},
        {"Nome": "Andrés Cuenca", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 8, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Lucas Da Cunha", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 20, "Status": "Esterno Offensivo", "Convenienza": "Media"},
        {"Nome": "Assane Diao", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 28, "Status": "Talento / Velocità", "Convenienza": "Alta"},
        {"Nome": "Alberto Dossena", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 20, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Tasos Douvikas", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 32, "Status": "Bomber Titolare", "Convenienza": "Alta"},
        {"Nome": "Alieu Fadera", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 18, "Status": "Rotazione Attacco", "Convenienza": "Media"},
        {"Nome": "Tommaso Fumagalli", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 30, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Alessandro Gabrielloni", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 10, "Status": "Uomo Spogliatoio / Riserva", "Convenienza": "Bassa"},
        {"Nome": "Edoardo Goldaniga", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 12, "Status": "Titolare Esperto", "Convenienza": "Media"},
        {"Nome": "Ali Jasim", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 12, "Status": "Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Kaiki", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Riserva", "Convenienza": "Molto Bassa"},
        {"Nome": "Marc Oliver Kempf", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 16, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Nicolas Kühn", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 24, "Status": "Esterno Rapido", "Convenienza": "Media"},
        {"Nome": "Adrian Lahdo", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Mattia Liberali", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 8, "Status": "Giovane Talento", "Convenienza": "Bassa"},
        {"Nome": "Luca Mazzitelli", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 24, "Status": "Titolare / Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Luis Milla", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 26, "Status": "Regista di Classe", "Convenienza": "Alta"},
        {"Nome": "Álvaro Morata", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 75, "Status": "Super Top / Stella Como", "Convenienza": "Altissima"},
        {"Nome": "Marlon Mustapha", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 30, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Nico Paz", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 45, "Status": "Top Slot / Qualità", "Convenienza": "Altissima"},
        {"Nome": "Máximo Perrone", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 20, "Status": "Titolare / Visione", "Convenienza": "Media"},
        {"Nome": "Stefan Posch", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 22, "Status": "Titolare / Bonus", "Convenienza": "Alta"},
        {"Nome": "Jacobo Ramón", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 10, "Status": "Giovane Difensore", "Convenienza": "Bassa"},
        {"Nome": "Fabio Rispoli", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Jesús Rodríguez", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 10, "Status": "Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Ivan Smolcic", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Noel Törnqvist", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 2, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "álex Valle", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 18, "Status": "Terzino Spinta", "Convenienza": "Media"},
        {"Nome": "Mauro Vigorito", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},

        # --- FIORENTINA ---
        {"Nome": "Arthur Atta", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 16, "Status": "Rotazione Dinamica", "Convenienza": "Media"},
        {"Nome": "Riccardo Braschi", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Marco Brescianini", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 28, "Status": "Incursore da Gol", "Convenienza": "Alta"},
        {"Nome": "Oliver Christensen", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 5, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Lapo Deli", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Dodô", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 24, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Radu Dragusin", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 28, "Status": "Muro Difensivo", "Convenienza": "Alta"},
        {"Nome": "Giovanni Fabbian", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 32, "Status": "Incursore Pericoloso", "Convenienza": "Alta"},
        {"Nome": "Nicolò Fagioli", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 28, "Status": "Regista di Qualità", "Convenienza": "Alta"},
        {"Nome": "Niccolò Fortini", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "David De Gea", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 48, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Albert Gudmundsson", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 75, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "álex Jiménez", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 16, "Status": "Giovane Fascia", "Convenienza": "Media"},
        {"Nome": "Moise Kean", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 65, "Status": "Bomber Titolare", "Convenienza": "Altissima"},
        {"Nome": "Eman Kospo", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Luca Lezzerini", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Rolando Mandragora", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 18, "Status": "Tiro da Fuori / Piazzati", "Convenienza": "Media"},
        {"Nome": "Matías Moreno", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Rotazione Difesa", "Convenienza": "Bassa"},
        {"Nome": "Cher Ndour", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 15, "Status": "Scommessa", "Convenienza": "Media"},
        {"Nome": "M'bala Nzola", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 18, "Status": "Alternativa Offensiva", "Convenienza": "Bassa"},
        {"Nome": "Christ Inao Oulaï", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Fabiano Parisi", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 14, "Status": "Alternativa Fascia", "Convenienza": "Media"},
        {"Nome": "Roberto Piccoli", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 24, "Status": "Vice Kean / Gol", "Convenienza": "Media"},
        {"Nome": "Marin Pongracic", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 16, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Luca Ranieri", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 22, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Abdelhamid Sabiri", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 35, "Quotazione": 12, "Status": "Incognita", "Convenienza": "Bassa"},
        {"Nome": "Simon Sohm", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 15, "Status": "Rotazione Fisica", "Convenienza": "Media"},
        {"Nome": "Riccardo Sottil", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 18, "Status": "Spunto / Alternativa", "Convenienza": "Media"},
        {"Nome": "Nicolás Valentini", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 16, "Status": "Rinforzo Solido", "Convenienza": "Media"},
        {"Nome": "Viery", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},

        # --- FROSINONE ---
        {"Nome": "Wisdom Amey", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 8, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Anouar El Azzouzi", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Kevin Barcella", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Gabriele Bracaglia", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Giacomo Calò", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 22, "Status": "Regista e Piazzati", "Convenienza": "Alta"},
        {"Nome": "Matteo Cichella", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Alejandro Cichero", "Squadra": "Frosinone", "Ruolo": "Attaccante", "Titolarita_%": 25, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Giorgio Cittadini", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 14, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Muhammed Colley", "Squadra": "Frosinone", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Niccolò Corrado", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 16, "Status": "Spinta a Sinistra", "Convenienza": "Media"},
        {"Nome": "Sebastiano Desplanches", "Squadra": "Frosinone", "Ruolo": "Portiere", "Titolarita_%": 80, "Quotazione": 20, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Jacopo Gelli", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 3, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Francesco Gelli", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 16, "Status": "Quantità e Inserimenti", "Convenienza": "Media"},
        {"Nome": "Farès Ghedjemis", "Squadra": "Frosinone", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 18, "Status": "Dribbling e Velocità", "Convenienza": "Media"},
        {"Nome": "Filippo Grosso", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Luis Hasa", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 20, "Status": "Talento / Assist", "Convenienza": "Alta"},
        {"Nome": "Sergio Kalaj", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 35, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Ben Kone", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ilias Koutsoupias", "Squadra": "Frosinone", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 15, "Status": "Titolare Centrocampo", "Convenienza": "Media"},
        {"Nome": "Giorgi Kvernadze", "Squadra": "Frosinone", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva Offensiva", "Convenienza": "Bassa"},
        {"Nome": "Eldin Lolic", "Squadra": "Frosinone", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Edoardo Masciangelo", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ilario Monterisi", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Titolare / Jolly", "Convenienza": "Alta"},
        {"Nome": "Anthony Oyono", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 15, "Status": "Terzino Titolare", "Convenienza": "Media"},
        {"Nome": "Jérémy Oyono", "Squadra": "Frosinone", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Lorenzo Palmisani", "Squadra": "Frosinone", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 3, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Matteo Pisseri", "Squadra": "Frosinone", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Edoardo Vergani", "Squadra": "Frosinone", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 10, "Status": "Riserva Attacco", "Convenienza": "Bassa"},
        {"Nome": "Alessio Zerbin", "Squadra": "Frosinone", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 24, "Status": "Esterno Titolare", "Convenienza": "Alta"},

        # --- GENOA ---
        {"Nome": "Alex Amorim", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Justin Bijlow", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 35, "Status": "Portiere Top", "Convenienza": "Altissima"},
        {"Nome": "Gabriele Calvani", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Lorenzo Colombo", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 30, "Status": "Titolare / Bomber", "Convenienza": "Alta"},
        {"Nome": "Hugo Cuenca", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 8, "Status": "Giovane Talento", "Convenienza": "Bassa"},
        {"Nome": "Alessandro Debenedetti", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mamedi Doucouré", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Chec Bebel Doumbia", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Caleb Ekuban", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 16, "Status": "Spaccapartite", "Convenienza": "Media"},
        {"Nome": "Mikael Ellertsson", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Seydou Fini", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Morten Frendrup", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 30, "Status": "Recupera-palloni / Voto Top", "Convenienza": "Altissima"},
        {"Nome": "Elias Havel", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Ernestas Lysionok", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Alessandro Marcandalli", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 14, "Status": "In Crescita", "Convenienza": "Media"},
        {"Nome": "Aarón Martín", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Titolare Fascia", "Convenienza": "Alta"},
        {"Nome": "Patrizio Masini", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Alan Matturro", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ethan Meichtry", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Junior Messias", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 32, "Status": "Qualità / Bonus", "Convenienza": "Alta"},
        {"Nome": "Brooke Norton-Cuffy", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 20, "Status": "Spinta e Fisico", "Convenienza": "Alta"},
        {"Nome": "Joi Nuredini", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Sebastian Otoa", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Wedtoin Ouedraogo", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "David Puczka", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Stefano Sabelli", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 15, "Status": "Affidabile / Titolare", "Convenienza": "Media"},
        {"Nome": "Daniele Sommariva", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Franz Stolz", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 2, "Status": "Secondo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Hamed Traoré", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 40, "Status": "Top Slot / Trequartista", "Convenienza": "Altissima"},
        {"Nome": "Marcelo Vaz", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Lorenzo Venturino", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Alessandro Vogliacco", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 15, "Status": "Titolare / Rotazione", "Convenienza": "Media"},
        {"Nome": "Johan Vásquez", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 24, "Status": "Leader Difensivo", "Convenienza": "Alta"},
        {"Nome": "Vítinha", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 35, "Status": "Titolare / Attacco", "Convenienza": "Alta"},
        {"Nome": "Samuel Wiafe", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Leo østigård", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 20, "Status": "Titolare / Goleador", "Convenienza": "Alta"},

        # --- INTER ---
        {"Nome": "Manuel Akanji", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 45, "Status": "Top Difesa", "Convenienza": "Altissima"},
        {"Nome": "Ebenezer Akinsanmiro", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Kristjan Asllani", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 12, "Status": "Vice Regia", "Convenienza": "Bassa"},
        {"Nome": "Carlos Augusto", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 28, "Status": "Jolly di Qualità", "Convenienza": "Alta"},
        {"Nome": "Nicolò Barella", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 58, "Status": "Top Centrocampo", "Convenienza": "Altissima"},
        {"Nome": "Alessandro Bastoni", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 48, "Status": "Top Difesa", "Convenienza": "Altissima"},
        {"Nome": "Yann Bisseck", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 18, "Status": "In Crescita", "Convenienza": "Media"},
        {"Nome": "Ange-Yoan Bonny", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 28, "Status": "Rinforzo Attacco", "Convenienza": "Media"},
        {"Nome": "Leonardo Bovio", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Federico Dimarco", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 70, "Status": "Super Top Difesa / Assist", "Convenienza": "Altissima"},
        {"Nome": "Andy Diouf", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 22, "Status": "Dinamismo", "Convenienza": "Media"},
        {"Nome": "Francesco Pio Esposito", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 16, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "Matteo Farronato", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Davide Frattesi", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 50, "Status": "Incursore Spietato da Gol", "Convenienza": "Altissima"},
        {"Nome": "Raffaele Di Gennaro", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Luis Henrique", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 22, "Status": "Esterno Spinta", "Convenienza": "Media"},
        {"Nome": "Jamal Iddrissou", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Matteo Lavelli", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mattia Marello", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Josep Martínez", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 25, "Quotazione": 12, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Lautaro Martínez", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 135, "Status": "📌 TOP RE ASSOLUTO ASTA", "Convenienza": "Altissima"},
        {"Nome": "Yanis Massolin", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Yvan Maye", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Henrikh Mkhitaryan", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 42, "Status": "Titolare / Quantità e Qualità", "Convenienza": "Alta"},
        {"Nome": "Mattia Mosconi", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Benjamin Pavard", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 40, "Status": "Titolare Top", "Convenienza": "Alta"},
        {"Nome": "Ivan Provedel", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 45, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Aleksandar Stankovic", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Petar Sucic", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 22, "Status": "Interessante Novità", "Convenienza": "Media"},
        {"Nome": "Marcus Thuram", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 100, "Status": "Super Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Luka Topalovic", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 6, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Piotr Zielinski", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 38, "Status": "Qualità / Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Hakan Çalhanoglu", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 85, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},

        # --- JUVENTUS ---
        {"Nome": "Shane Van Aarle", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Vasilije Adzic", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 14, "Status": "Talento / Scommessa", "Convenienza": "Media"},
        {"Nome": "Arthur", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Jérémie Boga", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 35, "Status": "Dribbling e Bonus", "Convenienza": "Alta"},
        {"Nome": "Bremer", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 55, "Status": "Muro Inamovibile", "Convenienza": "Altissima"},
        {"Nome": "Juan Cabal", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 18, "Status": "Rotazione Difesa", "Convenienza": "Media"},
        {"Nome": "Andrea Cambiaso", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 42, "Status": "Titolare / Assist", "Convenienza": "Altissima"},
        {"Nome": "Francisco Conceição", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 45, "Status": "Spaccapartite / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Jonathan David", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 90, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Arman Durmisi", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Jeff Ekhator", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 25, "Quotazione": 6, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Destiny Elimoghale", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Federico Gatti", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 30, "Status": "Titolare / Gol di Testa", "Convenienza": "Alta"},
        {"Nome": "Javier Gil", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Nico González", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 65, "Status": "Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Michele Di Gregorio", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 45, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Pierre Kalulu", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 26, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Lloyd Kelly", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 22, "Status": "Rinforzo Solido", "Convenienza": "Alta"},
        {"Nome": "Teun Koopmeiners", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 75, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Filip Kostic", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 18, "Status": "Cross e Assist", "Convenienza": "Media"},
        {"Nome": "Adin Licina", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Manuel Locatelli", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 28, "Status": "Regista Titolare", "Convenienza": "Alta"},
        {"Nome": "Douglas Luiz", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 55, "Status": "Top Centrocampo / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Weston Mckennie", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 32, "Status": "Jolly / Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Arkadiusz Milik", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 20, "Status": "Vice Vlahovic", "Convenienza": "Media"},
        {"Nome": "Fabio Miretti", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "João Mário", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Justin Oboavwoduo", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Augusto Owusu", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mattia Perin", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 8, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Carlo Pinsoglio", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Jonas Rouhi", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 35, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Daniele Rugani", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Khéphren Thuram", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 42, "Status": "Top / Fisicità e Dribbling", "Convenienza": "Altissima"},
        {"Nome": "Dusan Vlahovic", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 120, "Status": "Super Top Bomber / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Kenan Yildiz", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 45, "Status": "Talento Puro / Scommessa Top", "Convenienza": "Altissima"},
        {"Nome": "Edon Zhegrova", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 38, "Status": "Esterno Fantasia", "Convenienza": "Alta"},
        {"Nome": "Zeki Çelik", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},

        # --- LAZIO ---
        {"Nome": "Gabriele Artistico", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 3, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Reda Belahyane", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 22, "Status": "Quantità e Titolare", "Convenienza": "Alta"},
        {"Nome": "Filipe Bordon", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Matteo Cancellieri", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 16, "Status": "Jolly d'Attacco", "Convenienza": "Media"},
        {"Nome": "Danilo Cataldi", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Fisayo Dele-Bashiru", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 24, "Status": "Incursore Fisico", "Convenienza": "Media"},
        {"Nome": "Boulaye Dia", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 65, "Status": "Top Slot / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Danilho Doekhi", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 22, "Status": "Titolare / Goleador di Testa", "Convenienza": "Alta"},
        {"Nome": "Alessio Furlanetto", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Bruno Galassi", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Samuel Gigot", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Gustav Isaksen", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 22, "Status": "Spunto / Ala", "Convenienza": "Media"},
        {"Nome": "Manuel Lazzari", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 16, "Status": "Spinta sulla Fascia", "Convenienza": "Media"},
        {"Nome": "Christos Mandas", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 8, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Adam Marusic", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Titolare Multi-ruolo", "Convenienza": "Alta"},
        {"Nome": "Edoardo Motta", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Romano Floriani Mussolini", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Tijjani Noslin", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 30, "Status": "Velocità e Gol", "Convenienza": "Alta"},
        {"Nome": "Patric", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 12, "Status": "Rotazione Centrali", "Convenienza": "Media"},
        {"Nome": "Alfonso Pedraza", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 20, "Status": "Spinta a Sinistra", "Convenienza": "Alta"},
        {"Nome": "Luca Pellegrini", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Oliver Provstgaard", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 10, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Adrian Przyborek", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 6, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Petar Ratkov", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 26, "Status": "Centravanti / Gol", "Convenienza": "Media"},
        {"Nome": "Davide Renzetti", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Alessio Romagnoli", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 28, "Status": "Leader Difensivo", "Convenienza": "Alta"},
        {"Nome": "Nicolò Rovella", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 22, "Status": "Regista Titolare", "Convenienza": "Alta"},
        {"Nome": "Nuno Tavares", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 32, "Status": "Treno sulla Fascia / Assist", "Convenienza": "Altissima"},
        {"Nome": "Kenneth Taylor", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 30, "Status": "Qualità e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Mattia Zaccagni", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 72, "Status": "Top Slot / Rigorista", "Convenienza": "Altissima"},

        # --- LECCE ---
        {"Nome": "Vernon Addo", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Lameck Banda", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 24, "Status": "Velocità / Dribbling", "Convenienza": "Alta"},
        {"Nome": "Medon Berisha", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 12, "Status": "In Crescita", "Convenienza": "Media"},
        {"Nome": "Alexandru Borbei", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Rares Burnete", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 30, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Lassana Coulibaly", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare / Quantità", "Convenienza": "Alta"},
        {"Nome": "Sebastian Esposito", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 25, "Status": "Titolare / Qualità", "Convenienza": "Alta"},
        {"Nome": "Wladimiro Falcone", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 35, "Status": "Saracinesca Titolare", "Convenienza": "Altissima"},
        {"Nome": "Sadik Fofana", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Christian Früchtl", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 3, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Tiago Gabriel", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Antonino Gallo", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 20, "Status": "Titolare / Assist", "Convenienza": "Alta"},
        {"Nome": "Omri Gandelman", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 16, "Status": "Inserimenti / Gol", "Convenienza": "Media"},
        {"Nome": "Kialonda Gaspar", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Olaf Gorter", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Gaby Jean", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Milos Jovic", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Mohamed Kaba", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 14, "Status": "In Recupero", "Convenienza": "Media"},
        {"Nome": "Owen Kouassi", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Niko Kovac", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Youssef Maleh", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Corrie Ndaba", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Oumar Ngom", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Konan N’dri", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Santiago Pierotti", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 18, "Status": "Lotta / Sponda", "Convenienza": "Media"},
        {"Nome": "Matías Pérez", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Jasper Samooja", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Jamil Siebert", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 16, "Status": "Titolare / Roccia", "Convenienza": "Media"},
        {"Nome": "Nikola Stulic", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 22, "Status": "Centravanti", "Convenienza": "Media"},
        {"Nome": "Danilo Veiga", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},

        # --- MILAN ---
        {"Nome": "Zachary Athekame", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 12, "Status": "Riserva Fascia", "Convenienza": "Bassa"},
        {"Nome": "Davide Bartesaghi", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 35, "Quotazione": 10, "Status": "Giovane / Riserva", "Convenienza": "Bassa"},
        {"Nome": "Ismaël Bennacer", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 26, "Status": "Regista", "Convenienza": "Media"},
        {"Nome": "Warren Bondo", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 20, "Status": "Dinamismo e Quantità", "Convenienza": "Media"},
        {"Nome": "Emanuele Borsani", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Léo-paul Bouyer", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Francesco Camarda", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 20, "Status": "Talento Puro / Scommessa", "Convenienza": "Alta"},
        {"Nome": "Samuel Chukwueze", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 28, "Status": "Spunto da Panchina", "Convenienza": "Media"},
        {"Nome": "Alphadjo Cissè", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Christian Comotto", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Sankhoun Diawara", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Pervis Estupiñán", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 35, "Status": "Titolare / Assist a Sinistra", "Convenienza": "Altissima"},
        {"Nome": "Youssouf Fofana", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 38, "Status": "Diga Titolare / Voto Alto", "Convenienza": "Altissima"},
        {"Nome": "Matteo Gabbia", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 22, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Mario Gila", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 20, "Status": "Rinforzo Difensivo", "Convenienza": "Alta"},
        {"Nome": "Santiago Giménez", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 110, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Aurelien Guernier", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Ardon Jashari", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 26, "Status": "Regia e Sostanza", "Convenienza": "Alta"},
        {"Nome": "Andrej Kostic", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Rafael Leão", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 115, "Status": "Super Top Attacco", "Convenienza": "Altissima"},
        {"Nome": "Ruben Loftus-Cheek", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 48, "Status": "Incursore / Fisico", "Convenienza": "Altissima"},
        {"Nome": "Mike Maignan", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 52, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Luka Modric", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 55, "Status": "Leggenda / Super Classe", "Convenienza": "Altissima"},
        {"Nome": "Yunus Musah", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 18, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Christopher Nkunku", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 95, "Status": "Super Top / Fantasia e Gol", "Convenienza": "Altissima"},
        {"Nome": "David Odogu", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Lorenzo Ossola", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Strahinja Pavlovic", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 28, "Status": "Titolare / Grinta", "Convenienza": "Alta"},
        {"Nome": "Matteo Pittarella", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Christian Pulisic", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 85, "Status": "Super Top Centrocampo / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Adrien Rabiot", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 65, "Status": "Top Centrocampo / Gol", "Convenienza": "Altissima"},
        {"Nome": "Gonçalo Ramos", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 80, "Status": "Top Attacco / Bomber", "Convenienza": "Altissima"},
        {"Nome": "Samuele Ricci", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 32, "Status": "Regista Affidabile", "Convenienza": "Alta"},
        {"Nome": "Alexis Saelemaekers", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 25, "Status": "Jolly Tattico", "Convenienza": "Alta"},
        {"Nome": "Jacopo Sardo", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Pietro Terracciano", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 4, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Filippo Terracciano", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Jolly Difesa", "Convenienza": "Bassa"},
        {"Nome": "Fikayo Tomori", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 35, "Status": "Titolare Top", "Convenienza": "Alta"},
        {"Nome": "Lorenzo Torriani", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Valeri Vladimirov", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Silvano Vos", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 12, "Status": "Giovane Interessante", "Convenienza": "Bassa"},
        {"Nome": "Koni De Winter", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 22, "Status": "Rotazione Difesa", "Convenienza": "Alta"},
        {"Nome": "Kevin Zeroli", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 12, "Status": "Giovane Promessa", "Convenienza": "Bassa"},

        # --- MONZA ---
        {"Nome": "Valentin Antov", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Adam Bakoune", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Keita Baldé", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 20, "Status": "Esperienza / Gol", "Convenienza": "Media"},
        {"Nome": "Nicolò Ballabio", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Samuele Birindelli", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 14, "Status": "Spinta Fascia", "Convenienza": "Media"},
        {"Nome": "Arvid Brorsson", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Andrea Carboni", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 15, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Filippo Delli Carri", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 30, "Quotazione": 6, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Patrick Ciurria", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 24, "Status": "Jolly / Assist", "Convenienza": "Alta"},
        {"Nome": "Leonardo Colombo", "Squadra": "Monza", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Lorenzo Colonnese", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Andrea Colpani", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 55, "Status": "Top Slot / Gol", "Convenienza": "Altissima"},
        {"Nome": "Patrick Cutrone", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 38, "Status": "Bomber Titolare", "Convenienza": "Alta"},
        {"Nome": "Omari Forson", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 16, "Status": "Talento / Scommessa", "Convenienza": "Media"},
        {"Nome": "Nicolas Galazzi", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Eddy Kouadio", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Solomon Loubao", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Lorenzo Lucchesi", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 14, "Status": "Difensore Solido", "Convenienza": "Media"},
        {"Nome": "Ricardo Mangas", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 16, "Status": "Spinta a Sinistra", "Convenienza": "Media"},
        {"Nome": "Kevin Martins", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Giuseppe Martone", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Dany Mota", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 26, "Status": "Titolare Attacco", "Convenienza": "Alta"},
        {"Nome": "Mathis Mout", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Manga Foe Ondoa", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Matteo Pessina", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 45, "Status": "Capitano / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Andrea Petagna", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 12, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Semuel Pizzignacco", "Squadra": "Monza", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 6, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Aljaz Strajnar", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Demba Thiam", "Squadra": "Monza", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 4, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Danilo Treffiletti", "Squadra": "Monza", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Gustavo Varela", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 30, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},

        # --- NAPOLI ---
        {"Nome": "Frank Anguissa", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 35, "Status": "Titolare / Fisico", "Convenienza": "Alta"},
        {"Nome": "Sam Beukema", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 28, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Kevin De Bruyne", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 110, "Status": "Super Top Assoluto / Assist", "Convenienza": "Altissima"},
        {"Nome": "Alessandro Buongiorno", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 48, "Status": "Muro Difensivo / Top Slot", "Convenienza": "Altissima"},
        {"Nome": "Jens Cajuste", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Emmanuele De Chiara", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Antonio Cioffi", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Nikita Contini", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 3, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Michael Folorunsho", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 22, "Status": "Incursore Potente", "Convenienza": "Media"},
        {"Nome": "Christian Garofalo", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Billy Gilmour", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 25, "Status": "Regia e Geometrie", "Convenienza": "Alta"},
        {"Nome": "Giovane", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 25, "Quotazione": 6, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Miguel Gutiérrez", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 35, "Status": "Spinta e Assist a Sinistra", "Convenienza": "Altissima"},
        {"Nome": "Rasmus Højlund", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 95, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Noa Lang", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 55, "Status": "Esterno Top / Dribbling e Gol", "Convenienza": "Altissima"},
        {"Nome": "Jesper Lindstrøm", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 18, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Stanislav Lobotka", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 32, "Status": "Metronomo / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Giovanni Di Lorenzo", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 48, "Status": "Top Difesa / Capitano", "Convenienza": "Altissima"},
        {"Nome": "Lorenzo Lucca", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 42, "Status": "Centravanti / Torre", "Convenienza": "Alta"},
        {"Nome": "Romelu Lukaku", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 115, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Luca Marianucci", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Rafa Marín", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 16, "Status": "Rotazione Difesa", "Convenienza": "Media"},
        {"Nome": "Pasquale Mazzocchi", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 15, "Status": "Jolly Fascia", "Convenienza": "Media"},
        {"Nome": "Scott Mctominay", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 65, "Status": "Top Centrocampo / Inserimenti Top", "Convenienza": "Altissima"},
        {"Nome": "Alex Meret", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 42, "Status": "Titolare Portiere", "Convenienza": "Alta"},
        {"Nome": "Vanja Milinkovic-Savic", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 10, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "David Neres", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 60, "Status": "Top Slot / Assist e Gol", "Convenienza": "Altissima"},
        {"Nome": "Cyril Ngonge", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 22, "Status": "Spacca-partite", "Convenienza": "Media"},
        {"Nome": "Nosa Obaretin", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mathías Olivera", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Titolare Fascia", "Convenienza": "Alta"},
        {"Nome": "Matteo Politano", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 45, "Status": "Titolare / Rigori / Bonus", "Convenienza": "Alta"},
        {"Nome": "Emanuele Rao", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Amir Rrahmani", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 26, "Status": "Titolare Centrali", "Convenienza": "Alta"},
        {"Nome": "Coli Saco", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Alisson Santos", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Leonardo Spinazzola", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 22, "Status": "Rotazione / Spinta", "Convenienza": "Media"},
        {"Nome": "Antonio Vergara", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 6, "Status": "Giovane", "Convenienza": "Bassa"},

        # --- PARMA ---
        {"Nome": "Pontus Almqvist", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 25, "Status": "Velocità e Assist", "Convenienza": "Alta"},
        {"Nome": "Peter Amoran", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Gianluca Astaldi", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Botond Balogh", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 14, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Adrián Bernabé", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 40, "Status": "🔥 Talento Top / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Sascha Britschgi", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Franco Carboni", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 12, "Status": "Rotazione Fascia", "Convenienza": "Bassa"},
        {"Nome": "Alessandro Cardinali", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Hans Nicolussi Caviglia", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 24, "Status": "Regia e Tiro dalla Distanza", "Convenienza": "Alta"},
        {"Nome": "Alessandro Circati", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 16, "Status": "Giovane Centrale Titolare", "Convenienza": "Alta"},
        {"Nome": "Edoardo Corvi", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 3, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Benjamín Cremaschi", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 20, "Status": "Talento / Inserimenti", "Convenienza": "Media"},
        {"Nome": "Roberto D'intino", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Giovanni Daffara", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Enrico Delprato", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 18, "Status": "Capitano / Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Dominik Drobnic", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Nesta Elphege", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Matija Frigan", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 28, "Status": "Attaccante / Gol", "Convenienza": "Media"},
        {"Nome": "Antoine Joujou", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 18, "Status": "Velocità e Spunto", "Convenienza": "Media"},
        {"Nome": "Mandela Keita", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 22, "Status": "Diga di Centrocampo", "Convenienza": "Alta"},
        {"Nome": "Abdou-salam Konate", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mateusz Kowalski", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 30, "Quotazione": 8, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Daniel Mikolajewski", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Abdoulaye Ndiaye", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 16, "Status": "Rinforzo Difensivo", "Convenienza": "Media"},
        {"Nome": "Jacob Ondrejka", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 20, "Status": "Esterno Offensivo", "Convenienza": "Media"},
        {"Nome": "Christian Ordóñez", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 16, "Status": "Interessante Novità", "Convenienza": "Media"},
        {"Nome": "Mateo Pellegrino", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 22, "Status": "Attaccante di Movimento", "Convenienza": "Media"},
        {"Nome": "Zion Suzuki", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 32, "Status": "Portiere Titolare Reattivo", "Convenienza": "Altissima"},
        {"Nome": "Oliver Sørensen", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 22, "Status": "Quantità e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Edoardo Tigani", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mariano Troilo", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Lautaro Valenti", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Emanuele Valeri", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 22, "Status": "Titolare / Spinta", "Convenienza": "Alta"},

        # --- ROMA ---
        {"Nome": "Angeliño", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 30, "Status": "Titolare / Assist a Sinistra", "Convenienza": "Altissima"},
        {"Nome": "Antonio Arena", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Neil El Aynaoui", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 24, "Status": "Dinamismo e Interdizione", "Convenienza": "Media"},
        {"Nome": "Muhammed Bah", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Tommaso Baldanzi", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 28, "Status": "Talento / Trequartista", "Convenienza": "Media"},
        {"Nome": "Luigi Cherubini", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Bryan Cristante", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 30, "Status": "Titolare Inamovibile", "Convenienza": "Alta"},
        {"Nome": "Artem Dovbyk", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 110, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Paulo Dybala", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 105, "Status": "Super Top / Classe Purissima", "Convenienza": "Altissima"},
        {"Nome": "Daniele Ghilardi", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 55, "Quotazione": 14, "Status": "Giovane / Rotazione", "Convenienza": "Media"},
        {"Nome": "Gioele Giammattei", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Pierluigi Gollini", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 6, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Mario Hermoso", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 28, "Status": "Titolare / Impostazione", "Convenienza": "Alta"},
        {"Nome": "Manu Koné", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 38, "Status": "Top Centrocampo / Fisico", "Convenienza": "Altissima"},
        {"Nome": "Emanuele Lulli", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Donyell Malen", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 60, "Status": "Top Slot / Velocità e Gol", "Convenienza": "Altissima"},
        {"Nome": "Gianluca Mancini", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 34, "Status": "Titolare / Bonus Testa", "Convenienza": "Alta"},
        {"Nome": "Mattia Mannini", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Giorgio De Marzi", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Jacopo Mirra", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Edoardo Morucci", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Federico Nardin", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Evan Ndicka", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 26, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Alessandro Di Nunzio", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Francesco Panico", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Lorenzo Pellegrini", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 58, "Status": "Top Slot / Piazzati", "Convenienza": "Altissima"},
        {"Nome": "Niccolò Pisilli", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 22, "Status": "Inserimenti / Gol Pesanti", "Convenienza": "Alta"},
        {"Nome": "Devyne Rensch", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 26, "Status": "Titolare / Spinta", "Convenienza": "Alta"},
        {"Nome": "Mattia Della Rocca", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Anass Salah-eddine", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 16, "Status": "Alternativa Fascia", "Convenienza": "Media"},
        {"Nome": "Mohamed Seck", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Matías Soulé", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 70, "Status": "Top Attacco / Fantasia", "Convenienza": "Altissima"},
        {"Nome": "Mile Svilar", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 48, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Robinio Vaz", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Devis Vásquez", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Wesley", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 24, "Status": "Terzino di Spinta", "Convenienza": "Alta"},
        {"Nome": "Radoslaw Zelezny", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Jan Ziólkowski", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},

        # --- SASSUOLO ---
        {"Nome": "Janis Antiste", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Darryl Bakola", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Luca Barani", "Squadra": "Sassuolo", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Domenico Berardi", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 90, "Status": "Top / Rigorista Assoluto", "Convenienza": "Altissima"},
        {"Nome": "Daniel Boloca", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare Centrocampo", "Convenienza": "Alta"},
        {"Nome": "Fabrizio Caligara", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 16, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Fali Candé", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 15, "Status": "Difensore Solido", "Convenienza": "Media"},
        {"Nome": "Walid Cheddira", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 28, "Status": "Attaccante / Gol", "Convenienza": "Alta"},
        {"Nome": "Riccardo Ciervo", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Luca D'andrea", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 14, "Status": "Scommessa Esterna", "Convenienza": "Media"},
        {"Nome": "Josh Doig", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 22, "Status": "Spinta a Sinistra", "Convenienza": "Alta"},
        {"Nome": "Andrea Ghion", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 14, "Status": "Rotazione Regia", "Convenienza": "Bassa"},
        {"Nome": "Edoardo Iannoni", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 15, "Status": "Dinamismo", "Convenienza": "Media"},
        {"Nome": "Jay Idzes", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare / Roccia", "Convenienza": "Alta"},
        {"Nome": "Ismaël Koné", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 25, "Status": "Qualità e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Justin Kumi", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Armand Laurienté", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 45, "Status": "Titolare / Dribbling", "Convenienza": "Alta"},
        {"Nome": "Luca Lipani", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 10, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Tommaso Macchioni", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Nemanja Matic", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 24, "Status": "Esperienza e Visione", "Convenienza": "Alta"},
        {"Nome": "Kevin Miranda", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Filippo Missori", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 12, "Status": "Rotazione Fascia", "Convenienza": "Bassa"},
        {"Nome": "Luca Moro", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 14, "Status": "Riserva Attacco", "Convenienza": "Bassa"},
        {"Nome": "Samuele Mulattieri", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 24, "Status": "Rotazione / Gol", "Convenienza": "Media"},
        {"Nome": "Arijanet Muric", "Squadra": "Sassuolo", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 28, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Patrick Nuamah", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Cas Odenthal", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 14, "Status": "Titolare / Rotazione", "Convenienza": "Media"},
        {"Nome": "Yeferson Paz", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 40, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Edoardo Pieragnolo", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 12, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Nicholas Pierini", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 20, "Status": "Esterno Offensivo", "Convenienza": "Media"},
        {"Nome": "Andrea Pinamonti", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 50, "Status": "Bomber Titolare", "Convenienza": "Alta"},
        {"Nome": "Flavio Russo", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 25, "Quotazione": 6, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Laurs Skjellerup", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 30, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Kristian Thorstvedt", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 32, "Status": "Incursore / Gol", "Convenienza": "Alta"},
        {"Nome": "Stefano Turati", "Squadra": "Sassuolo", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 8, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Giorgio Vezzosi", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Cristian Volpato", "Squadra": "Sassuolo", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 22, "Status": "Fantasia / Scommessa", "Convenienza": "Media"},
        {"Nome": "Sebastian Walukiewicz", "Squadra": "Sassuolo", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 16, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Gioele Zacchi", "Squadra": "Sassuolo", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Agustín Álvarez", "Squadra": "Sassuolo", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 12, "Status": "Riserva", "Convenienza": "Bassa"},

        # --- TORINO ---
        {"Nome": "Zakaria Aboukhlal", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 32, "Status": "Velocità e Bonus", "Convenienza": "Alta"},
        {"Nome": "Wisdom Acquah", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Ché Adams", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 45, "Status": "Titolare / Gol e Lavoro Sporco", "Convenienza": "Alta"},
        {"Nome": "Tino Anjorin", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 18, "Status": "Qualità in Mezzo", "Convenienza": "Media"},
        {"Nome": "Cristiano Biraghi", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 24, "Status": "Piazzati e Assist", "Convenienza": "Alta"},
        {"Nome": "Alessio Cacciamani", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Cesare Casadei", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 35, "Status": "Inserimenti Pericolosi / Gol", "Convenienza": "Altissima"},
        {"Nome": "Saúl Coco", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 20, "Status": "Titolare / Gol dalla Distanza", "Convenienza": "Alta"},
        {"Nome": "Pietro Comuzzo", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Titolare Difesa Solida", "Convenienza": "Alta"},
        {"Nome": "Eray Cömert", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Alessandro Dellavalle", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Ali Dembélé", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 45, "Quotazione": 10, "Status": "Riserva Fascia", "Convenienza": "Bassa"},
        {"Nome": "Tommaso Gabellini", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Gvidas Gineitis", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 12, "Status": "Giovane Promessa", "Convenienza": "Media"},
        {"Nome": "Ivan Ilic", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 24, "Status": "Titolare / Tiro da Fuori", "Convenienza": "Media"},
        {"Nome": "Emirhan Ilkhan", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Ardian Ismajli", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Franco Israel", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 28, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Sandro Kulenovic", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 55, "Quotazione": 18, "Status": "Alternativa in Attacco", "Convenienza": "Media"},
        {"Nome": "Tommaso Di Marco", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Diego Mascardi", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Alieu Njie", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 10, "Status": "Giovane Scommessa", "Convenienza": "Bassa"},
        {"Nome": "Gaetano Oristanio", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 26, "Status": "Fantasia / Trequartista", "Convenienza": "Alta"},
        {"Nome": "Alberto Paleari", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 5, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Marcus Pedersen", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 22, "Status": "Spinta sulla Fascia", "Convenienza": "Alta"},
        {"Nome": "Pietro Pellegri", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 12, "Status": "Riserva / Fisico", "Convenienza": "Bassa"},
        {"Nome": "Zanos Savva", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 25, "Quotazione": 6, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Giovanni Simeone", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 35, "Status": "Bomber / Titolare", "Convenienza": "Alta"},
        {"Nome": "Lapo Siviero", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Adrien Tamèze", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 16, "Status": "Jolly Difesa / Centrocampo", "Convenienza": "Media"},
        {"Nome": "Nikola Vlasic", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 42, "Status": "Trequartista Titolare", "Convenienza": "Alta"},
        {"Nome": "Duván Zapata", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 85, "Status": "Panzer / Bomber Titolare", "Convenienza": "Altissima"},

        # --- UDINESE ---
        {"Nome": "Juan Arizala", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Vakoun Bayo", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 18, "Status": "Rotazione Attacco", "Convenienza": "Media"},
        {"Nome": "Nicolò Bertola", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 15, "Status": "Giovane Centrale", "Convenienza": "Media"},
        {"Nome": "Adam Buksa", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 30, "Status": "Centravanti / Gol di Testa", "Convenienza": "Alta"},
        {"Nome": "Abdoulaye Camara", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Giorgi Chakvetadze", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 28, "Status": "Dribbling e Assist", "Convenienza": "Alta"},
        {"Nome": "Keinan Davis", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 25, "Status": "Lavoro Sporco / Titolare", "Convenienza": "Alta"},
        {"Nome": "Enzo Ebosse", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 50, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Kingsley Ehizibue", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 14, "Status": "Corsa / Rotazione", "Convenienza": "Media"},
        {"Nome": "Jurgen Ekkelenkamp", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 26, "Status": "Inserimenti / Gol", "Convenienza": "Alta"},
        {"Nome": "Saba Goglichidze", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 16, "Status": "Titolare Difesa", "Convenienza": "Media"},
        {"Nome": "Idrissa Gueye", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Unai Gómez", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 20, "Status": "Qualità in Mezzo", "Convenienza": "Media"},
        {"Nome": "Christian Kabasele", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 10, "Status": "Esperienza", "Convenienza": "Bassa"},
        {"Nome": "Hassane Kamara", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 16, "Status": "Spinta", "Convenienza": "Media"},
        {"Nome": "Jesper Karlström", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 22, "Status": "Diga / Voto Fisso", "Convenienza": "Alta"},
        {"Nome": "Thomas Kristensen", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Sandi Lovric", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 28, "Status": "Titolare / Tiro da Fuori", "Convenienza": "Alta"},
        {"Nome": "Lennon Miller", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 30, "Quotazione": 8, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Branimir Mlacic", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Rui Modesto", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 18, "Status": "Esterno Spinta", "Convenienza": "Media"},
        {"Nome": "Maduka Okoye", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 30, "Status": "Portiere Titolare", "Convenienza": "Altissima"},
        {"Nome": "Daniele Padelli", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 3, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Matteo Palma", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Martín Payero", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 22, "Status": "Fisico e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "David Pejicic", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Edoardo Piana", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Jakub Piotrowski", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 26, "Status": "Inserimenti e Gol", "Convenienza": "Alta"},
        {"Nome": "Oumar Solet", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 24, "Status": "Top Difesa / Fisicità", "Convenienza": "Altissima"},
        {"Nome": "Giulio Vinciati", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Mërgim Vojvoda", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Rotazione / Affidabile", "Convenienza": "Media"},
        {"Nome": "Nicolò Zaniolo", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 55, "Status": "Top Slot / Scommessa di Classe", "Convenienza": "Altissima"},
        {"Nome": "Alessandro Zanoli", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 16, "Status": "Spinta Fascia", "Convenienza": "Media"},
        {"Nome": "Oier Zarraga", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Jordan Zemura", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 15, "Status": "Alternativa Fascia", "Convenienza": "Media"},

        # --- VENEZIA ---
        {"Nome": "Akor Adams", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 42, "Status": "Bomber Titolare / Potenza", "Convenienza": "Alta"},
        {"Nome": "Andrea Adorante", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 16, "Status": "Riserva / Gol", "Convenienza": "Bassa"},
        {"Nome": "Giorgio Altare", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 12, "Status": "Saltatore di Testa", "Convenienza": "Media"},
        {"Nome": "Toma Basic", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 24, "Status": "Qualità e Tiro", "Convenienza": "Alta"},
        {"Nome": "Armel Bella-Kotchap", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 22, "Status": "Muro Difensivo", "Convenienza": "Alta"},
        {"Nome": "Lorenzo Berardi", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Bjarki Bjarkason", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Emil Bohinen", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 16, "Status": "Regia", "Convenienza": "Media"},
        {"Nome": "Gianluca Busio", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 24, "Status": "Inserimenti / Incursore", "Convenienza": "Alta"},
        {"Nome": "Antonio Casas", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 14, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Thierry Correia", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 20, "Status": "Terzino Spinta", "Convenienza": "Alta"},
        {"Nome": "Matteo Dagasso", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 25, "Quotazione": 5, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Alfred Duncan", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 22, "Status": "Quantità ed Esperienza", "Convenienza": "Alta"},
        {"Nome": "Lamine Fanne", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 10, "Status": "Giovane Promessa", "Convenienza": "Bassa"},
        {"Nome": "Marko Farji", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Bartol Franjic", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 16, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Ale Gomes", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Matteo Grandi", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 4, "Status": "Secondo Portiere", "Convenienza": "Bassa"},
        {"Nome": "Saad El Haddad", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Antoine Hainaut", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Ridgeciano Haps", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 15, "Status": "Spinta a Sinistra", "Convenienza": "Media"},
        {"Nome": "Thórir Helgason", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 15, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Lion Lauberbach", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 12, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Nunzio Lella", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 55, "Quotazione": 14, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Calixte Ligue", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Kornel Lisman", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Edoardo Mariani", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Filippo Neri", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Terzo Portiere", "Convenienza": "Molto Bassa"},
        {"Nome": "Alvin Okoro", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Simone Panada", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Alessio Pozzi", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Lorenzo Da Pozzo", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Kike Pérez", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 20, "Status": "Quantità e Qualità", "Convenienza": "Media"},
        {"Nome": "Albion Rrahmani", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 38, "Status": "Bomber Titolare", "Convenienza": "Alta"},
        {"Nome": "Richie Sagrado", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 14, "Status": "Rotazione Fascia", "Convenienza": "Bassa"},
        {"Nome": "Joël Schingtienne", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 16, "Status": "Difensore Centrale", "Convenienza": "Media"},
        {"Nome": "Ahmed Sidibé", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 15, "Quotazione": 2, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Filip Stankovic", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 32, "Status": "Portiere Titolare", "Convenienza": "Altissima"},
        {"Nome": "Marin Sverko", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 14, "Status": "Titolare / Rotazione", "Convenienza": "Media"},
        {"Nome": "Mohamed Malang Touré", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 20, "Quotazione": 4, "Status": "Giovane", "Convenienza": "Bassa"},
        {"Nome": "Michael Venturi", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "John Yeboah", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 26, "Status": "Esterno Offensivo / Dribbling", "Convenienza": "Alta"}
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
  import random

def genera_rosa_fantacalcio():
    # Definizione della lista dei giocatori con Nome, Ruolo, Quotazione (crediti) e Fantamedia stimata
    # Formato: {"nome": "...", "ruolo": "...", "crediti": ..., "fantamedia": ...}
    listone = [
        # PORTIERI (3 titolari/alternanze + 3 panchinari)
        {"nome": "Svilar", "ruolo": "P", "crediti": 45, "fantamedia": 5.2},
        {"nome": "Sommer", "ruolo": "P", "crediti": 130, "fantamedia": 5.8},
        {"nome": "Di Gregorio", "ruolo": "P", "crediti": 110, "fantamedia": 5.5},
        {"nome": "Maignan", "ruolo": "P", "crediti": 140, "fantamedia": 5.7},
        {"nome": "Skorupski", "ruolo": "P", "crediti": 30, "fantamedia": 4.8},
        {"nome": "Falcone", "ruolo": "P", "crediti": 25, "fantamedia": 4.7},
        {"nome": "Turati", "ruolo": "P", "crediti": 15, "fantamedia": 4.5},
        {"nome": "Okoye", "ruolo": "P", "crediti": 15, "fantamedia": 4.5},
        
        # DIFENSORI (8 totali: 3 top/semitop + 5 low cost/panchinari)
        {"nome": "Dimarco", "ruolo": "D", "crediti": 150, "fantamedia": 6.8},
        {"nome": "Theo Hernandez", "ruolo": "D", "crediti": 160, "fantamedia": 6.7},
        {"nome": "Bastoni", "ruolo": "D", "crediti": 100, "fantamedia": 6.4},
        {"nome": "Bremer", "ruolo": "D", "crediti": 90, "fantamedia": 6.3},
        {"nome": "Buongiorno", "ruolo": "D", "crediti": 85, "fantamedia": 6.3},
        {"nome": "Cambiaso", "ruolo": "D", "crediti": 75, "fantamedia": 6.2},
        {"nome": "Bellanova", "ruolo": "D", "crediti": 70, "fantamedia": 6.1},
        {"nome": "Zappacosta", "ruolo": "D", "crediti": 50, "fantamedia": 5.9},
        {"nome": "Baschirotto", "ruolo": "D", "crediti": 20, "fantamedia": 5.6},
        {"nome": "Gila", "ruolo": "D", "crediti": 15, "fantamedia": 5.5},
        {"nome": "Beukema", "ruolo": "D", "crediti": 15, "fantamedia": 5.5},
        {"nome": "Ismajli", "ruolo": "D", "crediti": 10, "fantamedia": 5.4},
        
        # CENTROCAMPISTI (8 totali: 3 top + 5 panchinari/titolari di provincia)
        {"nome": "Pulisic", "ruolo": "C", "crediti": 220, "fantamedia": 7.8},
        {"nome": "Koopmeiners", "ruolo": "C", "crediti": 230, "fantamedia": 7.9},
        {"nome": "Calhanoglu", "ruolo": "C", "crediti": 240, "fantamedia": 8.0},
        {"nome": "Zaccagni", "ruolo": "C", "crediti": 140, "fantamedia": 6.9},
        {"nome": "Colpani", "ruolo": "C", "crediti": 100, "fantamedia": 6.6},
        {"nome": "Ferguson", "ruolo": "C", "crediti": 80, "fantamedia": 6.5},
        {"nome": "Vlasic", "ruolo": "C", "crediti": 70, "fantamedia": 6.3},
        {"nome": "Suslov", "ruolo": "C", "crediti": 30, "fantamedia": 5.9},
        {"nome": "Frendrup", "ruolo": "C", "crediti": 25, "fantamedia": 5.8},
        {"nome": "Prass", "ruolo": "C", "crediti": 20, "fantamedia": 5.7},
        {"nome": "Brescianini", "ruolo": "C", "crediti": 25, "fantamedia": 6.0},
        
        # ATTACCANTI (6 totali: 2 top + 4 completamenti/panchinari)
        {"nome": "Lautaro Martinez", "ruolo": "A", "crediti": 400, "fantamedia": 9.5},
        {"nome": "Retegui", "ruolo": "A", "crediti": 320, "fantamedia": 8.8},
        {"nome": "Thuram", "ruolo": "A", "crediti": 300, "fantamedia": 8.5},
        {"nome": "Lukaku", "ruolo": "A", "crediti": 290, "fantamedia": 8.4},
        {"nome": "Dovbyk", "ruolo": "A", "crediti": 260, "fantamedia": 8.1},
        {"nome": "Gudmundsson", "ruolo": "A", "crediti": 200, "fantamedia": 7.7},
        {"nome": "Castellanos", "ruolo": "A", "crediti": 150, "fantamedia": 7.3},
        {"nome": "Krstovic", "ruolo": "A", "crediti": 80, "fantamedia": 6.6},
        {"nome": "Lucca", "ruolo": "A", "crediti": 70, "fantamedia": 6.5},
        {"nome": "Pohjanpalo", "ruolo": "A", "crediti": 60, "fantamedia": 6.4}
    ]

    budget_massimo = 1500
    requisiti = {"P": 3, "D": 8, "C": 8, "A": 6}

    tentativi = 0
    while tentativi < 10000:
        rosa = []
        spesa_totale = 0
        conteggio = {"P": 0, "D": 0, "C": 0, "A": 0}
        
        # Copia mescolata del listone per simulare aste diverse
        giocatori_disponibili = list(listone)
        random.shuffle(giocatori_disponibili)
        
        for g in giocatori_disponibili:
            r = g["ruolo"]
            if conteggio[r] < requisiti[r] and (spesa_totale + g["crediti"] <= budget_massimo):
                # Controllo di massima per non esaurire troppo presto i crediti impedendo di completare i ruoli minimi
                crediti_rimasti = budget_massimo - (spesa_totale + g["crediti"])
                slot_mancanti = (requisiti["P"] - conteggio["P"]) + (requisiti["D"] - conteggio["D"]) + \
                                (requisiti["C"] - conteggio["C"]) + (requisiti["A"] - conteggio["A"]) - 1
                
                if crediti_rimasti >= slot_mancanti * 10: # Lascia almeno 10 crediti per ogni slot rimanente
                    rosa.append(g)
                    spesa_totale += g["crediti"]
                    conteggio[r] += 1
                    
            if len(rosa) == 25:
                break
                
        if len(rosa) == 25 and spesa_totale <= budget_massimo:
            return rosa, spesa_totale
        
        tentativi += 1

    return None, 0

# Esecuzione del generatore
rosa_ideale, spesa = genera_rosa_fantacalcio()

if rosa_ideale:
    print(f"=== ROSA IDEALE DEL FANTACALCIO (Spesa totale: {spesa}/1500 crediti) ===\n")
    for ruolo in ["P", "D", "C", "A"]:
        nomi_ruolo = {"P": "PORTIERI (3)", "D": "DIFENSORI (8)", "C": "CENTROCAMPISTI (8)", "A": "ATTACCANTI (6)"}
        print(f"--- {nomi_ruolo[ruolo]} ---")
        giocatori_ruolo = [g for g in rosa_ideale if g["ruolo"] == ruolo]
        for g in giocatori_ruolo:
            print(f"- {g['nome']} | Costo: {g['crediti']} crediti | FantaMedia: {g['fantamedia']}")
        print()
else:
    print("Impossibile trovare una combinazione con i vincoli attuali.")
