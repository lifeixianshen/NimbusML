# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------

# This file is manually created. It's not autogenerated.

__all__ = ['create_loss', 'check_loss',
           'classificationlossfunction_exploss',
           'classificationlossfunction_hingeloss',
           'classificationlossfunction_logloss',
           'classificationlossfunction_smoothedhingeloss',
           'sdcaclassificationlossfunction_hingeloss',
           'sdcaclassificationlossfunction_logloss',
           'sdcaclassificationlossfunction_smoothedhingeloss',
           'sdcaregressionlossfunction_squaredloss',
           'regressionlossfunction_poissonloss',
           'regressionlossfunction_squaredloss',
           'regressionlossfunction_tweedieloss']

from .loss_table_json import loss_table_json
from ...entrypoints._classificationlossfunction_exploss import \
    exp_loss as classificationlossfunction_exploss
from ...entrypoints._classificationlossfunction_hingeloss import \
    hinge_loss as classificationlossfunction_hingeloss
from ...entrypoints._classificationlossfunction_logloss import \
    log_loss as classificationlossfunction_logloss
from ...entrypoints._classificationlossfunction_smoothedhingeloss import \
    smoothed_hinge_loss as classificationlossfunction_smoothedhingeloss
from ...entrypoints._regressionlossfunction_poissonloss import \
    poisson_loss as regressionlossfunction_poissonloss
from ...entrypoints._regressionlossfunction_squaredloss import \
    squared_loss as regressionlossfunction_squaredloss
from ...entrypoints._regressionlossfunction_tweedieloss import \
    tweedie_loss as regressionlossfunction_tweedieloss
from ...entrypoints._sdcaclassificationlossfunction_hingeloss import \
    hinge_loss as sdcaclassificationlossfunction_hingeloss
from ...entrypoints._sdcaclassificationlossfunction_logloss import \
    log_loss as sdcaclassificationlossfunction_logloss
from ...entrypoints._sdcaclassificationlossfunction_smoothedhingeloss \
    import \
    smoothed_hinge_loss as sdcaclassificationlossfunction_smoothedhingeloss
from ...entrypoints._sdcaregressionlossfunction_squaredloss import \
    squared_loss as sdcaregressionlossfunction_squaredloss


class _LossFactory:
    loss_table = None
    valid_component_kinds = None
    valid_loss_str_per_kind = None
    available_losses = globals()

    @classmethod
    def _load_table(cls):
        cls.loss_table = loss_table_json
        cls.valid_component_kinds = set(cls.loss_table.keys())
        cls.valid_loss_str_per_kind = {
            k: set(
                v.keys()) for (k, v) in cls.loss_table.items()}

    @classmethod
    def _get_ep(cls, ep_function, params):
        assert ep_function in cls.available_losses, f'{ep_function} is not imported'
        ep_function = cls.available_losses[ep_function]
        return ep_function(**params) if params else ep_function()

    @classmethod
    def create_loss(cls, component_kind, learner, api_loss):
        if cls.loss_table is None:
            cls._load_table()

        assert (
            component_kind in cls.valid_component_kinds
        ), f'{component_kind} component kind does not exist in loss table'

        component_kind_losses = cls.loss_table[component_kind]
        valid_str_losses = cls.valid_loss_str_per_kind[component_kind]

        error_msg = (
            "{} does not support '{}' as loss. The supported values "
            "are {} and their class variants. "
            + "Please see the documentation page for more "
            "information."
        ).format(
            learner, api_loss, ', '.join([f"'{s}'" for s in valid_str_losses])
        )

        if isinstance(api_loss, str):
            api_loss_name = api_loss
            api_loss_params = None
        else:
            try:
                api_loss_name = getattr(api_loss, '_string_name')
                api_loss_params = getattr(api_loss, '_params')
            except BaseException:
                # The given object is not a nimbusml loss object
                raise TypeError(error_msg)

        if api_loss_name not in valid_str_losses:
            raise TypeError(error_msg)

        return cls._get_ep(component_kind_losses[api_loss_name], api_loss_params)


def create_loss(component_kind, learner, api_loss):
    return _LossFactory.create_loss(component_kind, learner, api_loss)


def check_loss(component_kind, learner, api_loss):
    # Just run create_loss(), which will throw in case of errors
    _LossFactory.create_loss(component_kind, learner, api_loss)
