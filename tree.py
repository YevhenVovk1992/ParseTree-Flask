import copy
import json
import nltk
import itertools


nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


tree_str = """
(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )
"""


class TreeEditor:
    def __init__(self, tree: str):
        self.main_tree = nltk.Tree.fromstring(tree)
        self.__nodes = []
        self.__words_list = []
        self.__combination_list = []
        self.combinations_of_trees = []

    def __find_nodes(self) -> None:
        """
        Looking for phrases in the tree with which we will create new trees
        """
        for subtree in self.main_tree.subtrees(filter=lambda t: t.label() == 'NP'):
            if all(_.label() in ('NP', 'CC', ',') for _ in subtree):
                for i, el in enumerate(subtree):
                    if el.label() == 'CC' and el[0] == 'and':
                        self.__nodes.append(subtree)

    def __find_words_in_node(self) -> None:
        """
        Analyze the snippet and find indexes of words for permutation
        """
        for node in self.__nodes:
            list_positions = []
            for i, el in enumerate(node):
                if el.label() == 'NP':
                    list_positions.append(i)
            self.__combination_list.append({tuple(list_positions): node})
            list_positions.clear()

    def create_combinations_from_tree(self, combinations_number=None) -> list:
        """
        Start the process of tree analysis and permutation of phrases
        :return: list with trees
        """
        self.__find_nodes()
        self.__find_words_in_node()
        for element in self.__combination_list:
            for coord, node in element.items():
                combinations_of_coord = list(itertools.permutations(coord))
                start_coord = coord
                for el_coord in combinations_of_coord:
                    for i in range(len(el_coord)):
                        if start_coord[i] == el_coord[i]:
                            continue
                        node[start_coord[i]], node[el_coord[i]] = node[el_coord[i]], node[start_coord[i]]
                        new_trees = copy.deepcopy(self.main_tree)
                        self.combinations_of_trees.append(new_trees)
                    start_coord = el_coord
        if combinations_number:
            return self.combinations_of_trees[:combinations_number]
        return self.combinations_of_trees

    def to_json(self) -> str:
        """
        Create a string with trees, valid for passing as a Json file
        :return: json valid string
        """
        tree_list = list(
            {'tree': ' '.join(str(i).split())} for i in self.combinations_of_trees
        )
        return json.dumps({'paraphrases': tree_list})


if __name__ == "__main__":
    editor = TreeEditor(tree_str)
    editor.create_combinations_from_tree(3)
    json_str = editor.to_json()
    print(json_str)
