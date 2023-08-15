# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TreeFeaturizer
"""

__all__ = ["TreeFeaturizer"]


from ...entrypoints.transforms_treeleaffeaturizer import \
    transforms_treeleaffeaturizer
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignature


class TreeFeaturizer(BasePipelineItem, DefaultSignature):
    """

    TreeFeaturizer.

    .. remarks::
        Trains a tree ensemble, or loads it from a file, then maps a numeric
        feature vector to three outputs:

        * A vector containing the individual tree outputs of the tree
          ensemble.
        * A vector indicating the leaves that the feature vector falls on in
          the tree ensemble.
        * A vector indicating the paths that the feature vector falls on in
          the
          tree ensemble. If a both a model file and a trainer are specified,
          will use the model file. If neither are specified, will train a
          default FastTree model. This can handle key labels by training a
          regression model towards their optionally permuted indices.

    :param predictor_model: Trainer to use.

    :param suffix: Output column: The suffix to append to the default column
        names.

    :param label_permutation_seed: If specified, determines the permutation
        seed for applying this featurizer to a multiclass problem.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`TensorFlowScorer
        <nimbusml.preprocessing.TensorFlowScorer>`
    """

    @trace
    def __init__(
            self,
            predictor_model,
            suffix=None,
            label_permutation_seed=0,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.predictor_model = predictor_model
        self.suffix = suffix
        self.label_permutation_seed = label_permutation_seed

    @property
    def _entrypoint(self):
        return transforms_treeleaffeaturizer

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            predictor_model=self.predictor_model,
            suffix=self.suffix,
            label_permutation_seed=self.label_permutation_seed)

        all_args |= algo_args
        return self._entrypoint(**all_args)
