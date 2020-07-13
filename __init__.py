"""
获取所有文件
获取文件中的类、方法、常量、变量
找到可重构优化的点
给出解决方案
替换执行方案
"""
from inspect import getmembers


class FileFilter(object):
    def get_all_py_files(self, path) -> list:
        pass

    def get_class_from_file(self, path):
        pass

    def get_func_from_file(self, path):
        pass

    def get_method_from_file(self, path):
        pass

    def get_constant_from_file(self, path):
        pass

    def get_locals_from_file(self, path):
        pass

    def get_globals_from_file(self, path):
        pass


class Comparer(object):
    def check_class_has_more_than_methods(self, c):
        pass

    def check_func_has_more_than_lines(self, f):
        pass

    def check_func_has_constant(self, f):
        pass

    def check_func_has_more_than_arguments(self, f):
        pass

    def check_variable_name_is_legal(self, n):
        pass

    def check_func_has_doc_string(self, f):
        pass

    def check_class_has_doc_string(self, c):
        pass


class Solution(object):
    def solution_of_class_has_more_than_methods(self):
        pass

    def solution_of_func_has_more_than_lines(self):
        pass

    def solution_of_func_has_constant(self):
        pass

    def solution_of_func_has_more_than_arguments(self):
        pass

    def solution_of_variable_name_is_legal(self):
        pass

    def solution_of_func_has_doc_string(self):
        pass

    def solution_of_class_has_doc_string(self):
        pass


def replace(old, new, path, line_no):
    pass
