# # # # def decor(func):
# # # #     print('decor')
# # # #
# # # #     def inner():
# # # #         print('inner')
# # # #         func()
# # # #
# # # #     return inner
# # # #
# # # # @decor
# # # # def num():
# # # #     print('num')
# # # #
# # # #
# # # # num()
# # #
# # # def my_split(string,delimiter):
# # #     lst=[]
# # #     count =0
# # #     if type(string) is not str:
# # #         raise ValueError
# # #     if delimiter =="":
# # #         lst.append(string)
# # #
# # #     else:
# # #         i = 0
# # #
# # #         while(i<len(string)):
# # #
# # #             if string[i] == delimiter and count==0  :
# # #                 if i == len(string)-1:
# # #                     lst.append(" ")
# # #                 count += 1
# # #                 continue
# # #             else:
# # #                 count=0
# # #                 res = ''
# # #                 while i<len(string) and string[i]!=delimiter:
# # #                     res+=string[i]
# # #                     i+=1
# # #
# # #                 lst.append(res)
# # #
# # #             i+=1
# # #
# # #
# # #
# # #     return lst
# # #
# # # s = "anisha   dhameja"
# # # print(s.split(" "))
# # # print(my_split(s," "))
# #
# #
# # def merge_the_tools(string, k):
# #     i = 0
# #     l = int(len(string) / k)
# #     while (i < len(string)):
# #         r = ''
# #         for j in range(i, i + l):
# #             if string[j] not in r:
# #                 r += string[j]
# #
# #         print(r)
# #         i +=
# #         l
# # import requests
# #
# # state = 'maharashtra'.lower()
# # api_address = "https://api.covid19india.org/data.json"
# # json_data = requests.get(api_address).json()
# #
# # for n in range(0, 30):
# #     if state == json_data['statewise'][n]['state'].lower():
# #         Confirmed_Case = json_data['statewise'][n]['confirmed']
# #
# # print(f"Active Case in {state} is {Confirmed_Case}")
# import requests
#
#
# def get_confirmed_case_by_state(state):
#     state = state.lower()
#     api_address = "https://api.covid19india.org/data.json"
#     json_data = requests.get(api_address).json()
#
#     confirmed_case = None
#     for n in range(0, 30):
#         if state == json_data['statewise'][n]['state'].lower():
#             confirmed_case = json_data['statewise'][n]['confirmed']
#
#     return confirmed_case
#
#
# case = get_confirmed_case_by_state(input("Enter state name:"))
# print(f"Total case are {case}")
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result = [];
        dictionary = {};
        for i in paths:
            lst = i.split();
            for j in range(1, len(lst)):
                string = lst[j];
                filename = str()
                extension = str()
                content = str()
                k = 0
                while (string[k] != '.'):
                    filename + str[j];
                    k += 1
                while (string[k] != '('):
                    extension += str[k];
                    k += 1
                k += 1
                while (string[k] != ')'):
                    content += string[k]
                    k += 1
                k += 1
                if (dictionary[content] !=None):
                    lt = [];
                    lt.add(lst[0] + filename + extension);
                    dictionary[content] = lt;

                else:
                    l = dictionary[content];
                    l.add(lst[0] + filename + extension)
                    dictionary[content] = l



        for key in dictionary:
            if dictionary[key].len() >1:
                result.append(dictionary[key])
        return result