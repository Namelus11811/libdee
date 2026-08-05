dee_lib = get_variable('dee_lib')

dee_tool = executable(
  'dee-tool',
  sources: 'dee-tool.c',
  include_directories: include_directories('.', '../src'),
  dependencies: [dee_dep],
  link_with: dee_lib,
  install: true,
)
