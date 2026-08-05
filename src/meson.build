devel_headers = files(
  'dee.h',
  'dee-analyzer.h',
  'dee-file-resource-manager.h',
  'dee-filter-model.h',
  'dee-filter.h',
  'dee-hash-index.h',
  'dee-index.h',
  'dee-model.h',
  'dee-model-reader.h',
  'dee-peer.h',
  'dee-server.h',
  'dee-client.h',
  'dee-proxy-model.h',
  'dee-resource-manager.h',
  'dee-result-set.h',
  'dee-sequence-model.h',
  'dee-serializable.h',
  'dee-serializable-model.h',
  'dee-shared-model.h',
  'dee-term-list.h',
  'dee-text-analyzer.h',
  'dee-transaction.h',
  'dee-tree-index.h',
)

install_headers(
  devel_headers,
  subdir: 'dee-1.0'
)

libdee_sources = files(
  'dee-analyzer.c',
  'dee-file-resource-manager.c',
  'dee-filter-model.c',
  'dee-filter.c',
  'dee-glist-result-set.c',
  'dee-hash-index.c',
  'dee-index.c',
  'dee-model.c',
  'dee-model-reader.c',
  'dee-peer.c',
  'dee-server.c',
  'dee-client.c',
  'dee-proxy-model.c',
  'dee-resource-manager.c',
  'dee-result-set.c',
  'dee-sequence-model.c',
  'dee-serializable.c',
  'dee-serializable-model.c',
  'dee-shared-model.c',
  'dee-term-list.c',
  'dee-text-analyzer.c',
  'dee-transaction.c',
  'dee-tree-index.c',
)

dee_deps = [
  glib_dep,
  gthread_dep,
  gio_dep,
  gio_unix_dep,
]

libdee_c_args = [
  '-DG_LOG_DOMAIN="dee"',
  '-DPREFIX="@0@"'.format(get_option('prefix')),
  '-DLIBDIR="@0@"'.format(get_option('libdir')),
  '-DG_DISABLE_DEPRECATED',
  '-DDEE_COMPILATION',
]

xml_header_generator = find_program('generate-xml-header.py', native: true)

model_xml_header = custom_target(
  'com.canonical.Dee.Model.xml header',
  input: 'dbus/com.canonical.Dee.Model.xml',
  output: 'com.canonical.Dee.Model-xml.h',
  command: [
    xml_header_generator,
    '@INPUT@',
    '@OUTPUT@',
  ],
)

peer_xml_header = custom_target(
  'com.canonical.Dee.Peer.xml header',
  input: 'dbus/com.canonical.Dee.Peer.xml',
  output: 'com.canonical.Dee.Peer-xml.h',
  command: [
    xml_header_generator,
    '@INPUT@',
    '@OUTPUT@',
  ],
)

libdee_sources += [
  model_xml_header,
  peer_xml_header,
]

if get_option('icu')
  devel_headers += files('dee-icu.h')
  libdee_sources += files('dee-icu-term-filter.c')
  dee_deps += icu_dep
endif

if get_option('trace-log')
  libdee_sources += files('trace-log.c')
  libdee_c_args += '-DENABLE_TRACE_LOG'
endif

dee_marshal = gnome.genmarshal(
  'dee-marshal',
  sources: 'dee-marshal.list',
  prefix: '_dee_marshal',
)

libdee_sources += dee_marshal

libdee = library(
  'dee-1.0',
  libdee_sources,
  dependencies: dee_deps,
  c_args: libdee_c_args,
  include_directories: include_directories('.', '..'),
  install: true,
  version: '4.2.1',
  soversion: '4',
)

libdee_dep = declare_dependency(
  link_with: libdee,
  include_directories: include_directories('.', '..'),
  dependencies: dee_deps,
)

if get_option('introspection').allowed()
  dee_gir = gnome.generate_gir(
    libdee,
    sources: libdee_sources,
    namespace: 'Dee',
    nsversion: 'gir_version',
    header: 'dee.h',
    export_packages: 'dee-1.0',
    includes: [
      'GObject-2.0',
      'GLib-2.0',
      'Gio-2.0',
    ],
    install: true,
  )
endif

dee_lib = libdee
set_variable('libdee', libdee)
set_variable('dee_dep', dee_deps)
set_variable('dee_gir', dee_gir)
