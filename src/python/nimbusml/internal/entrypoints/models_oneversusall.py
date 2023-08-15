# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Models.OneVersusAll
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def models_oneversusall(
        nodes,
        training_data,
        output_for_sub_graph=0,
        predictor_model=None,
        feature_column_name='Features',
        use_probabilities=True,
        label_column_name='Label',
        example_weight_column_name=None,
        normalize_features='Auto',
        caching='Auto',
        **params):
    """
    **Description**
        One-vs-All macro (OVA)

    :param nodes: The subgraph for the binary trainer used to
        construct the OVA learner. This should be a TrainBinary node.
        (inputs).
    :param training_data: The data to be used for training (inputs).
    :param output_for_sub_graph: The training subgraph output.
        (inputs).
    :param feature_column_name: Column to use for features (inputs).
    :param use_probabilities: Use probabilities in OVA combiner
        (inputs).
    :param label_column_name: Column to use for labels (inputs).
    :param example_weight_column_name: Column to use for example
        weight (inputs).
    :param normalize_features: Normalize option for the feature
        column (inputs).
    :param caching: Whether trainer should cache input training data
        (inputs).
    :param predictor_model: The trained multiclass model (outputs).
    """

    entrypoint_name = 'Models.OneVersusAll'
    inputs = {}
    outputs = {}

    if nodes is not None:
        inputs['Nodes'] = try_set(
            obj=nodes,
            none_acceptable=False,
            is_of_type=list)
    if training_data is not None:
        inputs['TrainingData'] = try_set(
            obj=training_data,
            none_acceptable=False,
            is_of_type=str)
    if output_for_sub_graph is not None:
        inputs['OutputForSubGraph'] = try_set(
            obj=output_for_sub_graph,
            none_acceptable=False,
            is_of_type=dict,
            field_names=['Model'])
    if feature_column_name is not None:
        inputs['FeatureColumnName'] = try_set(
            obj=feature_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if use_probabilities is not None:
        inputs['UseProbabilities'] = try_set(
            obj=use_probabilities,
            none_acceptable=True,
            is_of_type=bool)
    if label_column_name is not None:
        inputs['LabelColumnName'] = try_set(
            obj=label_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if example_weight_column_name is not None:
        inputs['ExampleWeightColumnName'] = try_set(
            obj=example_weight_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if normalize_features is not None:
        inputs['NormalizeFeatures'] = try_set(
            obj=normalize_features,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'No',
                'Warn',
                'Auto',
                'Yes'])
    if caching is not None:
        inputs['Caching'] = try_set(
            obj=caching,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Auto',
                'Memory',
                'None'])
    if predictor_model is not None:
        outputs['PredictorModel'] = try_set(
            obj=predictor_model, none_acceptable=False, is_of_type=str)

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
