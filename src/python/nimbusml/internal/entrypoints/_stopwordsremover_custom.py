# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Custom
"""


from ..utils.entrypoints import Component
from ..utils.utils import try_set


def custom(
        stopword=None,
        **params):
    """
    **Description**
        Remover with list of stopwords specified by the user.

    :param stopword: List of stopwords (settings).
    """

    entrypoint_name = 'Custom'
    settings = {}

    if stopword is not None:
        settings['Stopword'] = try_set(
            obj=stopword, none_acceptable=True, is_of_type=list)

    return Component(
        name=entrypoint_name, settings=settings, kind='StopWordsRemover'
    )
