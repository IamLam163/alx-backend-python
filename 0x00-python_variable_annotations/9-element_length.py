#!/usr/bin/env python3
'''duck typing an iterable object'''


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''gets the lenght of a list of Sequence'''
    return [(itr, len(itr)) for itr in lst]
