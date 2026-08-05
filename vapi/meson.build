dee_gir = get_variable('dee_gir')

if get_option('introspection').allowed()
  dee_vapi = gnome.generate_vapi(
    'dee-1.0',
    sources: [dee_gir[0]],
    packages: ['gio-2.0'],
    metadata_dirs: meson.current_source_dir(),
    install: true,
    install_dir: join_paths(get_option('datadir'), 'vala', 'vapi')
  )
endif
