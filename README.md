
# Neural Network Trainer

This project is a neural network trainer that performs image processing and classification. It trains a neural network on a given dataset of images and saves the trained model for future use.

## Installation

To use this project, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/momysnow/rete_neurale.git
   ``` 

2.  Install the required dependencies. You can use `pip` to install them:
    
    ```shell
    pip install -r requirements.txt
    ``` 
    

## Usage

The trainer can be executed from the command line using the `trainer.py` script. It accepts various command-line arguments to configure the neural network and training process.

```shell
python trainer.py --num_inputs 2 --num_outputs 1 --num_hidden 2 --num_layers 1 --use_memory --image_paths path/to/images --image_size 64 --kernel_size 3 --pool_size 2 --epochs 100 --learning_rate 0.1 --save_model --model_file model.pkl
```

The available command-line arguments are:

-   `--num_inputs`: Number of input neurons.
-   `--num_outputs`: Number of output neurons.
-   `--num_hidden`: Number of neurons in the hidden layer.
-   `--num_layers`: Number of hidden layers.
-   `--use_memory`: Use neurons with memory.
-   `--image_paths`: Paths to the input images.
-   `--image_size`: Dimensione delle immagini di input.
-   `--kernel_size`: Size of the kernel.
-   `--pool_size`: Size of the pooling.
-   `--epochs`: Number of training epochs.
-   `--learning_rate`: Learning rate for training.
-   `--save_model`: Save the trained model.
-   `--model_file`: File path to save the trained model.

## Modules

The project consists of the following modules:

-   `trainer.py`: The main script that controls the training process.
-   `convert_img.py`: Module for image conversion and processing.
-   `neuron.py`: Module containing the neural network and neuron classes.

For detailed information about each module and its functionalities, refer to their respective source code files.

## Overview

Il progetto "Neural Network Trainer" è un'applicazione che utilizza reti neurali per l'elaborazione e la classificazione delle immagini. L'obiettivo principale è quello di allenare una rete neurale su un dataset di immagini fornito dall'utente e salvare il modello allenato per utilizzi futuri.

## Funzionamento

Il funzionamento del progetto può essere suddiviso in diverse fasi:

1.  **Caricamento delle immagini**: L'applicazione carica le immagini di input specificate dall'utente utilizzando il modulo `convert_img.py`. Le immagini vengono ridimensionate a una dimensione specificata e convertite in scala di grigi per semplificare l'elaborazione.
    
2.  **Elaborazione delle immagini**: Dopo il caricamento, le immagini vengono sottoposte a un processo di elaborazione utilizzando tecniche come il filtraggio del kernel e il pooling. Il modulo `convert_img.py` fornisce le funzioni per applicare il filtro del kernel e il pooling alle immagini caricate.
    
3.  **Creazione della rete neurale**: Utilizzando il modulo `neuron.py`, viene creata una rete neurale configurata in base ai parametri specificati dall'utente. La rete neurale può consistere di uno o più strati nascosti, ognuno contenente un numero specificato di neuroni. È anche possibile utilizzare neuroni con memoria.
    
4.  **Allenamento della rete neurale**: La rete neurale viene allenata utilizzando il dataset di immagini elaborate. Durante il processo di allenamento, la rete neurale cerca di adattare i pesi dei collegamenti tra i neuroni per minimizzare l'errore tra l'output previsto e il valore di target corretto. L'algoritmo di retropropagazione dell'errore viene utilizzato per aggiornare i pesi e il bias dei neuroni.
    
5.  **Salvataggio del modello**: Alla fine dell'allenamento, è possibile salvare il modello allenato utilizzando il modulo `neuron.py`. Il modello viene serializzato utilizzando il modulo `pickle` e salvato in un file specificato dall'utente per un utilizzo futuro.
    

## Estensioni e Contributi

Il progetto può essere esteso e personalizzato in vari modi. È possibile esplorare diverse architetture di reti neurali, aggiungere nuove funzionalità di elaborazione delle immagini o implementare algoritmi di ottimizzazione diversi per migliorare le prestazioni del modello. I contributi a questo progetto sono i benvenuti! Se hai idee o suggerimenti, non esitare ad aprire una issue o inviare una pull request.

Speriamo che questa breve spiegazione del funzionamento del progetto sia utile per comprendere come utilizzare e contribuire a questa applicazione basata su reti neurali

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/momysnow/rete_neurale/blob/image-classification/LICENSE) file for more information.


Assicurati di personalizzare il codice Markdown con le informazioni specifiche del tuo progetto, come il nome utente nel link del repository e la descrizione delle funzionalità e dei moduli.
