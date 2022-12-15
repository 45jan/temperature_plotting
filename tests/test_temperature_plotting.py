import pytest, os

import temperature_plotting as tpl

def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 10 # test if the answer is the expected
    assert type(calc) == float # test if the type of the answer is the one expeced

    calc = tpl.compute_mean([-10, 10])
    assert calc == 0 # test special cases (negative numbers)

    calc = tpl.compute_mean([0, 10, 0])
    # assert calc == 3.33 # this would fail
    assert round(calc,4) == 3.3333, "Check that the average is roughly correct" # displays a message if an error
    
    with pytest.raises(TypeError) as e: # asserts that this particular error type will occur
        calc = tpl.compute_mean(["a", "b", "c"]) # this would fail, because the function does not work with strings
    assert e is not None, "We should not be able to average strin"
    
    calc = tpl.compute_mean([])
    assert calc == None # this failed in original function definition, so we will change it (see below)
    
    calc = tpl.compute_mean([-5, 5])
    assert calc == 1

    
test_compute_mean()

# integration test
import os

def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")

test_main()
