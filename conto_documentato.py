## @file conto.documentati.py
# @brief Semplice implementazione di un conto bancario con operazioni di deposito e prlievo.


## @brief Rappresenta un conto bancario co ointestatario e saldo 
# @details consente di depositarte e prelevare denaro. il prelievo e possibile se il saldo e in positivo.


class ContoBancario():

    ## @brief inizializza un nuovo conto bancario.
    # @param intestatrio Nome dell'intestatazio del conto. 
    
    def __init__ (self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0

    ##@brief preleva una somm a di denaro 
    # @param importo somma da prlevare
    # @exception valueError sollevata se il saldo e insufficiente 

    def deposita(self, importo):
        self.saldo += importo

    def preleva(self, importo):
        if self.saldo < importo:
            raise ValueError('Saldo insufficiente')
        else:
            self.saldo -= importo

    def __str__ (self):
        return f'Conto di {self.intestatario} saldo: {self.saldo}'


def main():
    conto = ContoBancario("Mario Rossi")
    print (conto)
    conto.deposita(200)
    conto.preleva(50)
    conto.preleva(25)
    print(conto)
    try:
        conto.preleva(700)
    except ValueError as e:
        print('Operazione rifiutata: ', e)

if __name__ == "__main__":
    main()
