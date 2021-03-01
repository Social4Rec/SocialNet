# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Tencent Inc. All rights reserved.
# Authors: xinghaisun

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from components.transforms.base_transform import BaseTransform


class FeatureSelector(BaseTransform):

    def __init__(self, feature_configs):
        self._feature_configs = feature_configs

    def _transform_fn(self, example):
        feature_map = dict()
        for config in self._feature_configs:
            if config.size == -1:
                feature_map[config.name] = tf.FixedLenSequenceFeature(
                    shape=[],
                    dtype=config.dtype,
                    allow_missing=True,
                    default_value=config.default_value,
                )
            else:
                feature_map[config.name] = tf.FixedLenFeature(
                    shape=[config.size],
                    dtype=config.dtype,
                    default_value=config.default_value
                )
        return tf.parse_example(example, feature_map)
