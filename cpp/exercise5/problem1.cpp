
#include <iostream>
#include <vector>
#include <algorithm>

double mean(std::vector<double> &values)
{

    double sum{};
    double meanValue{};

    for (auto it = values.begin(); it != values.end(); ++it)
    {
        sum += *it;
    }

    meanValue = sum / values.size();

    return meanValue;
}

double median(std::vector<double> &values)
{
    double median{};
    std::vector<double> sortedValues = values;
    std::sort(sortedValues.begin(), sortedValues.end());

    auto middle = sortedValues.begin() + sortedValues.size() / 2;

    if (values.size() % 2 == 0)
    {
        median = *(middle - 1);
    }
    else
    {
        median = *middle;
    }

    return median;
}

