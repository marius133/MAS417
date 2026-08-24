#include <iostream>

void problem7()
{
    double temperatureDegreesToCelsius{};

    std::cout << "input degrees in Celsius: ";
    std::cin >> temperatureDegreesToCelsius;

    const double temperatureConvertedFahrenheit{(temperatureDegreesToCelsius * 9.0 / 5.0) + 32.0};

    std::cout << temperatureDegreesToCelsius << " C is " << temperatureConvertedFahrenheit << " Fahrenheit \n";
}