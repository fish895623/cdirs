#include <cstdint>
#include <vector>
#include <filesystem>
#include <iostream>

struct file {
  std::string name;
  std::string path;
  std::string extension;
  uint64_t size;
};

auto main() -> int
{
  // get file on the same directory
  const std::filesystem::path path = std::filesystem::current_path();
  std::cout << "Current path: " << path << "\n";

  std::vector<file> files;

  for (const auto& entry : std::filesystem::directory_iterator(path)) {
    // file last access time
    const auto last_access_time = std::filesystem::last_write_time(entry);
    last_access_time.time_since_epoch().count();

    // convert entry.path() to string exclude parent path
    const auto path_string = entry.path().filename().string();

    const bool is_directory = std::filesystem::is_directory(entry);

    files.push_back({
      path_string,
      entry.path().string(),
      entry.path().extension().string(),
      is_directory ? 0 : std::filesystem::file_size(entry)
    });
  }

  for (const auto& file : files) {
    std::cout << "\033[31m" << file.name << "\033[0m" << file.size << file.extension << "\n";
  }

  return 0;
}
