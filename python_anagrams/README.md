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

### Output

~~~
[(11,
  ['nagor',
   'Orang',
   'angor',
   'organ',
   'orang',
   'groan',
   'grano',
   'Ronga',
   'goran',
   'argon',
   'rogan']),
 (10,
  ['saeter',
   'reseat',
   'staree',
   'seater',
   'Teresa',
   'Eastre',
   'Easter',
   'teaser',
   'asteer',
   'easter']),
 (10,
  ['Lepas',
   'salep',
   'lapse',
   'speal',
   'Elaps',
   'slape',
   'sepal',
   'spale',
   'Pales',
   'saple']),
 (9,
  ['stree',
   'terse',
   'steer',
   'reest',
   'tsere',
   'estre',
   'ester',
   'reset',
   'stere']),
 (9,
  ['cater',
   'trace',
   'recta',
   'crate',
   'react',
   'creat',
   'carte',
   'creta',
   'caret']),
 (9,
  ['carina',
   'acinar',
   'Carian',
   'Crania',
   'narica',
   'crania',
   'Canari',
   'arnica',
   'canari']),
 (9,
  ['armet',
   'Trema',
   'mater',
   'Merat',
   'terma',
   'trame',
   'metra',
   'ramet',
   'tamer']),
 (9, ['Tuna', 'tuan', 'Antu', 'antu', 'naut', 'Tuan', 'taun', 'tuna', 'aunt']),
 (8, ['tane', 'neat', 'ante', 'Nate', 'Aten', 'tean', 'etna', 'taen']),
 (8,
  ['relast',
   'stelar',
   'slater',
   'resalt',
   'laster',
   'salter',
   'lastre',
   'rastle']),
 (8, ['male', 'Male', 'alem', 'meal', 'mela', 'lame', 'alme', 'leam']),
 (8, ['lira', 'lari', 'rail', 'lair', 'aril', 'rial', 'Lari', 'liar']),
 (8, ['leapt', 'plate', 'pleat', 'palet', 'patel', 'petal', 'pelta', 'tepal']),
 (8, ['arist', 'astir', 'tarsi', 'tisar', 'stair', 'sitar', 'Trias', 'stria']),
 (7, ['swat', 'staw', 'sawt', 'wast', 'Swat', 'twas', 'taws']),
 (7, ['stale', 'steal', 'setal', 'least', 'slate', 'stela', 'tales']),
 (7, ['snite', 'stine', 'tsine', 'Stein', 'neist', 'stein', 'inset']),
 (7, ['retard', 'retrad', 'darter', 'trader', 'dartre', 'redart', 'tarred']),
 (7, ['reland', 'enlard', 'lander', 'randle', 'lenard', 'aldern', 'darnel']),
 (7, ['reim', 'rime', 'mire', 'emir', 'Imer', 'Remi', 'riem'])]
 ~~~
 
 [end]
