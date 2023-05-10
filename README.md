# Documentazione del progetto "Neural Network Trainer"
Il progetto "Neural Network Trainer" è un'applicazione che permette di addestrare una rete neurale utilizzando un dataset e successivamente calcolare l'output corrispondente per un dato set di input.

## Requisiti
- Python 3.x

- Librerie Python: numpy, argparse

## Installazione
1. Clonare il repository del progetto:
	```` bash
	git clone <URL del repository>
	````

2. Creare un ambiente virtuale e attivarlo:
	```` bash
	python3 -m venv env
	source env/bin/activate
	````

3. Installare le dipendenze:
	```` bash
	pip install -r requirements.txt
	```` 

## Utilizzo
Il programma principale si trova nel file '**main.py**'. Puoi eseguirlo da riga di comando specificando diversi argomenti:

```` bash
python main.py --num_inputs <num_inputs> --num_outputs <num_outputs> --num_hidden <num_hidden> --num_layers <num_layers> --dataset <dataset_file> --epochs <num_epochs> --learning_rate <learning_rate>
```` 

- **'--num_inputs'**: il numero di neuroni di input della rete neurale (valore predefinito: 2)
- **'--num_outputs'**: il numero di neuroni di output della rete neurale (valore predefinito: 1)
- **'--num_hidden'**: il numero di neuroni nel livello nascosto della rete neurale (valore predefinito: 2)
- **'--num_layers'**: il numero di livelli nascosti nella rete neurale (valore predefinito: 1)
- **'--dataset'**: il percorso al file CSV contenente il dataset di addestramento (valore predefinito: dataset.csv)
- **'--epochs'**: il numero di epoche di addestramento (valore predefinito: 100)
- **'--learning_rate'**: il tasso di apprendimento per l'addestramento (valore predefinito: 0.1)

## Dataset
Il dataset di addestramento deve essere un file CSV valido. Ogni riga del file rappresenta un esempio di addestramento, con i valori di input seguiti dal valore di output desiderato.

## Addestramento
Durante l'addestramento, la rete neurale utilizza l'algoritmo di discesa del gradiente con retropropagazione dell'errore per aggiornare i pesi in base all'errore commesso. Viene eseguito un numero specificato di epoche di addestramento utilizzando il dataset fornito.

## Calcolo dell'output
Dopo l'addestramento, è possibile calcolare l'output corrispondente a un dato set di input utilizzando la rete neurale addestrata.

## Esempio
Di seguito è riportato un esempio di esecuzione del programma:

```` bash
python main.py --num_inputs 2 --num_outputs 1 --num_hidden 2 --num_layers 1 --dataset dataset.csv --epochs 100 --learning_rate 0.1
````

## Conclusioni
Il progetto "Neural Network Trainer offre un'implementazione semplice ma funzionale di una rete neurale. Può essere utilizzato per addestrare reti neurali su dataset di piccole dimensioni e calcolare gli output corrispondenti per dati di input specifici.

La modularità del codice consente di personalizzare facilmente il numero di neuroni di input, di output e nascosti, nonché il numero di livelli nascosti della rete neurale. Inoltre, è possibile specificare il file CSV del dataset di addestramento, il numero di epoche di addestramento e il tasso di apprendimento come argomenti da linea di comando.

Si consiglia di esplorare ulteriormente il codice sorgente per comprendere meglio il funzionamento interno della classe NeuralNetwork e della classe Neuron, nonché l'implementazione dell'algoritmo di addestramento e del calcolo dell'output.

Per ulteriori informazioni, fare riferimento alla documentazione delle librerie utilizzate, come numpy per la manipolazione di array multidimensionali e argparse per il parsing degli argomenti da linea di comando.

## Limitazioni
È importante notare che questa implementazione è pensata per scopi didattici o per problemi semplici. In scenari più complessi o con dataset di grandi dimensioni, potrebbe essere necessario utilizzare librerie specializzate per il deep learning, come TensorFlow o PyTorch, che offrono funzionalità avanzate e ottimizzazioni per reti neurali complesse.

