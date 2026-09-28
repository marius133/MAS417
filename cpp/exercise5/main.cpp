#include <iostream>
#include <vector>
#include <algorithm>


double mean(std::vector<double> &values);
double median(std::vector<double> &values);
void sensorValueGenerator();

int main()
{

    // std::vector<double> values{0, 1, 2, 3, 4};

    // std::vector<double> vectorFifty(50,0.0);


    // double result = mean(values);
    // double result2 = median(values);
    // double result3 = mean(vectorFifty);

    // std::cout << "Median is: " << result2 << std::endl;
    // std::cout << "Mean is: " << result << std::endl;
    // std::cout << "Mean is: " << result3 << std::endl;



    sensorValueGenerator();


}
