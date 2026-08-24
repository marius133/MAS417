#include <iostream>

void problem15()
{

    unsigned int number{};
    int fac{1};

    std::cout << " Input a number: ";
    std::cin >> number;

    for (unsigned int i{1}; i <= number; ++i)
    {
        fac *= i;
    }
    std::cout << fac << '\n';
}