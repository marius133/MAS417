
#include <string>
#include <iostream>


std::string questionAsker()
{
std::string answer;

std::cout << "What is your name? \n"; 
std::cin >> answer;

return answer;
}



void problem5()
{

std::string name = questionAsker();

std::cout << "Hello "<< name << '\n';
}