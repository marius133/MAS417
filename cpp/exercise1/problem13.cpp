#include <iostream>


void problem13()
{
    int number{};
    std::cout << " Input a number: ";
    std::cin >> number;



    for(int i{1}; i <= 10; ++i)
    {
        std::cout << i << " x " << number << " = " << number * i << '\n';
        
    }
}