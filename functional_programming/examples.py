import functools
from typing import Callable

def compose_two_func(f:Callable, g:Callable) -> Callable:
    return lambda *a, **kw: g(f(*a, **kw))

def compose(components:list[Callable]) -> Callable:
    return functools.reduce(compose_two_func, components)


def split_phrase(phrase:str) -> list[str]:
  return phrase.split(" ")

def remove_long_words(words:list[str]) -> list[str]:
  return [word for word in words if len(word)<=5]

def remove_short_words(words:list[str]) -> list[str]:
  return [word for word in words if len(word)>2]

def build_phrase(words:list[str]) -> str:
  return " ".join(words)


phrase_example = "La composition c'est bien, la composition c'est bon"

# Cas avec les 4 fonctions
modify_phrase = compose(components=[split_phrase, remove_short_words, remove_long_words, build_phrase])
phrase_without_short_and_long_words = modify_phrase(phrase=phrase_example)
print(phrase_without_short_and_long_words)

# Cas avec seulement 3 fonctions
modify_phrase = compose(components=[split_phrase, remove_long_words, build_phrase])
phrase_without_long_words = modify_phrase(phrase=phrase_example)
print(phrase_without_long_words)