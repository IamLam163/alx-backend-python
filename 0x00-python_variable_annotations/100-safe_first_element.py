#!/usr/bin/env python3
'''Duck typing first element in a sequence'''


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''returns the first element in a sequence'''
    if lst:
        return lst[0]
    else:
        return None
