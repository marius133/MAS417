cmake_minimum_required(VERSION 3.10.0)
project(exercise1 VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(exercise1 main.cpp
problem4.cpp
problem5.cpp
problem6.cpp
problem7.cpp)

