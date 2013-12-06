## Anagram problem

### Assignment

~~~
Given a dictionary, output the top 20 most "anagrammable" 4-, 5-, and 6-letter words, e.g.

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

### Decisions

 1. Data file in `DATA/`. Unlike the example in the statement of the problem, this version does not accept a source dictionary file on the command line.
 1. I find two words containing hyphens in my dictionary file, so all words must be compared in a "cleaned" version only — stripped of hyphens and made lower-case. But words found to be anagrams must still be added in their original, uncleaned forms, i.e, with any hyphens and with original capitalization.
 1. Please introspect to see a few optional arguments to `main()`.

### Timing

There are two versions, `anagrams.py` and the original but much less efficient `anagrams_1.py`:

~~~
time -p ./anagrams.py
...
real 16.85
user 16.83
sys 0.02

time -p ./anagrams_1.py
...
real 364.65
user 364.56
sys 0.10
~~~

### Output

~~~
 Top 20 most anagrammable 4-letter words:

['tuan', 'antu', 'aunt', 'Antu', 'Tuna', 'taun', 'Tuan', 'tuna', 'naut'] 

['neat', 'ante', 'etna', 'Nate', 'Aten', 'taen', 'tean', 'tane'] 

['liar', 'lair', 'lari', 'Lari', 'rail', 'rial', 'lira', 'aril'] 

['leam', 'lame', 'alem', 'mela', 'male', 'meal', 'Male', 'alme'] 

['twas', 'wast', 'taws', 'sawt', 'swat', 'Swat', 'staw'] 

['tale', 'leat', 'atle', 'late', 'laet', 'teal', 'tael'] 

['sart', 'tars', 'Sart', 'tsar', 'stra', 'star', 'Star'] 

['name', 'nema', 'mane', 'enam', 'amen', 'mean', 'Amen'] 

['mate', 'team', 'Tema', 'tame', 'meta', 'meat', 'Tame'] 

['lone', 'leno', 'enol', 'Elon', 'noel', 'Leon', 'Noel'] 

['lear', 'earl', 'Earl', 'eral', 'Lear', 'real', 'Real'] 

['lean', 'Lena', 'lane', 'neal', 'alen', 'Neal', 'nael'] 

['albe', 'beal', 'bale', 'blae', 'Abel', 'able', 'bela'] 

['Troy', 'ryot', 'troy', 'tyro', 'royt', 'tory', 'Tory'] 

['Mina', 'mian', 'Naim', 'main', 'amin', 'mina', 'mani'] 

['Mari', 'Irma', 'rima', 'Mira', 'rami', 'amir', 'Amir'] 

['Imer', 'reim', 'riem', 'mire', 'rime', 'Remi', 'emir'] 

['Dian', 'dian', 'naid', 'Dani', 'Andi', 'dain', 'Adin'] 

['Dale', 'lead', 'dale', 'Leda', 'Lead', 'deal', 'lade'] 

['vlei', 'live', 'Levi', 'veil', 'vile', 'evil'] 


Top 20 most anagrammable 5-letter words:

['grano', 'organ', 'orang', 'Ronga', 'angor', 'argon', 'nagor', 'groan', 'rogan', 'Orang', 'goran'] 

['slape', 'salep', 'lapse', 'Lepas', 'Pales', 'Elaps', 'speal', 'saple', 'spale', 'sepal'] 

['reest', 'stere', 'steer', 'ester', 'tsere', 'estre', 'terse', 'reset', 'stree'] 

['ramet', 'metra', 'Merat', 'terma', 'trame', 'armet', 'tamer', 'mater', 'Trema'] 

['creat', 'react', 'crate', 'caret', 'recta', 'trace', 'creta', 'cater', 'carte'] 

['pleat', 'plate', 'leapt', 'palet', 'pelta', 'petal', 'tepal', 'patel'] 

['Trias', 'astir', 'tarsi', 'stair', 'arist', 'sitar', 'stria', 'tisar'] 

['setal', 'least', 'slate', 'steal', 'tales', 'stela', 'stale'] 

['rated', 'trade', 'derat', 'drate', 'dater', 'tread', 'detar'] 

['pearl', 'relap', 'lepra', 'parel', 'Perla', 'paler', 'parle'] 

['neist', 'inset', 'snite', 'stine', 'stein', 'tsine', 'Stein'] 

['nabla', 'alban', 'Balan', 'banal', 'Laban', 'Alban', 'Nabal'] 

['ergal', 'glare', 'lager', 'large', 'garle', 'argel', 'regal'] 

['alter', 'later', 'telar', 'taler', 'artel', 'ratel', 'alert'] 

['Galen', 'glean', 'agnel', 'lagen', 'angle', 'genal', 'angel'] 

['Elian', 'laine', 'elain', 'anile', 'Aline', 'linea', 'alien'] 

['Alcor', 'coral', 'claro', 'carol', 'Carlo', 'calor', 'Carol'] 

['tepor', 'poter', 'prote', 'trope', 'toper', 'repot'] 

['tarse', 'serta', 'teras', 'stare', 'aster', 'strae'] 

['targe', 'grate', 'retag', 'Greta', 'gater', 'great'] 


Top 20 most anagrammable 6-letter words:

['saeter', 'Easter', 'staree', 'easter', 'asteer', 'Eastre', 'reseat', 'seater', 'Teresa', 'teaser'] 

['canari', 'Carian', 'acinar', 'arnica', 'carina', 'Crania', 'Canari', 'narica', 'crania'] 

['lastre', 'stelar', 'slater', 'laster', 'resalt', 'relast', 'salter', 'rastle'] 

['trader', 'retrad', 'darter', 'tarred', 'redart', 'dartre', 'retard'] 

['enrapt', 'trepan', 'entrap', 'panter', 'pretan', 'parent', 'arpent'] 

['darnel', 'lander', 'reland', 'enlard', 'aldern', 'randle', 'lenard'] 

['canter', 'trance', 'nectar', 'tanrec', 'Cretan', 'creant', 'recant'] 

['baltei', 'albite', 'betail', 'libate', 'Bletia', 'albeit', 'Belait'] 

['arango', 'agroan', 'onagra', 'Anogra', 'Angora', 'Argoan', 'Onagra'] 

['Daniel', 'Aldine', 'Delian', 'denial', 'enalid', 'aldine', 'leadin'] 

['sector', 'corset', 'scoter', 'escort', 'Cortes', 'coster'] 

['rangle', 'angler', 'garnel', 'largen', 'Arleng', 'regnal'] 

['parsec', 'scrape', 'spacer', 'secpar', 'escarp', 'Casper'] 

['mercal', 'Marcel', 'Carmel', 'clamer', 'marcel', 'calmer'] 

['maiden', 'median', 'Median', 'Medina', 'daimen', 'damine'] 

['leaser', 'alerse', 'resale', 'reales', 'reseal', 'sealer'] 

['dunair', 'Diurna', 'Danuri', 'durain', 'Durani', 'durian'] 

['bedral', 'blader', 'bardel', 'belard', 'bedlar', 'balder'] 

['atrail', 'talari', 'Altair', 'lariat', 'latria', 'atrial'] 

['arrect', 'recart', 'Carter', 'carter', 'crater', 'tracer']
~~~
 
 [end]
