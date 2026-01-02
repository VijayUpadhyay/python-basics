#As we can see innerFunction() can easily be accessed inside the outerFunction body 
#but not outside of it’s body. Hence, here, innerFunction() is treated as nested 
#Function which uses text as non-local variable.
import string


def outer_function(text) -> str:
    def inner_function(name):
        print(name)
        return name + ''.join(str(i) for i in range(1, 10))

    final_name = inner_function(text)
    print("Final:", final_name)
    return text


if __name__ == '__main__':
    outer_function('Ram!')
    outer_function('Sita!')
