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
