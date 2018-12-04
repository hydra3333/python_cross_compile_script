{
	'ffmpeg_base_config' : # the base for all ffmpeg configurations.
		'--arch={bit_name2} '
		'--target-os=mingw32 '
		'--cross-prefix={cross_prefix_bare} '
		'--pkg-config=pkg-config '
		'--disable-w32threads '
		'--enable-cross-compile '
		'--enable-pic '
		'--enable-libsoxr '
		'--enable-libass '
		'--enable-iconv '
		'--enable-libtwolame '
		'--enable-libzvbi '
		'--enable-libcaca '
		'--enable-libmodplug '
		'--enable-cuvid '
		'--enable-libmp3lame '
		'--enable-version3 '
		'--enable-zlib '
		'--enable-librtmp '
		'--enable-libvorbis '
		'--enable-libtheora '
		'--enable-libspeex '
		'--enable-libgsm '
		'--enable-libopus '
		'--enable-bzlib '
		'--enable-libopencore-amrnb '
		'--enable-libopencore-amrwb '
		'--enable-libvo-amrwbenc '
		'--enable-libvpx '
		'--enable-libilbc '
		'--enable-libwavpack '
		'--enable-libwebp '
		'--enable-dxva2 '
		'--enable-avisynth '
		# '--enable-vapoursynth ' #maybe works?
		'--enable-gray '
		'--enable-libmysofa '
		'--enable-libflite '
		'--enable-lzma '
		'--enable-libsnappy '
		'--enable-libzimg '
		'--enable-libx264 '
		'--enable-libx265 '
		'--enable-libaom '
		'--enable-libdav1d '
		'--enable-frei0r '
		'--enable-filter=frei0r '
		'--enable-librubberband '
		'--enable-libvidstab '
		'--enable-libxavs '
		'--enable-libxvid '
		'--enable-libgme '
		'--enable-runtime-cpudetect '
		'--enable-libfribidi '
		'--enable-gnutls ' # nongpl: openssl,libtls(libressl)
		'--enable-gmp '
		'--enable-fontconfig '
		'--enable-libfontconfig '
		'--enable-libfreetype '
		'--enable-libbluray '
		'--enable-libcdio '
		'--enable-libmfx '
		'--disable-schannel '
		'--disable-gcrypt '
		#'--enable-libcodec2 ' # Requires https://github.com/traviscross/freeswitch/tree/master/libs/libcodec2, too lazy to split that off.
		'--enable-ladspa '
		'--enable-libxml2 '
		'--enable-libdavs2 '
		'--enable-libkvazaar '
		'--enable-libopenmpt '
		'--enable-libxavs '
		'--enable-libxavs2 '
		'--enable-libsrt '
		'--enable-liblensfun '
		'--enable-libtesseract '
		
		# HW Dec/Enc
		'--enable-libmfx '
		'--enable-amf '
		'--enable-ffnvcodec '
		'--enable-cuvid '
		#'--enable-cuda-sdk ' --enable-nonfree
		'--enable-opengl '
		'--enable-d3d11va '
		'--enable-nvenc '
		'--enable-nvdec '
		'--enable-dxva2 '
		
		'--enable-gpl '
		
		'--extra-version=DeadSix27/python_cross_compile_script '
		#'--enable-avresample ' # deprecated.
		'--pkg-config-flags="--static" '
		#'--extra-libs="-liconv" ' # -lschannel #-lsecurity -lz -lcrypt32 -lintl -liconv -lpng -loleaut32 -lstdc++ -lspeexdsp -lpsapi
		'--extra-cflags="-DLIBTWOLAME_STATIC" '
		'--extra-cflags="-DMODPLUG_STATIC" '
	,
}