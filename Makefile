TARGET=asdf
CXX=g++
CXXFLAGS=-Wall -Wextra -Werror -std=c++11

all: $(TARGET)

$(TARGET): main.o lib.o
	$(CXX) $(CXXFLAGS) $^ -o $@

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

lib.o: lib.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(TARGET) *.o