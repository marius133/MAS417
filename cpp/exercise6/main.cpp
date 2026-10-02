#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <sstream>
#include <ctime>

int main()
{
    std::ifstream logFile("log.txt");

    if (!logFile)
    {
        std::cerr << "Could not open file \n";
        return 1;
    }

    int numberOfLines{};
    std::tm firstDate{}; // structure to hold date and time form <ctime> (empty container that will hold date and time later on)
    std::string line;
    while (std::getline(logFile, line))
    {
        std::cout << line << '\n';

        if (numberOfLines == 0)
        {
            std::istringstream lineStream{line};

            std::string scriptName;
            lineStream >> scriptName;                            // Reading script name (first word)
            lineStream >> std::get_time(&firstDate, "%Y-%m-%d"); // reading date from file (second "Word")
        }
        ++numberOfLines;
    }
    std::cout << "First log entry date "
              << std::put_time(&firstDate, "%Y-%m-%d")
              << ". Number of log entries: "
              << numberOfLines
              << ".\n";

    return 0;
}
