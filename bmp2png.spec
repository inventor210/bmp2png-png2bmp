Summary: A pair of simple converters between Windows BMP and PNG.
Summary(ja): Windows BMP と PNG とを相互変換するシンプルなプログラム
Name: bmp2png
Version: 1.62
Release: 1
Group: Applications/Multimedia
License: OSI-Approved
Source: http://hp.vector.co.jp/authors/VA010446/b2p-home/archives/bmp2png-%{version}.tar.gz
BuildPrereq: libpng-devel >= 1.0.4 zlib-devel
Requires: libpng >= 1.0.4 zlib
Buildroot: %{_tmppath}/%{name}-root


%description
bmp2png and png2bmp are a pair of simple command-line utilities to
convert files from the Windows Bitmap format (BMP) to the Portable
Network Graphics (PNG) format, and vice versa.

%description -l ja
bmp2png & png2bmp は、Windows Bitmap (BMP) と Portable Network
Graphics (PNG) とを相互変換するための、シンプルなコマンドライン・
ユーティリィティです。


%prep
%setup -q


%build
make clean
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

make install BINDIR=$RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README
%{_bindir}/bmp2png
%{_bindir}/png2bmp


%changelog
* Sun Sep 04 2005 MIYASAKA Masaru <alkaid@coral.ocn.ne.jp>
- updated to 1.62

* Tue Aug 24 2004 MIYASAKA Masaru <alkaid@coral.ocn.ne.jp>
- initial spec-file creation.

