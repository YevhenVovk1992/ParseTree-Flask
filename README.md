# Derivation tree (Parse tree)
### Concrete syntax tree is an ordered, rooted tree that represents the syntactic structure of a string according to some context-free grammar. 
___
## Content
 - [Technologies](#what-we-used)
 - [Desription](#what-we-do)
 - [Star Project](#how-to-start-project)
 - [Sources](#sources)

___
## What we used?
_Technologies used_: Flask, NLTK

## What we do?
Create an API in Python, which implements a single endpoint that accepts syntactic input
tree of the English text and returns its paraphrased versions:
 - path: /paraphrase
 - HTTP method: GET
 - query parameters:
   - tree: str (required) – a syntactic tree in the form of a string (see example below)
   - limit: int (optional, default: 20) - the maximum number of paraphrased texts that
response must be returned: a list of paraphrased trees in JSON format.

Paraphrasing should be done as follows:
   - Find in the text all NP (noun phrase) - noun phrases consisting of
several NPs separated by tags , (comma) or SS (conjunctive inflection, e.g. "and").
   - Generate permutations of these child NPs with each other.

Take the following text as an example: **The charming Gothic Quarter, or Barri
Gòtic, has narrow medieval streets filled with trendy bars, clubs and Catalan restaurants.**
Him the syntax tree looks like this:
`(S
(NP
(NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))
(, ,)
(CC or)
(NP (NNP Barri) (NNP Gòtic)))
(, ,)
(VP
(VBZ has)
(NP
(NP (JJ narrow) (JJ medieval) (NNS streets))
(VP
(VBN filled)
(PP
(IN with)
(NP
(NP (JJ trendy) (NNS bars))
(, ,)
(NP (NNS clubs))
(CC and)
(NP (JJ Catalan) (NNS restaurants))))))))`

An example of a request URL: <br>
`localhost:<port>/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )`<br>

The file `expected-result-example.json` contains an example of the expected result of calling the endpoint.

## How to start project?
1. Run `git clone {SSH-link from GitHub}` on your PC;
2. Run `pip install -r requirements.txt`;
3. Create '.env' file and write to it the enviroment variables:
	- SECRET_KEY (Fot example: '*jfjn&nf8jfghg=fgkhd6k56566')
	- DEBUG 	
4. Run `python3 app.py`;

## Sources
1. [wikipedia.Parse_tree](https://en.wikipedia.org/wiki/Parse_tree#Constituency-based_parse_trees)
