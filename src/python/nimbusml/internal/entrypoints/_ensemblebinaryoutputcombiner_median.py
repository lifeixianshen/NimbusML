# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Median
"""


from ..utils.entrypoints import Component


def median(
        **params):
    """
    **Description**
        None

    """

    entrypoint_name = 'Median'
    settings = {}

    return Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleBinaryOutputCombiner',
    )
