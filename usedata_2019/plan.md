# TODO:
* number of words in language - DONE



* why so many identifiers - bigger and remove normalization - DONE
* code naturallness - image - DONE
* Take away - reformulate - DONE
* Basics - picture - DONE

* Identifier splitter - everything - DONE

* Identifier embeddings - image? - DONE

* Nearest to "foo" - сократить и пошагово показывать - и показать, что testing появляется - крупнее текст - DONE
* Analogies - крупнее текст - DONE

* Candidates ranking - logistic regression -> binary classification - DONE
* why so hard - add number of unique programming languages - DONE

* word mover's distance - remove text - DONE



* developer similarity - image - DONE

* developer similarity results - image? - WONTFIX

* developer similarity - engineering teams at gitlab - white background

* remove - awesome ml on code - fix picture

* short link - DONE
* qr code -DONE







## сперва результаты потом подход

## больше ссы


## словарь англ/ русского / турецкого / identifier'ы
https://en.wikipedia.org/wiki/List_of_dictionaries_by_number_of_words


# что такое MLonCode? 
## количество слайдов 1 + 5

* http://vmarkovtsev.github.io/techtalks-2017-moscow/#source-ml
* awesomeMLonCode - рассказать про разные проблемы и почему они могут быть решены или не могут быть решены быстро

# почему применение машинного обучения к исходному коду так сложно? 
## количество слайдов 1 + 11

* data size
http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#21


https://github.com/niderhoff/nlp-datasets

https://github.com/src-d/datasets/#public-git-archive

https://gluon-cv.mxnet.io/build/examples_datasets/imagenet.html

https://octoverse.github.com/

* code tools
http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#23
до 
http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#django

### влияние фильтрации - рассказать про размер бинарников, конфигов и тд - поискать 



### Parse ast
#### Code first
https://github.com/src-d/wmd-relax/blob/98f9510fee8a5c4593378eef22a47baef69c241f/wmd/__init__.py
#### ast next

# Почему почти ни одна из задач не может быть решена без использования методов для обработки естественных языков? Какие сложности надо преодолеть на этом пути?
## количество слайдов 4 + 1 + 2 + 1 + 4 + (22) + 1

* code naturallness  4
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#7
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#10

* code autocompletion 1
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#nncomplete-example

* code style 2
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#15
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#16

* Many other applications 1
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#17

* code2vec  4
        * https://docs.google.com/presentation/d/1THcPCLlucV7Q7EKYCKn1NFu62RjTrN-4nbOI_t0Ga3A/edit#slide=id.g462a4056c7_1_35

* optional: difference in embeddings (22)
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#45
        * http://localhost:63342/usedata_2019/index.html?_ijt=2ucguamd5td6hpfcc32a0tf45j#pmi

## словарь англ/ русского / турецкого / identifier'ы
## перенести в начало - сложность как реальный язык
* формулирование задач как НЛП
* какие подходы
* общие проблемы 
* общие пайплайны
* переходить к задачам
## тулы в конец перенести

## перенести в начало тоже
* Summary 
    * Отличия кода от текста
        * нелинейная структура
    * Похожесть - https://ru.wikipedia.org/wiki/Агглютинативные_языки
    * как работать?
        * parse: text -> AST
        * optional: tokenize - `_tcp_socket_connect -> [tcp, socket, connect]`
        * ML:
            * неупорядоченный набор фич
                * bag-of-features -> ML
                * set2something approach -> transformer-like model
            



# код-ревью — почему мы тратим так много времени на него? Как оптимизировать этот процесс и избавить разработчиков от "глупых" задач? Какие существуют решения на основе машинного обучения и как выкатить их в продакшн?

## количество слайдов 11 + 5 + 5 + ?

* почему мы тратим так много времени на него? Как оптимизировать этот процесс и избавить разработчиков от "глупых" задач?

* architecture/pipeline (11)
        * http://vmarkovtsev.github.io/devpro-2019-tomsk/#18

* style analyzer (5)
        * http://vmarkovtsev.github.io/devpro-2019-tomsk/#43

* typos correction 5 +
        * https://irinakhismatullina.github.io/2019-vienna-pydays/
        * idea https://irinakhismatullina.github.io/2019-vienna-pydays/#3

http://vmarkovtsev.github.io/msr-2019-montreal/


# поиск похожих репозиториев — почему поиск для исходного кода работает плохо? Как искать похожие по смыслу и решаемым задачам репозитории?
## количество слайдов 2 + 5

http://vmarkovtsev.github.io/techtalks-2017-moscow/

* idea - WMD
     * http://vmarkovtsev.github.io/techtalks-2017-moscow/#33
     * http://vmarkovtsev.github.io/techtalks-2017-moscow/#34
* pipeline
     * parsing at scale
     * identifier extraction
     * splitting
     * bag-of-identitifers/words
     * bag-of-embeddings
     * WMD

# поиск разработчиков с похожим опытом — как формализовать похожесть? Как извлечь необходимую информацию из кода? Какие методы позволят решить эту задачу?

## количество слайдов 7

* DATA PROCESSING
* COMMIT TIME SERIES
* CONTRIBUTIONS BY PROGRAMMING LANGUAGES
* SOURCE CODE IDENTIFIERS + topic modeling
* clustering


https://arxiv.org/abs/1905.06782
https://github.com/src-d/poc-pluralsight


пирамида по частям

агглютативные языки - примеры дать

ast - рассказать побольше на примере

PGA - рассказать про слайсы данных, что они очень сильно уменьшать размер данных для задачи конкретной

number of words - bar chart

какие еще языки бывают? 

nearest to foo
по слайдам - и рассказать 

analogy - такое же - появление текста по частям
может быть только woman quenn king man


увеличить текст в среднем

word movers distance - убрать все слова, кроме картинки
