import nltk
from itertools import permutations, product
import json


def make_tree(string_tree: str):
    if string_tree == "":
        return ""
    else:
        try:
            list_of_trees = string_tree.split('.')
            trees = []
            for tree in list_of_trees:
                trees.append(nltk.ParentedTree.fromstring(tree))
            return trees
        except Exception as ex:
            error = f"Error: {ex}"
            return error.strip()


def make_variations(string_tree: str):
    parent_trees = make_tree(string_tree)
    if isinstance(parent_trees, str):
        return parent_trees
    else:
        variations = []
        for parent_tree in parent_trees:
            np_trees = parent_tree.subtrees(lambda t: t.label() == 'NP')
            np_good_trees, np_good_trees_positions = [], []
            for children_tree in np_trees:
                np_children_trees = get_children(children_tree)
                children_labels = []
                for np_children_tree in np_children_trees:
                    children_labels.append(np_children_tree.label())
                check = False
                for label in children_labels:
                    if label == "NP" or label == "," or label == "CC":
                        check = True
                    else:
                        check = False
                        break
                if check is True:
                    np_good_trees.append(children_tree)
            good_tree_children = []
            for good_tree in np_good_trees:
                child_list = []
                children = get_children(good_tree, label='NP')
                for child in children:
                    np_good_trees_positions.append(child.treeposition())
                    child_list.append(child)
                good_tree_children.append(child_list)
            variants, dictionary = combinations(good_tree_children)
            variation = []
            for variant in variants:
                conc_var = []
                for var in variant:
                    conc_var += list(var)
                editable_tree = parent_tree.copy(deep=True)
                for numb, pos in enumerate(np_good_trees_positions):
                    tree_no_parent = nltk.Tree.convert(dictionary[conc_var[numb]])
                    editable_tree[pos] = nltk.ParentedTree.convert(tree_no_parent)
                variation.append(editable_tree)
            variations.append(variation)
        text_variants = []
        for element in product(*variations):
            text_variants.append(list(element))
    return text_variants


def get_children(sub_tree: nltk.ParentedTree, label=None):
    if label is None:
        return sub_tree.subtrees(lambda t: t.parent() == sub_tree)
    else:
        return sub_tree.subtrees(lambda t: t.parent() == sub_tree and t.label() == label)


def combinations(good_children):
    var_list, var_dict, num = [], {}, 1
    for tr_gen in good_children:
        lst = []
        for tr in tr_gen:
            lst.append(num)
            var_dict.update({num: tr})
            num += 1
        var_list.append(lst)
    num_vars, l_vars = [], []
    for vl in range(0, len(var_list)):
        l_vars.append(list(permutations(var_list[vl], len(var_list[vl]))))
    for element in product(*l_vars):
        num_vars.append(list(element))
    return num_vars, var_dict


if __name__ == '__main__':
    str_tree = str(input("Enter grammar structure: "))
    parse_trees = make_variations(str_tree)
