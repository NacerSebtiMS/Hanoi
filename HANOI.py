## Fonctions annexes
def Envoie (LD,LA): #Permet de déplacer le premier élément de LD dans le premier élément de LA
    LA=[LD[0]]+LA
    LD=LD[1:]
    return LD,LA

def CalcHanoi(n): #Calcule le nombre minimal de déplacements
    if n==1:
        return 1
    return 2*CalcHanoi(n-1)+1 
    
##Gestion de Doc TxT

def writeList(Flux,L): #Transcrit les étapes dans un document texte, une variable list global pourrai faire l'affaire
    for i in range(len(L)):
        Erf=L[i]
        Arf=str(Erf)
        Flux.write(Arf)
    if len(L)==0:
        Flux.write(" ")
    Flux.write("\n")
    
def ReturnListofListofList(FLUX,n): #Transcrit le document txt en une liste contenant des listes des différentes étapes qui contiennent les listes des états des différentes tours
    BigBossList=[]
    for i in range(n):
        ListEtape =[]
        for j in range(3):
            Tour=list(FLUX.readline ())
            Tour.remove('\n')
            ListEtape=ListEtape+[Tour]
        BigBossList=BigBossList+[ListEtape]
    return BigBossList
 
## Remise en position
def ArrangeLesTours(L,n): #Arrange la list issue du doc txt afin que les tours reprennent leur position d'origine
    for i in range(2,n,2):
        for j in range(i,n):
            L[j][2],L[j][0],L[j][1]=L[j][0],L[j][1],L[j][2]
    return L

## Retranscription des Etapes    
def EtapesKudasai(L,n): #Donne les déplacements effectués pour arriver au résultat
    E=[]
    for i in range(len(L)):
        move=0
        if i!=0:
            kur1,kur2,kur3=len(L[i-1][0]),len(L[i-1][1]),len(L[i-1][2])
        else :
            kur1,kur2,kur3=n,0,0
        isu1,isu2,isu3=len(L[i][0]),len(L[i][1]),len(L[i][2])
        kurisu1,kurisu2,kurisu3=kur1-isu1,kur2-isu2,kur3-isu3
        if kurisu1 == 1 and kurisu2 == -1 :
            move = 1
        if kurisu1 == 1 and kurisu3 == -1 :
            move = 2
        if kurisu2 == 1 and kurisu3 == -1 :
            move = 3
        if kurisu3 == 1 and kurisu2 == -1 :
            move = 4
        if kurisu3 == 1 and kurisu1 == -1 :
            move = 5
        if kurisu2 == 1 and kurisu1 == -1 :
            move = 6
        E=E+[move]
    return E
    
## Fonctions Hanoi
def Hanoi(n,L1,L2,L3,Record): #Execute tout les déplacements de disques et de tours. /!\ Si n est pair l'ensemble des disque sera déplacé en L2 et non L3
    """
    La suite d'Hanoi s'écrit comme ce qui suit : H(n) = 2 H(n-1) + 1
en décomposant se résultat, on retrouve qu'il faut déplacer suivant H(n-1), ensuite effectuer un déplacement supplémentaire représenté par le +1, puis refaire les H(n-1) déplacements.
En suivant cette logique, on essayera de transposer les tours afin que le H(n-1) conserve les mêmes déplacements dans les 2 cas.
En effet supposant avoir 3 disques. Il faudra déplacer L1 ==> L3 // L1 ===> L2 // L3 ==> L2 // L1 ==> L3 // ect ... aucune logique ne se répète.
Afin de dégager une logique, notons le déplacement L1 ==> L3 le déplacement 1 (D1), L1 ==> L2 le D2 et L2 ==> L1 le D3
A chaque fois qu'un déplacement différent de D1 est effectué, on décale les tours de façon à ce que L3 prenne la première place, L1 la seconde et L2 la dernière.
On execute alors D1, suivit de D2. On intervertit les tours. On ré-exécute D1. Nous venons d'empiler les 2 blocs sur L2 présente à la 3eme position suivant la suite D1/D2/D1
Pour arriver à empiler 3 bloc, on éxécute ce qui a été fait précédement, soit D1/D2/D1 (H(2)). Executons D3, intervertissons les tours, on a alors L2 a la première place, L3 a la seconde et L1 a la dernière. Effectuons à nouveau la même série que pour 2 (H(2)), soit D1/D2/D1 en changeant de place à nouveau lors du déplacement D2.
On arrive alors a empiler les 3 blocs en L3 qui se trouve a la 3eme position.
Il est possible de montrer que pour le neme déplacement, il faudra éxécuter le déplacement Dn qui est suivant la parité de n soit le D2 (si n est pair) soit le D3 (si n est impaire)
    """
    if n==1: #Donne le déplacement élémentaire pour n=1
        L1,L3=Envoie(L1,L3)
        writeList(Record,L1) #Prend note des différentes étapes, elles ne sont pas affichées directement car les tours changent de position
        writeList(Record,L2)
        writeList(Record,L3)
        return(L1,L2,L3)
    L1,L2,L3=Hanoi(n-1,L1,L2,L3,Record) # On exécute H(n-1)
    if n%2 == 0:
        L1,L2=Envoie(L1,L2) # On effectue le D2
        writeList(Record,L1)
        writeList(Record,L2)
        writeList(Record,L3)
    else:
        L2,L1=Envoie(L2,L1) #On effectue le D3
        writeList(Record,L1)
        writeList(Record,L2)
        writeList(Record,L3)
    L1,L2,L3=L3,L1,L2 # On change la place des tours
    L1,L2,L3=Hanoi(n-1,L1,L2,L3,Record)# On exécute H(n-1)
    return(L1,L2,L3)    
##Programme Principal
def Jefaistout(): #Fait office de programme principal
    Record=open("Enregistre Hanoi.txt",'w')
    n=int(input("Choisir le nombre de disques de la Tour d'Hanoï : "))
    L1,L2,L3=[],[],[]
    for i in range(n):
        L1=L1+[i+1]
    print("Etape initiale : Tour n°1 :",L1,"Tour n°2 :",L2,"Tour n°3 :",L3)
    L1,L2,L3 = Hanoi(n,L1,L2,L3,Record)
    Record.close()
    Record=open("Enregistre Hanoi.txt",'r')
    NbrEtape = CalcHanoi(n)
    L=ReturnListofListofList(Record,NbrEtape)
    L=ArrangeLesTours(L,NbrEtape)
    for i in range(len(L)):
        for j in range(len(L[i])):
            for k in range(len(L[i][j])):
                if  L[i][j][k]!=' ':
                    L[i][j][k]=int(L[i][j][k])
                else :
                    L[i][j]=[]
    print("===ETAPES===")
    for i in range(len(L)):
        print("Etape",i+1,":",end=' ')     
        print("Tour n°1 :",L[i][0],"Tour n°2 :",L[i][1],"Tour n°3 :",L[i][2]) 
    E=EtapesKudasai(L,n)
    #print(E)

EXECUTE=True
if EXECUTE:
    Jefaistout()