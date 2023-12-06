#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    sort = sorted(a_dictionary.items(), key=lambda kv: kv[1], reverse=True)
    return sort[0][0]
