#include <iostream>

void problem8()
{

    int number{};
    std::string evenOrOdd{};

    std::cout << "Enter an integer to check whether its is odd or even: ";

    std::cin >> number;

    if (number % 2 == 0)
    {
        evenOrOdd = "even";
    }
    else
    {
        evenOrOdd = "odd";
    }

    std::cout << "\n The number " << number << " is " << evenOrOdd << '\n';
}