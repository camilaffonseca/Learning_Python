# coding: utf-8

'''Moid para aux com iout out.

Recebe tipo para perguntar ao usr
'''

# Validators


def _max_length(element, control_value):
    return len(element) <= control_value


def _max_value_int(element, control_value):
    return int(element) <= control_value


def _is_numeric(element):
    return element.isnumeric()


def _is_positive_number_int(element):
    return int(element) > 0

QUESTION_TYPES = {
    'default': {
        'input_message': '> ',
        'error_message': '',
        'cast': str,
        'validations': {
            'binary_validations': [],
            'controlled_validations': []
        }
    },
    'age': {
        'input_message': 'Qual a sua idade? > ',
        'error_message': 'Idade invalida. Tente novamente.',
        'cast': int,
        'validations': {
            'binary_validations': [_is_numeric, _is_positive_number_int],
            'controlled_validations': [
                {'validator': _max_length, 'control_value': 3},
                {'validator': _max_value_int, 'control_value': 130},
            ]
        }
    },
}


def type_input(type='default', input_message='', error_message='', cast=str, validation_funtions=[], extends=True):
    while True:
        try:
            response_user = input(
                input_message or QUESTION_TYPES[type]['input_message'])

            if validation_funtions:
                for validation_function in validation_funtions:
                    if validation_function(response_user) is False:
                        raise Exception

            if extends is True:
                for validation_function in QUESTION_TYPES[type]['validations']['binary_validations']:
                    if validation_function(response_user) is False:
                        raise Exception

                for validation_schema in QUESTION_TYPES[type]['validations']['controlled_validations']:
                    if validation_schema['validator'](response_user, validation_schema['control_value']) is False:
                        raise Exception

            return cast(response_user)

        except Exception:
            print(error_message or QUESTION_TYPES[type]['error_message'])
