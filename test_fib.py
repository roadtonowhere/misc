import pytest
import urllib2
import json

path = "http://ec2-52-33-166-73.us-west-2.compute.amazonaws.com:5000/api/fibonacci/"

def test_inputs():
    inputs = [0,1,2,3,4]
    outputs = [0,1,1,2,3]
    for idx, i in enumerate(inputs):
        input_path = path + str(i)
        rsp = urllib2.urlopen(input_path)
        data = json.load(rsp);
        assert(data['fibonacci'] == outputs[idx])

def test_corner():
    inputs = ['a', 'B', 'foo', '@', -1, -10, -0]
    for i in inputs:
        input_path = path + str(i)
	try:
            rsp = urllib2.urlopen(input_path)
        except urllib2.HTTPError as e:
            assert(e.code == 404)

