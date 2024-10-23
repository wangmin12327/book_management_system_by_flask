# test_search.py
from search_page import SearchPage


class TestSearch:
    def test_search(self):
        """
        调用SearchPage类中的search_stock方法
        :return:
        """
        text = SearchPage().search_stock("阿里巴巴-sw")

        # 断言要写在主调函数中
        assert "阿里巴巴-sw" == text
