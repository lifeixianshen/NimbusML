# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Models.RankingEvaluator
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def models_rankingevaluator(
        data,
        warnings=None,
        overall_metrics=None,
        per_instance_metrics=None,
        name_column='Name',
        group_id_column=None,
        dcg_truncation_level=3,
        label_gains='0,3,7,15,31',
        label_column=None,
        weight_column=None,
        score_column=None,
        strat_column=None,
        **params):
    """
    **Description**
        Evaluates a ranking scored dataset.

    :param data: The data to be used for evaluation. (inputs).
    :param name_column: Name column name. (inputs).
    :param group_id_column: Column to use for the group ID (inputs).
    :param dcg_truncation_level: Maximum truncation level for
        computing (N)DCG (inputs).
    :param label_gains: Label relevance gains (inputs).
    :param label_column: Column to use for labels. (inputs).
    :param weight_column: Weight column name. (inputs).
    :param score_column: Score column name. (inputs).
    :param strat_column: Stratification column name. (inputs).
    :param warnings: Warning dataset (outputs).
    :param overall_metrics: Overall metrics dataset (outputs).
    :param per_instance_metrics: Per instance metrics dataset
        (outputs).
    """

    entrypoint_name = 'Models.RankingEvaluator'
    inputs = {}
    outputs = {}

    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if name_column is not None:
        inputs['NameColumn'] = try_set(
            obj=name_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if group_id_column is not None:
        inputs['GroupIdColumn'] = try_set(
            obj=group_id_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if dcg_truncation_level is not None:
        inputs['DcgTruncationLevel'] = try_set(
            obj=dcg_truncation_level,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if label_gains is not None:
        inputs['LabelGains'] = try_set(
            obj=label_gains,
            none_acceptable=True,
            is_of_type=str)
    if label_column is not None:
        inputs['LabelColumn'] = try_set(
            obj=label_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if weight_column is not None:
        inputs['WeightColumn'] = try_set(
            obj=weight_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if score_column is not None:
        inputs['ScoreColumn'] = try_set(
            obj=score_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if strat_column is not None:
        inputs['StratColumn'] = try_set(
            obj=strat_column,
            none_acceptable=True,
            is_of_type=list,
            is_column=True)
    if warnings is not None:
        outputs['Warnings'] = try_set(
            obj=warnings, none_acceptable=False, is_of_type=str)
    if overall_metrics is not None:
        outputs['OverallMetrics'] = try_set(
            obj=overall_metrics, none_acceptable=False, is_of_type=str)
    if per_instance_metrics is not None:
        outputs['PerInstanceMetrics'] = try_set(
            obj=per_instance_metrics, none_acceptable=False, is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    return EntryPoint(
        name=entrypoint_name,
        inputs=inputs,
        outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables,
    )
