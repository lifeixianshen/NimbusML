# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
MultiDisagreementDiversityMeasure
"""


from ..utils.entrypoints import Component


def multi_disagreement_diversity_measure(
        **params):
    """
    **Description**
        None

    """

    entrypoint_name = 'MultiDisagreementDiversityMeasure'
    settings = {}

    return Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleMulticlassDiversityMeasure',
    )
