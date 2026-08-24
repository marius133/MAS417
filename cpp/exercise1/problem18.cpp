
#include <iostream>
#include <cstdio>
#include <numbers>
#include <iomanip>


void problem18()
{

    const double temperatureDegreesCelsius{23.456};
    const unsigned int deviceId{42};
    
    //with std::cout

    std::cout << "Temperature: " << std::fixed << std::setprecision(2) << std::setw(10) << temperatureDegreesCelsius << " C";
    std::cout << "\nDevice ID: " << std::showbase << std::hex << std::uppercase << std::setw(10) << deviceId << '\n';

    // with std::printf

    std::printf("Temperature: %10.2f C\n",temperatureDegreesCelsius);
    std::printf("Device ID: %#10X\n",deviceId);



}