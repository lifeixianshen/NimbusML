# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
ExpLoss
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def exp_loss(
        beta=1.0,
        **params):
    """
    **Description**
        Exponential loss.

    :param beta: Beta (dilation) (settings).
    """

    entrypoint_name = 'ExpLoss'
    settings = {}

    if beta is not None:
        settings['Beta'] = try_set(
            obj=beta,
            none_acceptable=True,
            is_of_type=numbers.Real)

    return Component(
        name=entrypoint_name,
        settings=settings,
        kind='ClassificationLossFunction',
    )
