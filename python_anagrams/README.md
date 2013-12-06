## Anagram problem

### Assignment

~~~
Given a "dictionary" (in the conventional natural language sense), output the top 20 most "anagrammable" 4-, 5-, and 6-letter words, e.g.

    $ ./anagrams.py /usr/share/dict/words

    Top 20 most anagrammable 4-letter words:

      ['aril', 'lair', 'lari', 'liar', 'lira', 'rail', 'rial']

      ['alem', 'alme', 'lame', 'leam', 'male', 'meal', 'mela']

      ['atle', 'laet', 'late', 'leat', 'tael', 'tale', 'teal']

      ['sawt', 'staw', 'swat', 'taws', 'twas', 'wast']

      ['ates', 'east', 'eats', 'sate', 'seat', 'seta']

      ['antu', 'aunt', 'naut', 'taun', 'tuan', 'tuna']

      ['amen', 'enam', 'mane', 'mean', 'name', 'nema']

      ['able', 'albe', 'bale', 'beal', 'bela', 'blae']

      ['ante', 'etna', 'neat', 'taen', 'tane', 'tean']

      ['hart', 'rath', 'tahr', 'thar', 'trah']

      ...

    Top 20 most anagrammable 5-letter words:

      ...
~~~

### To run

~~~
./anagrams.py
~~~

### Design

Anagrammic equivalence between two words is determined by stripping punctuation, forcing to all lower-case, and sorting the characters — producing and "alphagram" of each word. 

There are three versions of the program: 

 * `anagrams.py`, which uses dictionaries to count alphagrams quickly;
 * `anagrams_1.py`, which iterates through sets of words to find anagrams (slower than `anagrams.py`);
 * `anagrams_2.py`, a much less efficient version of `anagrams_1.py`.

`anagrams.py` is by far the most efficient version, as shown in the Timing section, below.

### Decisions

 1. Data file is located in `DATA/`. Unlike the example in the statement of the problem, this version does not accept a source dictionary file on the command line.
 1. I find two words containing hyphens in my dictionary file, so all words must be compared in a "cleaned" version only — stripped of hyphens and made lower-case. But words found to be anagrams must still be added in their original, uncleaned forms, i.e, with any hyphens and with original capitalization.
 1. Please introspect to see a few optional arguments to `main()`.

### Timing

~~~
time -p ./anagrams.py
...
real 0.86
user 0.84
sys 0.01

time -p ./anagrams_1.py
...
real 16.85
user 16.83
sys 0.02

time -p ./anagrams_2.py
...
real 364.65
user 364.56
sys 0.10
~~~

### Output

~~~
Top 20 most anagrammable 4-letter words:

['Antu', 'antu', 'aunt', 'naut', 'taun', 'Tuan', 'tuan', 'Tuna', 'tuna']
['aril', 'lair', 'Lari', 'lari', 'liar', 'lira', 'rail', 'rial']
['alem', 'alme', 'lame', 'leam', 'Male', 'male', 'meal', 'mela']
['ante', 'Aten', 'etna', 'Nate', 'neat', 'taen', 'tane', 'tean']
['Abel', 'able', 'albe', 'bale', 'beal', 'bela', 'blae']
['emir', 'Imer', 'mire', 'reim', 'Remi', 'riem', 'rime']
['Sart', 'sart', 'Star', 'star', 'stra', 'tars', 'tsar']
['amin', 'main', 'mani', 'mian', 'Mina', 'mina', 'Naim']
['Amir', 'amir', 'Irma', 'Mari', 'Mira', 'rami', 'rima']
['Adin', 'Andi', 'dain', 'Dani', 'Dian', 'dian', 'naid']
['sawt', 'staw', 'Swat', 'swat', 'taws', 'twas', 'wast']
['Dale', 'dale', 'deal', 'lade', 'Lead', 'lead', 'Leda']
['Elon', 'enol', 'leno', 'Leon', 'lone', 'Noel', 'noel']
['Earl', 'earl', 'eral', 'Lear', 'lear', 'Real', 'real']
['atle', 'laet', 'late', 'leat', 'tael', 'tale', 'teal']
['alen', 'lane', 'lean', 'Lena', 'nael', 'Neal', 'neal']
['royt', 'ryot', 'Tory', 'tory', 'Troy', 'troy', 'tyro']
['mate', 'meat', 'meta', 'Tame', 'tame', 'team', 'Tema']
['Amen', 'amen', 'enam', 'mane', 'mean', 'name', 'nema']
['amil', 'amli', 'Lima', 'mail', 'mali', 'mila']
['alin', 'anil', 'lain', 'Lina', 'lina', 'nail']

Top 20 most anagrammable 5-letter words:

