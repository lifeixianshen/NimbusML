# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
AllSelector
"""


from ..utils.entrypoints import Component


def all_selector(
        **params):
    """
    **Description**
        None

    """

    entrypoint_name = 'AllSelector'
    settings = {}

    return Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleRegressionSubModelSelector',
    )
