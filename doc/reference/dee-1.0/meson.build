gnome.gtkdoc(
  'dee-1.0',
  main_sgml: 'dee-1.0-docs.sgml',
  src_dir: join_paths(meson.source_root(), 'src'),
  dependencies: [dee_dep],
  install: true,
  check: false,  # Equivalent to commenting out TESTS
  mkdb_args: [
    '--sgml-mode',
    '--output-format=xml',
    '--ignore-files=trio',
  ],
  ignore_headers: ['trace-log.h'],
  content_files: [],
  expand_content_files: [],
)