Inoltre, il progetto attuale non include funzionalità come la regolarizzazione, la normalizzazione dei dati o la gestione di tipi di dato diversi. Queste sono considerazioni importanti da prendere in considerazione quando si lavora con reti neurali in contesti reali.
## Contributi
Sono benvenuti contributi per migliorare questo progetto. Se desideri contribuire, puoi aprire una pull request nel repository del progetto indicando le modifiche apportate e la motivazione dietro di esse.

## Licenza
Il progetto è concesso in licenza secondo i termini della licenza MIT. Fare riferimento al file LICENSE per ulteriori dettagli.



innanzitutto, è stato aggiunto un nuovo parametro al costruttore della classe NeuralNetwork, chiamato use_memory, che indica se la rete neurale deve utilizzare la memoria o meno. Di default, use_memory è impostato su False.

La classe MemoryNeuron è stata introdotta come una sottoclasse di Neuron per rappresentare i neuroni con memoria. Oltre ai pesi e al bias, MemoryNeuron ha anche un attributo aggiuntivo chiamato state, che rappresenta lo stato interno del neurone.

La funzione create_network() nella classe NeuralNetwork è stata modificata per creare neuroni normali (Neuron) o neuroni con memoria (MemoryNeuron) a seconda del valore di use_memory. Inoltre, i neuroni dell'ultimo strato (output layer) sono ora creati come MemoryNeuron se use_memory è impostato su True.

Nella classe MemoryNeuron, il metodo calculate() è stato sovrascritto per aggiungere lo stato interno (self.state) al risultato del calcolo del neurone.

Il metodo backpropagate() nella classe MemoryNeuron è stato esteso per aggiornare anche lo stato interno (self.state) durante il processo di retropropagazione dell'errore.

Nello script main.py, è stata aggiunta l'opzione --use_memory come argomento del programma. Se questa opzione viene specificata durante l'esecuzione dello script, viene creato un oggetto NeuralNetwork che utilizza la memoria.

Ad esempio, per creare una rete neurale con memoria, puoi eseguire lo script come segue:

	'''bash
	python main.py --num_inputs 2 --num_outputs 1 --num_hidden 2 --num_layers 1 --use_memory
	'''
In questo modo, verrà creata una rete neurale con memoria, in cui i neuroni utilizzano uno stato interno per memorizzare informazioni.




Certamente! Consideriamo un esempio in cui una rete neurale con memoria potrebbe essere utile. Supponiamo di voler creare un modello per la previsione delle vendite giornaliere di un negozio al dettaglio, prendendo in considerazione vari fattori come la stagionalità, gli eventi speciali, le promozioni passate e così via.

In questo caso, una rete neurale con memoria potrebbe essere adatta per affrontare il problema. La memoria della rete consentirebbe di considerare i dati storici delle vendite e di catturare le relazioni complesse tra i fattori che influenzano le vendite.

Ad esempio, la rete potrebbe prendere in input i dati delle vendite degli ultimi sette giorni, insieme a informazioni aggiuntive come la stagionalità (es. giorno della settimana, mese) e gli eventi speciali (es. festività). La rete avrebbe una serie di strati ricorrenti (come le celle LSTM o GRU) che mantengono la memoria delle informazioni storiche. Questa memoria consentirebbe alla rete di catturare pattern e tendenze a lungo termine nelle vendite.

Durante la fase di addestramento, la rete neurale con memoria apprenderebbe come le diverse variabili influiscono sulle vendite giornaliere e come esse interagiscono tra loro nel corso del tempo. Una volta addestrata, la rete sarebbe in grado di prendere in input i dati correnti (come la stagionalità e gli eventi speciali) insieme alle informazioni storiche e fare previsioni accurate sulle vendite future.

In questo caso, l'utilizzo di una rete neurale con memoria permetterebbe di sfruttare al meglio le informazioni storiche e il contesto temporale per migliorare le previsioni delle vendite rispetto a una rete senza memoria, che potrebbe avere difficoltà a catturare le relazioni complesse e a considerare l'effetto delle informazioni storiche sulle vendite future.

Quindi, in scenari in cui il contesto storico è importante e l'andamento dipende da relazioni complesse nel tempo, l'utilizzo di una rete neurale con memoria può essere molto vantaggioso per ottenere previsioni più accurate.
