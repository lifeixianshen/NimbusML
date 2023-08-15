# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
LinearSvmBinaryClassifier
"""

__all__ = ["LinearSvmBinaryClassifier"]


from ...entrypoints.trainers_linearsvmbinaryclassifier import \
    trainers_linearsvmbinaryclassifier
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class LinearSvmBinaryClassifier(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Linear Support Vector Machine (SVM) Binary Classifier

    .. remarks::
        Linear SVM implements an algorithm that finds a hyperplane in the
        feature space for binary classification, by solving an SVM problem.
        For instance, for a given feature vector, the prediction is given by
        determining what side of the hyperplane the    point falls into. That is
        the same as the sign of the feautures' weighted sum (the weights being
        computed by the algorithm) plus the bias computed by the algorithm.

        This algorithm implemented is the PEGASOS method, which alternates
        between stochastic gradient descent steps and projection steps,
        introduced by Shalev-Shwartz, Singer and Srebro.


        **Reference**

            `Wikipedia entry for Support Vector Machine
            <https://en.wikipedia.org/wiki/Support-vector_machine>`_

            `Pegasos: Primal Estimated sub-GrAdient SOlver for SVM
            <https://ttic.uchicago.edu/~shai/papers/ShalevSiSr07.pdf>`_


    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling ensures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MinMax`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether trainer should cache input training data.

    :param l2_regularization: L2 regularization weight. It also controls the
        learning rate, with the learning rate being inversely proportional to
        it.

    :param perform_projection: Perform projection to unit-ball? Typically used
        with batch size > 1.

    :param number_of_iterations: Number of iterations.

    :param initial_weights_diameter: Sets the initial weights diameter that
        specifies the range from which values are drawn for the initial
        weights. These weights are initialized randomly from within this range.
        For example, if the diameter is specified to be ``d``, then the weights
        are uniformly distributed between ``-d/2`` and ``d/2``. The default
        value is ``0``, which specifies that all the  weights are set to zero.

    :param no_bias: No bias.

    :param initial_weights: Initial Weights and bias, comma-separated.

    :param shuffle: Whether to shuffle for each training iteration.

    :param batch_size: Batch size.

    :param params: Additional arguments sent to compute engine.

    .. index:: models, classification, svm

    Example:
       .. literalinclude:: /../nimbusml/examples/LinearSvmBinaryClassifier.py
               :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            l2_regularization=0.001,
            perform_projection=False,
            number_of_iterations=1,
            initial_weights_diameter=0.0,
            no_bias=False,
            initial_weights=None,
            shuffle=True,
            batch_size=1,
            **params):
        BasePipelineItem.__init__(
            self, type='classifier', **params)

        self.normalize = normalize
        self.caching = caching
        self.l2_regularization = l2_regularization
        self.perform_projection = perform_projection
        self.number_of_iterations = number_of_iterations
        self.initial_weights_diameter = initial_weights_diameter
        self.no_bias = no_bias
        self.initial_weights = initial_weights
        self.shuffle = shuffle
        self.batch_size = batch_size

    @property
    def _entrypoint(self):
        return trainers_linearsvmbinaryclassifier

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column_name=self._getattr_role(
                'feature_column_name',
                all_args),
            label_column_name=self._getattr_role(
                'label_column_name',
                all_args),
            example_weight_column_name=self._getattr_role(
                'example_weight_column_name',
                all_args),
            normalize_features=self.normalize,
            caching=self.caching,
            lambda_=self.l2_regularization,
            perform_projection=self.perform_projection,
            number_of_iterations=self.number_of_iterations,
            initial_weights_diameter=self.initial_weights_diameter,
            no_bias=self.no_bias,
            initial_weights=self.initial_weights,
            shuffle=self.shuffle,
            batch_size=self.batch_size)

        all_args |= algo_args
        return self._entrypoint(**all_args)
