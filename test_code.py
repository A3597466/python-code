def heart_status():
    return "good"

def test_heart():
    ###
    ###测试一下心脏状态
    ###
    assert heart_status() == "healthy"
    print("hello world")