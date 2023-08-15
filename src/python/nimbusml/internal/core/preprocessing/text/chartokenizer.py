# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
CharTokenizer
"""

__all__ = ["CharTokenizer"]


from ....entrypoints.transforms_charactertokenizer import \
    transforms_charactertokenizer
from ....utils.utils import trace
from ...base_pipeline_item import BasePipelineItem, DefaultSignature


class CharTokenizer(BasePipelineItem, DefaultSignature):
    """

    Text transforms that can be performed on data before training
    a model.

    .. remarks::
        The ``CharTokenizer`` transform is a character-oriented tokenizer
        where
        text is considered a sequence of characters.

    :param use_marker_chars: Whether to mark the beginning/end of each row/slot
        with start of text character (0x02)/end of text character (0x03).

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`FromKey <nimbusml.preprocessing.FromKey>`,
        :py:class:`ToKey <nimbusml.preprocessing.ToKey>`,
        :py:class:`OneHotHashVectorizer
        <nimbusml.feature_extraction.categorical.OneHotHashVectorizer>`,
        :py:class:`OneHotVectorizer
        <nimbusml.feature_extraction.categorical.OneHotVectorizer>`,
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`.

    .. index:: transform, preprocessing, text

    Example:
       .. literalinclude:: /../nimbusml/examples/CharTokenizer.py
              :language: python
    """

    @trace
    def __init__(
            self,
            use_marker_chars=True,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.use_marker_chars = use_marker_chars

    @property
    def _entrypoint(self):
        return transforms_charactertokenizer

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
            use_marker_chars=self.use_marker_chars)

        all_args |= algo_args
        return self._entrypoint(**all_args)
