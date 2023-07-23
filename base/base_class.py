class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current_url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Good value word - {value_word}")

    def information_output(self, var1):
        value_var1 = var1.text
        print("******Print information about product*******")
        print(value_var1)



    def assert_text(self, text1, text2):
        value_text1 = text1.text
        value_text2 = text2.text
        assert value_text1 == value_text2
        print(f"Good {value_text1} = {value_text2}")


