"""
获取所有文件
获取文件中的类、方法、常量、变量
找到可重构优化的点
给出解决方案
替换执行方案
"""
import os
import importlib
from inspect import getmembers


class FileFilter(object):
    def get_all_py_files(self, path):
        py_files = []
        project = os.path.abspath(path)

        print(self.find_py_files(project, py_files))

    def find_py_files(self, base, py_files):
        # if os.path.isdir(base):
        # todo 遍历并递归文件夹
        sub = os.listdir(base)
        py_files += self._find_py_files_in_current_dir(sub, py_files)

        sub_dir = list(filter(lambda x: os.path.isdir(os.path.join(base, x)), sub))
        # print(sub_dir)
        if sub_dir:
            for _sub_dir in sub_dir:
                self.find_py_files(os.path.join(base, _sub_dir), py_files)
        # return self._find_py_files_in_current_dir(base, sub)

    def _find_py_files_in_current_dir(self, base, files):
        files = self.filter_py_file_names(files)
        py_files = self.complete_py_file_path(base, files)
        return py_files

    def filter_py_file_names(self, files: list):
        return list(filter(lambda x: x.endswith(".py"), files))

    def complete_py_file_path(self, base: str, files: list):
        return list(map(lambda x: os.path.join(base, x), files))

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


if __name__ == '__main__':
    t = FileFilter()
    t.get_all_py_files("./t1")
