# Проверить валидность расстановки скобочек в выражении.
#
# Скобки могут быть всех трех видов - ()[]{}.
#
# На вход программа или функция должна принимать строку, а на выходе ответить правильно ли расставлены скобочки в ней.
#
# Те есть открывающиеся скобочки корректно закрываются скобочкой того же вида.
#
# Например:
#
# "([])" - true
# "{[(]}"- false


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    my_brackets_stack = []
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    for i in brackets_row:
        if i in brackets_open:
            my_brackets_stack.append(i)
        if i in brackets_closed:
            if len(my_brackets_stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if my_brackets_stack[-1] == open_bracket:
                my_brackets_stack = my_brackets_stack[:-1]
            else:
                return False
    return (not my_brackets_stack)
