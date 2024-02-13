# Programació per a la ciència de dades - PAC 4

Aquest projecte ha estat desenvolupat com a entrega de l'assignatura Programació per a la ciència de dades cursada a la Universitat Oberta de Catalunya durant el curs 2022-2023.

## Índex
- [Programació per a la ciència de dades - PAC 4](#programació-per-a-la-ciència-de-dades---pac-4)
  - [Índex](#índex)
  - [Instalació](#instalació)
    - [Linux i MacOS](#linux-i-macos)
    - [Windows](#windows)
  - [Configuració adicional](#configuració-adicional)
  - [Execució del programa](#execució-del-programa)
  - [Execució dels test](#execució-dels-test)
  - [Execució del pylint](#execució-del-pylint)
  - [Estructura](#estructura)
    - [Mòduls](#mòduls)
      - [data\_frame\_utils.py](#data_frame_utilspy)
      - [file\_utils.py](#file_utilspy)
        - [list\_utils.py](#list_utilspy)
      - [text\_utils.py](#text_utilspy)
      - [tweet\_utils.py](#tweet_utilspy)
      - [analysis\_utils.py](#analysis_utilspy)
    - [Test](#test)
  - [Informe de resultats](#informe-de-resultats)
  - [Llicència](#llicència)
  - [Fonts utilitzades](#fonts-utilitzades)
    - [Exercici 1](#exercici-1)
    - [Exercici 2](#exercici-2)
    - [Exercici 3](#exercici-3)
    - [Exercici 4](#exercici-4)
    - [Exercici 5](#exercici-5)
    - [Exercici 6](#exercici-6)
    - [Testing](#testing)


## Instalació

### Linux i MacOS
Per la execució d'aquest projecte es recomana la utilització d'un entorn virtual. Per a la creació de l'entorn virtual cal executar dins la carpeta desitjada:

```
python3 -m venv nom_de_lentorn
```

Una vegada creat l'entorn virtual ja es pot instalar el projecte.

**1. Iniciar l'entorn virtual.** S'inicia l'entorn virtual amb el que s'executarà tot el projecte:

```
source nom_de_lentorn/bin/activate
```

**2. Instalació de dependències.** Utilitzant el paquet requirement.txt, s'instalen totes les dependències necessàries:

```
pip install -r requirements.txt
```


### Windows
Per la execució d'aquest projecte es recomana la utilització d'un entorn virtual. Per a la creació de l'entorn virtual cal executar dins la carpeta desitjada:

```
python -m venv nom_de_lentorn
```

Una vegada creat l'entorn virtual ja es pot instalar el projecte.

**1. Iniciar l'entorn virtual.** S'inicia l'entorn virtual amb el que s'executarà tot el projecte:

```
nom_de_lentorn\Scripts\activate
```

**2. Instalació de dependències.** A partir d'aquest punt les comandes s'han de realitzar al directori del projecte. Utilitzant el paquet requirement.txt, s'instalen totes les dependències necessàries:

```
pip install -r requirements.txt
```


## Configuració adicional

Per tal de poder executar correctament el projecte, és necessari incloure al projecte una carpeta "data" que contingui l'arxiu twitter_reduced.zip. Cal que aquesta carpeta no estigui on es mostra a l'apartat d'estructura.


## Execució del programa

Aquest programa s'ha estructurat per a que es puguin obtenir tots els resultats dels diferents exercicis mitjançant la execució del fitxer main.py. El programa s'executa desde el terminal, situats a la carpeta del projecte mitjançant el següent:

```
python main.py
```

## Execució dels test

Per a la execució dels unit test del projecte s'ha d'utilitzar la següent comanda desde la consola desde la carpeta del projecte:

```
python run_test.py
```
Amb l'execucució d'aquest script es un informe sobre les proves, aquest arxiu és test_report.html

A banda d'això, també es mostra per consola un resum dels resultats del test i un resum del coverage de cada script/mòdul. Per veure més en detall el coverage del codi es genera un informe per cada arxiu dins la carpeta 'coverage_report'.

## Execució del pylint
Per a desenvolupar aquesta entrega s'ha utilitzat un autoformatejador de codi que és autopep8. L'unic inconvenient és que el formateig el fa per un màxim de 120 caracters en comptes de 79. De totes maneres s'ha intentat revisar tots els arxius per a que no superin els 79 caracters, els únics que no ha estat possible fer-ho ha estat els de test ja que al separar una cadena en dues linies, tot i utilitzar ''' ''' per fer cadenes en bloc, el test ho entenia com un \n fent fallar els test. Es pot executar pylint per a tenir un resum dels errors d'estil que s'han fet al codi. Per a executar-ho es pot utilitzar:
```
pylint main.py utils
```
Cal remarcar que s'ha afegit un document [.pylintrc](.pylintrc) per a que pylint no detecti com a noms de variable incorrectes df, e i n. De totes maneres pel que he pogut comprovar de vegades quan s'instala el projecte, no acaba de detectar l'arxiu i salten els errors relacionats amb la nomenclatura d'aquestes varibales.

Observació: a l'arxiu main.py hi ha una variable vocabulary que no s'utilitza. A nivell d'estil hagués estat més correcte posar un nom com _ per deixar clar que no s'utilitza, de totes maneres s'ha preferit que el nom fos descriptiu ja que és la resposta a un dels exercicis.

## Estructura

```
├──  README.md
├──  main.py
├──  run_test.py
├──  requirements.txt
├──  report.pdf
├──  .pylintrc
├──  LICENSE.txt
├──  utils
│    ├──  analysis_utils.py
│    ├──  constants.py
│    ├──  data_frame_utils.py
│    ├──  file_utils.py
│    ├──  list_utils.py
│    ├──  text_utils.py
│    └──  tweet_utils.py
│
├──  data
│    └──  twitter_reduced.zip
│
└──  test
     ├──  analysis_utils_test.py
     ├──  constants_test.py
     ├──  data_frame_utils_test.py
     ├──  file_utils_test.py
     ├──  list_utils_test.py
     ├──  text_utils_test.py
     ├──  tweet_utils_test.py
     ├──  main_test.py
     └──  test_files
          ├──  test.csv
          └──  test.zip
```

### Mòduls

Per a la realització d'aquesta PAC s'han utilitzat diferents mòduls. Aquests mòduls es troben dins la carpeta utils. El contingut dels mòduls és el següent:

#### data_frame_utils.py

Aquest mòdul proporciona funcions d'utilitat per a la manipulació de Pandas DataFrame.

- **get_unique_clusters(data_frame, column)**: Retorna els clústers únics d'un DataFrame basant-se en la columna especificada.
- **calculate_missing_pct(data_frame, column)**: Calcula el percentatge de valors mancants en una columna específica del DataFrame.
- **drop_na(data_frame, column)**: Elimina les files amb valors mancants en la columna especificada d'un DataFrame.
- **df_column_to_dict(data_frame, column)**: Converteix una columna de diccionari en un DataFrame de format de cadena a format de diccionari.

#### file_utils.py

Aquest mòdul està dedicat a les operacions de gestió de fitxers.

- **unzip_file(zip_path, output_path)**: Descomprimeix un fitxer a la ruta de sortida especificada.
- **read_csv_to_dict_list(file_path)**: Llegeix un fitxer CSV i retorna el seu contingut com a llista de diccionaris.
- **dict_list_to_csv(out_path, dataset)**: Escriu una llista de diccionaris en un fitxer CSV.
- **csv_to_df(file_path)**: Converteix un fitxer CSV en un DataFrame.
- **set_file_path(base_dir, file_name)**: Crea una ruta de fitxer completa concatenant el directori base i el nom del fitxer.

##### list_utils.py

Aquest mòdul conté funcions de processament de llistes.

- **apply_function_to_list(func, lst, *kwargs)**: Aplica una funció a cada element d'una llista i retorna els resultats en una nova llista.
- **print_list(lst, n = 5)**: Imprimeix els primers 'n' elements d'una llista si 'n' és positiu, o els últims 'n' elements si 'n' és negatiu.

#### text_utils.py

Aquest mòdul conté funcions de processament de text.

- **normalize_text(text)**: Neteja una cadena de text donada convertint-la a minúscules i eliminant caràcters especials.
- **remove_urls(text)**: Elimina les URL d'una cadena de text donada.
- **delete_words(text, words_list)**: Esborra certes paraules d'una cadena de text donada.
- **count_words(words)**: Compta la freqüència de cada paraula en una llista de paraules donada.
- **split_string(text)**: Divideix una cadena de text donada en una llista de paraules.

#### tweet_utils.py

Aquest mòdul conté funcions de processament de dades de tweets.

- **normalize_tweet(tweet)**: Normalitza el text d'un diccionari de tweets donat.
- **clean_tweet(tweet, words_list)**: Neteja el text d'un diccionari de tweets donat eliminant certes paraules.
- **add_vocab(words, vocab)**: afegix paraules noves d'una llista donada a una llista de vocabulari.
- **tweet_vocab(tweet, vocab)**: Calcula el recompte de paraules d'un tweet i actualitza el vocabulari.
- **add_frequencies_to_tweets(tweets, frequencies)**: Afegeix una clau 'words' a cada diccionari de tweet, amb les freqüències corresponents.

#### analysis_utils.py

Aquest mòdul està dedicat a la generació i visualització de núvols de paraules.

- **set_word_clouds_and_frequency_dicts(df, clusters, cluster_col, freq_col)**: Genera núvols de paraules i diccionaris de freqüències per a cada cluster.
- **show_word_clouds(word_clouds)**: Mostra núvols de paraules per a cada cluster.
- **get_most_common_words(freq_dicts, words_num=25)**: Obté les paraules més comunes i les seves freqüències per a cada cluster.
- **plot_word_frequencies(words_freq, cluster_name)**: Genera histogramas per a cada cluster.

### Test
Per al desenvolupament d'aquesta entrega, s'han realitzat unit test per gairebé totes les funcions que es troben a "utils". No s'han realitzat aquests test unitaris per a les funcions que mostren una gràfica o imatge. La estructura dels test és equivalent a la dels mòduls, s'ha creat un fitxer per a cada mòdul i aquests fitxers es troben dins la carpeta test. En el desenvolupament d'aquests unit test, s'ha decidit utilitzar petites mostres de dades per a provar les funcionalitats en comptes d'utilitzar totes les dades del problema pels següents motius:

- Utilitzant mostres de dades "inventades" es pot cubrir un gran nombre de possibles escenaris utilitzant una bateria de dades realment petites. 
- Fa que sigui possible provar funcionalitats a molt baix nivell la qual cosa fa que sigui més fàcil depurar els test i trobar els possibles errors
- Al treballar amb un gran nombre de dades, moltes vegades dependrem d'eines externes per a validar els resultats d'aquests test
- Les dades d'un programa han de poder canviar en el temps, i tot i així els test haurien de seguir funcionant. En un cas real, si basem les proves en les dades reals, cada vegada que canviin els test s'han de modificar
- Al utilitzar un mock, les dades són fàcilment modificables i per tant tenim a l'abast afegir casos frontera que potser no tenim en les nostres dades actualment però que poden fer fallar el codi en un futur.

Tot i això sí que s'han realitzat test amb les dades reals per als exercicis que no necessitaven inputs directes d'altres exercicis, en aquest cas son l'exercici 1, 2, 3 i 5. Aquest test es troben dins l'arxiu main_test.py dins la carpeta test i s'executa conjuntament amb la resta de test.

Degut a problemes de compatibilitat amb la llibreria HtmlTestRunner, s'ha utilitzat la llibreria pytest.

## Informe de resultats
Els resultats d'aquesta PAC es troben resumits a l'arxiu [report.pdf](report.pdf)


## Llicència

Aquest projecte està llicenciat sota la [Llicència Creative Commons Attribution 4.0 International](LICENSE.txt). Si us plau, consulta l'arxiu de la llicència per a més detalls.

## Fonts utilitzades
### Exercici 1
[Convert CSV to dictionary list](https://www.pythonforbeginners.com/basics/read-csv-into-list-of-dictionaries-in-python)

### Exercici 2

[Ignore case in Regex](https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile)

[Regex for url](https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url)

### Exercici 3

[Update a set](https://www.programiz.com/python-programming/methods/set/update)

[Create a frequency dict](https://stackoverflow.com/questions/21852066/counting-word-frequency-and-making-a-dictionary-from-it)

### Exercici 4

[Convert dict to csv](https://docs.python.org/3/library/csv.html#csv.DictWriter)

### Exercici 5

[Convert a df column from string to dictionary](https://stackoverflow.com/questions/39169718/convert-string-to-dict-then-access-keyvalues-how-to-access-data-in-a-class)

[How to use wordcloud](https://amueller.github.io/word_cloud/cli.html)

[wordcloud examples](https://www.datacamp.com/tutorial/wordcloud-python)

[How to update a frequency dict with another frequency dict](https://stackoverflow.com/questions/73522306/update-existing-counter-with-item-frequencies-from-another-list)

[Get n maximum values of dictionary](https://stackoverflow.com/questions/7197315/5-maximum-values-in-a-python-dictionary)

### Exercici 6
[Plot a histogram from a frequency dictionary](https://stackoverflow.com/questions/21195179/plot-a-histogram-from-a-dictionary)


### Testing
[Documentation Pytest](https://realpython.com/pytest-python-testing/)

[Create a report using Pytest](https://www.tutorialspoint.com/selenium_webdriver/selenium_webdriver_generating_html_test_reports_in_python.htm)

[Generate coverage report](https://www.lambdatest.com/blog/pytest-code-coverage-report/)