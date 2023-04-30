from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from nltk import TreePrettyPrinter
from .tree import make_variations
import json

# Create your views here.


def index(request):
    return render(request, 'changer_site/index.html')


def paraphrase(request):
    error = ''
    if request.method == 'GET':
        if request.GET.keys().__contains__('tree'):
            param_name = 'tree'
        else:
            param_name = None
        response = {}
        keys = list(request.GET.keys())
        for key in keys:
            response.update({key: request.GET.get(key, "")})

        response.update({'tree': request.GET.get('tree', "")})
        response.update({'limit': request.GET.get('limit', 20)})
        response.update({'print_options': request.GET.get('print_options', 'string')})

        parse_trees = make_variations(response['tree'])
        text_variations, num = {}, 1
        if response['print_options'] == 'string':
            if not isinstance(parse_trees, str):
                for variation in parse_trees:
                    for sentence in variation:
                        if num <= int(response['limit']):
                            text_variations.update({num: "".join(str(sentence).split("\n")).strip()})
                        else:
                            break
                    num += 1
            else:
                text_variations = parse_trees
        elif response['print_options'] == 'tree':
            if not isinstance(parse_trees, str):
                for variation in parse_trees:
                    for sentence in variation:
                        if num <= int(response['limit']):
                            text_variations.update({num: TreePrettyPrinter(sentence).text()})
                        else:
                            break
                    num += 1
            else:
                text_variations = parse_trees
        elif response['print_options'] == 'json':
            if not isinstance(parse_trees, str):
                sentence_str, data_str = [], []
                for variation in parse_trees:
                    for sentence in variation:
                        if num <= int(response['limit']):
                            sentence_str.append({"tree": "".join(str(sentence).split("\n")).strip()})
                        else:
                            break
                data_str.append({"paraphrases": sentence_str})
                text_variations = json.dumps(data_str)
            else:
                text_variations = parse_trees
        else:
            text_variations = "Wrong 'print_options' parameter value!"
        response.update({'tree': text_variations})
        data = Data(**response)
        info = {
            'data': data,
            'param_name': param_name,
            'error': error
        }
    else:
        response = {'tree': "", 'limit': 20}
        data = Data(**response)
        param_name = None
        info = {
            'data': data,
            'param_name': param_name,
            'error': error
        }
    return render(request, 'changer_site/paraphrase.html', info)


class Data(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class GrammarTree(APIView):
    def get(self, request):
        response = {}
        keys = list(request.GET.keys())
        for key in keys:
            response.update({key: request.GET.get(key, "")})

        response.update({'tree': request.GET.get('tree', "")})
        response.update({'limit': request.GET.get('limit', 20)})
        response.update({'print_options': request.GET.get('print_options', 'string')})

        parse_trees = make_variations(response['tree'])
        text_variations, num = {}, 1
        if response['print_options'] == 'string':
            if not isinstance(parse_trees, str):
                for variation in parse_trees:
                    for sentence in variation:
                        if num <= int(response['limit']):
                            text_variations.update({num: "".join(str(sentence).split("\n")).strip()})
                        else:
                            break
                    num += 1
            else:
                text_variations = parse_trees
        elif response['print_options'] == 'tree':
            if not isinstance(parse_trees, str):
                for variation in parse_trees:
                    for sentence in variation:
                        if num <= int(response['limit']):
                            text_variations.update({num: TreePrettyPrinter(sentence).text()})
                        else:
                            break
                    num += 1
            else:
                text_variations = parse_trees
        elif response['print_options'] == 'json':
            if not isinstance(parse_trees, str):
                sentence_str, data_str = [], []
                for variation in parse_trees:
                    for sentence in variation:
                        if num <= int(response['limit']):
                            sentence_str.append({"tree": "".join(str(sentence).split("\n")).strip()})
                        else:
                            break
                data_str.append({"paraphrases": sentence_str})
                text_variations = json.dumps(data_str)
            else:
                text_variations = parse_trees
        else:
            text_variations = "Wrong 'print_options' parameter value!"
        response.update({'result': text_variations})
        return Response(response)
