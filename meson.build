project('cdirs', 'cpp',
  version : '0.1',
  default_options : ['warning_level=3', 'cpp_std=c++17'])

spdlog_proj = subproject('spdlog')
spdlog_dep = spdlog_proj.get_variable('spdlog_dep')

gtest_proj = subproject('gtest')
gtest_dep = gtest_proj.get_variable('gtest_dep')

sqlite_proj = subproject('sqlite3')
sqlite_dep = sqlite_proj.get_variable('sqlite3_dep')

tabulate_proj = subproject('tabulate')
tabulate_dep = tabulate_proj.get_variable('tabulate_dep')

executable('cdirs',
           'lib.cpp',
           'main.cpp',
           dependencies: [spdlog_dep, sqlite_dep, tabulate_dep],
           install : true)
