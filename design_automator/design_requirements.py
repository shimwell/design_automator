import operator as op

requirements = {
    "weight_of_vessel": [
        (op.lt, 3e6)
    ],
    "radius_of_vessel": [
        (op.lt, 100)
    ],
    "tritium_breeding_ratio": [
        (op.ge, 1.1),
        (op.lt, 3)
    ],
    "heating_of_the_blanket": [
        (op.ge, 10e6)
    ]
}
