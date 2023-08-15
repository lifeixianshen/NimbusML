# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TimeSeriesProcessingEntryPoints.SsaSpikeDetector
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def timeseriesprocessingentrypoints_ssaspikedetector(
        source,
        data,
        name,
        output_data=None,
        model=None,
        training_window_size=100,
        confidence=99.0,
        seasonal_window_size=10,
        side='TwoSided',
        pvalue_history_length=100,
        error_function='SignedDifference',
        **params):
    """
    **Description**
        This transform detects the spikes in a seasonal time-series using
        Singular Spectrum Analysis (SSA).

    :param source: The name of the source column. (inputs).
    :param data: Input dataset (inputs).
    :param name: The name of the new column. (inputs).
    :param training_window_size: The number of points from the
        beginning of the sequence used for training. (inputs).
    :param confidence: The confidence for spike detection in the
        range [0, 100]. (inputs).
    :param seasonal_window_size: An upper bound on the largest
        relevant seasonality in the input time-series. (inputs).
    :param side: The argument that determines whether to detect
        positive or negative anomalies, or both. (inputs).
    :param pvalue_history_length: The size of the sliding window for
        computing the p-value. (inputs).
    :param error_function: The function used to compute the error
        between the expected and the observed value. (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'TimeSeriesProcessingEntryPoints.SsaSpikeDetector'
    inputs = {}
    outputs = {}

    if source is not None:
        inputs['Source'] = try_set(
            obj=source,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if name is not None:
        inputs['Name'] = try_set(
            obj=name,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if training_window_size is not None:
        inputs['TrainingWindowSize'] = try_set(
            obj=training_window_size,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if confidence is not None:
        inputs['Confidence'] = try_set(
            obj=confidence,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if seasonal_window_size is not None:
        inputs['SeasonalWindowSize'] = try_set(
            obj=seasonal_window_size,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if side is not None:
        inputs['Side'] = try_set(
            obj=side,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Positive',
                'Negative',
                'TwoSided'])
    if pvalue_history_length is not None:
        inputs['PvalueHistoryLength'] = try_set(
            obj=pvalue_history_length,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if error_function is not None:
        inputs['ErrorFunction'] = try_set(
            obj=error_function,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'SignedDifference',
                'AbsoluteDifference',
                'SignedProportion',
                'AbsoluteProportion',
                'SquaredDifference'])
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

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
