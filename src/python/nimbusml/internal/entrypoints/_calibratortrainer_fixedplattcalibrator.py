# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
FixedPlattCalibrator
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def fixed_platt_calibrator(
        slope=1.0,
        offset=0.0,
        **params):
    """
    **Description**
        None

    :param slope: The slope parameter of f(x) = 1 / (1 + exp(-slope *
        x + offset) (settings).
    :param offset: The offset parameter of f(x) = 1 / (1 + exp(-slope
        * x + offset) (settings).
    """

    entrypoint_name = 'FixedPlattCalibrator'
    settings = {}

    if slope is not None:
        settings['Slope'] = try_set(
            obj=slope,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if offset is not None:
        settings['Offset'] = try_set(
            obj=offset,
            none_acceptable=True,
            is_of_type=numbers.Real)

    return Component(
        name=entrypoint_name, settings=settings, kind='CalibratorTrainer'
    )
