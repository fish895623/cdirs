#include <filesystem>
#include <iostream>

auto main() -> int
{
  // get file on the same directory
  const std::filesystem::path path = std::filesystem::current_path();
  std::cout << "Current path: " << path << "\n";

  for (const auto& entry : std::filesystem::directory_iterator(path)) {
    std::cout << entry.path() << "\n";
  }

  return 0;
}
