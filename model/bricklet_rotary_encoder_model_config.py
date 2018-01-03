# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

mod = {}
sensor_fields = {}
actor_fields = {}
other_actor_fields = {}
other_sensors = {}
special_fields = {}
other_fields = {}
callbacks = {}
enabled_fields = {}
debounce_period_fields = {}
threshold_fields = {}

mod['getCount'] = {
            'field': 'count',
            'subdevice_type': 'sensor',
            'function_type': 'getter',
            'skip': False
            }

mod['getCountCallbackThreshold'] = {
            'field': 'countCallbackThreshold',
            'subdevice_type': 'actor',
            'function_type': 'callback_threshold_getter',
            'skip': False
            }

mod['getDebouncePeriod'] = {
            'field': 'debouncePeriod',
            'subdevice_type': 'actor',
            'function_type': 'callback_debounce_period_getter',
            'skip': False
            }

mod['getCountCallbackPeriod'] = {
            'field': 'countCallbackPeriod',
            'subdevice_type': 'actor',
            'function_type': 'callback_period_getter',
            'skip': False
            }

mod['setCountCallbackPeriod'] = {
            'field': 'countCallbackPeriod',
            'subdevice_type': 'actor',
            'function_type': 'callback_period_setter',
            'skip': False
            }

mod['setCountCallbackThreshold'] = {
            'field': 'countCallbackThreshold',
            'subdevice_type': 'actor',
            'function_type': 'callback_threshold_setter',
            'skip': False
            }

mod['setDebouncePeriod'] = {
            'field': 'debouncePeriod',
            'subdevice_type': 'actor',
            'function_type': 'callback_debounce_period_setter',
            'skip': False
            }

mod['getIdentity'] = {
            'field': 'identity',
            'subdevice_type': 'identity',
            'function_type': 'getter',
            'skip': False
            }

mod['isPressed'] = {
            'field': 'isPressed',
            'subdevice_type': 'other',
            'function_type': 'setter',
            'skip': False
            }

callbacks['count'] = {
            'field': 'count',
            'function_type': 'callback',
            'skip': False
            }
        
callbacks['countReached'] = {
            'field': 'countReached',
            'function_type': 'callback',
            'skip': False
            }
        
callbacks['pressed'] = {
            'field': 'pressed',
            'function_type': 'callback',
            'skip': False
            }
        
callbacks['released'] = {
            'field': 'released',
            'function_type': 'callback',
            'skip': False
            }
        
sensor_fields['getCount'] = {
            'value_type': 'number',
            'field': 'count',
            'field_type': ['int32'],
            'field_type_cardinality': [1],
            'default_value': 100,
            'max_value': 1000,
            'min_value': 0,
            'step_value': 1,
            'skip': False
        }
        
threshold_fields['getCountCallbackThreshold'] = {
            'value_type': 'threshold_buffer',
            'field': 'countCallbackThreshold',
            'field_type': ['char', 'int32', 'int32'],
            'field_type_cardinality': [1, 1, 1],
            'default_value': 'x00',
            'max_value': 1000,
            'min_value': 0,
            'skip': False
        }
        
debounce_period_fields['getDebouncePeriod'] = {
            'value_type': 'number',
            'field': 'debouncePeriod',
            'field_type': ['uint32'],
            'field_type_cardinality': [1],
            'default_value': 100,
            'max_value': 1000,
            'min_value': 0,
            'step_value': 1,
            'skip': False
        }
        
other_fields['getIdentity'] = {
            'field': 'identity',
            'skip': False
            }

other_fields['isPressed'] = {
            'value_type': 'number',
            'field': 'isPressed',
            'field_type': ['bool'],
            'field_type_cardinality': [1],
            'default_value': 100,
            'max_value': 1000,
            'min_value': 0,
            'step_value': 1,
            'skip': False
        }
        