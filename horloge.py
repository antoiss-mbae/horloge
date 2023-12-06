import time

def afficher_heure(heure):
    """Affiche l'heure au format hh:mm:ss"""
    heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format)

def regler_alarme(heure_alarme):
    """Règle l'alarme pour une heure spécifique"""
    alarme_format = "{:02d}:{:02d}:{:02d}".format(heure_alarme[0], heure_alarme[1], heure_alarme[1])
    print(f"Alarme réglée à {alarme_format}")

def verifier_alarme(heure_actuelle, heure_alarme):
    """Vérifie si l'heure actuelle correspond à l'heure de l'alarme"""
    return heure_actuelle == heure_alarme

def main():
    heure_actuelle = (0, 0, 0)  # Heure de départ (00:00:00)

    while True:
        afficher_heure(heure_actuelle)

        # Régler l'heure actuelle à l'aide de la fonction afficher_heure
        # Remplacez ces lignes par un appel à une fonction pour récupérer l'heure réelle du système
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)
        if heure_actuelle[2] == 60:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
            if heure_actuelle[1] == 60:
                heure_actuelle = (heure_actuelle[0] + 1, 0, 0)
                if heure_actuelle[0] == 24:
                    heure_actuelle = (0, 0, 0)

        # Régler l'alarme à une heure spécifique (modifiable selon vos besoins)
        heure_alarme = (11, 0, 0)
        regler_alarme(heure_alarme)

        # Vérifier si l'alarme doit être déclenchée
        if verifier_alarme(heure_actuelle, heure_alarme):
            print("Réveil! L'heure de l'alarme est atteinte.")

        time.sleep(1)  # Attente d'une seconde avant la mise à jour de l'heure

if __name__ == "__main__":
    main()
def afficher_heure(heure, minute, seconde, mode_12h=False):
    if mode_12h:
        if heure >= 12:
            suffixe = 'PM'
            if heure > 12:
                heure -= 12
        else:
            suffixe = 'AM'
            if heure == 0:
                heure = 12
        heure_format = "{:02d}:{:02d}:{:02d} {}".format(heure, minute, seconde, suffixe)
    else:
        heure_format = "{:02d}:{:02d}:{:02d}".format(heure, minute, seconde)

    print(heure_format)

# Exemple d'utilisation
afficher_heure(16, 30, 0, mode_12h=True)
import time
import threading

class Horloge:
    def __init__(self, heure, minute, seconde, mode_12h=False):
        self.heure = heure
        self.minute = minute
        self.seconde = seconde
        self.mode_12h = mode_12h
        self.pause_flag = False
        self.thread = threading.Thread(target=self.actualiser_heure, daemon=True)
        self.thread.start()

    def actualiser_heure(self):
        while True:
            if not self.pause_flag:
                self.afficher_heure()
                self.attendre(1)
                self.incrementer_seconde()

    def afficher_heure(self):
        if self.mode_12h:
            if self.heure >= 12:
                suffixe = 'PM'
                if self.heure > 12:
                    self.heure -= 12
            else:
                suffixe = 'AM'
                if self.heure == 0:
                    self.heure = 12
            heure_format = "{:02d}:{:02d}:{:02d} {}".format(self.heure, self.minute, self.seconde, suffixe)
        else:
            heure_format = "{:02d}:{:02d}:{:02d}".format(self.heure, self.minute, self.seconde)

        print(heure_format)

    def attendre(self, secondes):
        time.sleep(secondes)

    def incrementer_seconde(self):
        self.seconde += 1
        if self.seconde == 60:
            self.seconde = 0
            self.incrementer_minute()
        if self.mode_12h and self.heure == 12 and self.minute == 0 and self.seconde == 0:
            self.heure = 0
        elif not self.mode_12h and self.heure == 23 and self.minute == 59 and self.seconde == 59:
            self.heure = 0
        else:
            self.heure += 1

    def incrementer_minute(self):
        self.minute += 1
        if self.minute == 60:
            self.minute = 0

    def mettre_en_pause(self):
        self.pause_flag = True

    def relancer(self):
        self.pause_flag = False

# Exemple d'utilisation
horloge = Horloge(16, 30, 0, mode_12h=True)
time.sleep(5)  # Laissez l'horloge s'exécuter pendant 5 secondes
horloge.mettre_en_pause()
print("L'horloge est en pause.")
time.sleep(5)  # Attendez pendant 5 secondes
horloge.relancer()
print("L'horloge est relancée.")
time.sleep(5)  # Laissez l'horloge s'exécuter pendant 5 secondes
