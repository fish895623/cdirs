cmake_minimum_required(VERSION 3.14)

include(cmake/prelude.cmake)

project(
    cdirs
    VERSION 0.1.0
    DESCRIPTION "Short description"
    HOMEPAGE_URL "https://example.com/"
    LANGUAGES CXX
)

include(cmake/project-is-top-level.cmake)
include(cmake/variables.cmake)

find_package(spdlog REQUIRED)
# ---- Declare library ----

add_library(
    cdirs_lib OBJECT
    source/lib.cpp
)

target_include_directories(
    cdirs_lib ${warning_guard}
    PUBLIC
    "$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/source>"
)

target_compile_features(cdirs_lib PUBLIC cxx_std_17)

target_link_libraries(cdirs_lib PUBLIC spdlog::spdlog)

# ---- Declare executable ----

add_executable(cdirs_exe source/main.cpp)
add_executable(cdirs::exe ALIAS cdirs_exe)

set_property(TARGET cdirs_exe PROPERTY OUTPUT_NAME cdirs)

target_compile_features(cdirs_exe PRIVATE cxx_std_17)

target_link_libraries(cdirs_exe PRIVATE cdirs_lib spdlog::spdlog)

# ---- Install rules ----

if(NOT CMAKE_SKIP_INSTALL_RULES)
  include(cmake/install-rules.cmake)
endif()

# ---- Developer mode ----

if(NOT cdirs_DEVELOPER_MODE)
  return()
elseif(NOT PROJECT_IS_TOP_LEVEL)
  message(
      AUTHOR_WARNING
      "Developer mode is intended for developers of cdirs"
  )
endif()

include(cmake/dev-mode.cmake)
