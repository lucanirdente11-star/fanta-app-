# Lista fissa della Rosa Ideale (25 giocatori: 3 P, 8 D, 8 C, 6 A)
# Totale esatto: 1500 crediti
rosa_ideale = [
    # --- PORTIERI (3) ---
    {"nome": "Sommer", "ruolo": "P", "ruolo_preciso": "Portiere Titolare", "crediti": 80, "fantamedia": 5.8},
    {"nome": "Skorupski", "ruolo": "P", "ruolo_preciso": "Portiere di Riserva", "crediti": 20, "fantamedia": 4.8},
    {"nome": "Turati", "ruolo": "P", "ruolo_preciso": "Terzo Portiere", "crediti": 10, "fantamedia": 4.5},
    
    # --- DIFENSORI (8) ---
    {"nome": "Theo Hernandez", "ruolo": "D", "ruolo_preciso": "Terzino Sinistro / Spingitore", "crediti": 120, "fantamedia": 6.7},
    {"nome": "Dimarco", "ruolo": "D", "ruolo_preciso": "Terzino / Esterno Titolare", "crediti": 110, "fantamedia": 6.8},
    {"nome": "Bastoni", "ruolo": "D", "ruolo_preciso": "Braccetto Sinistro", "crediti": 80, "fantamedia": 6.4},
    {"nome": "Bremer", "ruolo": "D", "ruolo_preciso": "Difensore Centrale Puro", "crediti": 75, "fantamedia": 6.3},
    {"nome": "Cambiaso", "ruolo": "D", "ruolo_preciso": "Terzino / Esterno a Tutta Fascia", "crediti": 60, "fantamedia": 6.2},
    {"nome": "Bellanova", "ruolo": "D", "ruolo_preciso": "Esterno Destro Titolare", "crediti": 55, "fantamedia": 6.1},
    {"nome": "Zappacosta", "ruolo": "D", "ruolo_preciso": "Quinto di Centrocampo (Panchina)", "crediti": 35, "fantamedia": 5.9},
    {"nome": "Baschirotto", "ruolo": "D", "ruolo_preciso": "Centralone di Riserva", "crediti": 15, "fantamedia": 5.6},
    
    # --- CENTROCAMPISTI (8) ---
    {"nome": "Calhanoglu", "ruolo": "C", "ruolo_preciso": "Regista / Rigorista", "crediti": 170, "fantamedia": 8.0},
    {"nome": "Koopmeiners", "ruolo": "C", "ruolo_preciso": "Trequartista / Mezzala", "crediti": 160, "fantamedia": 7.9},
    {"nome": "Pulisic", "ruolo": "C", "ruolo_preciso": "Ala Destra / Trequartista", "crediti": 150, "fantamedia": 7.8},
    {"nome": "Zaccagni", "ruolo": "C", "ruolo_preciso": "Ala Sinistra", "crediti": 100, "fantamedia": 6.9},
    {"nome": "Colpani", "ruolo": "C", "ruolo_preciso": "Mezzala / Esterno Offensivo", "crediti": 70, "fantamedia": 6.6},
    {"nome": "Ferguson", "ruolo": "C", "ruolo_preciso": "Mezzala Inseritrice", "crediti": 60, "fantamedia": 6.5},
    {"nome": "Vlasic", "ruolo": "C", "ruolo_preciso": "Trequartista Centrale", "crediti": 50, "fantamedia": 6.3},
    {"nome": "Brescianini", "ruolo": "C", "ruolo_preciso": "Mezzala di Riserva", "crediti": 25, "fantamedia": 6.0},
    
    # --- ATTACCANTI (6) ---
    {"nome": "Lautaro Martinez", "ruolo": "A", "ruolo_preciso": "Prima Punta / Centravanti", "crediti": 280, "fantamedia": 9.5},
    {"nome": "Retegui", "ruolo": "A", "ruolo_preciso": "Centravanti Titolare", "crediti": 230, "fantamedia": 8.8},
    {"nome": "Thuram", "ruolo": "A", "ruolo_preciso": "Attaccante Esterno / Seconda Punta", "crediti": 210, "fantamedia": 8.5},
    {"nome": "Gudmundsson", "ruolo": "A", "ruolo_preciso": "Seconda Punta / Esterno a Sinistra", "crediti": 150, "fantamedia": 7.7},
    {"nome": "Krstovic", "ruolo": "A", "ruolo_preciso": "Panchinaro / Prima Punta", "crediti": 50, "fantamedia": 6.6},
    {"nome": "Lucca", "ruolo": "A", "ruolo_preciso": "Riserva di Spinta (Torre)", "crediti": 40, "fantamedia": 6.5}
]

# Calcolo spesa totale
spesa_totale = sum(g["crediti"] for g in rosa_ideale)

# Stampa a schermo
print(f"=== ROSA IDEALE DEL FANTACALCIO (Spesa totale: {spesa_totale}/1500 crediti) ===")
print(f"Crediti avanzati: {1500 - spesa_totale}\n")

mapping_ruoli = {
    "P": "PORTIERI (3)", 
    "D": "DIFENSORI - Titolari e Panchinari (8)", 
    "C": "CENTROCAMPISTI - Mezzali, Ali e Registi (8)", 
    "A": "ATTACCANTI - Centravanti e Ali (6)"
}

for ruolo_chiave in ["P", "D", "C", "A"]:
    print(f"--- {mapping_ruoli[ruolo_chiave]} ---")
    giocatori = [g for g in rosa_ideale if g["ruolo"] == ruolo_chiave]
    spesa_reparto = sum(g["crediti"] for g in giocatori)
    print(f"(Spesa totale reparto: {spesa_reparto} crediti)\n")
    
    for g in giocatori:
        print(f"• {g['nome']} | Ruolo: {g['ruolo_preciso']} | Costo: {g['crediti']} crediti | FantaMedia: {g['fantamedia']}")
    print("\n" + "="*50 + "\n")

# Evita la chiusura improvvisa della schermata
input("Premi INVIO per chiudere il programma...")
