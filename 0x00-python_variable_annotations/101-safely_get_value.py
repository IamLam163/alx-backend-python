#!/usr/bin/env python3
'''adding type annotations to functions'''


from typing import Any, Dict, Optional, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Dict[Any, T], key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    if key in dct:
        return dct[key]
    else:
        return default
