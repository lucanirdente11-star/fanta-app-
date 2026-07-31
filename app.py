# Programma per inserire e gestire la tua rosa del Fantacalcio personalizzata

budget_massimo = 1500
rosa_utente = []
spesa_totale = 0

print("=== GESTORE ROSA FANTACALCIO (Budget: 1500 crediti) ===")
print("Inserisci i tuoi giocatori uno alla volta. Scrivi 'fine' nel nome per terminare prima.\n")

while True:
    nome = input("Nome del giocatore (o 'fine' per chiudere): ").strip()
    if nome.lower() == 'fine':
        break
        
    ruolo = input("Ruolo generale (P = Portiere, D = Difensore, C = Centrocampista, A = Attaccante): ").strip().upper()
    if ruolo not in ["P", "D", "C", "A"]:
        print("Ruolo non valido! Usa P, D, C o A.\n")
        continue
        
    ruolo_preciso = input("Ruolo preciso (es. Mezzala, Ala Sinistra, Terzino, ecc.): ").strip()
    
    try:
        crediti = int(input("Crediti spesi per questo giocatore: "))
    except ValueError:
        print("Inserisci un numero valido per i crediti!\n")
        continue
        
    # Controllo budget
    if spesa_totale + crediti > budget_massimo:
        print(f"ATTENZIONE: Non hai abbastanza crediti! Te ne restano {budget_massimo - spesa_totale}.\n")
        continue
        
    try:
        fantamedia = float(input("Fantamedia stimata (es. 6.5): "))
    except ValueError:
        fantamedia = 0.0

    # Aggiungiamo il giocatore alla lista
    giocatore = {
        "nome": nome,
        "ruolo": ruolo,
        "ruolo_preciso": ruolo_preciso,
        "crediti": crediti,
        "fantamedia": fantamedia
    }
    
    rosa_utente.append(giocatore)
    spesa_totale += crediti
    
    print(f"--> Aggiunto! Spesa totale finora: {spesa_totale}/{budget_massimo} crediti (Restanti: {budget_massimo - spesa_totale})\n")
    print("-" * 40 + "\n")

# --- RIEPILOGO FINALE ---
print("\n" + "="*50)
print(f"=== LA TUA ROSA FINALE (Spesa Totale: {spesa_totale}/{budget_massimo} crediti) ===")
print(f"Crediti avanzati: {budget_massimo - spesa_totale}\n")

mapping_ruoli = {
    "P": "PORTIERI", 
    "D": "DIFENSORI (Titolari e Panchinari)", 
    "C": "CENTROCAMPISTI (Titolari e Panchinari)", 
    "A": "ATTACCANTI (Titolari e Panchinari)"
}

for ruolo_chiave in ["P", "D", "C", "A"]:
    giocatori = [g for g in rosa_utente if g["ruolo"] == ruolo_chiave]
    if giocatori:
        print(f"--- {mapping_ruoli[ruolo_chiave]} ({len(giocatori)}) ---")
        spesa_reparto = sum(g["crediti"] for g in giocatori)
        print(f"(Spesa reparto: {spesa_reparto} crediti)\n")
        
        for g in giocatori:
            print(f"• {g['nome']} | Ruolo: {g['ruolo_preciso']} | Costo: {g['crediti']} crediti | FantaMedia: {g['fantamedia']}")
        print("\n" + "-"*40 + "\n")

# Evita la chiusura improvvisa dello schermo nero
input("Premi INVIO per chiudere il programma...")
