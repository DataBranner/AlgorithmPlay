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

Anagrammic equivalence between two words is determined by stripping punctuation, converting all characters to lower-case, and sorting the characters — producing an "alphagram" of each word. See "Decisions" below for more information.

There are three versions of the program: 

 * `anagrams.py`, which uses dictionaries to count alphagrams quickly;
 * `anagrams_1.py`, which iterates through sets of words to find anagrams (slower than `anagrams.py`);
 * `anagrams_2.py`, a much less efficient version of `anagrams_1.py`.

File `anagrams.py` is by far the most efficient version, as shown in the Timing section below.

### Decisions

 1. Data file is located in `DATA/`. Unlike the example in the statement of the problem, this version does not accept a source dictionary file on the command line.
 1. I find two words containing hyphens in my dictionary file, so all words must be compared in a "cleaned" version only — stripped of hyphens and made lower-case. But words found to be anagrams must still be added in their original, uncleaned forms, i.e, with any hyphens and with original capitalization.
 1. Please introspect to see a few optional arguments to `main()`.

### Timing

~~~
time ./anagrams.py
...
real    0m0.881s
user    0m0.861s
sys	    0m0.016s

time ./anagrams_1.py
...
real 16.85
user 16.83
sys 0.02

time ./anagrams_2.py
...
real 364.65
user 364.56
sys 0.10
~~~

### Output

~~~
Top 20 most anagrammable 4-letter words:

['Antu', 'antu', 'aunt', 'naut', 'taun', 'Tuan', 'tuan', 'Tuna', 'tuna']
['ante', 'Aten', 'etna', 'Nate', 'neat', 'taen', 'tane', 'tean']
['aril', 'lair', 'Lari', 'lari', 'liar', 'lira', 'rail', 'rial']
['alem', 'alme', 'lame', 'leam', 'Male', 'male', 'meal', 'mela']
['Abel', 'able', 'albe', 'bale', 'beal', 'bela', 'blae']
['amin', 'main', 'mani', 'mian', 'Mina', 'mina', 'Naim']
['Amir', 'amir', 'Irma', 'Mari', 'Mira', 'rami', 'rima']
['Sart', 'sart', 'Star', 'star', 'stra', 'tars', 'tsar']
['sawt', 'staw', 'Swat', 'swat', 'taws', 'twas', 'wast']
['atle', 'laet', 'late', 'leat', 'tael', 'tale', 'teal']
['emir', 'Imer', 'mire', 'reim', 'Remi', 'riem', 'rime']
['royt', 'ryot', 'Tory', 'tory', 'Troy', 'troy', 'tyro']
['Dale', 'dale', 'deal', 'lade', 'Lead', 'lead', 'Leda']
['mate', 'meat', 'meta', 'Tame', 'tame', 'team', 'Tema']
['Amen', 'amen', 'enam', 'mane', 'mean', 'name', 'nema']
['Adin', 'Andi', 'dain', 'Dani', 'Dian', 'dian', 'naid']
['alen', 'lane', 'lean', 'Lena', 'nael', 'Neal', 'neal']
['Earl', 'earl', 'eral', 'Lear', 'lear', 'Real', 'real']
['Elon', 'enol', 'leno', 'Leon', 'lone', 'Noel', 'noel']
['iter', 'reit', 'rite', 'Teri', 'tier', 'tire']

Top 20 most anagrammable 5-letter words:

['angor', 'argon', 'goran', 'grano', 'groan', 'nagor', 'Orang', 'orang', 'organ', 'rogan', 'Ronga']
['Elaps', 'lapse', 'Lepas', 'Pales', 'salep', 'saple', 'sepal', 'slape', 'spale', 'speal']
['armet', 'mater', 'Merat', 'metra', 'ramet', 'tamer', 'terma', 'trame', 'Trema']
['ester', 'estre', 'reest', 'reset', 'steer', 'stere', 'stree', 'terse', 'tsere']
['caret', 'carte', 'cater', 'crate', 'creat', 'creta', 'react', 'recta', 'trace']
['leapt', 'palet', 'patel', 'pelta', 'petal', 'plate', 'pleat', 'tepal']
['arist', 'astir', 'sitar', 'stair', 'stria', 'tarsi', 'tisar', 'Trias']
['alert', 'alter', 'artel', 'later', 'ratel', 'taler', 'telar']
['lepra', 'paler', 'parel', 'parle', 'pearl', 'Perla', 'relap']
['least', 'setal', 'slate', 'stale', 'steal', 'stela', 'tales']
['inset', 'neist', 'snite', 'Stein', 'stein', 'stine', 'tsine']
['alien', 'Aline', 'anile', 'elain', 'Elian', 'laine', 'linea']
['Alban', 'alban', 'Balan', 'banal', 'Laban', 'Nabal', 'nabla']
['dater', 'derat', 'detar', 'drate', 'rated', 'trade', 'tread']
['argel', 'ergal', 'garle', 'glare', 'lager', 'large', 'regal']
['agnel', 'angel', 'angle', 'Galen', 'genal', 'glean', 'lagen']
['Alcor', 'calor', 'Carlo', 'Carol', 'carol', 'claro', 'coral']
['Darin', 'dinar', 'drain', 'Indra', 'nadir', 'ranid']
['roset', 'Rotse', 'Soter', 'stero', 'store', 'torse']
['acrid', 'caird', 'carid', 'Darci', 'daric', 'Dirca']

Top 20 most anagrammable 6-letter words:

['asteer', 'Easter', 'easter', 'Eastre', 'reseat', 'saeter', 'seater', 'staree', 'teaser', 'Teresa']
['acinar', 'arnica', 'Canari', 'canari', 'Carian', 'carina', 'Crania', 'crania', 'narica']
['laster', 'lastre', 'rastle', 'relast', 'resalt', 'salter', 'slater', 'stelar']
['arpent', 'enrapt', 'entrap', 'panter', 'parent', 'pretan', 'trepan']
['Aldine', 'aldine', 'Daniel', 'Delian', 'denial', 'enalid', 'leadin']
['albeit', 'albite', 'baltei', 'Belait', 'betail', 'Bletia', 'libate']
['darter', 'dartre', 'redart', 'retard', 'retrad', 'tarred', 'trader']
['agroan', 'Angora', 'Anogra', 'arango', 'Argoan', 'Onagra', 'onagra']
['aldern', 'darnel', 'enlard', 'lander', 'lenard', 'randle', 'reland']
['canter', 'creant', 'Cretan', 'nectar', 'recant', 'tanrec', 'trance']
['angler', 'Arleng', 'garnel', 'largen', 'rangle', 'regnal']
['arrect', 'Carter', 'carter', 'crater', 'recart', 'tracer']
['balder', 'bardel', 'bedlar', 'bedral', 'belard', 'blader']
['calmer', 'Carmel', 'clamer', 'Marcel', 'marcel', 'mercal']
['alerse', 'leaser', 'reales', 'resale', 'reseal', 'sealer']
['daimen', 'damine', 'maiden', 'Median', 'median', 'Medina']
['alevin', 'alvine', 'valine', 'veinal', 'venial', 'vineal']
['corset', 'Cortes', 'coster', 'escort', 'scoter', 'sector']
['Casper', 'escarp', 'parsec', 'scrape', 'secpar', 'spacer']
['Altair', 'atrail', 'atrial', 'lariat', 'latria', 'talari']
~~~
[end]
