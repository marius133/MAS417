#include <iostream>
#include <random>
#include <fstream>

std::ofstream file("../Sensor_data.csv");
std::random_device rd;
std::mt19937 generator(rd());

void sensorValueGenerator()
{
    std::uniform_real_distribution<double> temperatureDistribution(20.0, 30.0);
    std::uniform_real_distribution<double> pressureDistribution(95000.0, 105000.0);

    file << "timestamp,temperature,pressure\n";

    for (int i = 0; i < 5; ++i)
    {
        double temperature = temperatureDistribution(generator);
        double pressure = pressureDistribution(generator);

        file << i << ',' << temperature << ',' << pressure << '\n';
    }
}

void writeToCsv()
{
}