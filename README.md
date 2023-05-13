# Neural Network Trainer

Questo progetto è un trainer di reti neurali che utilizza immagini come input per l'addestramento. Le immagini vengono elaborate e convertite in un formato adatto per l'addestramento della rete neurale.

## Requisiti

- Python 3.x
- OpenCV (cv2)
- NumPy

## Installazione

1. Clonare il repository:

```bash
git clone https://github.com/tuout03/neural-network-trainer.git
```

Accedere alla directory del progetto:
```bash
cd neural-network-trainer
```
Installare le dipendenze:
```bash
pip install -r requirements.txt
```
Utilizzo
Il programma viene eseguito dal file main.py. Ecco un esempio di comando per l'esecuzione:

```bash
python main.py --num_inputs 2 --num_outputs 1 --num_hidden 2 --num_layers 1 --use_memory --image_paths path1.jpg path2.jpg --image_size 64 --kernel_size 3 --pool_size 2 --epochs 100 --learning_rate 0.1 --save_model --model_file model.pkl
```
### Argomenti

**--num_inputs**: Numero di neuroni di input della rete neurale (valore predefinito: 2)

**--num_outputs**: Numero di neuroni di output della rete neurale (valore predefinito: 1)

**--num_hidden**: Numero di neuroni nel layer nascosto della rete neurale (valore predefinito: 2)

**--num_layers**: Numero di layer nascosti della rete neurale (valore predefinito: 1)

**--use_memory**: Utilizza neuroni con memoria (opzione booleana)

**--image_paths**: Percorsi delle immagini di input separati da spazi

**--image_size**: Dimensione delle immagini di input (valore predefinito: 64)

**--kernel_size**: Dimensione del kernel per il filtro (valore predefinito: 3)

**--pool_size**: Dimensione della finestra di pooling (valore predefinito: 2)

**--epochs**: Numero di epoche di addestramento (valore predefinito: 100)

**--learning_rate**: Tasso di apprendimento per l'addestramento (valore predefinito: 0.1)

**--save_model**: Salva il modello addestrato (opzione booleana)

**--model_file**: Percorso del file per salvare il modello addestrato (valore predefinito: model.pkl)

## Contributi
Sono benvenuti i contributi a questo progetto. Se hai suggerimenti, correzioni o miglioramenti, puoi aprire una Issue o inviare una Pull Request.
