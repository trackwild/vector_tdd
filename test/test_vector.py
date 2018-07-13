from source.vector import Vector

def test_make_vector():
    v = Vector([1, 2, 3])
    assert len(v.nums) == 3

def test_dimension():
    v = Vector([2,4,6,8])
    assert v.dims == 4

def test_norm():
    v = Vector([3,4])
    assert v.norm == 5
    
def test_unit_vector():
    v = Vector([5,3,1,9,2])
    assert v.unit_vector().norm == 1

def test_scale_vector():
    v = Vector([1, 2, 3])
    assert v.scale_vector(3) == Vector([3,6,9])

