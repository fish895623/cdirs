#include "lib.hpp"

auto main() -> int
{
  auto const lib = library {};

  return lib.name == "cdirs" ? 0 : 1;
}
