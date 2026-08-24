
#include <iostream>

void problem16a()
{

    const double pi{3.14159};
    double radius{};

    std::cout << "What is the radius? ";
    std::cin >> radius;

   const double circumference = 2 * pi * radius;
    std::cout << "The circumference of the circle is: " << circumference << '\n';
}