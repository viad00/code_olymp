cmake_minimum_required(VERSION 2.6)
project(session)

add_executable(session main.cpp)

install(TARGETS session RUNTIME DESTINATION bin)
