#include <iostream>
bool askUserForYesNoInput()
{
    char answer{};

    while (true)
    {
        std::cout << "\n(Yes/no)?\n";
        std::cin >> answer;

        if (answer == 'y' || answer == 'Y')
        {
            return true;
        }
        if (answer == 'n' || answer == 'N')
        {
            return false;
        }
        std::cout << "\nWrong answer, try again: ";
    }
}

void problem1()
{
    bool answer = askUserForYesNoInput();
    std::cout << answer << '\n';
}
