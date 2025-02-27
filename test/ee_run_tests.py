import sys
sys.path.append(r"C:\fMRIData\git-repo\load-heka-python")

from test_load_heka import test_heka_reader
from os.path import join

ASSERT_MODE = True
TEST_PATH = r"C:\fMRIData\git-repo\load-heka-python\ee_test_files\stim_extraction"

def test_f1_v2x90_2(base_path):

    version = "f1_v2x90.2"
    group_num_series_num_to_test = [["1", "1"], ["1", "18"], ["5", "6"],
                                    ["7", "3"], ["8", "16"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)

def test_f2_v2x90_2(base_path):

    version = "f2_v2x90.2"
    group_num_series_num_to_test = [["1", "4"], ["1", "1"], ["1", "2"], ["1", "3"], ["1", "4"], ["1", "5"],
                                     ["1", "6"], ["1", "7"], ["1", "8"], ["1", "9"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)

def test_f3_v2x90_2(base_path):

    version = "f3_v2x90.2"
    group_num_series_num_to_test = [["1", "1"], ["1", "2"],  ["1", "3"], ["1", "4"], ["1", "5"],
                                    ["1", "6"], ["1", "7"], ["1", "8"], ["1", "9"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)


def test_f4_v2x90_5(base_path):

    version = "f4_v2x90.5"
    group_num_series_num_to_test = [["1", "1"], ["1", "2"], ["1", "3"], ["1", "4"], ["1", "5"], ["1", "14"], ["1", "16"],
                                     ["1", "17"], ["1", "18"], ["1", "19"], ["1", "20"], ["1", "22"], ["1", "23"], ["1", "24"],
                                     ["1", "25"], ["1", "26"], ["1", "27"], ["1", "28"], ["1", "29"], ["1", "30"], ["1", "31"],
                                     ["1", "32"], ["1", "33"], ["1", "34"], ["1", "35"], ["1", "36"],

                                     ["2", "1"], ["2", "2"], ["2", "3"], ["2", "4"], ["2", "5"], ["2", "6"], ["2", "7"], ["2", "9"], ["2", "12"], ["2", "14"],
                                     ["2", "15"], ["2", "16"], ["2", "18"], ["2", "21"], ["2", "24"], ["2", "25"], ["2", "26"], ["2", "27"], ["2", "28"], ["2", "29"],
                                     ["2", "30"], ["2", "31"], ["2", "32"], ["2", "33"], ["2", "34"], ["2", "35"], ["2", "36"], ["2", "37"], ["2", "38"], ["2", "39"],
                                     ["2", "40"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)


def test_f5_v2x90_5(base_path):
    version = "f5_v2x90.5"
    group_num_series_num_to_test = [["1", "1"], ["1", "4"], ["1", "5"], ["1", "6"],  # ["3", "3"], series has records with three channels
                                     ["1", "7"], ["3", "9"], ["5", "6"], ["5", "8"],
                                     ["5", "10"],  ["6", "2"], ["6", "14"], ["6", "20"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)


def f6_1_2_0_build_1469(base_path):
    version = "f6_1.2.0_[Build 1469]"
    group_num_series_num_to_test = [["1", "1"], ["1", "2"], ["1", "3"], ["1", "4"],  # ["1", "6"] series has records with three channels
                                     ["1", "5"], ["1", "7"], ["1", "8"],
                                     ["1", "9"], ["1", "10"], ["1", "11"], ["1", "12"], ["1", "13"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)

def f7_1_2_0_build_1469(base_path):

    version = "f7_1.2.0_[Build 1469]"
    group_num_series_num_to_test = [["1", "1"], ["1", "2"], ["1", "3"], ["1", "4"], ["1", "5"],  # ["1", "8"], series has records with three channels
                                     ["1", "6"], ["1", "7"], ["1", "9"], ["1", "10"],
                                     ["1", "11"], ["1", "12"], ["1", "13"], ["1", "14"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)

def test_f8_v2x65(base_path):
    version = "f8_v2x65"
    group_num_series_num_to_test = [["1", "6"], ["1", "13"], ["3", "1"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE, include_stim_protocol=False)

def test_f9_v2x65(base_path):
    version = "f9_v2x65"
    group_num_series_num_to_test = [["1", "1"], ["1", "2"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE, include_stim_protocol=False)

def test_f10_v2x91(base_path):
    version = "f10_v2x91"
    group_num_series_num_to_test = [["1", "1"], ["1", "3"], ["1", "5"], ["1", "9"]]
    test_heka_reader(base_path, version, group_num_series_num_to_test, assert_mode=ASSERT_MODE)


test_f1_v2x90_2(TEST_PATH)
test_f2_v2x90_2(TEST_PATH)
test_f3_v2x90_2(TEST_PATH)
test_f4_v2x90_5(TEST_PATH)
test_f5_v2x90_5(TEST_PATH)
f6_1_2_0_build_1469(TEST_PATH)
f7_1_2_0_build_1469(TEST_PATH)
test_f8_v2x65(TEST_PATH)
test_f9_v2x65(TEST_PATH)
test_f10_v2x91(TEST_PATH)
