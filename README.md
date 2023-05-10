# Neural Network Trainer

Questo progetto è un addestratore di una semplice rete neurale. L'obiettivo è fornire una base per l'apprendimento automatico utilizzando una rete neurale con un numero configurabile di input, output e layer nascosti.

## Utilizzo

Segui i passaggi seguenti per utilizzare il progetto:

1.  Assicurati di avere Python installato sul tuo sistema.
    
2.  Clona il repository o scarica i file del progetto.
    
3.  Installa le dipendenze eseguendo il comando seguente:
    
    `pip install -r requirements.txt` 
    
4.  Prepara il tuo dataset di addestramento:
    
    -   Crea un file CSV che contenga i dati di addestramento. Ogni riga del file rappresenta un esempio di input-output per la rete neurale. Assicurati di separare gli input dagli output con una virgola.
        
    -   Modifica il file `dataset.csv` esistente con i tuoi dati di addestramento o crea un nuovo file CSV e specifica il percorso nel parametro `--dataset` durante l'esecuzione del programma.
        
5.  Esegui il programma utilizzando il seguente comando:
    
    `python main.py --num_inputs <num_inputs> --num_outputs <num_outputs> --num_hidden <num_hidden> --num_layers <num_layers> --use_memory --dataset <dataset_path> --epochs <num_epochs> --learning_rate <learning_rate> --save_model --model_file <model_path>` 
    
    -   Sostituisci `<num_inputs>`, `<num_outputs>`, `<num_hidden>`, `<num_layers>`, `<dataset_path>`, `<num_epochs>`, `<learning_rate>`, `<model_path>` con i valori desiderati.
        
    -   L'opzione `--use_memory` è facoltativa e può essere inclusa per utilizzare neuroni con memoria.
        
    -   L'opzione `--save_model` è facoltativa e può essere inclusa per salvare il modello addestrato su un file.
        
6.  Durante l'esecuzione del programma, verranno visualizzati i risultati dell'addestramento, inclusi l'epoca corrente e l'errore medio.
    
7.  Alla fine dell'addestramento, verranno generati input casuali e verrà calcolato l'output corrispondente utilizzando il modello addestrato. L'input e l'output saranno visualizzati a schermo.
    
8.  Se hai incluso l'opzione `--save_model`, il modello addestrato verrà salvato nel file specificato.
    

## Personalizzazioni

Puoi personalizzare il comportamento del programma modificando gli argomenti passati durante l'esecuzione o apportando modifiche al codice sorgente.

-   Puoi regolare il numero di neuroni di input, output, layer nascosti e layer totali tramite gli argomenti `--num_inputs`, `--num_outputs`, `--num_hidden` e `--num_layers`.
    
-   Puoi abilitare l'uso dei neuroni con memoria utilizzando l'opzione `--use_memory`.
    
-   Puoi modificare il percorso del file CSV di addestramento utilizzando l'argomento `--dataset`.

-   Puoi regolare il numero di epoche di addestramento utilizzando l'argomento `--epochs`.
    
-   Puoi specificare il tasso di apprendimento utilizzando l'argomento `--learning_rate`.
    
-   Puoi scegliere di salvare il modello addestrato su un file specifico utilizzando l'opzione `--save_model` e specificando il percorso del file con l'argomento `--model_file`.
    
-   Se desideri apportare modifiche al comportamento del programma, puoi modificare il codice sorgente nei file `main.py` e `neuron.py` per adattarlo alle tue esigenze.
    

## Esempi

Ecco alcuni esempi di comandi che puoi utilizzare per eseguire il programma:

-   Addestrare una rete neurale con 2 neuroni di input, 1 neurone di output, 2 neuroni nascosti, 1 layer nascosto, utilizzando neuroni con memoria e salvando il modello addestrato:
    
    `python main.py --num_inputs 2 --num_outputs 1 --num_hidden 2 --num_layers 1 --use_memory --save_model` 
    
-   Addestrare una rete neurale utilizzando un file CSV diverso come dataset di addestramento:
    
    `python main.py --dataset my_dataset.csv` 
    
-   Addestrare una rete neurale per 200 epoche con un tasso di apprendimento di 0.01:
    
    `python main.py --epochs 200 --learning_rate 0.01` 
    
-   Addestrare una rete neurale e salvare il modello addestrato su un file specifico:
    
    `python main.py --save_model --model_file my_model.pkl` 
    

## Conclusioni

Questo progetto ti offre una base per comprendere e sperimentare con le reti neurali. Puoi personalizzare il numero di neuroni, il dataset di addestramento, le epoche e il tasso di apprendimento per adattare la rete neurale ai tuoi dati e obiettivi specifici. Speriamo che questo progetto sia un punto di partenza utile per il tuo apprendimento delle reti neurali!

Se hai domande o suggerimenti, non esitare a contattarci o a inviare una richiesta di pull. Buon divertimento nell'utilizzare questa semplice rete neurale!
