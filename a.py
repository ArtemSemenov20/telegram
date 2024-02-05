# words_count = dict()
# a = "Hello, my name is Artem. He is 17 years old. She have a beautiful name."
# list_of_text = a.replace(",", "").replace(".", "").split()
#
# for i in list_of_text:
#     words_count[i] = list_of_text.count(i)
#
# result = dict()
# text = None
# count = 0
#
# for i in range(10):
#     for key, value in words_count.items():
#         if count < value and key not in result:
#             text = key
#             count = value
#     result[text] = count
#     count = 0
#
# print(result)



class NumberStatistics:
    def __init__(self):
        self.number_list = []

    def get_user_input(self):
        user_input = input("Enter a list of numbers separated by a space: ")
        self.number_list = [int(num) for num in user_input.split()]

    def generate_statistics(self):
        statistics_dict = {}
        for num in self.number_list:
            if num in statistics_dict:
                statistics_dict[num] += 1
            else:
                statistics_dict[num] = 1
        return statistics_dict

    def print_statistics(self, statistics_dict):
        print("Statistics of entered numbers:")
        for key, value in statistics_dict.items():
            print(f"{key}: {value} times")

number_stats = NumberStatistics()

number_stats.get_user_input()

statistics_result = number_stats.generate_statistics()
number_stats.print_statistics(statistics_result)



