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


def _is_positive_number(element):
    return element > 0


def _is_number_int(element):
    return int(element)


def _is_in_options(element, control_value):
    return element in control_value


# Processors

def _process_to_title_string(element):
    return element.title()


def _process_upper(element):
    return element.upper()


QUESTION_TYPES = {
    'default': {
        'input_message': '> ',
        'error_message': '',
        'cast': str,
        'validations': {
            'binary_validations': [],
            'controlled_validations': []
        },
        'processors': []
    },
    'age': {
        'input_message': 'Qual a sua idade? > ',
        'error_message': 'Idade invalida. Tente novamente.',
        'cast': int,
        'validations': {
            'binary_validations': [_is_numeric, _is_number_int, _is_positive_number],
            'controlled_validations': [
                {'validator': _max_length, 'control_value': 3},
                {'validator': _max_value_int, 'control_value': 130},
            ],
        },
        'processors': []
    },
    'name': {
        'input_message': 'Nome > ',
        'error_message': 'Valor inválido. Tente novamente.',
        'cast': str,
        'validations': {
            'binary_validations': [],
            'controlled_validations': [],
        },
        'processors': [
            {'processor': _process_to_title_string},
        ]
    },
    'gender': {
        'input_message': 'Sexo: [M/F] > ',
        'error_message': 'Valor inválido. Tente novamente.',
        'cast': str,
        'validations': {
            'binary_validations': [],
            'controlled_validations': [
                {'validator': _is_in_options, 'control_value': ['F', 'M']},
            ],
        },
        'processors': [
            {'processor': _process_upper},
        ]
    },
    'continue': {
        'input_message': 'Continuar: [S/N] > ',
        'error_message': 'Valor inválido. Tente novamente.',
        'cast': str,
        'validations': {
            'binary_validations': [],
            'controlled_validations': [
                {'validator': _is_in_options, 'control_value': ['S', 'N']},
            ],
        },
        'processors': [
            {'processor': _process_upper},
        ]
    },
    'int': {
        'input_message': 'Digite um valor inteiro > ',
        'error_message': 'Valor inválido. Tente novamente.',
        'cast': int,
        'validations': {
            'binary_validations': [_is_numeric, _is_number_int],
            'controlled_validations': [],
        },
        'processors': []
    },
}


def type_input(
        get_type='default',
        input_message='',
        error_message='',
        cast=None,
        validation_funtions=[],
        extends_validations=True,
        processors_functions=[],
        extends_processors=True):

    while True:
        try:

            response_user = input(
                input_message or QUESTION_TYPES[get_type]['input_message']
            )

            value_pre_processors = response_user

            if extends_processors is True:
                for processor in QUESTION_TYPES[get_type]['processors']:
                    value_pre_processors = processor['processor'](
                        value_pre_processors)

            if processors_functions:
                for processor in processors_functions:
                    value_pre_processors = processor(value_pre_processors)

            value_post_processors = value_pre_processors

            if extends_validations is True:
                for validation_function in QUESTION_TYPES[get_type]['validations']['binary_validations']:
                    if validation_function(value_post_processors) is False:
                        raise Exception

                for validation_schema in QUESTION_TYPES[get_type]['validations']['controlled_validations']:
                    if validation_schema['validator'](value_post_processors, validation_schema['control_value']) is False:
                        raise Exception

            if validation_funtions:
                for validation_function in validation_funtions:
                    if validation_function(value_post_processors) is False:
                        raise Exception

            if cast:
                return cast(value_post_processors)
            else:
                return QUESTION_TYPES[get_type]['cast'](value_post_processors)

        except Exception:
            print(error_message or QUESTION_TYPES[get_type]['error_message'])
