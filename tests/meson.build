dee_lib = get_variable('dee_lib')
dee_dep = get_variable('dee_dep')

test_inc = include_directories('.', '..')

test_c_args = [
  '-I' + meson.current_source_dir(),
  '-I' + join_paths(meson.source_root(), 'src'),
  '-DTESTDIR="' + meson.current_build_dir() + '"',
  '-DDEE_COMPILATION',
]

test_deps = [dee_dep]
test_link_with = [dee_lib]

if get_option('extended-tests')
  gtx_dep = dependency('gtx', version: '>=0.2.2')
  test_deps += gtx_dep
endif

test_dee_sources = [
  'test-analyzer.c',
  'test-dee.c',
  'test-filter-model.c',
  'test-glist-result-set.c',
  'test-index.c',
  'test-model-column.c',
  'test-model-complex-column.c',
  'test-model-readers.c',
  'test-model-rows.c',
  'test-model-signals.c',
  'test-model-seqnums.c',
  'test-model-tags.c',
  'test-resource-manager.c',
  'test-serializable.c',
  'test-transaction.c',
  'test-term-list.c',
  join_paths(meson.source_root(), 'src', 'dee-glist-result-set.h'),
]

# Conditional source additions
if get_option('icu')
  test_dee_sources += 'test-icu.c'
endif

if get_option('extended-tests')
  test_dee_sources += [
    'test-model-interactions.c',
    'test-peer-interactions.c',
    'test-client-server.c',
  ]
endif

test_dee = executable(
  'test-dee',
  test_dee_sources,
  include_directories: test_inc,
  c_args: test_c_args,
  dependencies: test_deps,
  link_with: test_link_with,
)

model_helpers = {}
if get_option('extended-tests')
  model_helper_names = [
    'add3rows',
    'append1',
    'change3rows',
    'clear3rows',
    'clear6rows',
    'clone3rows',
    'clone3rows-meta',
    'clear3add5',
    'insert1row',
    'introspect',
    'remove3rows',
    'replace',
    'resync3rows',
    'schemaless',
  ]

  foreach helper_name : model_helper_names
    exe_name = 'model-helper-' + helper_name
    executable(
      'model-helper-' + helper_name,
      'model-helper-' + helper_name + '.c',
      include_directories: test_inc_dirs,
      c_args: test_c_args,
      dependencies: test_deps_main,
      link_with: dee_lib,
      build_by_default: false,
    )
  endforeach

  peer_helper_1peer = executable(
    'peer-helper-1peer',
    'peer-helper-1peer.c',
    include_directories: test_inc,
    c_args: test_c_args,
    dependencies: test_deps,
    link_with: test_link_with,
    build_by_default: false,
  )

  server_helper_client = executable(
    'server-helper-client',
    'server-helper-client.c',
    include_directories: test_inc,
    c_args: test_c_args,
    dependencies: test_deps,
    link_with: test_link_with,
    build_by_default: false,
  )
endif

test_benchmark = executable(
  'test-benchmark',
  'test-benchmark.c',
  include_directories: test_inc,
  c_args: test_c_args,
  dependencies: test_deps + [declare_dependency(link_args: ['-lm'])],
  link_with: test_link_with,
)

test(
  'dee-tests',
  find_program('dbus-test-runner'),
  args: [
    '-m', '60',
    '--task', 'gtester',
    '--parameter', '--verbose',
    '--parameter', '-o=@0@/test-dee-results.xml'.format(meson.current_build_dir()),
    '--parameter', '-k',
    '--parameter', test_dee.full_path(),
  ],
  depends: test_dee,
  suite: 'dee',
  timeout: 300,
)

run_target(
  'benchmark-test',
  command: test_benchmark,
  depends: test_benchmark,
)

run_target(
  'check-report',
  command: [
    'bash', '-c',
    'dbus-test-runner -m 60 --task gtester ' +
    '--parameter -o=@0@/test-dee-results.xml '.format(meson.current_build_dir()) +
    '--parameter -k ' +
    '--parameter @0@ '.format(test_dee.full_path()) +
    '&& gtester-report @0@/test-dee-results.xml | '.format(meson.current_build_dir()) +
    'sed \'s/GTester Unit Test Report</>GTester Unit Test Report (normal)</\' ' +
    '> @0@/test-dee-results.html '.format(meson.current_build_dir()) +
    '&& gnome-open @0@/test-dee-results.html'.format(meson.current_build_dir()),
  ],
  depends: test_dee,
)

run_target(
  'full-report',
  command: [
    'bash', '-c',
    'dbus-test-runner -m 60 --task gtester ' +
    '--parameter -o=@0@/test-dee-results.xml '.format(meson.current_build_dir()) +
    '--parameter -k ' +
    '--parameter -m=slow ' +
    '--parameter @0@ '.format(test_dee.full_path()) +
    '&& gtester-report @0@/test-dee-results.xml | '.format(meson.current_build_dir()) +
    'sed \'s/>GTester Unit Test Report</>GTester Unit Test Report (normal)</\' ' +
    '> @0@/test-dee-results.html '.format(meson.current_build_dir()) +
    '&& xdg-open @0@/test-dee-results.html'.format(meson.current_build_dir()),
  ],
  depends: test_dee,
)
