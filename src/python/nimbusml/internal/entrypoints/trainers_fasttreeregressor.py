# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Trainers.FastTreeRegressor
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def trainers_fasttreeregressor(
        training_data,
        predictor_model=None,
        number_of_trees=100,
        number_of_leaves=20,
        feature_column_name='Features',
        minimum_example_count_per_leaf=10,
        label_column_name='Label',
        learning_rate=0.2,
        example_weight_column_name=None,
        row_group_column_name=None,
        normalize_features='Auto',
        caching='Auto',
        best_step_ranking_regression_trees=False,
        use_line_search=False,
        maximum_number_of_line_search_steps=0,
        minimum_step_size=0.0,
        optimization_algorithm='GradientDescent',
        early_stopping_rule=None,
        early_stopping_metrics=1,
        enable_pruning=False,
        use_tolerant_pruning=False,
        pruning_threshold=0.004,
        pruning_window_size=5,
        shrinkage=1.0,
        dropout_rate=0.0,
        get_derivatives_sample_rate=1,
        write_last_ensemble=False,
        maximum_tree_output=100.0,
        random_start=False,
        filter_zero_lambdas=False,
        baseline_scores_formula=None,
        baseline_alpha_risk=None,
        position_discount_freeform=None,
        parallel_trainer=None,
        number_of_threads=None,
        seed=123,
        feature_selection_seed=123,
        entropy_coefficient=0.0,
        histogram_pool_size=-1,
        disk_transpose=None,
        feature_flocks=True,
        categorical_split=False,
        maximum_categorical_group_count_per_node=64,
        maximum_categorical_split_point_count=64,
        minimum_example_fraction_for_categorical_split=0.001,
        minimum_examples_for_categorical_split=100,
        bias=0.0,
        bundling='None',
        maximum_bin_count_per_feature=255,
        sparsify_threshold=0.7,
        feature_first_use_penalty=0.0,
        feature_reuse_penalty=0.0,
        gain_confidence_level=0.0,
        softmax_temperature=0.0,
        execution_time=False,
        feature_fraction=1.0,
        bagging_size=0,
        bagging_example_fraction=0.7,
        feature_fraction_per_split=1.0,
        smoothing=0.0,
        allow_empty_trees=True,
        feature_compression_level=1,
        compress_ensemble=False,
        print_test_graph=False,
        print_train_valid_graph=False,
        test_frequency=2147483647,
        **params):
    """
    **Description**
        Trains gradient boosted decision trees to fit target values using
        least-squares.

    :param number_of_trees: Total number of decision trees to create
        in the ensemble (inputs).
    :param training_data: The data to be used for training (inputs).
    :param number_of_leaves: The max number of leaves in each
        regression tree (inputs).
    :param feature_column_name: Column to use for features (inputs).
    :param minimum_example_count_per_leaf: The minimal number of
        examples allowed in a leaf of a regression tree, out of the
        subsampled data (inputs).
    :param label_column_name: Column to use for labels (inputs).
    :param learning_rate: The learning rate (inputs).
    :param example_weight_column_name: Column to use for example
        weight (inputs).
    :param row_group_column_name: Column to use for example groupId
        (inputs).
    :param normalize_features: Normalize option for the feature
        column (inputs).
    :param caching: Whether trainer should cache input training data
        (inputs).
    :param best_step_ranking_regression_trees: Option for using best
        regression step trees (inputs).
    :param use_line_search: Should we use line search for a step size
        (inputs).
    :param maximum_number_of_line_search_steps: Number of post-
        bracket line search steps (inputs).
    :param minimum_step_size: Minimum line search step size (inputs).
    :param optimization_algorithm: Optimization algorithm to be used
        (GradientDescent, AcceleratedGradientDescent) (inputs).
    :param early_stopping_rule: Early stopping rule. (Validation set
        (/valid) is required.) (inputs).
    :param early_stopping_metrics: Early stopping metrics. (For
        regression, 1: L1, 2:L2; for ranking, 1:NDCG@1, 3:NDCG@3)
        (inputs).
    :param enable_pruning: Enable post-training pruning to avoid
        overfitting. (a validation set is required) (inputs).
    :param use_tolerant_pruning: Use window and tolerance for pruning
        (inputs).
    :param pruning_threshold: The tolerance threshold for pruning
        (inputs).
    :param pruning_window_size: The moving window size for pruning
        (inputs).
    :param shrinkage: Shrinkage (inputs).
    :param dropout_rate: Dropout rate for tree regularization
        (inputs).
    :param get_derivatives_sample_rate: Sample each query 1 in k
        times in the GetDerivatives function (inputs).
    :param write_last_ensemble: Write the last ensemble instead of
        the one determined by early stopping (inputs).
    :param maximum_tree_output: Upper bound on absolute value of
        single tree output (inputs).
    :param random_start: Training starts from random ordering
        (determined by /r1) (inputs).
    :param filter_zero_lambdas: Filter zero lambdas during training
        (inputs).
    :param baseline_scores_formula: Freeform defining the scores that
        should be used as the baseline ranker (inputs).
    :param baseline_alpha_risk: Baseline alpha for tradeoffs of risk
        (0 is normal training) (inputs).
    :param position_discount_freeform: The discount freeform which
        specifies the per position discounts of examples in a query
        (uses a single variable P for position where P=0 is first
        position) (inputs).
    :param parallel_trainer: Allows to choose Parallel FastTree
        Learning Algorithm (inputs).
    :param number_of_threads: The number of threads to use (inputs).
    :param seed: The seed of the random number generator (inputs).
    :param feature_selection_seed: The seed of the active feature
        selection (inputs).
    :param entropy_coefficient: The entropy (regularization)
        coefficient between 0 and 1 (inputs).
    :param histogram_pool_size: The number of histograms in the pool
        (between 2 and numLeaves) (inputs).
    :param disk_transpose: Whether to utilize the disk or the data's
        native transposition facilities (where applicable) when
        performing the transpose (inputs).
    :param feature_flocks: Whether to collectivize features during
        dataset preparation to speed up training (inputs).
    :param categorical_split: Whether to do split based on multiple
        categorical feature values. (inputs).
    :param maximum_categorical_group_count_per_node: Maximum
        categorical split groups to consider when splitting on a
        categorical feature. Split groups are a collection of split
        points. This is used to reduce overfitting when there many
        categorical features. (inputs).
    :param maximum_categorical_split_point_count: Maximum categorical
        split points to consider when splitting on a categorical
        feature. (inputs).
    :param minimum_example_fraction_for_categorical_split: Minimum
        categorical example percentage in a bin to consider for a
        split. (inputs).
    :param minimum_examples_for_categorical_split: Minimum
        categorical example count in a bin to consider for a split.
        (inputs).
    :param bias: Bias for calculating gradient for each feature bin
        for a categorical feature. (inputs).
    :param bundling: Bundle low population bins. Bundle.None(0): no
        bundling, Bundle.AggregateLowPopulation(1): Bundle low
        population, Bundle.Adjacent(2): Neighbor low population
        bundle. (inputs).
    :param maximum_bin_count_per_feature: Maximum number of distinct
        values (bins) per feature (inputs).
    :param sparsify_threshold: Sparsity level needed to use sparse
        feature representation (inputs).
    :param feature_first_use_penalty: The feature first use penalty
        coefficient (inputs).
    :param feature_reuse_penalty: The feature re-use penalty
        (regularization) coefficient (inputs).
    :param gain_confidence_level: Tree fitting gain confidence
        requirement (should be in the range [0,1) ). (inputs).
    :param softmax_temperature: The temperature of the randomized
        softmax distribution for choosing the feature (inputs).
    :param execution_time: Print execution time breakdown to stdout
        (inputs).
    :param feature_fraction: The fraction of features (chosen
        randomly) to use on each iteration (inputs).
    :param bagging_size: Number of trees in each bag (0 for disabling
        bagging) (inputs).
    :param bagging_example_fraction: Percentage of training examples
        used in each bag (inputs).
    :param feature_fraction_per_split: The fraction of features
        (chosen randomly) to use on each split (inputs).
    :param smoothing: Smoothing paramter for tree regularization
        (inputs).
    :param allow_empty_trees: When a root split is impossible, allow
        training to proceed (inputs).
    :param feature_compression_level: The level of feature
        compression to use (inputs).
    :param compress_ensemble: Compress the tree Ensemble (inputs).
    :param print_test_graph: Print metrics graph for the first test
        set (inputs).
    :param print_train_valid_graph: Print Train and Validation
        metrics in graph (inputs).
    :param test_frequency: Calculate metric values for
        train/valid/test every k rounds (inputs).
    :param predictor_model: The trained model (outputs).
    """

    entrypoint_name = 'Trainers.FastTreeRegressor'
    inputs = {}
    outputs = {}

    if number_of_trees is not None:
        inputs['NumberOfTrees'] = try_set(
            obj=number_of_trees,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if training_data is not None:
        inputs['TrainingData'] = try_set(
            obj=training_data,
            none_acceptable=False,
            is_of_type=str)
    if number_of_leaves is not None:
        inputs['NumberOfLeaves'] = try_set(
            obj=number_of_leaves,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_column_name is not None:
        inputs['FeatureColumnName'] = try_set(
            obj=feature_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if minimum_example_count_per_leaf is not None:
        inputs['MinimumExampleCountPerLeaf'] = try_set(
            obj=minimum_example_count_per_leaf,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if label_column_name is not None:
        inputs['LabelColumnName'] = try_set(
            obj=label_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if learning_rate is not None:
        inputs['LearningRate'] = try_set(
            obj=learning_rate,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if example_weight_column_name is not None:
        inputs['ExampleWeightColumnName'] = try_set(
            obj=example_weight_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if row_group_column_name is not None:
        inputs['RowGroupColumnName'] = try_set(
            obj=row_group_column_name,
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
    if best_step_ranking_regression_trees is not None:
        inputs['BestStepRankingRegressionTrees'] = try_set(
            obj=best_step_ranking_regression_trees,
            none_acceptable=True,
            is_of_type=bool)
    if use_line_search is not None:
        inputs['UseLineSearch'] = try_set(
            obj=use_line_search,
            none_acceptable=True,
            is_of_type=bool)
    if maximum_number_of_line_search_steps is not None:
        inputs['MaximumNumberOfLineSearchSteps'] = try_set(
            obj=maximum_number_of_line_search_steps,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if minimum_step_size is not None:
        inputs['MinimumStepSize'] = try_set(
            obj=minimum_step_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if optimization_algorithm is not None:
        inputs['OptimizationAlgorithm'] = try_set(
            obj=optimization_algorithm,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'GradientDescent',
                'AcceleratedGradientDescent',
                'ConjugateGradientDescent'])
    if early_stopping_rule is not None:
        inputs['EarlyStoppingRule'] = try_set(
            obj=early_stopping_rule,
            none_acceptable=True,
            is_of_type=dict)
    if early_stopping_metrics is not None:
        inputs['EarlyStoppingMetrics'] = try_set(
            obj=early_stopping_metrics,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if enable_pruning is not None:
        inputs['EnablePruning'] = try_set(
            obj=enable_pruning,
            none_acceptable=True,
            is_of_type=bool)
    if use_tolerant_pruning is not None:
        inputs['UseTolerantPruning'] = try_set(
            obj=use_tolerant_pruning,
            none_acceptable=True,
            is_of_type=bool)
    if pruning_threshold is not None:
        inputs['PruningThreshold'] = try_set(
            obj=pruning_threshold,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if pruning_window_size is not None:
        inputs['PruningWindowSize'] = try_set(
            obj=pruning_window_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if shrinkage is not None:
        inputs['Shrinkage'] = try_set(
            obj=shrinkage,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if dropout_rate is not None:
        inputs['DropoutRate'] = try_set(
            obj=dropout_rate,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if get_derivatives_sample_rate is not None:
        inputs['GetDerivativesSampleRate'] = try_set(
            obj=get_derivatives_sample_rate,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if write_last_ensemble is not None:
        inputs['WriteLastEnsemble'] = try_set(
            obj=write_last_ensemble,
            none_acceptable=True,
            is_of_type=bool)
    if maximum_tree_output is not None:
        inputs['MaximumTreeOutput'] = try_set(
            obj=maximum_tree_output,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if random_start is not None:
        inputs['RandomStart'] = try_set(
            obj=random_start,
            none_acceptable=True,
            is_of_type=bool)
    if filter_zero_lambdas is not None:
        inputs['FilterZeroLambdas'] = try_set(
            obj=filter_zero_lambdas,
            none_acceptable=True,
            is_of_type=bool)
    if baseline_scores_formula is not None:
        inputs['BaselineScoresFormula'] = try_set(
            obj=baseline_scores_formula, none_acceptable=True, is_of_type=str)
    if baseline_alpha_risk is not None:
        inputs['BaselineAlphaRisk'] = try_set(
            obj=baseline_alpha_risk, none_acceptable=True, is_of_type=str)
    if position_discount_freeform is not None:
        inputs['PositionDiscountFreeform'] = try_set(
            obj=position_discount_freeform,
            none_acceptable=True,
            is_of_type=str)
    if parallel_trainer is not None:
        inputs['ParallelTrainer'] = try_set(
            obj=parallel_trainer,
            none_acceptable=True,
            is_of_type=dict)
    if number_of_threads is not None:
        inputs['NumberOfThreads'] = try_set(
            obj=number_of_threads,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if seed is not None:
        inputs['Seed'] = try_set(
            obj=seed,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_selection_seed is not None:
        inputs['FeatureSelectionSeed'] = try_set(
            obj=feature_selection_seed,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if entropy_coefficient is not None:
        inputs['EntropyCoefficient'] = try_set(
            obj=entropy_coefficient,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if histogram_pool_size is not None:
        inputs['HistogramPoolSize'] = try_set(
            obj=histogram_pool_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if disk_transpose is not None:
        inputs['DiskTranspose'] = try_set(
            obj=disk_transpose,
            none_acceptable=True,
            is_of_type=bool)
    if feature_flocks is not None:
        inputs['FeatureFlocks'] = try_set(
            obj=feature_flocks,
            none_acceptable=True,
            is_of_type=bool)
    if categorical_split is not None:
        inputs['CategoricalSplit'] = try_set(
            obj=categorical_split,
            none_acceptable=True,
            is_of_type=bool)
    if maximum_categorical_group_count_per_node is not None:
        inputs['MaximumCategoricalGroupCountPerNode'] = try_set(
            obj=maximum_categorical_group_count_per_node,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if maximum_categorical_split_point_count is not None:
        inputs['MaximumCategoricalSplitPointCount'] = try_set(
            obj=maximum_categorical_split_point_count,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if minimum_example_fraction_for_categorical_split is not None:
        inputs['MinimumExampleFractionForCategoricalSplit'] = try_set(
            obj=minimum_example_fraction_for_categorical_split,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if minimum_examples_for_categorical_split is not None:
        inputs['MinimumExamplesForCategoricalSplit'] = try_set(
            obj=minimum_examples_for_categorical_split,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bias is not None:
        inputs['Bias'] = try_set(
            obj=bias,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bundling is not None:
        inputs['Bundling'] = try_set(
            obj=bundling,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'None',
                'AggregateLowPopulation',
                'Adjacent'])
    if maximum_bin_count_per_feature is not None:
        inputs['MaximumBinCountPerFeature'] = try_set(
            obj=maximum_bin_count_per_feature,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if sparsify_threshold is not None:
        inputs['SparsifyThreshold'] = try_set(
            obj=sparsify_threshold,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_first_use_penalty is not None:
        inputs['FeatureFirstUsePenalty'] = try_set(
            obj=feature_first_use_penalty,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_reuse_penalty is not None:
        inputs['FeatureReusePenalty'] = try_set(
            obj=feature_reuse_penalty,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if gain_confidence_level is not None:
        inputs['GainConfidenceLevel'] = try_set(
            obj=gain_confidence_level,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if softmax_temperature is not None:
        inputs['SoftmaxTemperature'] = try_set(
            obj=softmax_temperature,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if execution_time is not None:
        inputs['ExecutionTime'] = try_set(
            obj=execution_time,
            none_acceptable=True,
            is_of_type=bool)
    if feature_fraction is not None:
        inputs['FeatureFraction'] = try_set(
            obj=feature_fraction,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bagging_size is not None:
        inputs['BaggingSize'] = try_set(
            obj=bagging_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bagging_example_fraction is not None:
        inputs['BaggingExampleFraction'] = try_set(
            obj=bagging_example_fraction,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_fraction_per_split is not None:
        inputs['FeatureFractionPerSplit'] = try_set(
            obj=feature_fraction_per_split,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if smoothing is not None:
        inputs['Smoothing'] = try_set(
            obj=smoothing,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if allow_empty_trees is not None:
        inputs['AllowEmptyTrees'] = try_set(
            obj=allow_empty_trees,
            none_acceptable=True,
            is_of_type=bool)
    if feature_compression_level is not None:
        inputs['FeatureCompressionLevel'] = try_set(
            obj=feature_compression_level,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if compress_ensemble is not None:
        inputs['CompressEnsemble'] = try_set(
            obj=compress_ensemble,
            none_acceptable=True,
            is_of_type=bool)
    if print_test_graph is not None:
        inputs['PrintTestGraph'] = try_set(
            obj=print_test_graph,
            none_acceptable=True,
            is_of_type=bool)
    if print_train_valid_graph is not None:
        inputs['PrintTrainValidGraph'] = try_set(
            obj=print_train_valid_graph,
            none_acceptable=True,
            is_of_type=bool)
    if test_frequency is not None:
        inputs['TestFrequency'] = try_set(
            obj=test_frequency,
            none_acceptable=True,
            is_of_type=numbers.Real)
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
