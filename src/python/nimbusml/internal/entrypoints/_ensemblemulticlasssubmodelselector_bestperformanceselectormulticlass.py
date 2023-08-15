# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
BestPerformanceSelectorMultiClass
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def best_performance_selector_multi_class(
        metric_name='AccuracyMicro',
        learners_selection_proportion=0.5,
        validation_dataset_proportion=0.3,
        **params):
    """
    **Description**
        None

    :param metric_name: The metric type to be used to find the best
        performance (settings).
    :param learners_selection_proportion: The proportion of best base
        learners to be selected. The range is 0.0-1.0 (settings).
    :param validation_dataset_proportion: The proportion of instances
        to be selected to test the individual base learner. If it is
        0, it uses training set (settings).
    """

    entrypoint_name = 'BestPerformanceSelectorMultiClass'
    settings = {}

    if metric_name is not None:
        settings['MetricName'] = try_set(
            obj=metric_name,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'AccuracyMicro',
                'AccuracyMacro',
                'LogLoss',
                'LogLossReduction'])
    if learners_selection_proportion is not None:
        settings['LearnersSelectionProportion'] = try_set(
            obj=learners_selection_proportion,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if validation_dataset_proportion is not None:
        settings['ValidationDatasetProportion'] = try_set(
            obj=validation_dataset_proportion,
            none_acceptable=True,
            is_of_type=numbers.Real)

    return Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleMulticlassSubModelSelector',
    )
