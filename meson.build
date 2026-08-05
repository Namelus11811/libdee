project(
'dee',
'c',
version: '1.2.7',
meson_version: '>=0.55',
default_options: [
  'warning_level=2',
  'buildtype=debugoptimized',
  'default_library=shared'
]
)

gir_version = '1.0'

conf = configuration_data()

pkgconf = configuration_data()

conf.set(
  'PACKAGE_VERSION',
  meson.project_version()
)

if get_option('maintainer-flags')
  add_project_arguments(
    '-Werror',
    '-Wall',
    '-Wcast-align',
    '-Wno-uninitialized',
    '-Wempty-body',
    '-Wformat-security',
    '-Winit-self',
    '-Wno-error=deprecated-declarations',
    language: 'c'
  )
endif

cc = meson.get_compiler('c')

if cc.has_header('fcntl.h')
  conf.set10('HAVE_FCNTL_H', true)
endif

if cc.has_header('stdlib.h')
  conf.set10('HAVE_STDLIB_H', true)
endif

if cc.has_header('string.h')
  conf.set10('HAVE_STRING_H', true)
endif

if cc.has_header('unistd.h')
  conf.set10('HAVE_UNISTD_H', true)
endif

if cc.has_function('memset')
  conf.set10('HAS_MEMSET', true)
endif

if cc.has_function('munmap')
  conf.set10('HAS_MUNMAP', true)
endif

if cc.has_function('srcasecmp')
  conf.set10('HAS_STRCASECMP', true)
endif

if cc.has_function('strdup')
  conf.set10('HAS_STRDUP', true)
endif

if get_option('coverage')
  add_project_arguments(
    '--coverage',
    language: 'c'
  )

  add_project_link_arguments(
    '--coverage',
    language: 'c'
  )
endif

vapigen = find_program('vapigen', required: false)

have_vapigen = vapigen.found()

glib_dep = dependency('glib-2.0', version: '>=2.32')
gthread_dep = dependency('gthread-2.0', version: '>=2.32')
gio_dep = dependency('gio-2.0', version: '>= 2.32')
gio_unix_dep = dependency('gio-unix-2.0', version: '>= 2.32')

gnome = import('gnome')
dependency('gobject-introspection-1.0', version: '>=0.10.2')

python = import('python').find_installation()

override_dir = get_option('pygi_overrides_dir')
if override_dir == ''
  override_dir = join_paths(python.get_install_dir(), 'gi', 'overrides')
endif

set_variable('pygi_overrides_dir', override_dir)

conf.set_quoted(
  'PYGI_OVERRIDES_DIR',
  override_dir
)

if get_option('coverage')
  add_project_arguments(
    '--coverage',
    language: 'c'
  )

  add_project_link_arguments(
    '--coverage',
    language: 'c'
  )
endif

pkgconf = configuration_data()

pkgconf.set(
  'PACKAGE_NAME',
  meson.project_name()
)

pkgconf.set(
  'prefix',
  get_option('prefix')
)

pkgconf.set(
  'exec_prefix',
  '${prefix}'
)

pkgconf.set(
  'libdir',
  get_option('libdir')
)

pkgconf.set(
  'includedir',
  get_option('includedir')
)

pkgconf.set(
  'VERSION',
  meson.project_version()
)

configure_file(
  input: 'dee-1.0.pc.in',
  output: 'dee-1.0.pc',
  configuration: pkgconf,
  install: true,
  install_dir: join_paths(get_option('libdir'), 'pkgconfig')
)

if get_option('icu')
  icu_dep = dependency('icu-i18n', version: '>=4.6', required: true)

  configure_file(
    input: 'dee-icu-1.0.pc.in',
    output: 'dee-icu-1.0.pc',
    configuration: pkgconf,
    install: true,
    install_dir: get_option('libdir') / 'pkgconfig'
  )

  conf.set10(
    'HAVE_ICU',
    true
  )
endif

if get_option('tests')
  if get_option('extended-tests')
    gtx_dep = dependency('gtx', version: '>=0.2.2')
    conf.set10('HAVE_GTX', true)
  endif
endif

configure_file(
  output: 'config.h',
  configuration: conf,
)

subdir('src')
subdir('tools')
subdir('bindings')

if get_option('tests')
  subdir('tests')
endif

if get_option('docs')
  subdir('doc')
endif

if get_option('trace-log')
  conf.set10('ENABLE_TRACE_LOG', true)
endif

if have_vapigen
  subdir('vapi')
endif



message('''
dee ${meson.project_version()}
----------------

Prefix         : ${get_option('prefix')}

ICU support    : ${get_option('icu')}

Documentation  : ${get_option('gtk_doc')}
Introspection  : ${get_option('introspection')}
PyGi Overrides : ${override_dir}

Tests          : ${get_option('tests')}
Extended Tests : ${get_option('extended-tests')}
Coverage       : ${get_option('coverage')}
Verbose logging: ${get_option('trace-log')}
''')
