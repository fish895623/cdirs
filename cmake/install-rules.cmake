install(
    TARGETS cdirs_exe
    RUNTIME COMPONENT cdirs_Runtime
)

if(PROJECT_IS_TOP_LEVEL)
  include(CPack)
endif()
