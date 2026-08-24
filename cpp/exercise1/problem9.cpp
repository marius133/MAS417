#include <iostream>

void problem9()
{
    int batteryPercentage{};
    std::cout << "Insert battery percentage: ";
    std::cin >> batteryPercentage;

    if (batteryPercentage > 100 || batteryPercentage < 0)
    {

        std::cout << "Invalid \n";
    }
    else if (batteryPercentage <= 9)
    {
        std::cout << "Critical \n";
    }
    else if (batteryPercentage <= 29)
    {
        std::cout << "Charge \n";
    }
    else
    {
        std::cout << "Ready \n";
    }
}