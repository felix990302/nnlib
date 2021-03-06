from numpy.testing import assert_allclose
from numpy import array

from nnlib.utils.activation import sigmoid, relu


def test_sigmoid():
    arr = sigmoid(array([[1, 2]]))

    assert_allclose(
            arr,
            array([[0.73105858, 0.88079708]])
            )


def test_relu():
    arr = relu(array([[0.5, -0.5]]))

    assert_allclose(
            arr,
            array([[0.5, 0]])
            )
