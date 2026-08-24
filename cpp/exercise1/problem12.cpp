#include <iostream>

void problem12()
{
    int number{};
    int sum{};

    std::cout << " Input a number: ";
    std::cin >> number;

    for (int i{1}; i <= number; ++i)
    {
        sum += i;
    }
    std::cout << " The sum is: " << sum << '\n';
}