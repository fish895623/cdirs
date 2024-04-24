# Parent project does not export its library target, so this CML implicitly
# depends on being added from it, i.e. the testing is done only from the build
# tree and is not feasible from an install location

project(cdirsTests LANGUAGES CXX)

# ---- Tests ----

add_executable(cdirs_test source/cdirs_test.cpp)
target_link_libraries(cdirs_test PRIVATE cdirs_lib)
target_compile_features(cdirs_test PRIVATE cxx_std_17)

add_test(NAME cdirs_test COMMAND cdirs_test)

# ---- End-of-file commands ----

add_folders(Test)
