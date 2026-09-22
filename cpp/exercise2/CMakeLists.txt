cmake_minimum_required(VERSION 3.10)

project(exercise2 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(exercise2 main.cpp
 problem1.cpp
 problem2.cpp)