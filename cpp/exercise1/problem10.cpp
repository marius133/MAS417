#include <iostream>

void problem10()
{
    int a{2};
    int b{5};
    int c{100};

    if (a >= b && a >= c)
    {
        std::cout << a << " is the largest number \n";
    }
    else if (b >= c)
    {
        std::cout << b << " is the largest number \n";
    }
    else
    {
        std::cout << c << " is the largest number \n";
    }
}