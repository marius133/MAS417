#include <iostream>

void problem17()
{

    double a{};
    double b{};
    char op{};
    double result{};

    std::cout << "Input a number: ";
    std::cin >> a;
    std::cout << "Input another number: ";
    std::cin >> b;
    std::cout << "Input an operator: ";
    std::cin >> op;

    if (op == '+')
    {
        result = a + b;
    }
    else if (op == '-')
    {
        result = a - b;
    }
    else if (op == '*')
    {
        result = a * b;
    }

    else if (op == '/')
    {
        if (b == 0)
        {
            std::cout << "Error, cannot divide by zero! \n";
            return;
        }
        result = a / b;
    }
    else
    {
        std::cout << "Unknown operator: " << op << '\n';
        return;
    }

    std::cout << '\n'
              << a << op << b << '=' << result << '\n';
}