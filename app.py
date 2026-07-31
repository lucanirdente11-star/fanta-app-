import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quotazioni Fantacalcio", page_icon="⚽", layout="wide")

st.title("⚽ Database Quotazioni Fantacalcio")
st.markdown("Filtra i giocatori per squadra e ruolo per analizzare titolarità, quotazioni e convenienza.")

@st.cache_data
def load_data():
    giocatori = [
        # --- ATALANTA ---
        {"Nome": "Marco Carnesecchi", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 38, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Juan Musso", "Squadra": "Atalanta", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 12, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Matteo Ruggeri", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 22, "Status": "Titolare / Assist", "Convenienza": "Alta"},
        {"Nome": "Giorgio Scalvini", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 26, "Status": "Top Difesa / Vizio del Gol", "Convenienza": "Alta"},
        {"Nome": "Berat Djimsiti", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Sead Kolasinac", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 20, "Status": "Titolare Esperto", "Convenienza": "Alta"},
        {"Nome": "Davide Zappacosta", "Squadra": "Atalanta", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 24, "Status": "Bonus a Sorpresa", "Convenienza": "Media"},
        {"Nome": "Teun Koopmeiners", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 50, "Status": "Top Assoluto / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Ederson", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 28, "Status": "Titolare / Recupera Palloni", "Convenienza": "Altissima"},
        {"Nome": "Mario Pasalic", "Squadra": "Atalanta", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 28, "Status": "Incursore / Jolly", "Convenienza": "Alta"},
        {"Nome": "Charles De Ketelaere", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 45, "Status": "Top Fantasia / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Gianluca Scamacca", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 70, "Status": "Bomber Principale", "Convenienza": "Altissima"},
        {"Nome": "Ademola Lookman", "Squadra": "Atalanta", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 75, "Status": "Top Player / Imprevedibile", "Convenienza": "Altissima"},

        # --- BOLOGNA ---
        {"Nome": "Lukasz Skorupski", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 28, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Federico Ravaglia", "Squadra": "Bologna", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 5, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Stefan Posch", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 24, "Status": "Spinta Fascia", "Convenienza": "Alta"},
        {"Nome": "Sam Beukema", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 20, "Status": "Titolare Fisso", "Convenienza": "Altissima"},
        {"Nome": "Riccardo Calafiori", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 28, "Status": "Top Difesa / Impostazione", "Convenienza": "Altissima"},
        {"Nome": "Victor Kristiansen", "Squadra": "Bologna", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 16, "Status": "Rotazione Titolare", "Convenienza": "Media"},
        {"Nome": "Lewis Ferguson", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 32, "Status": "Top Centrocampo / Gol", "Convenienza": "Altissima"},
        {"Nome": "Giovanni Fabbian", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 22, "Status": "Jolly Incursore", "Convenienza": "Alta"},
        {"Nome": "Remo Freuler", "Squadra": "Bologna", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 18, "Status": "Regista / Voti Alti", "Convenienza": "Alta"},
        {"Nome": "Riccardo Orsolini", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 42, "Status": "Top Esterno / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Dan Ndoye", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 22, "Status": "Fascia Rapida", "Convenienza": "Media"},
        {"Nome": "Joshua Zirkzee", "Squadra": "Bologna", "Ruolo": "Attaccante", "Titolarita_%": 95, "Quotazione": 75, "Status": "Top Player / Genio", "Convenienza": "Altissima"},

        # --- CAGLIARI ---
        {"Nome": "Simone Scuffet", "Squadra": "Cagliari", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 22, "Status": "Titolare", "Convenienza": "Alta"},
        {"Nome": "Gabriele Zappa", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 15, "Status": "Titolare / Assist", "Convenienza": "Alta"},
        {"Nome": "Yerry Mina", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 16, "Status": "Carisma / Gol di Testa", "Convenienza": "Alta"},
        {"Nome": "Alberto Dossena", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 18, "Status": "Muro Difensivo", "Convenienza": "Altissima"},
        {"Nome": "Tommaso Augello", "Squadra": "Cagliari", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 15, "Status": "Cross e Piazzati", "Convenienza": "Alta"},
        {"Nome": "Antoine Makoumbou", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 14, "Status": "Quantità", "Convenienza": "Media"},
        {"Nome": "Nahitan Nandez", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 22, "Status": "Tuttofare / Grinta", "Convenienza": "Alta"},
        {"Nome": "Gaetano Oristanio", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 16, "Status": "Fantasia / Scommessa", "Convenienza": "Media"},
        {"Nome": "Gianluca Lapadula", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 32, "Status": "Titolare / Rigorista", "Convenienza": "Alta"},
        {"Nome": "Nicolas Viola", "Squadra": "Cagliari", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 18, "Status": "Specialista da Bonus", "Convenienza": "Alta"},
        {"Nome": "Leonardo Pavoletti", "Squadra": "Cagliari", "Ruolo": "Attaccante", "Titolarita_%": 40, "Quotazione": 18, "Status": "Uomo della Provvidenza", "Convenienza": "Media"},

        # --- COMO ---
        {"Nome": "Jean Butez", "Squadra": "Como", "Ruolo": "Portiere", "Titolarita_%": 85, "Quotazione": 20, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Alberto Dossena", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 15, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Edoardo Goldaniga", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 12, "Status": "Esperienza Difensiva", "Convenienza": "Media"},
        {"Nome": "Alessio Iovine", "Squadra": "Como", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 10, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Lucas Da Cunha", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 16, "Status": "Esterno Offensivo", "Convenienza": "Media"},
        {"Nome": "Matteo Braunoder", "Squadra": "Como", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 14, "Status": "Quantità e Qualità", "Convenienza": "Alta"},
        {"Nome": "Patrick Cutrone", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 28, "Status": "Bomber Principale", "Convenienza": "Alta"},
        {"Nome": "Andrea Belotti", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 35, "Status": "Esperienza e Gol", "Convenienza": "Alta"},
        {"Nome": "Gabriel Strefezza", "Squadra": "Como", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 26, "Status": "Trequartista / Bonus", "Convenienza": "Altissima"},

        # --- EMPOLI ---
        {"Nome": "Elia Caprile", "Squadra": "Empoli", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 24, "Status": "Saracinesca", "Convenienza": "Alta"},
        {"Nome": "Ardian Ismajli", "Squadra": "Empoli", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 12, "Status": "Muro Difensivo", "Convenienza": "Alta"},
        {"Nome": "Sebastiano Luperto", "Squadra": "Empoli", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 16, "Status": "Leader Difesa", "Convenienza": "Altissima"},
        {"Nome": "Liberato Cacace", "Squadra": "Empoli", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 10, "Status": "Fascia", "Convenienza": "Media"},
        {"Nome": "Alberto Grassi", "Squadra": "Empoli", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 11, "Status": "Lotta Mediana", "Convenienza": "Media"},
        {"Nome": "Youssef Maleh", "Squadra": "Empoli", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 13, "Status": "Dinamismo", "Convenienza": "Media"},
        {"Nome": "Jacopo Fazzini", "Squadra": "Empoli", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 18, "Status": "Talento Emergente", "Convenienza": "Alta"},
        {"Nome": "Nicolò Cambiaghi", "Squadra": "Empoli", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 25, "Status": "Imprevedibile", "Convenienza": "Alta"},
        {"Nome": "Francesco Caputo", "Squadra": "Empoli", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 24, "Status": "Esperienza / Rigorista", "Convenienza": "Media"},
        {"Nome": "M'Baye Niang", "Squadra": "Empoli", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 22, "Status": "Rigorista / Gol Pesanti", "Convenienza": "Alta"},

        # --- FIORENTINA ---
        {"Nome": "Pietro Terracciano", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 80, "Quotazione": 25, "Status": "Titolare Affidabile", "Convenienza": "Alta"},
        {"Nome": "Oliver Christensen", "Squadra": "Fiorentina", "Ruolo": "Portiere", "Titolarita_%": 20, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Dodo", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 20, "Status": "Spinta e Assist", "Convenienza": "Alta"},
        {"Nome": "Lucas Martinez Quarta", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 22, "Status": "Vizio del Gol", "Convenienza": "Altissima"},
        {"Nome": "Nikola Milenkovic", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Fabiano Parisi", "Squadra": "Fiorentina", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 15, "Status": "Alternativa Fascia", "Convenienza": "Media"},
        {"Nome": "Giacomo Bonaventura", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 35, "Status": "Top Centrocampo / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Arthur Melo", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 20, "Status": "Maestro di Regia", "Convenienza": "Alta"},
        {"Nome": "Rolando Mandragora", "Squadra": "Fiorentina", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 16, "Status": "Tiri dalla Distanza", "Convenienza": "Media"},
        {"Nome": "Nicolas Gonzalez", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 55, "Status": "Top Assoluto / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Lucas Beltran", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 32, "Status": "Prima Punta / Crescita", "Convenienza": "Alta"},
        {"Nome": "Jonathan Ikoné", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 20, "Status": "Fiammate Imprevedibili", "Convenienza": "Bassa"},
        {"Nome": "M'Bala Nzola", "Squadra": "Fiorentina", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 22, "Status": "Rotazione Offensiva", "Convenienza": "Bassa"},

        # --- GENOA ---
        {"Nome": "Josep Martínez", "Squadra": "Genoa", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 28, "Status": "Saracinesca", "Convenienza": "Altissima"},
        {"Nome": "Koni De Winter", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 16, "Status": "Giovane in Crescita", "Convenienza": "Alta"},
        {"Nome": "Johan Vásquez", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 18, "Status": "Titolare / Grinta", "Convenienza": "Altissima"},
        {"Nome": "Stefano Sabelli", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 12, "Status": "Fascia Affidabile", "Convenienza": "Alta"},
        {"Nome": "Aaron Martín", "Squadra": "Genoa", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 14, "Status": "Cross e Piazzati", "Convenienza": "Media"},
        {"Nome": "Milan Badelj", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 12, "Status": "Geometrie", "Convenienza": "Media"},
        {"Nome": "Morten Frendrup", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 20, "Status": "Recupera-palloni Top", "Convenienza": "Altissima"},
        {"Nome": "Ruslan Malinovskyi", "Squadra": "Genoa", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 28, "Status": "Tiri dalla Distanza / Bonus", "Convenienza": "Alta"},
        {"Nome": "Albert Gudmundsson", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 95, "Quotazione": 55, "Status": "Top Player / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Mateo Retegui", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 48, "Status": "Bomber Principale", "Convenienza": "Altissima"},
        {"Nome": "Junior Messias", "Squadra": "Genoa", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 24, "Status": "Jolly Offensivo", "Convenienza": "Media"},

        # --- HELLAS VERONA ---
        {"Nome": "Lorenzo Montipò", "Squadra": "Hellas Verona", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 25, "Status": "Para-tutto", "Convenienza": "Altissima"},
        {"Nome": "Giangiacomo Magnani", "Squadra": "Hellas Verona", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 12, "Status": "Esperienza Difensiva", "Convenienza": "Alta"},
        {"Nome": "Diego Coppola", "Squadra": "Hellas Verona", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 14, "Status": "Sorpresa Difesa / Gol", "Convenienza": "Alta"},
        {"Nome": "Jackson Tchatchoua", "Squadra": "Hellas Verona", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 13, "Status": "Spinta a Destra", "Convenienza": "Media"},
        {"Nome": "Suat Serdar", "Squadra": "Hellas Verona", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 16, "Status": "Dinamismo Mediano", "Convenienza": "Alta"},
        {"Nome": "Ondrej Duda", "Squadra": "Hellas Verona", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 18, "Status": "Piazzati e Assist", "Convenienza": "Altissima"},
        {"Nome": "Tomás Suslov", "Squadra": "Hellas Verona", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 22, "Status": "Fantasia e Qualità", "Convenienza": "Altissima"},
        {"Nome": "Darko Lazovic", "Squadra": "Hellas Verona", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 20, "Status": "Esperienza / Calci Piazzati", "Convenienza": "Alta"},
        {"Nome": "Tijjani Noslin", "Squadra": "Hellas Verona", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 26, "Status": "Fascia / Gol Pesanti", "Convenienza": "Altissima"},
        {"Nome": "Karol Swiderski", "Squadra": "Hellas Verona", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 24, "Status": "Punta Centrale", "Convenienza": "Alta"},

        # --- INTER ---
        {"Nome": "Yann Sommer", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 50, "Status": "Portiere Campione", "Convenienza": "Altissima"},
        {"Nome": "Emil Audero", "Squadra": "Inter", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 10, "Status": "Riserva di Lusso", "Convenienza": "Bassa"},
        {"Nome": "Alessandro Bastoni", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 35, "Status": "Top Difesa / Assist", "Convenienza": "Altissima"},
        {"Nome": "Benjamin Pavard", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 28, "Status": "Titolare Top", "Convenienza": "Altissima"},
        {"Nome": "Francesco Acerbi", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 20, "Status": "Affidabilità Totale", "Convenienza": "Alta"},
        {"Nome": "Federico Dimarco", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 45, "Status": "Top Assoluto / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Denzel Dumfries", "Squadra": "Inter", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 30, "Status": "Uomo Bonus a Gara", "Convenienza": "Alta"},
        {"Nome": "Hakan Calhanoglu", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 60, "Status": "Top Rigorista / Fenomeno", "Convenienza": "Altissima"},
        {"Nome": "Niccolò Barella", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 40, "Status": "Top Centrocampo", "Convenienza": "Altissima"},
        {"Nome": "Henrikh Mkhitaryan", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 32, "Status": "Titolare / Inserimenti", "Convenienza": "Altissima"},
        {"Nome": "Davide Frattesi", "Squadra": "Inter", "Ruolo": "Centrocampista", "Titolarita_%": 50, "Quotazione": 28, "Status": "Spacca-partite / Bonus", "Convenienza": "Alta"},
        {"Nome": "Marcus Thuram", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 80, "Status": "Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Lautaro Martínez", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 95, "Quotazione": 110, "Status": "Re del Fantacalcio / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Marko Arnautovic", "Squadra": "Inter", "Ruolo": "Attaccante", "Titolarita_%": 35, "Quotazione": 25, "Status": "Rotazione Offensiva", "Convenienza": "Bassa"},

        # --- JUVENTUS ---
        {"Nome": "Wojciech Szczesny", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 42, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Mattia Perin", "Squadra": "Juventus", "Ruolo": "Portiere", "Titolarita_%": 10, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Danilo", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 28, "Status": "Leader e Voti Alti", "Convenienza": "Altissima"},
        {"Nome": "Gleison Bremer", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 35, "Status": "Muro / Goleador di Testa", "Convenienza": "Altissima"},
        {"Nome": "Federico Gatti", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 20, "Status": "Gol Pesanti", "Convenienza": "Alta"},
        {"Nome": "Andrea Cambiaso", "Squadra": "Juventus", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 25, "Status": "Polivalenza / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Adrien Rabiot", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 38, "Status": "Top Centrocampo / Inserimenti", "Convenienza": "Altissima"},
        {"Nome": "Manuel Locatelli", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 22, "Status": "Regia e Sostanza", "Convenienza": "Alta"},
        {"Nome": "Weston McKennie", "Squadra": "Juventus", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 22, "Status": "Assist e Dinamismo", "Convenienza": "Alta"},
        {"Nome": "Dusan Vlahovic", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 90, "Status": "Bomber / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Federico Chiesa", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 70, "Status": "Top Player Imprevedibile", "Convenienza": "Alta"},
        {"Nome": "Kenan Yildiz", "Squadra": "Juventus", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 24, "Status": "Talento Puro / Scommessa", "Convenienza": "Alta"},

        # --- LAZIO ---
        {"Nome": "Ivan Provedel", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 40, "Status": "Top Portiere / Vizio del Gol", "Convenienza": "Altissima"},
        {"Nome": "Christos Mandas", "Squadra": "Lazio", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 8, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Manuel Lazzari", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 16, "Status": "Spinta Fascia", "Convenienza": "Media"},
        {"Nome": "Mario Gila", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Sorpresa Difesa", "Convenienza": "Alta"},
        {"Nome": "Alessio Romagnoli", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 24, "Status": "Titolare / Voti Alti", "Convenienza": "Altissima"},
        {"Nome": "Adam Marusic", "Squadra": "Lazio", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 18, "Status": "Jolly Difensivo", "Convenienza": "Alta"},
        {"Nome": "Matteo Guendouzi", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 25, "Status": "Grinta e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Luis Alberto", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 45, "Status": "Genio e Assist / Top", "Convenienza": "Altissima"},
        {"Nome": "Daichi Kamada", "Squadra": "Lazio", "Ruolo": "Centrocampista", "Titolarita_%": 60, "Quotazione": 20, "Status": "Incrocio Tattico", "Convenienza": "Media"},
        {"Nome": "Mattia Zaccagni", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 45, "Status": "Top Esterno / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Ciro Immobile", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 65, "Status": "Storico Bomber / Rigorista", "Convenienza": "Alta"},
        {"Nome": "Valentiny Castellanos", "Squadra": "Lazio", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 28, "Status": "Alternativa Offensiva", "Convenienza": "Media"},

        # --- LECCE ---
        {"Nome": "Wladimiro Falcone", "Squadra": "Lecce", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 26, "Status": "Para-tutto / Voti Alti", "Convenienza": "Altissima"},
        {"Nome": "Federico Baschirotto", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 18, "Status": "Guerriero Difensivo", "Convenienza": "Alta"},
        {"Nome": "Marin Pongracic", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 15, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Antonino Gallo", "Squadra": "Lecce", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 12, "Status": "Spinta a Sinistra", "Convenienza": "Media"},
        {"Nome": "Ylber Ramadani", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 14, "Status": "Quantità Industriale", "Convenienza": "Alta"},
        {"Nome": "Hamza Rafia", "Squadra": "Lecce", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 15, "Status": "Qualità sulla Trequarti", "Convenienza": "Media"},
        {"Nome": "Lameck Banda", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 20, "Status": "Velocità Bruciante", "Convenienza": "Alta"},
        {"Nome": "Nikola Krstovic", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 28, "Status": "Bomber e Tiri", "Convenienza": "Alta"},
        {"Nome": "Pontus Almqvist", "Squadra": "Lecce", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 18, "Status": "Fiammate e Dribbling", "Convenienza": "Media"},

        # --- MILAN ---
        {"Nome": "Mike Maignan", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 45, "Status": "Top Portiere Assoluto", "Convenienza": "Altissima"},
        {"Nome": "Marco Sportiello", "Squadra": "Milan", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Theo Hernández", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 55, "Status": "Top Difesa / Re dei Bonus", "Convenienza": "Altissima"},
        {"Nome": "Fikayo Tomori", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 25, "Status": "Velocità e Anticipo", "Convenienza": "Alta"},
        {"Nome": "Malick Thiaw", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 18, "Status": "Rotazione Titolare", "Convenienza": "Media"},
        {"Nome": "Davide Calabria", "Squadra": "Milan", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 18, "Status": "Capitano Affidabile", "Convenienza": "Alta"},
        {"Nome": "Ruben Loftus-Cheek", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 35, "Status": "Top Centrocampo / Inserimenti", "Convenienza": "Altissima"},
        {"Nome": "Tijani Reijnders", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 26, "Status": "Quantità e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Ismaël Bennacer", "Squadra": "Milan", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 22, "Status": "Regia di Qualità", "Convenienza": "Alta"},
        {"Nome": "Christian Pulisic", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 60, "Status": "Top Esterno / Gol e Assist", "Convenienza": "Altissima"},
        {"Nome": "Rafael Leão", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 85, "Status": "Top Player / Crack", "Convenienza": "Altissima"},
        {"Nome": "Olivier Giroud", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 70, "Status": "Bomber di Razza / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Noah Okafor", "Squadra": "Milan", "Ruolo": "Attaccante", "Titolarita_%": 50, "Quotazione": 25, "Status": "Jolly da Gol a Gara in Corso", "Convenienza": "Alta"},

        # --- MONZA ---
        {"Nome": "Michele Di Gregorio", "Squadra": "Monza", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 35, "Status": "Top Portiere Rivelazione", "Convenienza": "Altissima"},
        {"Nome": "Alessandro Sorrentino", "Squadra": "Monza", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 5, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Pablo Marí", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 18, "Status": "Esperienza e Voti Alti", "Convenienza": "Altissima"},
        {"Nome": "Armando Izzo", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 15, "Status": "Grinta e Cartellini", "Convenienza": "Media"},
        {"Nome": "Andrea Carboni", "Squadra": "Monza", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 12, "Status": "Giovane in Affidamento", "Convenienza": "Media"},
        {"Nome": "Patrick Ciurria", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 24, "Status": "Jolly Listato Centrocampo", "Convenienza": "Altissima"},
        {"Nome": "Matteo Pessina", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 30, "Status": "Titolare / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Roberto Gagliardini", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 16, "Status": "Inserimenti Aerei", "Convenienza": "Media"},
        {"Nome": "Andrea Colpani", "Squadra": "Monza", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 35, "Status": "Top Centrocampo / Gol", "Convenienza": "Altissima"},
        {"Nome": "Lorenzo Colombo", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 22, "Status": "Punta Titolare", "Convenienza": "Media"},
        {"Nome": "Milan Djuric", "Squadra": "Monza", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 24, "Status": "Torre / Gol Aerei", "Convenienza": "Alta"},

        # --- NAPOLI ---
        {"Nome": "Alex Meret", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 35, "Status": "Portiere Campione", "Convenienza": "Alta"},
        {"Nome": "Pierluigi Gollini", "Squadra": "Napoli", "Ruolo": "Portiere", "Titolarita_%": 15, "Quotazione": 10, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Giovanni Di Lorenzo", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 95, "Quotazione": 40, "Status": "Top Fascia / Assist", "Convenienza": "Altissima"},
        {"Nome": "Amir Rrahmani", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 20, "Status": "Titolare Fisso", "Convenienza": "Alta"},
        {"Nome": "Juan Jesus", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 65, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Bassa"},
        {"Nome": "Mathias Olivera", "Squadra": "Napoli", "Ruolo": "Difensore", "Titolarita_%": 60, "Quotazione": 15, "Status": "Alternativa Fascia", "Convenienza": "Media"},
        {"Nome": "Stanislav Lobotka", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 95, "Quotazione": 24, "Status": "Regia Pura / Voti Alti", "Convenienza": "Alta"},
        {"Nome": "André-Frank Zambo Anguissa", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 28, "Status": "Forza e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Piotr Zielinski", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 32, "Status": "Qualità e Bonus", "Convenienza": "Alta"},
        {"Nome": "Jens Cajuste", "Squadra": "Napoli", "Ruolo": "Centrocampista", "Titolarita_%": 40, "Quotazione": 14, "Status": "Riserva", "Convenienza": "Bassa"},
        {"Nome": "Matteo Politano", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 35, "Status": "Esterno Titolare / Rigorista", "Convenienza": "Alta"},
        {"Nome": "Khvicha Kvaratskhelia", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 95, "Quotazione": 90, "Status": "Top Player Assoluto", "Convenienza": "Altissima"},
        {"Nome": "Victor Osimhen", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 105, "Status": "Top Bomber / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Giacomo Raspadori", "Squadra": "Napoli", "Ruolo": "Attaccante", "Titolarita_%": 60, "Quotazione": 30, "Status": "Jolly Offensivo", "Convenienza": "Media"},

        # --- PARMA ---
        {"Nome": "Zion Suzuki", "Squadra": "Parma", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 25, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Alessandro Circati", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 16, "Status": "Muro Giovane", "Convenienza": "Altissima"},
        {"Nome": "Enrico Del Prato", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 18, "Status": "Capitano e Affidabilità", "Convenienza": "Alta"},
        {"Nome": "Lautaro Valenti", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Adrian Bernabé", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 90, "Quotazione": 28, "Status": "Geometrie / Top Serie B", "Convenienza": "Altissima"},
        {"Nome": "Hernani", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 20, "Status": "Piazzati e Fisicità", "Convenienza": "Alta"},
        {"Nome": "Nahuel Estévez", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 16, "Status": "Interdizione", "Convenienza": "Alta"},
        {"Nome": "Dennis Man", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 35, "Status": "Top Esterno / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Valentin Mihaila", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 24, "Status": "Fascia Rapida", "Convenienza": "Alta"},
        {"Nome": "Ange-Yoan Bonny", "Squadra": "Parma", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 22, "Status": "Boa Centrale", "Convenienza": "Media"},
        {"Nome": "Edoardo Tigani", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 10, "Quotazione": 1, "Status": "Giovane", "Convenienza": "Molto Bassa"},
        {"Nome": "Woyo Coulibaly", "Squadra": "Parma", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 15, "Status": "Titolare Fascia", "Convenienza": "Media"},
        {"Nome": "Simon Sohm", "Squadra": "Parma", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 22, "Status": "Titolare / Dinamismo", "Convenienza": "Alta"},

        # --- ROMA ---
        {"Nome": "Tommaso Baldanzi", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 65, "Quotazione": 25, "Status": "Trequartista / Qualità", "Convenienza": "Media"},
        {"Nome": "Zeki Çelik", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 70, "Quotazione": 16, "Status": "Rotazione Fascia", "Convenienza": "Media"},
        {"Nome": "Bryan Cristante", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 26, "Status": "Titolare / Quantità", "Convenienza": "Alta"},
        {"Nome": "Paulo Dybala", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 95, "Status": "Super Top / Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Stephan El Shaarawy", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 28, "Status": "Jolly Offensivo", "Convenienza": "Alta"},
        {"Nome": "Mats Hummels", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 24, "Status": "Esperienza / Centrali", "Convenienza": "Alta"},
        {"Nome": "Gianluca Mancini", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 30, "Status": "Titolare / Goleador di Testa", "Convenienza": "Altissima"},
        {"Nome": "Mile Svilar", "Squadra": "Roma", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 45, "Status": "Top Portiere", "Convenienza": "Altissima"},
        {"Nome": "Artem Dovbyk", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 95, "Status": "Super Top Bomber", "Convenienza": "Altissima"},
        {"Nome": "Evan Ndicka", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 22, "Status": "Titolare Difesa", "Convenienza": "Alta"},
        {"Nome": "Leandro Paredes", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 28, "Status": "Regia e Piazzati", "Convenienza": "Alta"},
        {"Nome": "Lorenzo Pellegrini", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 45, "Status": "Top Centrocampo / Bonus", "Convenienza": "Altissima"},
        {"Nome": "Alexis Saelemaekers", "Squadra": "Roma", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 25, "Status": "Esterno Tattico", "Convenienza": "Alta"},
        {"Nome": "Matías Soulé", "Squadra": "Roma", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 45, "Status": "Talento / Fantasia", "Convenienza": "Altissima"},
        {"Nome": "Angeliño", "Squadra": "Roma", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 26, "Status": "Spinta e Assist", "Convenienza": "Alta"},

        # --- TORINO ---
        {"Nome": "Che Adams", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 75, "Quotazione": 32, "Status": "Attaccante Titolare", "Convenienza": "Alta"},
        {"Nome": "Raoul Bellanova", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 35, "Status": "Top Fascia / Assist", "Convenienza": "Altissima"},
        {"Nome": "Saul Coco", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 20, "Status": "Titolare / Gol dalla Distanza", "Convenienza": "Alta"},
        {"Nome": "Valentino Lazaro", "Squadra": "Torino", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 18, "Status": "Spinta Fascia", "Convenienza": "Media"},
        {"Nome": "Karol Linetty", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 70, "Quotazione": 14, "Status": "Quantità", "Convenienza": "Bassa"},
        {"Nome": "Ciprian Tatarusanu", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 5, "Quotazione": 1, "Status": "Riserva", "Convenienza": "Molto Bassa"},
        {"Nome": "Antonio Sanabria", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 70, "Quotazione": 30, "Status": "Titolare / Rigorista", "Convenienza": "Alta"},
        {"Nome": "Duvan Zapata", "Squadra": "Torino", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 75, "Status": "Top Bomber Assoluto", "Convenienza": "Altissima"},
        {"Nome": "Nikola Vlasic", "Squadra": "Torino", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 38, "Status": "Trequartista / Rigori", "Convenienza": "Altissima"},
        {"Nome": "Vanja Milinkovic-Savic", "Squadra": "Torino", "Ruolo": "Portiere", "Titolarita_%": 95, "Quotazione": 30, "Status": "Titolare Affidabile", "Convenienza": "Alta"},

        # --- UDINESE ---
        {"Nome": "Lorenzo Lucca", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 80, "Quotazione": 35, "Status": "Bomber Principale", "Convenienza": "Alta"},
        {"Nome": "Florian Thauvin", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 85, "Quotazione": 42, "Status": "Top Squadra / Fantasia", "Convenienza": "Altissima"},
        {"Nome": "Sandi Lovric", "Squadra": "Udinese", "Ruolo": "Centrocampista", "Titolarita_%": 75, "Quotazione": 20, "Status": "Inserimenti / Qualità", "Convenienza": "Media"},
        {"Nome": "Jaka Bijol", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 90, "Quotazione": 22, "Status": "Muro Difensivo", "Convenienza": "Alta"},
        {"Nome": "Maduka Okoye", "Squadra": "Udinese", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 26, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Keinan Davis", "Squadra": "Udinese", "Ruolo": "Attaccante", "Titolarita_%": 65, "Quotazione": 22, "Status": "Lotta / Sponda", "Convenienza": "Media"},
        {"Nome": "Kingsley Ehizibue", "Squadra": "Udinese", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 16, "Status": "Spinta Fascia", "Convenienza": "Media"},

        # --- VENEZIA ---
        {"Nome": "Jesse Joronen", "Squadra": "Venezia", "Ruolo": "Portiere", "Titolarita_%": 90, "Quotazione": 22, "Status": "Portiere Titolare", "Convenienza": "Alta"},
        {"Nome": "Jay Idzes", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 85, "Quotazione": 15, "Status": "Perno Difensivo", "Convenienza": "Alta"},
        {"Nome": "Michael Svoboda", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 75, "Quotazione": 12, "Status": "Rotazione", "Convenienza": "Media"},
        {"Nome": "Antonio Candela", "Squadra": "Venezia", "Ruolo": "Difensore", "Titolarita_%": 80, "Quotazione": 14, "Status": "Fascia Destra", "Convenienza": "Media"},
        {"Nome": "Gianluca Busio", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 85, "Quotazione": 18, "Status": "Quantità e Inserimenti", "Convenienza": "Alta"},
        {"Nome": "Hans Nicolussi Caviglia", "Squadra": "Venezia", "Ruolo": "Centrocampista", "Titolarita_%": 80, "Quotazione": 16, "Status": "Regia e Tiri", "Convenienza": "Alta"},
        {"Nome": "Joel Pohjanpalo", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 90, "Quotazione": 42, "Status": "Bomber e Rigorista", "Convenienza": "Altissima"},
        {"Nome": "Christian Gytkjær", "Squadra": "Venezia", "Ruolo": "Attaccante", "Titolarita_%": 45, "Quotazione": 20, "Status": "Uomo Gol a Gara in Corso", "Convenienza": "Media"}
    ]
    return pd.DataFrame(giocatori)

df = load_data()

# --- INTERFACCIA STREAMLIT ---
st.sidebar.header("🔍 Filtri di Ricerca")
squadra_selezionata = st.sidebar.selectbox("Seleziona Squadra", ["Tutte"] + sorted(df["Squadra"].unique().tolist()))
ruolo_selezionato = st.sidebar.selectbox("Seleziona Ruolo", ["Tutti"] + sorted(df["Ruolo"].unique().tolist()))

# Filtraggio dataframe
df_filtrato = df.copy()
if squadra_selezionata != "Tutte":
    df_filtrato = df_filtrato[df_filtrato["Squadra"] == squadra_selezionata]
if ruolo_selezionato != "Tutti":
    df_filtrato = df_filtrato[df_filtrato["Ruolo"] == ruolo_selezionato]

st.subheader(f"Giocatori Trovati: {len(df_filtrato)}")
st.dataframe(df_filtrato, use_container_width=True, hide_index=True)
