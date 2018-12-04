{
	'repo_type' : 'mercurial',
	'url' : 'https://bitbucket.org/multicoreware/x265',
	'rename_folder' : 'libx265_hg_10bit',
	'source_subfolder' : 'source',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_AR={cross_prefix_full}ar -DENABLE_ASSEMBLY=ON -DHIGH_BIT_DEPTH=ON -DEXPORT_C_API=OFF -DENABLE_SHARED=OFF -DENABLE_CLI=OFF -DCMAKE_INSTALL_PREFIX={offtree_prefix}/libx265_10bit -DLIBXML_STATIC=ON -DGLIB_STATIC_COMPILATION=ON',
	'run_post_install' : [
		'mv -fv "{offtree_prefix}/libx265_10bit/lib/libx265.a" "{offtree_prefix}/libx265_10bit/lib/libx265_main10.a"'
	],
	'conf_system' : 'cmake',
	'_info' : { 'version' : 'mercurial (default)', 'fancy_name' : 'x265 (library (10))' },
}