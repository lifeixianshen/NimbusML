# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
OneHotVectorizer
"""

__all__ = ["OneHotVectorizer"]


from ....entrypoints.transforms_categoricalonehotvectorizer import \
    transforms_categoricalonehotvectorizer
from ....utils.utils import trace
from ...base_pipeline_item import BasePipelineItem, EqualInputOutputSignature


class OneHotVectorizer(
        BasePipelineItem,
        EqualInputOutputSignature):
    """

    Categorical transform that can be performed on data before
    training a model.

    .. remarks::
        The ``OneHotVectorizer`` transform passes through a data set,
        operating
        on text columns, to build a dictionary of categories. For each row,
        the entire text string appearing in the input column is defined as a
        category. The output of the categorical transform is an indicator
        vector.
        Each slot in this vector corresponds to a category in the dictionary,
        so
        its length is the size of the built dictionary. The categorical
        transform
        can be applied to one or more columns, in which case it builds a
        separate
        dictionary for each column that it is applied to.

        ``OneHotVectorizer`` is not currently supported to handle factor
        data.

    :param max_num_terms: An integer that specifies the maximum number of
        categories to include in the dictionary. The default value is
        1000000.

    :param output_kind: A character string that specifies the kind of output
        kind.

        * ``"Bag"``: Outputs a multi-set vector. If the input column is a
          vector of categories, the output contains one vector, where the
        value in
          each slot is the number of occurrences of the category in the input
          vector. If the input column contains a single category, the
        indicator
          vector and the bag vector are equivalent
        * ``"Ind"``: Outputs an indicator vector. The input column is a
        vector
          of categories, and the output contains one indicator vector per
        slot in
          the input column.
        * ``"Key"``: Outputs an index. The output is an integer id (between
          1 and the number of categories in the dictionary) of the category.
        * ``"Bin"``: Outputs a vector which is the binary representation of
        the category.

        The default value is ``"Ind"``.

    :param term: Optional character vector of terms or categories.

    :param sort: A character string that specifies the sorting criteria.

        * ``"Occurrence"``: Sort categories by occurences. Most frequent is
        first.
        * ``"Value"``: Sort categories by values.

    :param text_key_values: Whether key value metadata should be text,
        regardless of the actual input type.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`OneHotHashVectorizer
        <nimbusml.feature_extraction.categorical.OneHotHashVectorizer>`

    .. index:: transform, category

    Example:
       .. literalinclude:: /../nimbusml/examples/OneHotVectorizer.py
              :language: python
    """

    @trace
    def __init__(
            self,
            max_num_terms=1000000,
            output_kind='Indicator',
            term=None,
            sort='ByOccurrence',
            text_key_values=True,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.max_num_terms = max_num_terms
        self.output_kind = output_kind
        self.term = term
        self.sort = sort
        self.text_key_values = text_key_values

    @property
    def _entrypoint(self):
        return transforms_categoricalonehotvectorizer

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
            max_num_terms=self.max_num_terms,
            output_kind=self.output_kind,
            term=self.term,
            sort=self.sort,
            text_key_values=self.text_key_values)

        all_args |= algo_args
        return self._entrypoint(**all_args)