['angor', 'argon', 'goran', 'grano', 'groan', 'nagor', 'Orang', 'orang', 'organ', 'rogan', 'Ronga']
['Elaps', 'lapse', 'Lepas', 'Pales', 'salep', 'saple', 'sepal', 'slape', 'spale', 'speal']
['caret', 'carte', 'cater', 'crate', 'creat', 'creta', 'react', 'recta', 'trace']
['ester', 'estre', 'reest', 'reset', 'steer', 'stere', 'stree', 'terse', 'tsere']
['armet', 'mater', 'Merat', 'metra', 'ramet', 'tamer', 'terma', 'trame', 'Trema']
['arist', 'astir', 'sitar', 'stair', 'stria', 'tarsi', 'tisar', 'Trias']
['leapt', 'palet', 'patel', 'pelta', 'petal', 'plate', 'pleat', 'tepal']
['dater', 'derat', 'detar', 'drate', 'rated', 'trade', 'tread']
['inset', 'neist', 'snite', 'Stein', 'stein', 'stine', 'tsine']
['Alban', 'alban', 'Balan', 'banal', 'Laban', 'Nabal', 'nabla']
['argel', 'ergal', 'garle', 'glare', 'lager', 'large', 'regal']
['agnel', 'angel', 'angle', 'Galen', 'genal', 'glean', 'lagen']
['lepra', 'paler', 'parel', 'parle', 'pearl', 'Perla', 'relap']
['least', 'setal', 'slate', 'stale', 'steal', 'stela', 'tales']
['alert', 'alter', 'artel', 'later', 'ratel', 'taler', 'telar']
['Alcor', 'calor', 'Carlo', 'Carol', 'carol', 'claro', 'coral']
['alien', 'Aline', 'anile', 'elain', 'Elian', 'laine', 'linea']
['adlet', 'dealt', 'Delta', 'delta', 'lated', 'taled']
['actor', 'corta', 'Croat', 'rocta', 'taroc', 'troca']
['Ascot', 'ascot', 'coast', 'costa', 'tacso', 'tasco']
['grein', 'Inger', 'nigre', 'regin', 'reign', 'ringe']

Top 20 most anagrammable 6-letter words:

['asteer', 'Easter', 'easter', 'Eastre', 'reseat', 'saeter', 'seater', 'staree', 'teaser', 'Teresa']
['acinar', 'arnica', 'Canari', 'canari', 'Carian', 'carina', 'Crania', 'crania', 'narica']
['laster', 'lastre', 'rastle', 'relast', 'resalt', 'salter', 'slater', 'stelar']
['canter', 'creant', 'Cretan', 'nectar', 'recant', 'tanrec', 'trance']
['darter', 'dartre', 'redart', 'retard', 'retrad', 'tarred', 'trader']
['aldern', 'darnel', 'enlard', 'lander', 'lenard', 'randle', 'reland']
['arpent', 'enrapt', 'entrap', 'panter', 'parent', 'pretan', 'trepan']
['Aldine', 'aldine', 'Daniel', 'Delian', 'denial', 'enalid', 'leadin']
['agroan', 'Angora', 'Anogra', 'arango', 'Argoan', 'Onagra', 'onagra']
['albeit', 'albite', 'baltei', 'Belait', 'betail', 'Bletia', 'libate']
['Israel', 'relais', 'resail', 'sailer', 'serail', 'serial']
['alevin', 'alvine', 'valine', 'veinal', 'venial', 'vineal']
['arrect', 'Carter', 'carter', 'crater', 'recart', 'tracer']
['Casper', 'escarp', 'parsec', 'scrape', 'secpar', 'spacer']
['daimen', 'damine', 'maiden', 'Median', 'median', 'Medina']
['Altair', 'atrail', 'atrial', 'lariat', 'latria', 'talari']
['calmer', 'Carmel', 'clamer', 'Marcel', 'marcel', 'mercal']
['alerse', 'leaser', 'reales', 'resale', 'reseal', 'sealer']
['angler', 'Arleng', 'garnel', 'largen', 'rangle', 'regnal']
['balder', 'bardel', 'bedlar', 'bedral', 'belard', 'blader']
['corset', 'Cortes', 'coster', 'escort', 'scoter', 'sector']~~~

### Another idea

Another approach I thought of is to use a dictionary to count anagrams — one dictionary per word-length. Dictionaries are useful for counting things.

That saves time over repeatedly running through each set of words looking for anagrams, as in my code. You place each distinct alphagram into a key, and its value is a list of all the words that are anagrams of it. In this case, you only need to treat each word a total of once, in order to insert it into dictionary.

The slow part would be determining the largest lists in each dictionary — as far as I can see, you have to traverse the whole dictionary once, keeping track of the `top_quant_to_print = 20` longest values by one means or another. You can do this step with a second dictionary, maybe, using the cardinality of each value in the first dictionary as the key in the second dictionary; the value in the second dictionary would be the list of alphagram-keys from the first dictionary.

To return the top `top_quant_to_print = 20` values, you convert the keys of the second dictionary to a list, sort, and then retrieve the pertinent alphagrams from the high end of the sorted list. Those alphagrams allow you to retrieve the actual words in question from the first dictionary.
 
[end]
