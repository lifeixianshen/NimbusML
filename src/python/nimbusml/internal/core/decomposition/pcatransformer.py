# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
PcaTransformer
"""

__all__ = ["PcaTransformer"]


from ...entrypoints.transforms_pcacalculator import transforms_pcacalculator
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class PcaTransformer(BasePipelineItem, DefaultSignatureWithRoles):
    """

    Pca Transformer

    .. remarks::
        `Principle Component Analysis (PCA)
        <https://en.wikipedia.org/wiki/Principal_component_analysis>`_ is a
        dimensionality-reduction transform which computes the projection of
        the feature vector to onto a low-rank
        subspace. Its training is done using the technique described in the
        paper `Combining Structured and Unstructured
        Randomness in Large Scale PCA
        <https://arxiv.org/pdf/1310.6304v2.pdf>`_ by Nikos Karampatziakis and
        Paul
        Mineiro, and the paper `Finding Structure with Randomness:
        Probabilistic Algorithms for Constructing Approximate
        Matrix Decompositions <https://arxiv.org/pdf/0909.4061v2.pdf>`_ by N.
        Halko et al.

    :param rank: The number of components in the PCA. The default value is
        20.

    :param oversampling: Oversampling parameter for randomized PCA training.

    :param center: If enabled, data is centered to be zero mean.

    :param random_state: The seed for random number generation.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`PcaAnomalyDetector
        <nimbusml.decomposition.PcaAnomalyDetector>`.

    .. index:: normalize, preprocessing

    Example:
       .. literalinclude:: /../nimbusml/examples/PcaTransformer.py
              :language: python
    """

    @trace
    def __init__(
            self,
            rank=20,
            oversampling=20,
            center=True,
            random_state=0,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.rank = rank
        self.oversampling = oversampling
        self.center = center
        self.random_state = random_state

    @property
    def _entrypoint(self):
        return transforms_pcacalculator

    @trace
    def _get_node(self, **all_args):

        input_columns = self.input
        if input_columns is None and 'input' in all_args:
            input_columns = all_args['input']
        if 'input' in all_args:
            all_args.pop('input')

        output_columns = self.output
        if output_columns is None and 'output' in all_args:
            output_columns = all_args['output']
        if 'output' in all_args:
            all_args.pop('output')

        if any(isinstance(el, list) for el in input_columns):
            input_columns = [y for x in input_columns for y in x]
        conc = None
        if isinstance(
                input_columns,
                list) and len(input_columns) > 1:
            # We concatenate the columns.
            data = all_args.pop("data")
            outcol = f"temp_{id(self)}"
            if isinstance(output_columns, list):
                if len(output_columns) == 1:
                    outcol = output_columns[0]
            output_data = f"{all_args['output_data']}_c{id(self)}"
            model = f"{all_args['model']}_c{id(self)}"
            conc = self._add_concatenator_node(
                data, input_columns, output_data, outcol, model)
            input_columns = [outcol]
            all_args["data"] = output_data

        # validate input
        if input_columns is None:
            raise ValueError(
                "'None' input passed when it cannot be none.")

        if not isinstance(input_columns, list):
            raise ValueError(
                f"input has to be a list of strings, instead got {type(input_columns)}"
            )

        # validate output
        if output_columns is None:
            output_columns = input_columns

        if not isinstance(output_columns, list):
            raise ValueError(
                f"output has to be a list of strings, instead got {type(output_columns)}"
            )

        algo_args = dict(
            column=[
                dict(
                    Source=i,
                    Name=o) for i,
                o in zip(
                    input_columns,
                    output_columns)] if input_columns else None,
            example_weight_column_name=self._getattr_role(
                'example_weight_column_name',
                all_args),
            rank=self.rank,
            oversampling=self.oversampling,
            center=self.center,
            seed=self.random_state)

        all_args |= algo_args

        return [conc, self._entrypoint(
            **all_args)] if conc else self._entrypoint(**all_args)
