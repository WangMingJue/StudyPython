def check_condition(condition):
    if condition:
        return True
    else:
        return False


# 任何非0和非空（null）值为true，0 或者 null为false。
if __name__ == '__main__':
    print("Check Condition {} Result is : {}".format(0, check_condition(0)))
    print("Check Condition {} Result is : {}".format(-1, check_condition(-1)))
    print("Check Condition {} Result is : {}".format(-3, check_condition(-3)))
    print("Check Condition {} Result is : {}".format(3, check_condition(3)))
    print("Check Condition {} Result is : {}".format("", check_condition("")))
    print("Check Condition {} Result is : {}".format(" ", check_condition(" ")))
    print("Check Condition {} Result is : {}".format("a", check_condition("a")))
    print("Check Condition {} Result is : {}".format([], check_condition([])))
    print("Check Condition {} Result is : {}".format([1], check_condition([1])))
    print("Check Condition {} Result is : {}".format([""], check_condition([""])))
    print("Check Condition {} Result is : {}".format([0], check_condition([0])))
    print("Check Condition {} Result is : {}".format({}, check_condition({})))
    print("Check Condition {} Result is : {}".format({""}, check_condition({""})))
    print("Check Condition {} Result is : {}".format({"a"}, check_condition({"a"})))
    print("Check Condition {} Result is : {}".format({"a": 1}, check_condition({"a": 1})))
    print("Check Condition {} Result is : {}".format(None, check_condition(None)))
