import json

def transformTree(tree, attributes, currentDict, leaf_funct = prediction):
    # Get the current split question.
    split_col = str(tree.col)
    if attributes is not None:
        split_col = attributes[tree.col]

    if not tree.value:
        currentDict["name"] = str(leaf_funct(tree.results))
        return
    split_val = str(tree.value)
    if type(tree.value) == int or type(tree.value) == float:
        split_val = ">=" + str(tree.value)
    split_question = split_col + ': ' + split_val + '? '
    currentDict["name"] = split_question

    next_left_question = {}
    next_right_question = {}
    left_children = {
        "name" : "T",
        "children" : [
            next_left_question
        ]
    }
    right_children = {
        "name": "F",
        "children": [
            next_right_question
        ]
    }

    currentDict["children"] = [left_children, right_children]
    if tree.tb:
        transformTree(tree.tb, attributes, next_left_question)
    if tree.fb:
        transformTree(tree.fb, attributes, next_right_question)

dataTree = {}

transformTree(tree, columns_list, dataTree)
json_file = json.dumps(dataTree)

#Export JSON file.
with open(input("\nEnter File Name: "), 'w') as f:
    f.write(json_file)