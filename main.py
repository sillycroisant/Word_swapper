'''Word swapper, by Nguyen Van Huy
A tool helps you to re-paraphrase a sentence.'''

import random

#Set up the constants
COMPARE_MID_SENTENCE = ['in common with','as would a','has in common with','likewise']
COMPARE_BEGIN_SENTENCE = ['Similarly','This mirrors','This parallels','This reflects','This resembles']

CONTRAST_BEGIN_SENTENCE = ['Although','However','On the other hand',
                            'Unlike','In contract to','Conversely','This differs from']
CONTRAST_MID_SENTENCE = ['whereas','while','']

SUPPORT_ADJ = ['beneficial','advantageous','positive','desirable']
REFUTE_ADJ = ['disadvantageous','undesirable','negative']

INCREASE_VERB = ['climb','increase','grow']

DECREASE_VERB = ['decline','drop','shrink','reduce']

MAINTAIN_ADJ = ['steady','stable','unchanged']

INSTABILITY_ADJ = ['volatile','varied','unstable','unpredictable']

REMARKABLE_ADJ = ['unexpected','astounding','unorthodox']

#Take input 
text = input('>Nhập đoạn văn vào :').split()

for i in range(len(text)):
    if text[i] in CONTRAST_BEGIN_SENTENCE:
        text[i] = CONTRAST_BEGIN_SENTENCE[random.randint(0,len(CONTRAST_BEGIN_SENTENCE)-1)]

for word in text:
    print(word,end=' ')

#Need to design a more reliable pattern for English and an exhaustive library for languague synonyms
