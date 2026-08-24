#include <iostream>
#include <string>
#include <iomanip>
#include <numbers>

void problem19()
{

    const int minimumBatteryPercentage{30};
    const double maximumPayloadMassKg{5.0};
    const double minimumTemperatureDegreesCelsius{-10.0};
    const double maximumTemperatureDegreesCelsius{40.0};
    unsigned int missionNr{};
    std::string robotName{};
    double batteryPercentage{};
    double payLoadMass{};
    double missionTemperature{};
    bool missionReady{true};

    std::cout << "Insert mission number: ";
    std::cin >> missionNr;
    std::cout << "Insert robot name: ";
    std::cin >> robotName;
    std::cout << "Insert battery percentage: ";
    std::cin >> batteryPercentage;
    std::cout << "Insert battery payload mass: ";
    std::cin >> payLoadMass;
    std::cout << "Insert mission temperature: ";
    std::cin >> missionTemperature;

    const double remainingPayLoadCap{maximumPayloadMassKg - payLoadMass};

    if (batteryPercentage < minimumBatteryPercentage)
    {
        std::cout << "Warning, battery low!\n";
        missionReady = false;
    }
    if (missionTemperature < minimumTemperatureDegreesCelsius)
    {
        std::cout << "Warning, temperature is critically low!\n";
        missionReady = false;
    }
    else if (missionTemperature > maximumTemperatureDegreesCelsius)
    {
        std::cout << "Warning, temperature is critically high!\n";
        missionReady = false;
    }

    if (remainingPayLoadCap < 0)
    {
        std::cout << "Warning, payload is over capacity!\n";
        missionReady = false;
    }

    if (!missionReady)
    {
        std::cout << "Mission status: NOT READY\n";
    }
    else
    {
        std::cout << "Mission status: READY\n";
    }
    // Mission report:

    std::cout << std::fixed << std::setprecision(2);

    std::cout << std::left
              << std::setw(15) << "M.nr"
              << std::setw(15) << "Robot name"
              << std::setw(15) << "Battery"
              << std::setw(15) << "Payload [Kg]"
              << std::setw(15) << "Mission temp"
              << std::setw(15) << "Mission status\n";

    std::cout << std::left
              << std::setw(15) << missionNr
              << std::setw(15) << robotName
              << std::setw(15) << batteryPercentage
              << std::setw(15) << payLoadMass
              << std::setw(15) << missionTemperature
              << std::setw(15) << (missionReady ? "Ready" : "Not ready")
              << '\n';

    // Compact record:

    std::printf("Mission: %#X", missionNr);
    std::printf(" , payload=%.2f", payLoadMass);
    std::printf(" kg");
    std::printf(" , temperature=%.2f", missionTemperature);
    std::printf(" C\n");
}
