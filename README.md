# Neural Network Trainer
Benvenuto al mio progetto di rete neurale! Questo progetto utilizza una rete neurale per eseguire calcoli speciali. Una rete neurale è come un piccolo cervello artificiale che può prendere decisioni e risolvere problemi utilizzando matematica e codice.

## Documentazione semplificata
La classe "NeuralNetwork" rappresenta la nostra rete neurale. Quando creiamo una rete neurale, specifichiamo quanti "neuroni di input" e "neuroni di output" vogliamo. I neuroni di input raccolgono informazioni dall'esterno, mentre i neuroni di output comunicano il risultato al mondo esterno.

Abbiamo anche "neuroni nascosti" che sono come stanze segrete nel cervello. Questi neuroni nascosti ci aiutano a elaborare le informazioni in modo più intelligente. Possiamo decidere quanti neuroni nascosti e quanti livelli nascosti vogliamo nella nostra rete neurale.

La classe "Neuron" rappresenta un singolo neurone nella rete neurale. Ogni neurone ha dei "pesi" e un "bias". I pesi determinano l'importanza delle informazioni di input, mentre il bias rappresenta una preferenza personale del neurone. I pesi e il bias aiutano il neurone a prendere decisioni basate sui dati di input.

Il metodo "calculate()" della classe "NeuralNetwork" calcola l'output della rete neurale. Prendiamo i valori di input, li passiamo attraverso i neuroni e otteniamo un risultato finale. È come risolvere un puzzle matematico!

Il metodo "get_output()" restituisce l'output calcolato dalla rete neurale. Possiamo usarlo per ottenere il risultato dei nostri calcoli o per prendere decisioni basate sui dati elaborati dalla rete neurale.

In sintesi, il mio progetto su GitHub utilizza una rete neurale per eseguire calcoli speciali. Le reti neurali sono come cervelli artificiali che possono prendere decisioni e risolvere problemi. Spero che questa documentazione semplificata ti aiuti a capire meglio il progetto!

## Documentazione espansa

Ora che hai familiarità con i concetti di base, possiamo approfondire ulteriormente il funzionamento della rete neurale.

La classe "NeuralNetwork" rappresenta la struttura della rete neurale. Quando viene inizializzata, vengono specificati i seguenti parametri:

- **'num_inputs'**: il numero di neuroni di input che accettano le informazioni iniziali.
- **'num_outputs'**: il numero di neuroni di output che producono il risultato finale.
- **'num_hidden'**: il numero di neuroni in ogni livello nascosto.
- **'num_layers'**: il numero di livelli nascosti nella rete neurale.
All'interno del metodo **'create_network()'**, la rete neurale viene costruita come una lista di liste. Iniziamo creando i livelli nascosti. Per ogni livello nascosto, creiamo una lista di neuroni, dove ogni neurone ha il numero di input specificato. In pratica, ciascun neurone nel livello nascosto riceve informazioni da tutti i neuroni del livello di input precedente. Successivamente, creiamo il livello di output, che è una lista di neuroni connessi a tutti i neuroni dell'ultimo livello nascosto. Questo collegamento completo consente alla rete neurale di imparare e risolvere compiti più complessi.

Il metodo **'calculate()'** prende in input un array di valori e calcola l'output della rete neurale. Per farlo, iteriamo attraverso i livelli della rete neurale. Per ogni livello, calcoliamo l'output dei neuroni nel livello corrente utilizzando il metodo **'calculate()'** della classe **'Neuron'**. L'output di ciascun neurone viene raccolto in una lista e utilizzato come input per il calcolo dei neuroni nel livello successivo. Alla fine, l'output dell'ultimo livello (livello di output) viene assegnato all'attributo '**output**' della classe.

La classe "Neuron" rappresenta un singolo neurone all'interno della rete neurale. Ogni neurone ha i seguenti attributi:

- **'weights'**: una lista di pesi, uno per ciascun neurone di input. I pesi rappresentano l'importanza relativa dei valori di input per il neurone.
- **'bias'**: un valore che indica la preferenza o l'inclinazione del neurone verso l'attivazione o l'inattivazione.
Il metodo **'calculate()'** del neurone prende in input un array di valori e calcola l'output del neurone. Questo viene fatto calcolando la somma pesata dei valori di input moltiplicati per i rispettivi pesi. Il risultato viene poi sommato al bias del neurone. Il valore ottenuto rappresenta l'attivazione del neurone e viene restituito come output.

In conclusione, la tua rete neurale utilizza una struttura di rete configurabile con un numero specificato di neuroni di input, neuroni di output, neuroni nascosti e livelli nascosti. Ogni neurone calcola il suo output basato sui pesi dei suoi input e sul bias associato. L'output della rete neurale viene calcolato iterando attraverso i livelli e calcolando l'output dei neuroni in ciascun livello. Questo processo di calcolo degli output della rete neurale ci permette di ottenere una risposta finale basata sugli input forniti.

Le reti neurali sono ampiamente utilizzate per una varietà di compiti, come il riconoscimento di immagini, la previsione del tempo, l'elaborazione del linguaggio naturale e molto altro ancora. Possono imparare dai dati attraverso un processo chiamato "addestramento", dove i pesi dei neuroni vengono regolati gradualmente per adattarsi ai dati di input e produrre risultati più accurati.

Nel tuo progetto, puoi sperimentare diversi parametri come il numero di neuroni di input, il numero di neuroni di output, il numero di neuroni nascosti e il numero di livelli nascosti per adattare la rete neurale alle specifiche esigenze del tuo problema. Puoi anche esplorare tecniche di addestramento come l'algoritmo di retropropagazione per migliorare le prestazioni della rete neurale.

Spero che questa documentazione dettagliata ti abbia dato una migliore comprensione di come la rete neurale funzioni e come può essere personalizzata per adattarsi ai tuoi scopi. Se hai ulteriori domande, non esitare a chiedere!
