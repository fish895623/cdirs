#!/usr/bin/env python
import os


class Compile:
    def __init__(
        self,
        target,
        cc,
        cxx,
        cflags,
        cxxflags,
    ) -> None:
        self.TARGET = "asdf"
        self.CC = "clang"
        self.CXX = "clang++"
        self.CXXFLAGS = "-std=c++17"
        self.LIBRARY = []
        self.INCLUDES = "-Iextern/spdlog/include"

        # if dextern directory not exists, create it
        if not os.path.exists("extern"):
            os.makedirs("extern")

    def add_external_library(
        self,
        git_library,
        branch: str = "",
        depth: int = 1,
        compile_command: list = [],
    ):
        # get github repository name
        git_library_name = git_library.split("/")[-1].split(".git")[0]
        # skip if library already exists
        if os.path.exists(f"extern/{git_library_name}"):
            # compile library
            for command in compile_command:
                os.system(f"cd extern/{git_library_name} && {command}")
            return
        command = "git clone "
        if branch != "":
            command += branch
        if depth != None:
            command += f"--depth {depth}"

        os.system(f"git clone {git_library} extern/{git_library_name}")
        self.LIBRARY.append(f"-Iextern/{git_library}/include")

    def compile(self):
        command = f"{self.CXX} {self.CXXFLAGS} {self.INCLUDES} {' '.join(self.LIBRARY)} -o {self.TARGET} main.cpp"
        os.system(command)


def main():
    a = Compile("asdf", "clang", "clang++", "", "")
    a.add_external_library(
        git_library="https://github.com/gabime/spdlog.git",
        compile_command=["cmake -B build -S .", "cmake --build build"],
    )
    a.compile()


if __name__ == "__main__":
    main()
